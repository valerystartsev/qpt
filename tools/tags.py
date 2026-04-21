from enum import Enum

class AllureTag(str, Enum):
    LOGIN = 'login'
    LOGOUT = 'logout'
    EXTENDED = 'EXTENDED'
    REGRESSION = 'REGRESSION'
    SMOKE = 'smoke'


