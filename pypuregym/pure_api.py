import json
import logging
import re

import dateutil.parser
import requests


LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-instance-attributes
class PureAPI:
    """A class to perform queries through Pure Fitness/Yoga API.
    """

    def __init__(self, username, password, region):
        """Create a PureAPI object.

        :param username: `str` Pure Fitness/Yoga username.
        :param password: `str` Pure Fitness/Yoga password.
        :param region: `pypuregym.Region` Pure region.
        """
        self._username = username
        self._password = password

        self._region = region

        self._jwt_token = None
        self._token = None
        self._date = None

        self._session = requests.Session()
        self._session.headers = {
            'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/80.0.3987.163 Safari/537.36'),
        }

    def authenticate(self):
        """Authenticate on Pure Fitness API.
        """
        # No matter the gym type and subscription, everybody can log in to Pure
        # Fitness or (Pure Yoga).
        url = 'https://pure360.pure-fitness.com/en/%s' % (
            self._region.name.lower())

        LOGGER.debug('Get token from: %s', url)

        response = self._session.get(url=url, timeout=3)
        response.raise_for_status()

        match = re.search(
            r'"X-Date":(?P<date>\d+)."X-Token":"(?P<token>[a-z0-9]+)"',
            response.content.decode('utf-8'),
        )
        assert match, 'Can not find date and token from: %s' % url

        match = match.groupdict()
        self._token = match['token']
        self._date = match['date']

        if self._username and self._password:
            url = 'https://pure360-api.pure-international.com/api/v3/login'

            LOGGER.debug('Authenticating as "%s" on: %s', self._username, url)
            response = self._session.post(
                url=url,
                timeout=3,
                headers={
                    'x-date': match['date'],
                    'x-token': match['token'],
                    'content-type': 'application/json',
                },
                data=json.dumps({
                    'username': self._username,
                    'password': self._password,
                    'language_id': 1,
                    'region_id': self._region.value,
                    'jwt': True,
                    'platform': 'Web',
                }))
            response.raise_for_status()

            response = response.json()
            assert response['error']['code'] == 200, (
                'Authentication failed: %s' % response['error'])

            self._jwt_token = response['data']['user']['jwt']

    def get_locations(self, gym_type):
        """Get Pure studios location.

        :param gym_type: `pypuregym.GymType` Pure gym type.
        """
        if not self._token or not self._date:
            self.authenticate()

        LOGGER.debug('Get Pure locations')

        url = 'https://pure360-api.pure-international.com/api/v3/view_location'
        response = self._session.get(
            url=url,
            timeout=3,
            params={
                'type': gym_type.value,
                'language_id': 1,  # English
                'region_id': self._region.value,
            },
            headers={
                'x-date': self._date,
                'x-token': self._token,
            },
        )
        response.raise_for_status()

        response = response.json()
        assert response['error']['code'] == 200, (
            'Failed to get locations: %s' % response['error'])

        return response.get('data', {}).get('locations', [])

    def get_schedule(self, start_date, last_date, location_id):
        """Get classes schedule within a date range in a given location.

        You can pass `start_date` and `last_date` as `datetime` or `str`.

        :param start_date: First date to get the classes for (inclusive).
        :param last_date: Last date to get the classes for (inclusive).
        """
        if not self._token or not self._date:
            self.authenticate()

        LOGGER.debug('Getting schedule between %s and %s',
                     start_date, last_date)

        # Convert start and last dates to datetime objects.
        if isinstance(start_date, str):
            start_date = dateutil.parser.parse(start_date)
        if isinstance(last_date, str):
            last_date = dateutil.parser.parse(last_date)

        assert last_date >= start_date, (
            'Last date can not be < start date (%s < %s)' % (
                last_date, start_date))

        url = 'https://pure360-api.pure-international.com/api/v3/view_schedule'
        response = self._session.get(
            url=url,
            headers={
                'x-jwt-token': self._jwt_token,
                'x-token': self._token,
                'x-date': self._date,
            },
            params={
                'language_id': '1',
                'region_id': self._region.value,
                'location_ids': location_id,
                'start_date': start_date.strftime('%Y%m%d'),
                'days': (last_date - start_date).days + 1,
            },
        )
        response.raise_for_status()

        response = response.json()
        assert response['error']['code'] == 200, (
            'Get schedule failed: %s' % response['error'])

        return response['data']['classes']

    def book(self, class_id):
        """Book a class.

        :param class_id: `int` class id to book.
        """
        if not self._jwt_token:
            self.authenticate()

        LOGGER.debug('Booking class id #%d', class_id)

        url = 'https://pure360-api.pure-international.com/api/v3/booking'
        response = self._session.post(
            url=url,
            timeout=3,
            headers={
                'x-jwt-token': self._jwt_token,
                'x-token': self._token,
                'x-date': self._date,
                'content-type': 'application/json',
            },
            data=json.dumps({
                'language_id': 1,
                'region_id': self._region.value,
                'class_id': class_id,
                'booked_from': 'WEB',
                'book_type': 1,
            }),
        )
        response.raise_for_status()

        response = response.json()
        assert response['error']['code'] == 200, (
            'Failed to book class: %s' % response['error'])
