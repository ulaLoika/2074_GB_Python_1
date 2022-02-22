from os import path, mkdir
from os.path import join, exists, abspath, dirname

def my_project_func (path, directories):
   for key, value in directories.items():
      main = join(path, key)
      if not exists(main):
          mkdir(main)
      for el in value:
         sub = join(main, el)
         if not exists(sub):
            mkdir(sub)

main = dirname(abspath(__file__))
print ()
print (main)
folders_tree = {'my_project': ['settings', 'mainapp', 'authapp']}
if __name__ == '__main__':
   my_project_func(main, folders_tree)
