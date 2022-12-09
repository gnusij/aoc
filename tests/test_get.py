import os

import pytest

import aoc

def test_get(requests_mock):
    mock = requests_mock.get(
        url="https://adventofcode.com/2022/day/2/input",
        text="fake data for year 2022 day 2",
    )
    data = aoc.get(year=2022, day=2, session='fake session id')
    assert data == "fake data for year 2022 day 2"
    assert mock.called
    assert mock.call_count == 1
