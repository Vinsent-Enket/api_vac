import json
import os
import pandas as pd
"""
пометки на полях
0 - найти метод отслеживающий нажатия

1 - обязательно провести ренейм переменных
2 - описание каждому методу
3 - проверить ветки общения с юзером: проверить все ифы и елсы
4 - попытаться вывести универсальные методы для БЫСТРОГО ПОИСКА и сделать нормальный создатель шаблонов
5 - соответственно сделать редактор шаблонов
6 - правильно ли будет разнести на разные методы код в инициализаторе, когда есть папка и когда нет
"""


class User:

    def __init__(self, name):
        """
            Для инициализации нужно только имя, если есть директория то запуская сценарий old_user()
            Если папки нет, то запускается new_user()
            Так же желательно проверить подходит ли имя для образования папок (вдруг есть символы которые программа воспримет как файл)
            """
        self.name = name  # имя пользователя является образующим для всех папок
        self.choice = None  # по какому сценарию пошел пользователь, требуется для работы интерфейса

        self.sj_new_params = None  # так как blueprint не сохраняется в директорию во время работы программы,
        self.hh_new_params = None  # приходится сразу сохранять и параметры

        self.path_results = None  # путь до выбранного файла с результатами
        self.favorite_path = None  # путь до директории с избранными вакансиями
        self.results_directory = None  # путь до папки с результатами
        self.list_results = []  # список имен файлов с результатами
        self.list_blueprint_sj = []  # список имен файлов с шаблонами для superjob'а
        self.list_blueprint_hh = []  # список имен файлов с результатами head hanter'а
        self.directory = None  # директория пользователя
        self.path_blueprint = None

        if os.path.exists(f"../usrs/{self.name}"):
            print(f"{self.name}, добро пожаловать вновь!")
            self.old_user()
        else:
            self.new_user()

    def old_user(self):
        """
        Папка пользователя нашлась, по-хорошему, надо проверить всю директорию на целостность, но и так код раздул.
        Запомним пути для всех нужных папок и запускаем опрос, что делать дальше
        """
        self.directory = f"../usrs/{self.name}"  # директория пользователя
        self.list_blueprint_hh = (os.listdir(self.directory + '/blueprint/hh'))  # список шаблонов для hh
        self.list_blueprint_sj = (os.listdir(self.directory + '/blueprint/sj'))  # список шаблонов для sj
        self.list_results = (os.listdir(self.directory + '/results'))  # список файлов с результатами
        self.results_directory = f"../usrs/{self.name}/results"  # директория файлов с результатами

        self.favorite_path = f"../usrs/{self.name}/favorite"  # директория с избранными вакансиями
        while True:
            usr_answer = input(f"{self.name}, что вы ходите сделать?\n"
                               f"[1] - Взять готовый результат *[{len(self.list_results)}] - сохраненных результатов*\n"
                               # если он есть конечно
                               f"[2] - Взять готовый шаблон для HH и выполнить поиск *[{len(self.list_blueprint_hh)}] - сохраненных шаблонов*\n"
                               # если он есть конечно
                               f"[3] - Взять готовый шаблон для SJ и выполнить поиск *[{len(self.list_blueprint_sj)}] - сохраненных шаблонов*\n"
                               # если он есть конечно
                               "[4] - Создать шаблон для HH\n"
                               "[5] - Создать шаблон для SJ\n"
                               "[0] - выйти\n"
                               "---> ")
            if usr_answer == '1':
                if len(self.list_results) > 0:
                    self.path_results = self.results_selector()  # путь до выбранного файла с результатами
                    self.choice = "RES"
                    break
                else:
                    print("Ты чего, сказано же что нет готовых")
            elif usr_answer == '2':
                if len(self.list_blueprint_hh) > 0:
                    self.choice = "HH_ready"
                    self.path_blueprint = self.blueprint_selector()  # путь до выбранного файла с шаблоном для HH
                    break
                else:
                    print("Ты чего, сказано же что нет готовых")
            elif usr_answer == '3':
                if len(self.list_blueprint_sj) > 0:
                    self.choice = "SJ_ready"
                    self.path_blueprint = self.blueprint_selector()  # путь до выбранного файла с шаблоном для SJ
                    break
                else:
                    print("Ты чего, сказано же что нет готовых")
            elif usr_answer == '4':
                self.choice = "HH_new"
                self.path_blueprint, self.hh_new_params = self.mk_blueprint_hh()  # путь до созданного файла с шаблоном для HH
                break
            elif usr_answer == '5':
                self.choice = "SJ_new"
                self.path_blueprint, self.sj_new_params = self.mk_blueprint_sj()  # путь до созданного файла с шаблоном для SJ
                break
            elif usr_answer == "0":
                break
            else:
                print("Ты ввел что то не то, давай по новой")

    def new_user(self):
        """
        Если папки нет, то создаем ее и остальные
        :return:
        """
        os.mkdir(f"../usrs/{self.name}")
        os.mkdir(f"../usrs/{self.name}/results")
        os.mkdir(f"../usrs/{self.name}/favorite")
        os.mkdir(f"../usrs/{self.name}/blueprint")
        os.mkdir(f"../usrs/{self.name}/blueprint/hh")
        os.mkdir(f"../usrs/{self.name}/blueprint/sj")
        self.directory = f"../usrs/{self.name}"
        self.favorite_path = f"../usrs/{self.name}/favorite/favorite.txt"
        with open(self.favorite_path, 'w') as file:
            file.write("")

        usr_answer = input("Что вы ходите сделать?\n"
                           "[1] - Создать шаблон для HH\n"
                           "[2] - Создать шаблон для SJ\n"
                           "---> ")
        if usr_answer == '1':
            self.choice = "HH_new"
            self.path_blueprint = self.mk_blueprint_hh()  # путь до созданного файла с шаблоном для HH
        elif usr_answer == '2':
            self.choice = "SJ_new"
            self.path_blueprint = self.mk_blueprint_sj()  # путь до созданного файла с шаблоном для SJ

    def mk_blueprint_hh(self):
        """
        Не знаю, переделал ли я к моменту сдачи или нет, но если нет.
        Создаем словарь для параметров и сразу записываем туда page и per_page, не стоит давать тут свободу выбора
        Пока можно выбрать лишь быстрый поиск, и сохранить его в шаблоны, но проблема, файл появляется лишь после завершения программы
        Возможно допом возрвращать сразу и параметры?
        :return:
        """
        params = {}
        params['page'] = 1
        params['per_page'] = 99
        while True:
            usr_answ = input("[1] - Хотите выполнить быстрый поиск?\n"
                             "[2] - Поиск  по параметрам?\n"
                             "[0] - выйти"
                             "\n---> ")
            if usr_answ == "1":
                params['text'] = input("Введите одной строкой интересующие вас параметры \n---> ")
                return self.saver_blueprint(params)
            elif usr_answ == "0":
                break

    def mk_blueprint_sj(self):
        """
        Аналогично с mk hh, но быстрый поиск принимает значения по другому принципу
        :return:
        """
        params = {}
        while True:
            usr_answ = input("[1] - Хотите выполнить быстрый поиск?\n"
                             "[2] - Поиск  по параметрам?\n"
                             "[0] - выйти"
                             "\n---> ")
            if usr_answ == "1":
                params['keywords'] = []
                while True:
                    print("Давайте добавим слова которые вы хотите увидеть в вакансии")
                    usr_answ = input("Введите слово\nЕсли хотете закончить, введите [0] \n---> ")
                    if usr_answ == "0":
                        break
                    params['keywords'].append({"srws": 10, "skwc": "or", "keys": usr_answ})
                return self.saver_blueprint(params)

            elif usr_answ == "0":
                break
            self.saver_blueprint(params)

    def saver_blueprint(self, params):
        """
        Сохраняет шаблон в файл и передает его в атрибут
        :param params:
        :return:
        """
        if params != {}:
            file_name = input("Как изволите сохранить шаблон? \n---> ")
            if self.choice == "HH_new":
                temporary_path = f'{self.directory}/blueprint/hh/{file_name}.txt'
            elif self.choice == "SJ_new":
                temporary_path = f'{self.directory}/blueprint/sj/{file_name}.txt'
            with open(temporary_path, "w") as file:
                file.write(f"{params}")
                return temporary_path, params
        else:
            print("Параметры пусты, поиска не будет ")
            raise ("Что то ты накосячи с параметрами, чел")

    def blueprint_selector(self):
        """
        В зависимости от выбора пользователя, выводим список имен шаблонов hh/sj и
        :return:
        """
        while True:
            number = 1
            if self.choice == "HH_ready":
                list_blueprint = self.list_blueprint_hh
                file_path = f'{self.directory}/blueprint/hh'
            elif self.choice == "SJ_ready":
                list_blueprint = self.list_blueprint_sj
                file_path = f'{self.directory}/blueprint/sj'
            for file_name in list_blueprint:
                print(f"Есть следующие шаблоны: {file_name} Номер файла - {number}")
                number += 1
            usr_answer = input("Назовите номер ---> ")
            if 0 <= int(usr_answer) - 1 <= len(list_blueprint):
                file_path = file_path + f'/{list_blueprint[int(usr_answer) - 1]}'
                return file_path

    def results_selector(self):
        """
        получаем список результатов
        :return:
        """
        while True:
            number = 1
            for file_name in self.list_results:
                print(f"Есть следующие шаблоны: {file_name} Номер файла - {number}")
                number += 1

            usr_answer = input("Назовите номер ---> ")
            if int(usr_answer) - 1 <= len(self.list_results):
                file_path = self.results_directory + '/' + self.list_results[int(usr_answer) - 1]
                return file_path

    def favorite_updater(self, vaca_str, dict_characters):
        """
        чтобы он не перезаписывал значения, нужно чтобы он начинал с последней заполненной строки
        то есть надо получить ее номер, ааааа

        Пока не понял как можно создать xsxl файл при создании папки

        :param vaca_str:
        :param dict_characters:
        :return:
        """
        with open(self.favorite_path + '/favorite.txt', 'a') as file:
            file.write(vaca_str)
            print("вакансия была добавлена в избранное")
        path = self.favorite_path + '/favorite.xlsx'
        temporary_file = pd.read_excel(path)
        df_file = pd.DataFrame(dict_characters)
        asd = pd.concat([df_file, temporary_file])
        asd.to_excel(excel_writer=path, index=False)
