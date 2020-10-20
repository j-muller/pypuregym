import logging

from tabulate import tabulate

from pypuregym import PureAPI, Region

LOGGER = logging.getLogger(__name__)


def book_class(region_id, class_id, username, password):
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
        gym_type=None,
        region=region,
    )

    response = api.book(class_id=class_id)
    LOGGER.info('The class has been successfully booked!')
