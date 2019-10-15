import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    return Relation('country.csv',sep="|")


def test_join_expected1(r):
    r = r.query("continent == 'North America'").project(['name', 'region']).njoin(r.query('region == "Caribbean"').project(['name', 'region'])).head(4)
    r_expected = Relation("tests/test_join_expected1.csv",sep="|")
    assert r.equals(r_expected)


def test_join_expected2(r):
    r = r.query("indepyear == 1960").project(['name','continent','indepyear']).njoin(r.query("continent == 'Africa'").project(['name','continent','indepyear'])).head(4)
    r_expected = Relation("tests/test_join_expected2.csv",sep="|")
    assert r.equals(r_expected)


def test_join_expected3(r):
    r = (r.query("continent == 'Asia'").project(['name','continent','region','governmentform']).njoin(r.query('region == "Southeast Asia"').project(['name','continent','region','governmentform']))).njoin(r.query("governmentform == 'Republic'").project(['name','continent','region','governmentform'])).head(4)
    r_expected = Relation("tests/test_join_expected3.csv",sep="|")
    assert r.equals(r_expected)