from tabulate import tabulate

from pypuregym import PureAPI, Region


def get_schedule(region_id, location_id, date):
    """Get Pure schedule.
    """
    try:
        region = Region[region_id.upper()]
    except KeyError:
        raise ValueError(
            '"%s" is not a valid region. Should be one of: %s' % (
                region_id,
                ', '.join([e.name for e in Region]),
            )) from None

    api = PureAPI(
        username=None,
        password=None,
        region=region,
    )
    response = api.get_schedule(
        start_date=date,
        last_date=date,
        location_id=location_id,
    )

    # Format response
    response = [{
        'ID': entry['id'],
        'Class Name': entry['class_type']['name'],
        'Teacher': entry['teacher']['name'],
        'Start Time': entry['start_time'],
        'End Time': entry['end_time'],
    } for entry in response]

    print(tabulate(
        sorted(response, key=lambda e: e['Start Time']),
        headers='keys',
        tablefmt='fancy_grid',
    ))
