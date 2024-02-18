import json
from src.vacancy import Vacancy, Vacancies
from src.abc import JSONABCSaver
import os


class JSONSaver(Vacancies, JSONABCSaver):
    """
    Запись в файл и чтение json
    """

    def file_writer(self):
        directory = 'Data'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, 'vacancies.json'), 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def file_reader(self):
        directory = 'Data'
        with open(os.path.join(directory, 'vacancies.json'), 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))



