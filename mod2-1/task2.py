import csv
import re


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

    return headers, data


file_name = "vacancies2.csv"
headers, data = get_csv_data(file_name)

for row_data in data:
    for k, v in row_data.items():
        if isinstance(v, list):
            print(f"{k}: {', '.join(v)}")
        else:
            print(f"{k}: {v}")
    print()