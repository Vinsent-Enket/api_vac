import json
from datetime import datetime
import time


class Vacancy:
    all = []
    dict_characters = {'Название вакансии': [], 'Город': [], 'Зарплата от': [],
                       'Зарплата до': [], 'Требования': [], 'Чем придется заниматься': [],
                       'Справочное название вакансии': [], 'Тип занятости': [], 'Работодатель': [],
                       'Дата публикации': []
                       }
    """
    класс инициируется только через метод instantiate_from_json, в него передаются
    либо сами данные либо путь до файла с сохранными результатами
    """

    def __init__(self, name, city, salary_from, salary_to, requirement, responsibility, professional_roles,
                 employment, employer, date):
        self.name = name  # название вакансии
        self.city = city  # название города
        self.salary_from = int(salary_from)  # зарплата от
        self.salary_to = int(salary_to)  # зарплата до
        self.requirement = requirement  # требования к человеку
        self.responsibility = responsibility  # чем придется заниматься
        self.professional_roles = professional_roles  # справочное название вакансии
        self.employment = employment  # тип занятости
        self.employer = employer  # работодатель
        self.date = date # дата и время
        self.all.append(self)

    @classmethod
    def instantiate_from_json(cls, path_file=None, data=None):
        """
        Я так и не определился что лучше, через if ilse или все всегда оборачивать в try except
        поэтому встречается и тот и тот вариант

        в зависимости от кого получены данные инициализируем вакансию значениями из словаря данных, либо по шаблону HH либо SJ
        :param path_file:
        :param data:
        :return:
        """
        cls.all = [] # сбрасываем текущий пак вакансий
        cls.dict_characters = {'Название вакансии': [], 'Город': [], 'Зарплата от': [],
                           'Зарплата до': [], 'Требования': [], 'Чем придется заниматься': [],
                           'Справочное название вакансии': [], 'Тип занятости': [], 'Работодатель': [],
                           'Дата публикации': []
                           } # так же сбрасываем и словарь
        if path_file != None:
            with open(path_file, 'r') as jsonfile:
                data = json.load(jsonfile)

        try:
            for vaca in data['items']:

                try:

                    Vacancy(name=vaca['name'], city=vaca['area']['name'], salary_from=vaca['salary']['from'],
                            salary_to=vaca['salary']['to'], requirement=vaca['snippet']['requirement'],
                            responsibility=vaca['snippet']['responsibility'],
                            professional_roles=vaca['professional_roles'][0]['name'],
                            employment=vaca['employment']['name'], employer=vaca['employer']['name'],
                            date=cls.str_date_conv(vaca['published_at']))
                except TypeError:  # "тут не распознался словарь видимо это капча, потому как он проходит по всем объектам все равно")
                    # print()
                    continue
        except KeyError:
            for vaca in data['objects']:
                Vacancy(name=vaca['profession'],
                        city=vaca['town']['title'],
                        salary_from=vaca['payment_from'],
                        salary_to=vaca['payment_to'],
                        requirement='Образование - ' + vaca['education']['title'] + ' Семейный статус - ' +
                                    vaca['maritalstatus']['title'] + ' Возраст - ' + str(vaca['age_from']),
                        responsibility=vaca['work'],
                        professional_roles=vaca['profession'],
                        employment=vaca['type_of_work']['title'], employer=vaca['firm_name'],
                        date=cls.unuix_time_convert(vaca['date_published']))

    
    @classmethod
    def console_deco(cls):
        """
        Основной метод для работы с вакансиями, тот пакет данных что мы выбрали ранее создает вакансии
        Тут мы их визуализируем и при желании отправляем на сохрание в список избранных вакансий
        :return:
        """
        favorite_vacas = ""
        for i in range(len(cls.all)):
            vaca = cls.all[i]
            deco_str = (f"Название вакансии - {vaca.name}\n"
                        f"Город - {vaca.city}\n"
                        f"Зарплата - от {vaca.salary_from} и до {vaca.salary_to}\n"
                        f"тут должна быть дата публикации и соответсвтвенно нужен метод конвертер\n"
                        f"Описание - {vaca.requirement}\n"
                        f"Задача - {vaca.responsibility}\n"
                        f"Должность - {vaca.professional_roles}\n"
                        f"Занятость - {vaca.employment}\n"
                        f"Работодатель - {vaca.employer}\n"
                        f"Дата публикации - {vaca.date}")
            print(deco_str)
            print(vaca.dict_characters)
            user_answ = input("нажмите ентер чтобы продолжить\n[1] чтобы добавить вакансию в избранное \n"
                              "[0] - чтобы выйти\n"
                              "--->")
            if user_answ == "1":
                # записываем характеристики текущей вакансии в словарь по формату удобному для последующей конвертации в xlsx
                # возвращаем
                favorite_vacas += deco_str + "\n------------------\n"
                cls.dict_characters['Название вакансии'].append(vaca.name)
                cls.dict_characters['Город'].append(vaca.city)
                cls.dict_characters['Зарплата от'].append(vaca.salary_from)
                cls.dict_characters['Зарплата до'].append(vaca.salary_to)
                cls.dict_characters['Требования'].append(vaca.requirement)
                cls.dict_characters['Чем придется заниматься'].append(vaca.responsibility)
                cls.dict_characters['Справочное название вакансии'].append(vaca.professional_roles)
                cls.dict_characters['Тип занятости'].append(vaca.employment)
                cls.dict_characters['Работодатель'].append(vaca.employer)
                cls.dict_characters['Дата публикации'].append(vaca.date)
            elif user_answ == "0":
                break
        return favorite_vacas # смысла возвращать словарь не вижу, лучше получить его через обращение как к аттрибуту

    @classmethod
    def all_sort(cls):
        """
        Сортируем, что уж еще сказать
        :return:
        """
        user_answ = input("По какому параметру будем сортировать?\n"
                          "[1] - Минимальная ЗП\n"
                          "[2] - Дата\n"
                          "--->")
        if user_answ == "1":
            cls.all.sort(key=lambda x: x.salary_from, reverse=True)
        elif user_answ == "2":
            cls.all.sort(key=lambda x: x.date)

    @classmethod
    def sort_salary(cls, s):
        return s.salary_from

    @classmethod
    def sort_data(cls, s):
        return s.date

    @classmethod
    def unuix_time_convert(cls, time_unix):
        """
            Конвертер из юникс времени
            """
        unix_timestamp = time_unix
        unix_timestamp = float(unix_timestamp)
        time_struct = time.gmtime(unix_timestamp)
        format_date = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
        return format_date # сделать одинаково с временем хедхантера

    @classmethod
    def str_date_conv(cls, data_str):
        """
        конвертер из строкового значения
        :param data_str:
        :return:
        """
        format_date = datetime.strptime(data_str[:-5], "%Y-%m-%dT%H:%M:%S")
        return format_date
