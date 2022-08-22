'''
ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
'''
import os
import pickle

FILE_NAME_BUY = 'buy_pickle.txt'
FILE_NAME_MONEY = 'money_pickle.txt'
money_all = 0
buy_history = []
if os.path.exists(FILE_NAME_BUY):
    with open(FILE_NAME_BUY, 'rb') as f:
        buy_history = pickle.load(f)
if os.path.exists(FILE_NAME_MONEY):
    with open(FILE_NAME_MONEY, 'rb') as f:
        money_all  = int(pickle.load(f))

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        money = int(input('введите сумму'))
        money_all += money
    elif choice == '2':
        money = int(input('введите сумму покупки'))
        if money > money_all:
            print('недостаточно средств')
        else:
            money_all -= money
            buy = input('введите название покупки')
            buy_history.append((buy, money))

    elif choice == '3':
        print(buy_history)
    elif choice == '4':
        with open(FILE_NAME_BUY, 'wb') as f:
            pickle.dump(buy_history, f)
        with open(FILE_NAME_MONEY, 'wb') as f:
            pickle.dump(money_all, f)
        break
    else:
        print('Неверный пункт меню')