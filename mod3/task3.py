import json
import re
from bs4 import BeautifulSoup


class VacancyParser:
    __salary_rates = dict()

    def __init__(self, salary_rates: dict):
        self.__salary_rates = salary_rates

    def __get_text(self, html_tag):
        return re.sub(r'<.*?>', '', str(html_tag))

    def __convert_salary(self, salary: str) -> str:
        for currency, rate in self.__salary_rates.items():
            if currency in salary:
                numbers = re.findall(r'\d+\s*\d+', salary)
                converted_numbers = [str(float(re.sub(r'\s', '', x)) * rate) for x in numbers]
                converted_salary = '-'.join(converted_numbers)
                return converted_salary
        return salary

    def get_vacancy_data(self, file_name: str) -> json:
        with open(file_name, encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            vacancy_title = self.__get_text(soup.find('div', {'class': 'vacancy-title'}).find('h1'))

            salary = self.__convert_salary(
                self.__get_text(soup.find('div', {'data-qa': 'vacancy-salary'}).find('span')))

            experience = re.sub(r'<.*?>|[A-Za-zА-Яа-я ]', '',
                                str(soup.find('span', {'data-qa': 'vacancy-experience'}))).replace('–', '-')

            experience = None if experience == '' else experience

            company = self.__get_text(soup.find('span', {'class': 'vacancy-company-name'}))

            description = self.__get_text(soup.find('div', {'data-qa': 'vacancy-description'}))

            skills = [self.__get_text(skill) for skill in
                      soup.find('div', {'class': 'bloko-tag-list'}).find_all('span')]

            created_at = re.sub(r'<.*?>|\s', ' ',
                                str(soup.find('p', {'class': 'vacancy-creation-time-redesigned'}).find('span'))).strip()

            result = {
                'vacancy': vacancy_title,
                'salary': salary,
                'experience': experience,
                'company': company,
                'description': description,
                'skills': ', '.join(skills),
                'created_at': created_at,
            }
            return json.dumps(result, ensure_ascii=False)


input_file = input()

salary_rates = {
    '₽': 1.0,
    '$': 100.0,
    '€': 105.0,
    '₸': 0.210,
    'Br': 30.0,
}

parser = VacancyParser(salary_rates)
print(parser.get_vacancy_data(input_file))
