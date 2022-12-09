import os

import pytest

import aoc

def test_get_data_via_import(requests_mock, monkeypatch, freezer):
    rq_mock = requests_mock.get(
        url="https://adventofcode.com/2022/day/2/input",
        text="fake data for year 2022 day 2",
    )
    monkeypatch.setenv("AOC_SESSION", "fake session id")
    freezer.move_to("2022-12-02 12:00:00Z")
    from aoc import data
    assert data == "fake data for year 2022 day 2"
    assert rq_mock.called
    assert rq_mock.call_count == 1

def test_get_lines_via_import(requests_mock, monkeypatch, freezer):
    rq_mock = requests_mock.get(
        url="https://adventofcode.com/2022/day/2/input",
        text="fake\ndata for year 2022 day\n2",
    )
    monkeypatch.setenv("AOC_SESSION", "fake session id")
    freezer.move_to("2022-12-02 12:00:00Z")
    from aoc import lines
    assert lines == ["fake", "data for year 2022 day", "2"]
    assert rq_mock.called
    assert rq_mock.call_count == 1
