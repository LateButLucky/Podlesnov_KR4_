from src.abc import GetVacancies, JSONABCSaver
import pytest
from abc import ABC, abstractmethod


def test_get_vacancies_is_abstract():
    assert issubclass(GetVacancies, ABC)
    assert hasattr(GetVacancies, 'get_vacancies')
    assert GetVacancies.get_vacancies.__isabstractmethod__


def test_file_writer_is_abstract():
    assert issubclass(JSONABCSaver, ABC)
    assert hasattr(JSONABCSaver, 'file_writer')
    assert JSONABCSaver.file_writer.__isabstractmethod__


def test_file_reader_is_abstract():
    assert issubclass(JSONABCSaver, ABC)
    assert hasattr(JSONABCSaver, 'file_reader')
    assert JSONABCSaver.file_reader.__isabstractmethod__
