import json
import hashlib


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

def pervoe_zadanie():
    with open(PATH, encoding='utf-8') as f:
        json_data = json.load(f)

        for item in Country(json_data):
            country = item['name']['common']
            country_link = country.replace(' ', '_')
            print(f'{country}  -->   https://wikipedia.org/wiki/{country_link}\n')

def vtoroe_zadanie():
    for m in string_md5(PATH_2):
        print(m)


def main():

    pervoe_zadanie()
    vtoroe_zadanie()










main()

