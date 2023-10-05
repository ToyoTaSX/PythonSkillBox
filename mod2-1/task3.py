import csv
import re
from statistics import mean


def get_ending(number, forms):
    if number % 10 == 1 and number % 100 != 11:
        return forms[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return forms[1]
    else:
        return forms[2]


def get_clean_text(text: str):
    splited_text = [' '.join(s.split()) for s in text.split('\n')]
    return '\n'.join(re.sub(r'<.*?>', '', s) for s in splited_text)


def get_csv_data(file_name):
    headers = []
    data = []
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if reader.line_num - 1 == 0:
                headers = row
                continue

            row_data_dictionary = dict()
            for row_item, header in zip(row, headers):
                clean_text = get_clean_text(row_item)
                if '\n' in clean_text:
                    clean_text = [item.strip() for item in clean_text.split('\n')]
                row_data_dictionary[header] = clean_text

            data.append(row_data_dictionary)

    return data

#Загрузка данных
vacancies_data = [v for v in get_csv_data('vacancies3.csv') if v['salary_currency'] == 'RUR']


#Самые высокие зарплаты
vacancies_data.sort(key=lambda x: int(x['salary_from']), reverse=True)
print("Самые высокие зарплаты:")
for i, vc in enumerate(vacancies_data[:10], start=1):
    salary = (int(vc['salary_from']) + int(vc['salary_to'])) // 2
    print(f"    {i}) {vc['name']} в компании \"{vc['employer_name']}\" - {salary} {get_ending(salary, ['рубль', 'рубля', 'рублей'])} (г. {vc['area_name']})")
print()


#Самые низкие зарплаты
print("Самые низкие зарплаты:")
vacancies_data.sort(key=lambda x: int(x['salary_from']))
for i, vc in enumerate(vacancies_data[:10], start=1):
    salary = (int(vc['salary_from']) + int(vc['salary_to'])) // 2
    print(f"    {i}) {vc['name']} в компании \"{vc['employer_name']}\" - {salary} {get_ending(salary, ['рубль', 'рубля', 'рублей'])} (г. {vc['area_name']})")
print()


#Предобработка списка умений
skills_list = []
for vc in vacancies_data:
    skills_list += vc['key_skills'].split('\\n')
unique_skills = set(skills_list)

skill_counts = {}
for skill in unique_skills:
    skill_counts[skill] = skills_list.count(skill)

#Вывод списка по популярности
print(f"Из {len(unique_skills)} скиллов, самыми популярными являются:")
sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)
for i, (skill, count) in enumerate(sorted_skills[:10], start=1):
    skill = re.sub(r'["”\']', '', skill)
    print(f"    {i}) {skill.strip()} - упоминается {count} раз{get_ending(count, ['', 'а', ''])}")
print()


#Предобработка зарплат по городам
city_salaries = {}
for vc in vacancies_data:
    city = vc['area_name']
    salary = (int(vc['salary_from']) + int(vc['salary_to'])) // 2
    if not city in city_salaries:
        city_salaries[city] = [salary]
    else:
        city_salaries[city].append(salary)

city_avg = {city: mean(salaries) for city, salaries in city_salaries.items()}
sorted_city_averages = sorted(city_avg.items(), key=lambda x: x[1], reverse=True)

#Вывод зарплат
print("Из", len(sorted_city_averages), "городов, самые высокие средние ЗП:")
for i, (city, avg_salary) in enumerate(sorted_city_averages[:10], start=1):
    vacancy_count = len(city_salaries[city])
    print(f"    {i}) {city} - средняя зарплата {int(avg_salary)} {get_ending(int(avg_salary), ['рубль', 'рубля', 'рублей'])} ({vacancy_count} ваканси{get_ending(vacancy_count, ['я', 'и', 'й'])})")
