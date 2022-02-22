import shutil
import os

for root, dirs, files in os.walk(os.path.dirname(os.path.abspath('my_project'))):
    for dir in dirs:
        if dir == 'templates':
            shutil.copytree(os.path.join(root,dir), 'my_project/templates', dirs_exist_ok=True)