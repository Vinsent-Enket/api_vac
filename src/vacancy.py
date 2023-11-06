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
    либо сами данные
    """

    def __init__(self, name, city, salary_from, salary_to, requirement, responsibility, professional_roles,
                 employment, employer, date, service_name):
        """
        Пришлось поставить None ибо иногда приходят такие данные
        :param name:
        :param city:
        :param salary_from:
        :param salary_to:
        :param requirement:
        :param responsibility:
        :param professional_roles:
        :param employment:
        :param employer:
        :param date:
        :param service_name:
        """
        self.service_name = None
        self.name = name  # название вакансии
        self.city = city  # название города
        if salary_to is not None and salary_from is not None:
            self.salary_from = int(salary_from)  # зарплата от
            self.salary_to = int(salary_to)  # зарплата до
        else:
            self.salary_from = 0  # зарплата от
            self.salary_to = 0  # зарплата до
        self.requirement = requirement  # требования к человеку
        self.responsibility = responsibility  # чем придется заниматься
        self.professional_roles = professional_roles  # справочное название вакансии
        self.employment = employment  # тип занятости
        self.employer = employer  # работодатель
        self.date = date  # дата и время
        self.from_service = service_name
        self.all.append(self)

    def __repr__(self):
        return (
            f'Vacancy(name={self.name}, city={self.city}, salary_from={self.salary_from}, salary_to={self.salary_to},'
            f'requirement={self.requirement}, responsibility={self.responsibility}, professional_roles={self.professional_roles},'
            f'employment={self.employment}, employer={self.employer}, date={self.date}, service_name={self.service_name})')

    def __str__(self):
        return self.name

    @classmethod
    def instantiate_from_data(cls, data_hh, data_sj):
        """
        Я так и не определился что лучше, через if ilse или все всегда оборачивать в try except
        поэтому встречается и тот и тот вариант

        в зависимости от кого получены данные инициализируем вакансию значениями из словаря данных, либо по шаблону HH либо SJ
        :return:
        """
        cls.all = []  # сбрасываем текущий пак вакансий
        cls.dict_characters = {'Название вакансии': [], 'Город': [], 'Зарплата от': [],
                               'Зарплата до': [], 'Требования': [], 'Чем придется заниматься': [],
                               'Справочное название вакансии': [], 'Тип занятости': [], 'Работодатель': [],
                               'Дата публикации': []
                               }  # так же сбрасываем и словарь

        for vaca in data_hh['items']:
            """name, city, salary_from, salary_to, requirement, responsibility, professional_roles,
                        employment, employer, date, service_name):"""
            if vaca['salary'] is None:
                vaca['salary'] = {'to': 0, 'from': 0}
            try:
                Vacancy(name=vaca['name'],
                        city=vaca['area']['name'],
                        salary_from=vaca['salary']['from'],
                        salary_to=vaca['salary']['to'],
                        requirement=vaca['snippet']['requirement'],
                        responsibility=vaca['snippet']['responsibility'],
                        professional_roles=vaca['professional_roles'],
                        employment=vaca['employment'],
                        employer=vaca['employer'],
                        date=cls.str_date_conv(vaca['published_at']),
                        service_name="HeadHunter")
            except FileNotFoundError:  # некоторые данные иногда, почему-то, приходят поврежденными видимо капча

                continue
        for vaca in data_sj['objects']:
            Vacancy(name=vaca['profession'],
                    city=vaca['town']['title'],
                    salary_from=vaca['payment_from'],
                    salary_to=vaca['payment_to'],
                    requirement='Образование - ' + vaca['education']['title'] +
                                ' Семейный статус - ' + vaca['maritalstatus']['title'] +
                                ' Возраст - ' + str(vaca['age_from']),
                    responsibility=vaca['work'],
                    professional_roles=vaca['profession'],
                    employment=vaca['type_of_work']['title'], employer=vaca['firm_name'],
                    date=cls.unuix_time_convert(vaca['date_published']),
                    service_name="Super Job")

    @classmethod
    def choice_favorite(cls):
        """
        Основной метод для работы с вакансиями, тот пакет данных что мы создали ранее, создает вакансии
        Тут мы их визуализируем и при желании отправляем на сохрание в список избранных вакансий
        :return:
        """
        favorite_vacancises = ""
        for i in range(len(cls.all)):
            vaca = cls.all[i]
            deco_str = (f"Название вакансии - {vaca.name}\n"
                        f"Город - {vaca.city}\n"
                        f"Зарплата - от {vaca.salary_from} и до {vaca.salary_to}\n"
                        f"Описание - {vaca.requirement}\n"
                        f"Задача - {vaca.responsibility}\n"
                        f"Должность - {vaca.professional_roles}\n"
                        f"Занятость - {vaca.employment}\n"
                        f"Работодатель - {vaca.employer}\n"
                        f"Дата публикации - {vaca.date}\n"
                        f"Получено с сервиса - {vaca.from_service}\n")
            print(deco_str)
            user_answ = input("нажмите Ентер чтобы продолжить\n"
                              "[1] чтобы добавить вакансию в избранное \n"
                              "[0] - чтобы выйти\n"
                              "---> ")
            if user_answ == "1":
                # записываем характеристики текущей вакансии в словарь по формату удобному для последующей конвертации в xlsx
                # возвращаем
                favorite_vacancises += deco_str + "\n------------------\n"
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
            else:
                continue
        return favorite_vacancises  # смысла возвращать словарь не вижу, лучше получить его через обращение как к аттрибуту

    @classmethod
    def all_sort(cls):
        """
        Сортируем, что уж еще сказать
        :return:
        """
        user_answ = input("По какому параметру будем сортировать?\n"
                          "[1] - Минимальная ЗП\n"
                          "[2] - Дата\n"
                          "---> ")
        if user_answ == "1":
            cls.all.sort(key=lambda x: x.salary_from, reverse=True)
        elif user_answ == "2":
            cls.all.sort(key=lambda x: x.date, reverse=True)

    @classmethod
    def all_filtration(cls):
        user_answ = input("По какому параметру будем фильтровать?\n"
                          "[1] - Минимальная ЗП\n"
                          "[2] - Дата\n"
                          "---> ")
        cls.dict_characters = {'Название вакансии': [], 'Город': [], 'Зарплата от': [],
                               'Зарплата до': [], 'Требования': [], 'Чем придется заниматься': [],
                               'Справочное название вакансии': [], 'Тип занятости': [], 'Работодатель': [],
                               'Дата публикации': []
                               }  # так же сбрасываем и словарь
        if user_answ == "1":
            user_answ = int(input("Сколько вакансий оставить?\n---> "))
            for i in range(len(cls.all)):
                cls.all.sort(key=lambda x: x.salary_from, reverse=True)
                cls.all = cls.all[:user_answ]
        elif user_answ == "2":
            user_answ = int(input("Сколько вакансий оставить?\n---> "))

            for i in range(len(cls.all)):
                cls.all.sort(key=lambda x: x.date, reverse=True)
                cls.all = cls.all[:user_answ]

    @classmethod
    def unuix_time_convert(cls, time_unix):
        """
            Конвертер из юникс времени
            """
        unix_timestamp = time_unix
        unix_timestamp = float(unix_timestamp)
        time_struct = time.gmtime(unix_timestamp)
        format_date = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
        return format_date  # сделать одинаково с временем хедхантера

    @classmethod
    def str_date_conv(cls, data_str):
        """
        Конвертер из строкового значения
        :param data_str:
        :return:
        """
        format_date = datetime.strptime(data_str[:-5], "%Y-%m-%dT%H:%M:%S")
        return format_date
