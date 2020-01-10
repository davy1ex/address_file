import pickle
from abc import *
import os


def check():
    try:
        ff = open(my_file, 'rb')
        ff.close()
    except FileNotFoundError:
        with open(my_file, 'w'):
            print('создан файл: ', my_file)
    except EOFError:
        print()


def show_file():
    # ff = open(my_file, 'rb')
    with open(my_file, 'rb') as ff:
        try:
            for i in range(len(my_file)):
                d = pickle.load(ff)
                print(d)
        except EOFError:
            pass


class AddressMember(metaclass=ABCMeta):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        print('создан участник: {}'.format(self.name))

    @abstractmethod
    def show(self):
        print("\nимя -- {0}; номер -- {1}\n".format(self.name, self.number), end='')


class Member(AddressMember, ABC):
    def __init__(self, name, number):
        super(Member, self).__init__(name, number)

    def show(self):
        super(Member, self).show()


def contacts():
    for k, v in add_book.items():
        print("имя: |{0}| -- номер: |{1}|".format(k, v))


def new_member():
    n_name = input("имя: ")
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
        exit('end.\n')
    mem = Member(n_name, n_num)
    mem.show()
    add_book[n_name] = n_num


if __name__ == '__main__':
    add_book = {}
    my_file = 'add_file.data'
    
    print('путь у файлу:', os.path.abspath(my_file))
    
    check()
    show_file()
    contacts()
    print()

    while True:
        answer = input('хотите еще кого-то добавить в файл? y/n\n>: ')
        if answer in ['n']:
            break
        elif answer in ['y', '']:
            new_member()
            with open(my_file, 'ab') as f:
                pickle.dump(add_book, f)
            # f.close()
        else:
            pass

    print()
    check()
    contacts()
    show_file()
    
    del_all = input('сюда можно что-то дописать...\nудалить все содержимое? (сохранится последний участник) y/n\n')
    
    if del_all == 'y' or del_all == 'Y':
        f = open(my_file, 'wb')
        pickle.dump(add_book, f)
        f.close()

    show_file()
    print('\nend?')