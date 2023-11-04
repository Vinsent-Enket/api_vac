import requests

"""
я пока в процессе его создания
Идея в чем, создать шаблон полного запроса, с описанием что должно быть в значении вместо самих значений
Потом с помощью методов что ниже, пройти шаблон полностью и создать такую же структуру
Это будет правильнее чем вручную создавать структуру, шаблон поменялся и метод для перебора нет

:var это шаблон который нужно будет перибирать

этими двумя методами я горжусь как собственными детьми, они могут перебрать любой словарь с значениями из словарей и списков любого уровня вложенности
Надо только прикрутить правильно input


"""


def value_is_dict(dictionary_value):
    temporary_value_dict = {}
    for key, value in dictionary_value.items():
        # print(key, value, "работает is dict")

        if type(value) is dict:  # если значение словарь то
            temporary_value_dict[key] = value_is_dict(value)

        elif type(value) is list:  # если же он список то
            temporary_value_dict[key] = value_is_list(value)
        else:
            temporary_value_dict[key] = value
    return temporary_value_dict


def value_is_list(listianary_value):
    temporary_value_list = []
    for item in listianary_value:
        # print(item, "работает is list")
        if type(item) is dict:  # если значение словарь то
            temporary_value_list.append(value_is_dict(item))
        elif type(item) is list:  # если же он список то
            temporary_value_list.append(value_is_list(item))
        else:
            temporary_value_list.append(item)
    return temporary_value_list


value_is_dict(var["objects"][0])

for key, value in var["objects"][0].items():
    if type(value) is dict:
        temporary_value = value_is_dict(value)
        new_var['objects'][0][key] = temporary_value
    elif type(value) is list:
        temporary_value = value_is_list(value)
        new_var['objects'][0][key] = temporary_value
    else:
        new_var['objects'][0][key] = value

print(new_var == var)
with open('test.py', 'w') as file:
    file.write(str(new_var))

