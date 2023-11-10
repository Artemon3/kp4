import requests
from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_request(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HH(Engine):

    def __init__(self, keyword):
        self.keyword = keyword

    def get_request(self, count_page=5):
        params = {
            'page': 0,
            'per page': 20,
            'text': self.keyword
        }
        all_vacancies = []
        for i in range(1):
            params['page'] = i
            data = requests.get('https://api.hh.ru/vacancies', params=params).json()['items']
            all_vacancies.extend(data)
        return all_vacancies

    def get_vacancies(self):
        all_vacancies = []
        data = self.get_request(self.keyword)
        for vacancy in data:
            if vacancy['salary']:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            else:
                salary_from = 0
                salary_to = 0

            all_vacancies.append({
                "name": vacancy["name"],
                "description": vacancy["snippet"]["responsibility"],
                "company_name": vacancy["employer"]["name"],
                "salary_from": salary_from,
                "salary_to": salary_to
            })
        return all_vacancies
