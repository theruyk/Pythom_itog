#методы основных команд по работе с заметками
from counter import counter
import datetime
import os
from Note import Main_Note
def get_notice(): #вывод всех заметок
  with open ('Notice.json', 'r', encoding='utf8') as file:
    for line in file:
      print (line)

def find_notice(id): #поиск заметки по id и вывод ее
  with open('Notice.json', 'r') as file:
      for line in file:
          if line.startswith(f'{id};'):
              print(line)


def add_notice (note): # добавление заметки
  with open ('Notice.json', 'a', encoding='utf8') as file:
    file.write(note.str_1())


def find_notice_date(date): #поиск заметки по дате и ее вывод 
    with open('Notice.json', 'r', encoding='utf-8') as file:
        found = False
        for line in file:
            data = line.split(';')
            note_date = datetime.datetime.strptime(data[3].strip(), '%d.%m.%Y') 
            if note_date.date() == datetime.datetime.strptime(date, '%d.%m.%Y').date():
                found = True 
                print(line.strip()) 
        if not found: 
            print('Заметка с этой датой не найдена.')

def del_notice(id): #удаление заметки
    with open('Notice.json', 'r') as file:
        with open('temp.json', 'w') as temp:
            for line in file:
                if line.startswith(f'{id};'):
                    continue
                temp.write(line)
    file.close()
    temp.close()
    os.replace('temp.json', 'Notice.json')



def change_notice(id):#изменение заметки
    notes = []
    with open('Notice.json', 'r', encoding='utf8') as file:
        for line in file:
            data = line.strip().split(";")
            if len(data) == 4:
                note = Main_Note(data[0], data[1], data[2], data[3])
                notes.append(note)
            else:
                print("Ошибка: строка имеет неправильный формат.")

    for note in notes:
        if note.id == id:
            topic = input('Введите новый заголовок заметки: ')
            text = input('Введите новый текст заметки: ')
            date = print_date()
            note.topic = topic
            note.text = text
            note.date = date
            with open('Notice.json', 'w', encoding='utf8') as file:
                for note in notes:
                    file.write(f'{note.id};{note.topic};{note.text};{note.date}\n')
            break
    else:
        print('Заметка с таким ID не найдена.')

def print_date(): #добавление даты в заметку
    now = datetime.datetime.now()
    timestamp = now.strftime("%d.%m.%Y")
    return timestamp