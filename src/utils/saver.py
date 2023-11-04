import json
import pandas as pd  # Для формирования датафрейма с результатами


def saver_to_js(data, path):
    """
    сделать так чтобы получилось несколько файлов - страниц с результатами, по 50 вакансий на каждой
    :param data:
    :param path:
    :return:
    """
    file_name = input("Как назовем файл с результатами в  json? --->")
    with open(path + f"/results/{file_name}.json", "w") as file:
        capitals_json = json.dumps(data, ensure_ascii=False)
        file.write(capitals_json)
        #json.dump(data, file)
        print("Успешно сохранил Json")
        file.close()


def updater(data, path):
    with open(path, 'a') as file:
        capitals_json = json.dumps(data, ensure_ascii=False)
        file.write(capitals_json)


def saver_to_txt(data, path):
    file_name = input("Как назовем TXT файл? --->")
    with open(path + f"/results/{file_name}.txt", "a") as file:
        file.write(str(data))
        print("Успешно сохранил TXT")


def saver_to_exel():
    df = pd.DataFrame(dt, columns=[
        'id',
        'premium',
        'name',
        'department_name',
        'has_test',
        'response_letter_required',
        'area_id',
        'area_name',
        'salary_from',
        'salaty_to',
        'type_name',
        'address_raw',
        'response_url',
        'sort_point_distance',
        'published_at',
        'created_at',
        'archived',
        'apply_alternate_url',
        'insider_interview',
        'url',
        'alternate_url',
        'relations',
        'employer_id',
        'employer_name',
        'snippet_requirement',
        'snippet_responsibility',
        'contacts',
        'schedule_name',
        'working_days',
        'working_time_intervals',
        'working_time_modes',
        'accept_temporary'
    ])
    df.to_excel('result_2gis.xlsx')


