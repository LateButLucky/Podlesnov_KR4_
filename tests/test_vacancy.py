from src.vacancy import Vacancy, Vacancies
import pytest


@pytest.fixture
def sample_vacancy():
    return Vacancy("Программист", "Москва", 80000, 120000, "Полная занятость", "http://example.com")


def test_vacancy_creation(sample_vacancy):
    assert sample_vacancy.vacancy_title == "Программист"
    assert sample_vacancy.town == "Москва"
    assert sample_vacancy.salary_from == 80000
    assert sample_vacancy.salary_to == 120000
    assert sample_vacancy.employment == "Полная занятость"
    assert sample_vacancy.url == "http://example.com"


def test_vacancy_equality(sample_vacancy):
    same_vacancy = Vacancy("Программист", "Москва", 80000, 120000, "Полная занятость", "http://example.com")
    assert sample_vacancy == same_vacancy


def test_vacancy_inequality(sample_vacancy):
    diff_vacancy = Vacancy("Аналитик данных", "Санкт-Петербург", 90000, 130000, "Полная занятость",
                           "http://example.com")
    assert sample_vacancy != diff_vacancy


def test_vacancy_comparison(sample_vacancy):
    lesser_vacancy = Vacancy("Младший программист", "Екатеринбург", 60000, 90000, "Полная занятость",
                             "http://example.com")
    greater_vacancy = Vacancy("Старший программист", "Новосибирск", 100000, 150000, "Полная занятость",
                              "http://example.com")
    assert lesser_vacancy < sample_vacancy
    assert greater_vacancy > sample_vacancy


def test_vacancy_to_dict(sample_vacancy):
    expected_dict = {
        'vacancy_title': "Программист",
        'town': "Москва",
        'salary_from': 80000,
        'salary_to': 120000,
        'employment': "Полная занятость",
        'url': "http://example.com"
    }
    assert sample_vacancy.to_dict() == expected_dict


def test_vacancy_from_dict(sample_vacancy):
    vacancy_dict = {
        'vacancy_title': "Программист",
        'town': "Москва",
        'salary_from': 80000,
        'salary_to': 120000,
        'employment': "Полная занятость",
        'url': "http://example.com"
    }
    assert Vacancy.from_dict(vacancy_dict) == sample_vacancy


@pytest.fixture
def sample_vacancies():
    vacancies = [
        Vacancy("Программист", "Москва", 80000, 120000, "Полная занятость", "http://example.com"),
        Vacancy("Аналитик данных", "Санкт-Петербург", 90000, 130000, "Полная занятость", "http://example.com")
    ]
    return vacancies


def test_add_vacancies(sample_vacancies):
    vacancies = Vacancies()
    vacancies.add_vacancies(sample_vacancies)
    assert len(vacancies.all_vacancies) == 2


def test_delete_vacancies(sample_vacancies):
    vacancies = Vacancies()
    vacancies.add_vacancies(sample_vacancies)
    vacancies.delete_vacancies([sample_vacancies[0]])
    assert len(vacancies.all_vacancies) == 1


def test_sort_vacancies_by_salary(sample_vacancies):
    vacancies = Vacancies()
    vacancies.add_vacancies(sample_vacancies)
    vacancies.sort_vacancies_by_salary()
    assert vacancies.all_vacancies[0].salary_from == 90000
    assert vacancies.all_vacancies[1].salary_from == 80000
