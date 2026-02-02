__all__ = ("TimesSecondsEnum",)

import enum


class TimesSecondsEnum(enum.IntEnum):
    ONE_SECOND = 1
    FIVE_SECOND = 5
    TEN_SECONDS = 10
    HALF_MINUTE = 30
    ONE_MINUTE = 60
    FIVE_MINUTES = ONE_MINUTE * 5
    TEN_MINUTES = ONE_MINUTE * 10
    HALF_HOUR = ONE_MINUTE * 30
    ONE_HOUR = ONE_MINUTE * 60
    FOUR_HOURS = ONE_HOUR * 4
    TEN_HOURS = ONE_HOUR * 10
    ONE_DAY = ONE_HOUR * 24
    ONE_WEEK = ONE_DAY * 7
    ONE_MONTH = ONE_DAY * 30
    ONE_YEAR = ONE_DAY * 365
