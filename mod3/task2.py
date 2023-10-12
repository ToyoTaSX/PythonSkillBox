import csv
import re


class RefactoringProcessor:
    __keywords = []

    def __init__(self, keywords: list):
        self.__keywords = keywords

    def process_row(self, row: list) -> list:
        new_row = []
        for text in row:
            new_row.append(self.__process_field(text))
        return new_row

    def __process_field(self, field_text: str) -> str:
        field_text = self.__process_html_tags(field_text)
        field_text = self.__process_keywords(field_text)
        field_text = self.__process_time(field_text)
        field_text = self.__process_date(field_text)
        return field_text

    def __process_html_tags(self, field_text: str) -> str:
        return re.sub('<.*?>', '', field_text)

    def __process_keywords(self, field_text: str) -> str:
        result = field_text
        for word in self.__keywords:
            result = re.sub(r'\w*{}\w*'.format(word),
                            lambda x: x[0].upper(),
                            result,
                            flags=re.IGNORECASE)
        return result

    def __process_time(self, field_text: str) -> str:
        return re.sub(r'([0-2][0-9])\.([0-5][0-9])', r'\1:\2', field_text)

    def __process_date(self, field_text: str) -> str:
        return re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})([+-]\d{4})",
                      r"\4-\5-\6\7 \3/\2/\1",
                      field_text)



def refactor_csv_file(file, new_file, keywords):
    with open(file, 'r', encoding='utf-8') as input_file:
        with open(new_file, 'w', encoding='utf-8') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file, lineterminator='\n')
            processor = RefactoringProcessor(keywords)
            for row in reader:
                writer.writerow(processor.process_row(row))


file = input()
new_file = input()
keywords_list = input().split(',')
refactor_csv_file(file, new_file, keywords_list)