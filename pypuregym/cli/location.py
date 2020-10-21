from tabulate import tabulate

from pypuregym import PureAPI, Region, GymType


def get_location(gym_type, region_id):
    """Get Pure locations.

    :param gym_type: `str` Type of the studio.
    :param region_id: `str` region location of the studio.
    """
    try:
        region = Region[region_id.upper()]
    except KeyError:
        raise ValueError(
            '"%s" is not a valid region. Should be one of: %s' % (
                region_id,
                ', '.join([e.name for e in Region]),
            )) from None

    try:
        gym_type = GymType[gym_type.upper()]
    except KeyError:
        raise ValueError(
            '"%s" is not a valid gym type. Should be one of: %s' % (
                gym_type,
                ', '.join([e.name for e in GymType]),
            )) from None

    api = PureAPI(
        username=None,
        password=None,
        region=region,
    )
    response = api.get_locations(gym_type)

    # Format response
    response = [{
        'ID': entry['id'],
        'Code': entry['code'],
        'Name': entry['short_name']['en'],
        'District': entry['district']['en'],
    } for entry in response]

    print(tabulate(
        sorted(response, key=lambda e: e['ID']),
        headers='keys',
        tablefmt='fancy_grid',
    ))
