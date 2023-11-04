import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами
import pandas as pd  # Для формирования датафрейма с результатами

class HeadHanterAPI():
    def __init__(self, path_params=None, params=None):
        self.url = 'https://api.hh.ru/vacancies'
        try:
            with open(path_params, 'r') as file:
                for line in file:
                    self.params = eval(line)
                    self.params['per_page'] = 99
                    print(self.params)
        except:
            self.params = params
        self.data = self.get_vacancies()

    def get_vacancies(self):
        req = requests.get(self.url, self.params)
        all_data = json.loads(req.content.decode("utf-8"))
        req.close()
        return all_data



