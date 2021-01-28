import datetime
import logging
import time

import dateutil.parser

from pypuregym import PureAPI, Region

LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-arguments
def book_class(region_id, class_id, username, password, wait_until, retry):
    """Get Pure schedule.
    """
    LOGGER.info('Booking class #%d', class_id)

    try:
        region = Region[region_id.upper()]
    except KeyError:
        raise ValueError(
            '"%s" is not a valid region. Should be one of: %s' % (
                region_id,
                ', '.join([e.name for e in Region]),
            )) from None

    api = PureAPI(
        username=username,
        password=password,
        region=region,
    )

    if wait_until is not None:
        wait_until = dateutil.parser.parse(wait_until)
        now = datetime.datetime.now()
        delta = wait_until - now

        assert now <= wait_until, (
            '--wait-until can not be lower than current time')

        LOGGER.info('Wait until %s before booking...', wait_until)
        time.sleep(delta.seconds)

    retry = int(retry) if retry is not None else 1
    exception = None

    for _ in range(retry):
        # pylint: disable=broad-except
        try:
            api.book(class_id=class_id)
            exception = None
            break
        except Exception as exc:
            exception = exc

    if exception is not None:
        raise exception
    LOGGER.info('The class has been successfully booked!')
