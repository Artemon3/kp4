import requests
import os


class SJ:

    def __init__(self, keyword):
        self.keyword = keyword

    def get_request(self):
        params = {'keyword': self.keyword}
        API_KEY = os.environ['SJ_API_KEY']
        all_vacancies = []
        for i in range(1):
            params['page'] = i
            data = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                params=params,
                                headers={"X-Api-App-Id": API_KEY}).json()["objects"]
            all_vacancies.extend(data)
        return all_vacancies

    def get_vacancies(self):
        all_vacancies = []
        data = self.get_request(self.keyword)
        # print(data)
        for vacancy in data:
            if vacancy['payment_from'] or ['payment_to']:
                salary_from = vacancy['payment_from'] if vacancy['payment_from'] else 0
                salary_to = vacancy['payment_to'] if ['payment_to'] else 0
            else:
                salary_from = 0
                salary_to = 0
            if vacancy['candidat']:
                description = vacancy['candidat'] if vacancy['candidat'] else '-'
            else:
                description = '-'
            all_vacancies.append({
                "name": vacancy["profession"],
                "description": description,
                "company_name": vacancy["firm_name"],
                "salary_from": salary_from,
                "salary_to": salary_to
            })
        return all_vacancies
