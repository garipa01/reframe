import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    data_real = {"firstName": ["Alex","John", "Clark", "Haley"], "degree": ["Math", "Drama", "Computer Science", "Math"], "age": [20, 21, 19, 19]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)


def test_query_expected1(r):
    r = r.query("firstName == 'Haley'")
    r_expected= Relation("tests/test_query_expected1.csv", sep="|")
    assert r.equals(r_expected)


def test_query_expected2(r):
    r = r.query("degree == 'Math'")
    r_expected = Relation("tests/test_query_expected2.csv", sep="|")
    assert r.equals(r_expected)

def test_query_expected3(r):
    r = r.query("age == 19 and firstName == 'Clark'")
    r_expected = Relation("tests/test_query_expected3.csv", sep="|")
    assert r.equals(r_expected)