def mk_full_blueprint_hh():
    params_hh = {}
    params_sj = {}
    #req = requests.get() может сделать подкачку словаря со значениями?
    sj_dict = {
        "place_of_work":{
            "0":"не имеет значения",
            "1":"на территории работодателя",
            "2":"на дому",
            "3":"разъездного характера"
        },
        "type_of_work":{
            "0":"не имеет значения",
            "6":"полный рабочий день",
            "7":"временная работа / freelance",
            "9":"работа вахтовым методом",
            "10":"неполный рабочий день",
            "12":"сменный график работы",
            "13":"частичная занятость"
        },

        "experience":{
            "1":"без опыта",
            "2":"от 1 года",
            "3":"от 3 лет",
            "4":"от 6 лет"
        },
        "language":{
            "0":"Не имеет значения",
            "1":"Английский",
            "2":"Немецкий",
            "3":"Французский"  // ...
        },
        "lang_level":{
            "0":"Не имеет значения",
            "3":"Базовый",
            "5":"Технический",
            "7":"Разговорный",
            "9":"Свободно владею"
        },
        "language_resume":{
            "1":"Английский",
            "2":"Немецкий",
            "3":"Французский"
        },
        "lang_level_resume":{
            "3":"Базовый",
            "5":"Технический",
            "7":"Разговорный",
            "9":"Свободно владею"
        },
        "maritalstatus":{
            "0":"не имеет значения",
            "2":"cостоит в браке",
            "3":"не состоит в браке"
        },
        "maritalstatus_resume":{
            "2":"состою в браке",
            "3":"не состою в браке"
        },
        "maritalstatus_resume_gender":{
            "2":{
                "2":"Женат",
                "3":"Замужем"
            },
            "3":{
                "2":"Не женат",
                "3":"Не замужем"
            }
        },
        "children":{
            "0":"не имеет значения",
            "2":"нет",
            "3":"есть"
        },
        "children_resume":{
            "2":"детей нет",
            "3":"дети есть"
        },
        "agency":{
            "1":"Прямой работодатель",
            "2":"Кадровое агентство",
            "3":"Аутсорсинг/аутстаффинг"
        },
        "gender":{
            "0":"Не имеет значения",
            "2":"Мужской",
            "3":"Женский"
        },
        "gender_resume":{
            "2":"мужской",
            "3":"женский"
        },
        "currency":{
            "0":"rub",
            "1":"uah",
            "2":"uzs"
        },
        "education_form_resume":{
            "10":"Дневная/Очная",
            "20":"Вечерняя",
            "30":"Очно-заочная",
            "40":"Заочная",
            "50":"Экстернат",
            "60":"Дистанционная"
        },
        "education_type_resume":{
            "2":"Высшее",
            "3":"Неполное высшее",
            "4":"Среднее специальное",
            "5":"Среднее",
            "6":"Учащийся школы",
            "7":"  Бакалавр",
            "8":"  Магистр",
            "9":"  Кандидат наук",
            "10":"  Доктор наук"
        },
        "work_type":{
            "2":"Полная занятость",
            "3":"Частичная занятость",
            "4":"Временная"
        },
        "citizenship":{
            "1":"Россия",
            "9":"Украина",
            "10":"Беларусь",
            "11":"Молдова",
            "12":"Грузия",
            "13":"Армения",
            "14":"Азербайджан",
            "15":"Казахстан",
            "16":"Узбекистан",
            "17":"Таджикистан",
            "18":"Кыргызстан",
            "19":"Туркменистан",
            "20":"Латвия",
            "21":"Литва",
            "22":"Эстония",
            "23":"Абхазия",
            "24":"Южная Осетия",
            "1000":"Дальнее зарубежье"
        },
        "moveable":{
            "1": "живет в регионе или готов к переезду куда-либо",
            "2": "живет в регионе или готов к переезду в него",
            "3": "не живет в регионе, но готов к переезду в него",
            "4": "живет в регионе"
        },
        "business_trip":{
            "0":"не имеет значения",
            "1":"не готов",
            "2":"готов"
        },
        "published_resume":{
            "0":"Закрытый доступ",
            "1":"Открытый доступ",
            "4":"Отказано в публикации",
            "10":"Выборочный доступ",
            "100":"Черновик"
        },
        "social_links_resume":{
            "1":"Вконтакте",
            "2":"Твиттер",
            "3":"Фейсбук",
            "4":"Линкедин",
            "6":"Гугл+",
            "7":"Личный сайт",
            "8":"Github",
            "9":"Яндекс",
            "10":"Mail.RU",
            "14":"Apple ID",
            "15":"Telegram",
            "16":"Яндекс Дзен",
            "17":"YouTube",
        },
        "period": {
            "0":"все время",
            "1":"24 часа",
            "3":"3 дня",
            "7":"неделю",
            "14":"2 недели",
            "30":"1 месяц",
            "60":"2 месяца"
        }
}

    while len(params_hh) < 18 and len(params_sj):
        print("Итак, давайте создадим шаблон для многократного использования")
        usr_choice = input("Переданное значение ищется в полях вакансии")
        params_hh['text'] = usr_choice
        params_sj['keyword'] = usr_choice

        params_sj['experience'], params_hh['experience'] = get_exp()

        params_sj['id_client'] = input("Айди ID компании вакансии")  # ID компании
        params_hh['employer_id'] = input("Идентификатор работодателя")  # Необходимо передавать id из справочника

    params_hh['search_field'] = input("") #Справочник с возможными значениями: vacancy_search_fields в / dictionaries.По умолчанию, используются все поля. Можно указать несколько значениq
    params_hh['employment'] = input("Тип занятости") # Необходимо передавать id из справочника
    params_hh['schedule'] = input("График работы") # Необходимо передавать id из справочника
    params_hh['area'] = input("Регион") # Необходимо передавать id из справочника
    params_hh['metro'] = input("Метро") # Необходимо передавать id из справочника
    params_hh['currency'] = input("Код валюты") # Справочник с возможными значениями: currency(ключ code) в / dictionaries.                                     # Имеет смысл указывать только совместно с параметром salary
    params_hh['salary'] = input("Размер заработной платы") # Число размер заработной платы, если не указан код валюты то ставится RUR
    params_hh['only_with_salary'] = input("Показывать только вакансии с зп true/false")
    params_hh['label'] = input("Фильтр по меткам вакансий ") # Необходимо передавать id из справочника
    params_hh['date_from'] = input("С какого периода искать вакансии") #Значение указывается в формате ISO 8601 - YYYY - MM - DD
    params_hh['date_to'] = input("")                                   #или YYYY - MM - DDThh: mm:ss±hhmm.
    params_hh['order_by'] = input("Сортировка списка вакансий ") # Справочник vacancy_search_order
    params_hh['no_magic'] = input("Автоматическое преобразование запроса  ИСПОЛЬЗОВАТЬ ОСТОРОЖНО true / false")
    params_hh['accept_temporary'] = input("Искать только подработку true / false")

    params_sj['id_vacancy'] = input("Айди конкретной вакансии") # int
    params_sj['ids'] = input("Массив, состоящий из ID вакансий") # Массив, состоящий из ID вакансий. Может содержать не более 500 id.
    params_sj['sort_new'] = input("НЕ ПОНЯЛ") # При передаче этого параметра вакансии будут сортироваться особым образом - новые сверху НЕ ПОНЯЛ
    params_sj['keyword'] = input("Ключевое слово. Ищет по всей вакансии") # строка
    params_sj['keywords'] = input("Расширенный поиск ключевых слов.") # array Каждый элемент массива есть массив со следующими параметрами:
                                                                      #Название	Тип	Can
    """ 1 — должность 2 — название компании 3 — должностные обязанности 4 — требования к квалификации 5 — условия работы 10 — весь текст"""
    params_sj['payment_from'] = input("Сумма оклада от") # int
    params_sj['payment_to'] = input("Сумма оклада до") # int
    params_sj['no_agreement'] = input("Не показывать оклад «по договоренности» (установите параметр в 1)") # int
    params_sj['town'] = input("Название города или его ID") # string|int
    params_sj['m'] = input("Массив с ID метро") # int
    params_sj['t'] = input("Массив с ID городов") # int
    params_sj['o'] = input("Массив с ID областей") # int
    params_sj['c'] = input("Массив с ID стран") # int
    params_sj['type_of_work'] = input("Тип занятости. Возможные значения.") # int
    params_sj['age'] = input("Возраст") # int
    params_sj['gender'] = input("Пол. Возможные значения.") # int
    params_sj['education'] = input("Образование. Возможные значения.") # int
    params_sj['experience'] = input("Опыт работы. Возможные значения.") # int
    params_sj['driving_licence'] = input("111111111") # int
    params_sj['driving_licence'] = input("Наличие водительских прав.") # array Содержит одно или несколько наименований категорий прав: ['A', 'B', 'C', 'D', 'E']
    params_sj['driving_particular'] = input("наличие водительских прав имеет значение") # int int=1
    params_sj['language'] = input("Иностранный язык.") # int Значения можно также получить в справочниках (language).
    params_sj['lang_level'] = input("Уровень владения иностранным языком. Возможные значения.") # int
    params_sj['languages_particular'] = input("Показывать вакансии, в которых выбранный язык имеет значение (установите параметр в 1)") # int
    params_sj['nolang'] = input("Не показывать вакансии со знанием языков (установите параметр в 1") # int


