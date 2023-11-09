class Vacancy:

    def __init__(self, name, description, company_name, salary_from, salary_to):
        self.name = name
        self.description = description
        self.company_name = company_name
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return (f'Название: {self.name}'
                f'\nОписание: {self.description}'
                f'\nНазвание компании: {self.company_name}'
                f'\nЗарплата от: {self.salary_from}'
                f'\nЗарплата до: {self.salary_to}\n')
