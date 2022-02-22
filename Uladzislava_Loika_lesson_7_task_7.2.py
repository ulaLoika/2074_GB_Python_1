from os import path, mkdir
from os.path import join, exists, abspath, dirname

'''вторая рекурсивная функция, которая заходит в циклы'''
def create_folder(path, name, sub_folders):
    main = join(path, name)
    if not exists(main):
        if '.' in name:
            open(main, 'a').close()
        else:
            mkdir(main)

    if sub_folders:
        for dir in sub_folders:
            if type(dir) is str:
                create_folder(main, dir, None)
            if type(dir) is dict:
                create_dir(main, dir)

'''создаем рекурсивную фнкицю, которая будет заходить в  циклы
и выходить из них, пока не исчерпает себя'''

def create_dir(path, directories):
    for key, value in directories.items():
        create_folder(path, key, value)

'''определяем место создания главной директории и создаем словарь с деревом'''
main = dirname(abspath(__file__))
settings = {'settings':['__init__.py', 'dev.py', 'prod.py']}
mainapp = {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html']}]}]}
authapp = {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]}]}
folders_tree = {'my_project': [settings, mainapp, authapp]}

if __name__ == '__main__':
    create_dir(main, folders_tree)