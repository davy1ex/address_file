import pickle
from abc import *
import os

add_book = {}
my_file = 'add_file.data'
print('\nпуть у файлу:', os.path.abspath(my_file))


def check():
    try:
        ff = open(my_file, 'rb')
        ff.close()
    except FileNotFoundError:
        with open(my_file, 'w'):
            print('создан файл: ', my_file)
    except EOFError:
        print()


check()


def show_file():
    ff = open(my_file, 'rb')
    try:
        for i in range(len(my_file)):
            d = pickle.load(ff)
            print(d)
    except EOFError:
        pass
    ff.close()


show_file()


class AddressMember(metaclass=ABCMeta):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        # print('создан участник: {}'.format(self.name))

    @staticmethod
    def show1(self):
        print("\nимя -- {0}; номер -- {1}\n".format(self.name, self.number), end='')


class Member(AddressMember):
    #
    def __init__(self, name, number):
        AddressMember.__init__(self, name, number)
        print("создан участник: имя -- {}; номер -- {}".format(self.name, self.number))

    def show(self):
        AddressMember.show1(self)


def contacts():
    for k, v in add_book.items():
        print("имя: |{0}| -- номер: |{1}|".format(k, v))


contacts()
print()


def new_member():
    n_name = input("имя: ")
    # n_num = int(input("номер: "))
    while True:
        try:
            n_num = int(input('введите номер: '))
            break
        except ValueError:
            print('номер - это цифры, а не буквы!')

    if n_name in add_book:
        print('Это имя уже существует, придумайте другое!')
        n_name = input("имя: ")
    elif n_num in add_book.values():
        print('Этот номер уже существует!')
        exit('end.')
    mem = Member(n_name, n_num)
    print()
    mem.show()
    add_book[n_name] = n_num


while True:
    print('хотите еще кого-то добавить в файл? Y[да] -- N[нет]')
    question = input('\n$: ')
    if question == 'N' or question == 'n':
        break
    elif question == 'Y' or question =='y':
        new_member()
        f = open(my_file, 'ab')
        pickle.dump(add_book, f)
        f.close()
    else:
    	pass

print()
check()
contacts()
show_file()
print('сюда можно что-то дописать...')
del_all = input('удалить все содержимое? (сохранится последний участник) Y/N\n')
if del_all == 'y' or del_all == 'Y':
    f = open(my_file, 'wb')
    pickle.dump(add_book, f)
    f.close()

show_file()
print('\nend?')
