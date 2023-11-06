import json
import os
import pandas as pd


class User:

    def __init__(self, name="dflt_usr"):

        self.name = name  # имя пользователя является образующим для всех папок
        print(f"{self.name}, добро пожаловать!")
        self.directory = f"./users/{self.name}"  # директория пользователя
        self.favorite_path = f"./users/{self.name}/favorite"  # директория с избранными вакансиями
        self.__connect(f"./users/{self.name}")
        self.__connect(f"./users/{self.name}/favorite")
        self.req_text = input("По какому слову будем искать?\n")


    def __connect(self,path):
            """
            Проверка на существование файла с данными и
            создание его при необходимости
            Также проверить на деградацию и возбудить исключение
            если файл потерял актуальность в структуре данных
            """
            if not os.path.exists(path):
                os.mkdir(path)

    def __repr__(self):
        return f"User(name='{self.name}', req_text='{self.req_text}'"

    def __str__(self):
        return self.name


    def favorite_updater(self, vaca_str, dict_characters):
        """
        Сохраняем выбранные вакансии в свою папку

        :param vaca_str:
        :param dict_characters:
        :return:
        """
        with open(self.favorite_path + '/favorite.txt', 'a') as file:
            file.write(vaca_str)
        path = self.favorite_path + '/favorite.xlsx'
        try:
            temporary_file = pd.read_excel(path)
        except FileNotFoundError:
            temporary_file = pd.DataFrame({})
        df_file = pd.DataFrame(dict_characters)
        asd = pd.concat([df_file, temporary_file])
        asd.to_excel(excel_writer=path, index=False)