def fast_search():
    params_hh = {}
    params_sj = {}
    usr_choice = input("Переданное значение ищется в полях вакансии")
    params_hh['text'] = usr_choice
    params_sj['keyword'] = usr_choice
    return params_hh, params_sj


def get_exp():
    experience_sj = {
        "1": "без опыта",
        "2": "от 1 года",
        "3": "от 3 лет",
        "4": "от 6 лет"}

    experience_hh = {
        "1": "noExperience",
        "2": "between1And3",
        "3": "between3And6",
        "4": "moreThan6"
        }
    print("Какой у вас опыт работы?")
    i = 1
    for value in experience_sj.values():
        print(i, value)
        i += 1
    usr_choice = input(" \n--->")
    return experience_hh[usr_choice], experience_sj[usr_choice]

def get_emp_id():
    print("Давайте выберем компанию, как будем искать, по названиям или по параметрам?")
    usr_choice = input("[1] - по названиям\n[2] - по параметрам\n--->")
    company = []
    if usr_choice == "1":
        while True:
            usr_choice = input("Введите название компании\nВведите [0] - чтобы завершить--->")
            if usr_choice != "0":
                company.append(usr_choice)
            else:
                break
            pass # добавить reqvests получающий список компаний или мб не надо? хз хз
    elif usr_choice == "2":
        params = {}
        # Надо попытаться сделать класс ошибок, которые проверят ввод пользователя, вводит ли он в том виде, что хочу я
        params['keyword'] = input("Название фирмы или часть её названия, а так же url компании \n--->")
        params['town'] = input("Название города \n--->")
        params['all'] = int(input("Выводить ли компании без вакансий (поставьте параметр в 1)\n-->"))
        req = requests




    ''''"""
    params_hh['text'] = input("Переданное значение ищется в полях вакансии")
 params_hh['search_field'] = input("") #Справочник с возможными значениями: vacancy_search_fields в / dictionaries.По умолчанию, используются все поля. Можно указать несколько значениq
    params_hh['experience'] = input("Опыт работы ") # Необходимо передавать id из справочника
    params_hh['employment'] = input("Тип занятости") # Необходимо передавать id из справочника
    params_hh['schedule'] = input("График работы") # Необходимо передавать id из справочника
    params_hh['area'] = input("Регион") # Необходимо передавать id из справочника
    params_hh['metro'] = input("Метро") # Необходимо передавать id из справочника
    params_hh['employer_id'] = input("Идентификатор работодателя") # Необходимо передавать id из справочника
    params_hh['currency'] = input("Код валюты") # Справочник с возможными значениями: currency(ключ code) в / dictionaries.                                     # Имеет смысл указывать только совместно с параметром salary
    params_hh['salary'] = input("Размер заработной платы") # Число размер заработной платы, если не указан код валюты то ставится RUR
    params_hh['only_with_salary'] = input("Показывать только вакансии с зп true/false")
    params_hh['label'] = input("Фильтр по меткам вакансий ") # Необходимо передавать id из справочника
    params_hh['date_from'] = input("С какого периода искать вакансии") #Значение указывается в формате ISO 8601 - YYYY - MM - DD
    params_hh['date_to'] = input("")                                   #или YYYY - MM - DDThh: mm:ss±hhmm.
    params_hh['order_by'] = input("Сортировка списка вакансий ") # Справочник vacancy_search_order
    params_hh['no_magic'] = input("Автоматическое преобразование запроса  ИСПОЛЬЗОВАТЬ ОСТОРОЖНО true / false")
    params_hh['accept_temporary'] = input("Искать только подработку true / false")

    params_sj['id_vacancy'] = input("Айди конкретной вакансии") # int
    params_sj['ids'] = input("Массив, состоящий из ID вакансий") # Массив, состоящий из ID вакансий. Может содержать не более 500 id.
    params_sj['id_client'] = input("Айди ID компании вакансии") # ID компании
    params_sj['sort_new'] = input("НЕ ПОНЯЛ") # При передаче этого параметра вакансии будут сортироваться особым образом - новые сверху НЕ ПОНЯЛ
    params_sj['keyword'] = input("Ключевое слово. Ищет по всей вакансии") # строка
    params_sj['keywords'] = input("Расширенный поиск ключевых слов.") # array Каждый элемент массива есть массив со следующими параметрами:
                                                                      #Название	Тип	Can
1 — должность 2 — название компании 3 — должностные обязанности 4 — требования к квалификации 5 — условия работы 10 — весь текст
    params_sj['payment_from'] = input("Сумма оклада от") # int
    params_sj['payment_to'] = input("Сумма оклада до") # int
    params_sj['no_agreement'] = input("Не показывать оклад «по договоренности» (установите параметр в 1)") # int
    params_sj['town'] = input("Название города или его ID") # string|int
    params_sj['m'] = input("Массив с ID метро") # int
    params_sj['t'] = input("Массив с ID городов") # int
    params_sj['o'] = input("Массив с ID областей") # int
    params_sj['c'] = input("Массив с ID стран") # int
    params_sj['type_of_work'] = input("Тип занятости. Возможные значения.") # int
    params_sj['age'] = input("Возраст") # int
    params_sj['gender'] = input("Пол. Возможные значения.") # int
    params_sj['education'] = input("Образование. Возможные значения.") # int
    params_sj['experience'] = input("Опыт работы. Возможные значения.") # int
    params_sj['driving_licence'] = input("111111111") # int
    params_sj['driving_licence'] = input("Наличие водительских прав.") # array Содержит одно или несколько наименований категорий прав: ['A', 'B', 'C', 'D', 'E']
    params_sj['driving_particular'] = input("наличие водительских прав имеет значение") # int int=1
    params_sj['language'] = input("Иностранный язык.") # int Значения можно также получить в справочниках (language).
    params_sj['lang_level'] = input("Уровень владения иностранным языком. Возможные значения.") # int
    params_sj['languages_particular'] = input("Показывать вакансии, в которых выбранный язык имеет значение (установите параметр в 1)") # int
    params_sj['nolang'] = input("Не показывать вакансии со знанием языков (установите параметр в 1") # int
 
 
order_field	<string:date|payment>	Сортировка: date - по дате публикации, payment - по сумме оклада. По умолчанию - date.
order_direction	<string:asc|desc>	Направление сортировки: asc - прямая, desc - обратная. По умолчанию - desc.
period	int	Период публикации.
Список возможных значений:
  1 — 24 часа
  3 — 3 дня
  7 — неделя
  0 — за всё время
    """''''


