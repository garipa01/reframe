import pandas as pd
import pytest
from reframe import Relation


@pytest.fixture
def r():
    data_real = {"name": ["Alice", "Bob", "Carol"], "age": [86, 4, 37]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)


def test_foo(r):
    r = r.project(["name"])
    data_expected = {"name": ["Alice", "Bob", "Carol"]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)


def test_foo_2(r):
    r = r.project(["name"])
    r_expected_2 = Relation("tests/test_project_expected_1.csv", sep="|")
    assert r.equals(r_expected_2)