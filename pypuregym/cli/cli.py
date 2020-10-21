"""Interact with Pure Fitness/Yoga service.

Usage:
  pypuregym location <gym-type> <region-id>
  pypuregym schedule <region-id> <location-id> <date>
  pypuregym book <region-id> <class-id> <username> <password> [--wait-until <wait>] [--retry <retry>]

Options:
  <gym-type>                  Can be "fitness" or "yoga".
  <region-id>                 Can be "HK", "CN" or "SG".
  <location-id>               ID of the studio (given with the "location" command).
  <date>                      Date to get the schedule for.
  <class-id>                  Class ID to book.
  <username>                  Your Pure username/email.
  <password>                  Your Pure password.
  --wait-until <wait>         When booking a class, wait until the specified date time before booking.
  --retry <retry>             Number of time to retry when booking the class.
"""  # noqa
import logging

from docopt import docopt

from pypuregym import __version__
from pypuregym.cli.location import get_location
from pypuregym.cli.schedule import get_schedule
from pypuregym.cli.book import book_class


def main():
    """CLI entry point.
    """
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
            wait_until=args['--wait-until'],
            retry=args['--retry'],
        )


if __name__ == '__main__':
    main()
