import json
import re

class FieldProcessor:
    def process_field(self, field_text: str, result: dict) -> None:
        if field_text == "":
            return
        header, data = [i.strip() for i in field_text.split(':')]
        match header:
            case "description":
                result[header] = self.__process_description(data)
            case "salary":
                result[header] = self.__process_salary(data)
            case "key_phrase":
                result[header] = self.__process_key_phrase(data)
            case "addition":
                result[header] = self.__process_addition(data)
            case "reverse":
                result[header] = self.__process_reverse(data)
            case "company_info":
                result[header] = self.__process_company_info(data)
            case "key_skills":
                result[header] = self.__process_key_skills(data)


    def __process_description(self, data: str) -> str:
        def capitalized_sentence(sentence: str) -> str:
            words = [w.lower() for w in sentence.split()]
            words[0] = words[0].capitalize()
            return ' '.join(words)

        return ". ".join([capitalized_sentence(sent) for sent in data.split('.') if sent != ""])


    def __process_salary(self, data: str) -> str:
        return "%.3f" % float(data)


    def __process_key_phrase(self, data: str) -> str:
        return data.upper() + '!'


    def __process_addition(self, data: str) -> str:
        return "..." + data.lower() + "..."


    def __process_reverse(self, data: str) -> str:
        return data[::-1]


    def __process_company_info(self, data: str) -> str:
        n = 1  # run at least once
        while n:
            data, n = re.subn(r'\([^()]*\)', '', data)  # remove non-nested/flat balanced parts
        return data



    def __process_key_skills(self, data: str) -> str:
        return re.sub('&nbsp', ' ', data, flags=re.IGNORECASE)


def get_data(input_text, headings_text):
    output_headings = headings.split(", ")
    fields = [i.strip() for i in input_text.split(';')]
    processed = dict()
    fp = FieldProcessor()

    for field in fields:
        fp.process_field(field, processed)

    return json.dumps(dict(filter(lambda kv: kv[0] in output_headings, processed.items())))


input_text = input()
headings = input()

print(get_data(input_text, headings))
