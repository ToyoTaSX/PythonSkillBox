import csv

def reader_func(file_name):
    headers = []
    rows = []
    with open(file_name, mode="r", encoding='utf-8') as file:
        reader_object = csv.reader(file, delimiter=",")
        for row in reader_object:
            if reader_object.line_num - 1 == 0:
                headers = row
                continue
            if row.count("") == 0:
                rows.append(row)
    return headers, rows


#
# Создание файла
#
with open("vacancies.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(['name', 'premium', 'employer_name', 'salary_from', 'salary_to', 'area_name'])
    file_writer.writerow(['Программист', 'FALSE', 'Контур', '70000', '110000', 'Москва'])
    file_writer.writerow(['Инженер', 'FALSE', 'Сервисный центр ЭКСПЕРТ', '30000', '60000', 'Санкт-Петербург'])


headers, rows = reader_func(input())
print(headers)
print(rows)


