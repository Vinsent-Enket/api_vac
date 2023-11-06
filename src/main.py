from src.services_api_classes import HeadHanterAPI, SuperJobAPI
from src.mk_user import User
from src.vacancy import Vacancy


def main():
    """

    Нужно сделать так, чтобы юзр постепенно добавлял фильтры и в любой момент мог остановиться
    большой опросник запускающий подпрограммы которые уже дополняют словарь?????
    :return:
    """
    usr_name = input("Добрый день, представьтесь\n"
                     "---> ")
    user = User(usr_name)

    HH_response = HeadHanterAPI(user.req_text)
    SJ_response = SuperJobAPI(user.req_text)
    Vacancy.instantiate_from_data(HH_response.data, SJ_response.data)
    while True:
        print("\nЧто делаем сейчас?")
        user_answ = input("[1] Выводить по одной на консоль для добавления в избранное?\n"
                          "[2] Отсортировать по зп/дате?\n"
                          "[4] Новый запрос\n"
                          "[0] Выйти\n"
                          "---> ")
        if user_answ == "1":
            user.favorite_updater(vaca_str=Vacancy.choice_favorite(), dict_characters=Vacancy.dict_characters)
        elif user_answ == "2":
            Vacancy.all_sort()
        elif user_answ == "3":
            new_response_text = input("Какое новое слово?\n-->")
            HH_response = HeadHanterAPI(new_response_text)
            SJ_response = SuperJobAPI(new_response_text)
            Vacancy.instantiate_from_data(HH_response.data, SJ_response.data)
        elif user_answ == "0":
            break
        else:
            print("Выбирай внимательно!")


main()
