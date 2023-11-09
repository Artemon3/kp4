import sys

import hh_vacancies
import sj_vacancies
import json_save


def work():
    print("Привет!")
    keyword = input("Введите желаемую вакансию: ")
    hh_work = hh_vacancies.HH(keyword)
    sj_work = sj_vacancies.SJ(keyword)
    user_input = int(input("С какой платформы Вы хотите получить вакансии:"
                           "\n1 - HH"
                           "\n2 - SJ"
                           "\n3 - Две платформы\n"))
    if user_input == 1:
        vacancy_json = json_save.JSONsaver('json_hh')
        vacancy_json.write_data(hh_work.get_vacancies())
    elif user_input == 2:
        vacancy_json = json_save.JSONsaver('json_sj')
        vacancy_json.write_data(sj_work.get_vacancies())
    elif user_input == 3:
        vacancy_json = json_save.JSONsaver('json_all')
        hh = hh_work.get_vacancies()
        sj = sj_work.get_vacancies()
        hh.extend(sj)
        vacancy_json.write_data(hh)
    else:
        print('Такого варианта нет')
        sys.exit()
    user_selection = int(input('Какие вакансии Вам показать:'
                               '\n1 - Показать все вакансии '
                               '\n2 - Показать вакансии от 100000\n'))
    if user_selection == 1:
        for vacancy in vacancy_json.get_all_vacancies():
            print(vacancy)
    elif user_selection == 2:
        result = []
        for vacancy in vacancy_json.get_all_vacancies():
            if int(vacancy.salary_from) >= 100000:
                result.append(vacancy)
        for vacancy in result:
            print(vacancy)
    else:
        print('Такого варианта нет')
        sys.exit()


work()
