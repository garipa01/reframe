import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def course():
    return Relation('tests/COURSE.csv',sep=",")


@pytest.fixture
def student():
    return Relation('tests/STUDENT.csv',sep=",")


@pytest.fixture
def section():
    return Relation('tests/SECTION.csv',sep=",")


@pytest.fixture
def enroll():
    return Relation('tests/ENROLL.csv',sep=",")


@pytest.fixture
def dept():
    return Relation('tests/DEPT.csv',sep=",")


def test_join_expected1(course,student,section,enroll,dept):
    r = student.project(["SId","SName"]).njoin(enroll.project(["StudentId","Grade"]).rename("StudentId","SId"))
    r_expected = Relation("tests/test_join_expected1.csv",sep="|")
    assert r.equals(r_expected)


def test_join_expected2(course,student,section,enroll,dept):
    r = student.project(["SName","MajorId"]).njoin(dept.project(["DId","DName"]).rename("DId","MajorId"))
    r_expected = Relation("tests/test_join_expected2.csv",sep="|")
    assert r.equals(r_expected)


def test_join_expected3(course,student,section,enroll,dept):
    r = (section.project(["SectId","CourseId"]).njoin(course.project(["CId","Title","DeptId"]).rename("CId","CourseId"))).njoin(dept.project(["DId","DName"]).rename("DId","DeptId"))
    r_expected = Relation("tests/test_join_expected3.csv",sep="|")
    print(r)
    assert r.equals(r_expected) 