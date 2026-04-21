from enum import Enum

class AllureEpic(str, Enum):
    LOGIN = 'Login'
    SALE = 'Sale'
    ADD2CART = 'Add2Cart'