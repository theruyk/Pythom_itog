#методы основных команд по работе с заметками
from counter import counter
import datetime
import os
def get_notice(): #вывод всех заметок
  with open ('Notice.txt', 'r', encoding='utf8') as file:
    for line in file:
      print (line)

def find_notice(id): #поиск заметки по id и вывод ее
  with open('Notice.txt', 'r') as file:
      for line in file:
          if line.startswith(f'{id};'):
              print(line)


def add_notice (note): # добавление заметки
  with open ('Notice.txt', 'a', encoding='utf8') as file:
    file.write(note.str_1())


def find_notice_date(date): #поиск заметки по date и вывод ее



def del_notice(id):
    with open('Notice.txt', 'r') as file:
        with open('temp.txt', 'w') as temp:
            for line in file:
                if line.startswith(f'{id};'):
                    continue
                temp.write(line)
    file.close()
    temp.close()
    os.replace('temp.txt', 'Notice.txt')



def change_notice(id):

    file.write(input ('Введите новый текст заметки: ')) 

def print_date():
    now = datetime.datetime.now()
    timestamp = now.strftime("%d.%m.%Y")
    return timestamp