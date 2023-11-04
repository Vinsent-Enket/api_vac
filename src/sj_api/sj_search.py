import json
import os

import requests

#v3.r.137915697.945e8375d36a1a9743a267e5792ba4209162bd4b.da869bbbca52d7f1d066ae972bf155bf03e054d9
"""

_init__(self, top_n):
self. key
self. headers = {
'X-Api-App-Id': os.getenv("SECRET_KEY"),
v3.h. 4542271. f2f2076fcb6c982383e360b664fof8be2c1473d7.c7df7b74728caf963c263208b04a8dedaed793f2'
self. params = {
'count': top_n,
'page': 1,
"town':
"Moscow',
}
self. urL =
'https://api.superjob.ru/2.0/vacancies
曰
:
A5 ≤1 ^ 1 usage
def
get_vacancies (self, words) :
self. params keywords']
=words
r = requests. get(self.url, params=self. params, headers=self. headers)
vacancies =
json. Loads (r. text) ['objects']
return vacancies
obj
= Super Job_Api(2)
print(obj.get_vacancies ('python'))
"""

class SuperJobAPI:
    def __init__(self, path_params=None, params=None):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.key = os.getenv("SJ_API_KEY")
        self.headers = {'X-Api-App-Id': self.key}
        self.params = {
            'count': 1,
            'page': 1,
        }
        try:
            self.path_params = path_params
            with open(self.path_params, 'r') as file:
                for line in file:
                    self.params = eval(line)
        except:
            self.params = params
        self.data = self.get_vacancies()

    def get_vacancies(self):
        req = requests.get(self.url, params=self.params, headers=self.headers)
        #data = json.loads(req.text)['objects']
        data = json.loads(req.content.decode("utf-8"))
        req.close()
        return data

