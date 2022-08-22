'''
ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";
6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать) и сохранить туда содержимое рабочей директории следующим образом: сначала все файлы, потом все папки, пример как может выглядеть итоговый файл.


files: victory.py, bill.py, main.py
dirs: modules, packages
'''


import os
import shutil
import sys
import pickle
from use_functions import my_bill
from borndayforewer import victory_birth_date_selebrity
FILE_NAME_LISTDIR = 'listdir.txt'
file_name = []
dir_name = []

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_dir = input('Введите название папки: ')
        if not os.path.exists(name_dir):
            os.mkdir(name_dir)
        else:
            print('Такая папка уже существует: ')
    elif choice == '2':
        name_dir = input('введите название папки: ')
        if  os.path.exists(name_dir):
            os.rmdir(name_dir)
        else:
            print('Такой папки не существует: ')
    elif choice == '3':
        name_dir1 = input('введите название копируемоей папки: ')
        name_dir2 = input('введите название новой  папки: ')
        if os.path.exists(name_dir1) and not os.path.exists(name_dir2):
            shutil.copy(name_dir1, name_dir2)
        else:
            print('либо не существует такая копируемая папка, либо уже существует папка с названием новой: ')
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        content = os.listdir()
        for direct in content:
            if os.path.isdir(direct):
                print(direct)
    elif choice == '6':
        content = os.listdir()
        for file in content:
            if os.path.isfile(file):
                print(file)
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Ivan Shestopalov')
    elif choice == '9':
        victory_birth_date_selebrity()
    elif choice == '10':
        my_bill()
    elif choice == '11':
        print(f'Вы находитесь {os.getcwd()}')
        new_directory = input('введите название рабочей папки: ')
        os.mkdir(new_directory)
        path = os.path.join(os.getcwd(), new_directory)
        os.chdir(path)
        print(f'А теперь вы находитесь {os.getcwd()}')
    elif choice == '12':
        content = os.listdir()
        for direct in content:
            if os.path.isdir(direct):
                dir_name.append(direct)
            if os.path.isfile(direct):
                file_name.append(direct)
        with open(FILE_NAME_LISTDIR, 'wb') as f:
            pickle.dump(dir_name, f)
            pickle.dump(file_name, f)
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')