"""Interact with Pure Fitness/Yoga service.

Usage:
  pypuregym location <gym-type> <region-id>
  pypuregym schedule <region-id> <location-id> <date>
  pypuregym book <region-id> <class-id> <username> <password>

Options:
  <gym-type>                  Can be "fitness" or "yoga".
  <region-id>                 Can be "HK", "CN" or "SG".
"""
import logging

from docopt import docopt

from pypuregym import __version__
from .location import get_location
from .schedule import get_schedule
from .book import book_class

LOGGER = logging.getLogger(__name__)


def main():
    args = docopt(__doc__, version=__version__)

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )

    if args['location']:
        get_location(
            gym_type=args['<gym-type>'],
            region_id=args['<region-id>'],
        )
    elif args['schedule']:
        get_schedule(
            region_id=args['<region-id>'],
            location_id=int(args['<location-id>']),
            date=args['<date>'],
        )
    elif args['book']:
        book_class(
            region_id=args['<region-id>'],
            class_id=int(args['<class-id>']),
            username=args['<username>'],
            password=args['<password>'],
        )


if __name__ == '__main__':
    main()
