from src.hh_api.hh_search import HeadHanterAPI
from src.sj_api.sj_search import SuperJobAPI
from src.usrs.mk_user import User
from src.utils.saver import saver_to_js
from src.vacancy.vacancy import Vacancy

def interface():
    """

    Нужно сделать так, чтобы юзр постепенно добавлял фильтры и в любой момент мог остановиться
    большой опросник запускающий подпрограммы которые уже дополняют словарь?????
    :return:
    """
    usr_name = input("Добрый день, представьтесь\n"
                     "---> ")
    user = User(usr_name)


    # В зависимости от ответа запускаем метод поиска в HH или SJ
    if user.choice == "HH_ready":
        request = HeadHanterAPI(user.path_blueprint)
        all_data = request.data
        saver_to_js(all_data, user.directory)
        Vacancy.instantiate_from_json(data=all_data)
        #saver_to_txt(result, user.directory)


    elif user.choice == "HH_new":
        request = HeadHanterAPI(user.hh_new_params)
        all_data = request.data
        saver_to_js(all_data, user.directory)
        Vacancy.instantiate_from_json(data=all_data)

    elif user.choice == "SJ_ready" or user.choice == "SJ_new":
        request = SuperJobAPI(user.path_blueprint)
        all_data = request.data
        saver_to_js(all_data, user.directory)
        Vacancy.instantiate_from_json(data=all_data)



    elif user.choice == "RES":
        Vacancy.instantiate_from_json(path_file=user.path_results)



    while True:
        print("Что делаем сейчас?")
        user_answ = input("[1] Выводить по одной на консоль для добавления в избранное?\n"
                          "[2] Отсортировать по зп/дате?\n"
                          f"[3] - Выбрать другой файл с результатами для анализа *{len(user.list_results)} - результатов*\n"
                          "[0] Выйти\n"
                          "---> ")
        if user_answ == "1":
            user.favorite_updater(vaca_str=Vacancy.console_deco(), dict_characters=Vacancy.dict_characters)
        elif user_answ == "2":
            Vacancy.all_sort()
        elif user_answ == "3":
            if len(user.list_results) > 0:
                user.path_results = user.results_selector()
                Vacancy.all = []
                Vacancy.instantiate_from_json(path_file=user.path_results)
                user.favorite_updater(vaca_str=Vacancy.console_deco(), dict_characters=Vacancy.dict_characters)
            else:
                print("Ну сказано же, 0 результатов")
        elif user_answ == "0":
            break



#name, city, salary, requirement, responsibility, professional_roles, employment):  # добавить время!!!!!!!!!


interface()