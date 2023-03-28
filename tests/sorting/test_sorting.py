# from src.pre_built.sorting import sort_by
from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def jobs_sort_max():
    return [
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": -1, "min_salary": 10},
    ]


@pytest.fixture
def jobs_sort_min():
    return [
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": -1, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
    ]


def test_sort_by_criteria(jobs_sort_max, jobs_sort_min):
    """Testa se sort_by ordena corretamente"""
    jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == jobs_sort_max

    sort_by(jobs, "min_salary")
    assert jobs == jobs_sort_min
