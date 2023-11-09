import json
# import hh_vacancies
from vacancy import Vacancy


class JSONsaver:

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def write_data(self, data):
        with open(f"{self.filename}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_all_vacancies(self):
        with open(f"{self.filename}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        all_vacancies = []
        for vacancy in data:
            all_vacancies.append(Vacancy(vacancy['name'],
                                         vacancy['description'],
                                         vacancy['company_name'],
                                         vacancy['salary_from'],
                                         vacancy['salary_to']))
        return all_vacancies


js = JSONsaver('vacancies')
