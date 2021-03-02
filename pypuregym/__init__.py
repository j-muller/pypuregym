# pylint: disable=unused-import
import enum

from pypuregym.pure_api import PureAPI


class GymType(enum.Enum):
    """An enum to represent a Pure gym type.
    """

    YOGA = 'Y'
    FITNESS = 'F'


# pylint: disable=invalid-name
class Region(enum.Enum):
    """An enum to represent a Pure region location.
    """

    HK = 1
    SG = 2
    CN = 4


__version__ = '1.4.0'
