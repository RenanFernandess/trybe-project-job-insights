# from src.pre_built.brazilian_jobs import read_brazilian_file
import pytest
from unittest.mock import patch, Mock
from src.pre_built.brazilian_jobs import read_brazilian_file


@pytest.fixture
def brazilian_jobs():
    return [
        {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"},
        {"titulo": "Motorista", "salario": "3000", "tipo": "full time"},
    ]


@pytest.fixture
def brazilian_jobs_translated():
    return [
        {"title": "Maquinista", "salary": "2000", "type": "trainee"},
        {"title": "Motorista", "salary": "3000", "type": "full time"},
    ]


def test_brazilian_jobs(brazilian_jobs, brazilian_jobs_translated):
    "Testa se read_brazilian_file retorna os jobs tradusidos para o inglês"
    with patch("src.insights.jobs.read", Mock(return_value=brazilian_jobs)):
        assert type(read_brazilian_file("fake_path")) == list
        assert read_brazilian_file("fake_path") == brazilian_jobs_translated
