from abc import ABC, abstractmethod  # Для наследования
import requests  # Для запросов по API
import json  # Для обработки полученных результатов
import os  # Для работы с файлами


class abstract_api(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HeadHanterAPI(abstract_api):
    def __init__(self, keywords):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            "page": 0,
            "text": keywords,
            "per_page": 99
        }
        self.data = self.get_request()

    def get_request(self):
        """
        Мне обязательно нужно чтобы правильно де-кодировался ответ от сервиса
        :return:
        """

        req = requests.get(self.url, self.params)
        all_data = json.loads(req.content.decode("utf-8"))
        req.close()
        return all_data


# v3.r.137915697.945e8375d36a1a9743a267e5792ba4209162bd4b.da869bbbca52d7f1d066ae972bf155bf03e054d9

class SuperJobAPI(abstract_api):
    def __init__(self, keywords):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.key = os.getenv("SJ_API_KEY")
        self.headers = {'X-Api-App-Id': self.key}
        self.params = {
            'count': 99,
            'page': 0,
            "keywords": keywords,
        }
        self.data = self.get_request()

    def get_request(self):
        req = requests.get(self.url, params=self.params, headers=self.headers)
        all_data = json.loads(req.content.decode("utf-8"))
        req.close()
        return all_data

    @property
    def keywords(self):
        return self.params

    @keywords.setter
    def keywords(self, new_keyword):
        self.params = {
            'count': 99,
            'page': 0,
            "keywords": new_keyword}
        self.data = self.get_request()
