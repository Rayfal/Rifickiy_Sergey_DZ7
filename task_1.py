"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
 как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
 можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""

import os

my_dir = {'my_project':['settings', 'mainapp', 'adminapp', 'authapp']}
for key, val in my_dir.items():
    if os.path.exists(key):
        print(f'Папка {key} уже существует')
    else:
        for vals in val:
            val_dir = os.path.join(key, vals)
            os.makedirs(val_dir)