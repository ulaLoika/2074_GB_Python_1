import sys
import json

'''Создаем файлы csv и закидываем в них данные как в условии задачи.'''

users = ('Иванов,Иван,Иванович\nПетров,Петр,Петрович\nСергеев Сергей Сергеевич')
hobby = ('скалолазание,охота\nгорные лыжи')
with open ('users.csv', 'w', encoding = 'utf-8') as f:
    f.write(users)
with open ('hobby.csv', 'w', encoding = 'utf-8') as f:
    f.write(hobby)


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    list_users = []
    with open(path_users_file, 'r', encoding= 'utf-8') as f:
        for text in f:
            list_users.append(text.replace(',', ' ').strip('\n'))

    list_hobby = []
    with open (path_hobby_file, 'r', encoding='utf-8') as f:
        for text in f:
            list_hobby.append(text.strip('\n'))

    counter = 0
    users_dict = {}
    if len(list_users) > len(list_hobby):
        list_hobby.append(None)
    if len(list_users) == len(list_hobby):
        for el in list_users:
            users_dict[el] = list_hobby[counter]
            counter += 1
    else:
        users_dict = sys.exit(1)

    return users_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
print (dict_out)
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)