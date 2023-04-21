#пользовательский интерфейс
from counter import counter
from Note import Main_Note
from commands import  get_notice, find_notice, find_notice_date, print_date,\
del_notice,change_notice,add_notice
def menu(num):
  if numb == 1:
    topic = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    date = print_date()
    note = Main_Note(str(counter()),topic,text,date)
    add_notice(note)
  elif numb == 2:
    get_notice()
  elif numb == 3:
    id = input('Введите ID заметки: ')
    find_notice(id)
  elif numb == 4:
    date = input('Введите дату для поиска заметки: ')
    find_notice_date(date)
  elif numb == 5:
      id = input('Введите ID контакта для изменения: ')
      change_notice(id)
  elif numb == 6:
    id = input('Введите ID контакта для удаления: ')
    del_notice(id)
while True:
  numb = int(input('Введите 1 - для добавления заметки; 2 - для печати всех заметок;'' 3 - для поиска \
заметки по ID;''4 - для поиска заметки по дате;''5 - для \
изменения заметки;'' 6 - для удаления заметки;''7 - для выхода из программы: '))
  if numb == 7:
    break 
  menu(numb)