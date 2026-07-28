from datetime import datetime

from relatorios.domain.entities.date_range import DateRange


def test_get_datetime_range_covers_full_first_and_last_day():
    date_range = DateRange(start="01/03/2025", end="03/03/2025")

    start, end = date_range.get_datetime_range()

    assert start == datetime(2025, 3, 1, 0, 0, 0)
    assert end.date() == datetime(2025, 3, 3).date()
    assert end.hour == 23
    assert end.minute == 59
    assert end.second == 59


def test_get_datetime_range_single_day():
    date_range = DateRange(start="15/01/2026", end="15/01/2026")

    start, end = date_range.get_datetime_range()

    assert start == datetime(2026, 1, 15, 0, 0, 0)
    assert end.date() == datetime(2026, 1, 15).date()
    assert end.hour == 23
    assert end.minute == 59
    assert end.second == 59


def test_get_datetime_range_end_is_after_start():
    date_range = DateRange(start="01/03/2025", end="31/03/2025")

    start, end = date_range.get_datetime_range()

    assert end > start
