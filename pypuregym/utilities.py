def get_region_id(region):
    """Return Pure region ID from region code.

    Example:
        - Hong Kong -> #1
        - Singapore -> #2
        - Shanghai/CN -> #4
    """
    regions = {
        'HK': 1,
        'SG': 2,
        'CN': 4,
    }
    assert region in regions, (
        'Region "%s" does not exist.' % region)
    return regions[region]
