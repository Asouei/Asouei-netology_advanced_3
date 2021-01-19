import json
import hashlib

from logger import simple_logger as sl
from logger import complex_logger as cl

PATH = 'countries.json'
PATH_2 = 'test.txt'



class Country():

    def __init__(self, countries_list):
        self.countries_list = countries_list
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == len(self.countries_list):
            raise StopIteration
        item = self.countries_list[self.current_index]
        self.current_index += 1
        return item


def string_md5(path):
    with open(path, 'rb') as f:
        for line in f.readlines():
            m = hashlib.md5(line)
            m = m.hexdigest()
            yield m

@sl
def pervoe_zadanie(i):
    with open(PATH, encoding='utf-8') as f:
        json_data = json.load(f)

        for item in Country(json_data):
            country = item['name']['common']
            country_link = country.replace(' ', '_')
            print(f'{country}  -->   https://wikipedia.org/wiki/{country_link}\n')
        i = 1
        return i
#     просто для наглядности

@sl
def vtoroe_zadanie(i):
    for m in string_md5(PATH_2):
        print(m)
    i = 2
    return i
#   просто для наглядности

@cl('complex.log')
def vtoroe_zadanie_2(i):
    # просто дубликат для другого декоратора с хэшем того json файла
    for m in string_md5(PATH):
        print(m)
    i = 2
    return i
#   просто для наглядности

def main():

    pervoe_zadanie(2)
    vtoroe_zadanie(3)
    vtoroe_zadanie_2(11)










main()

