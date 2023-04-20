# класс сущности заметка


class Main_Note:

    def __init__(self, note_id, topic, text, date):
        self.id = note_id
        self.topic = topic
        self.text = text 
        self.date = date

    def str_1(self):
        return f"{self.id}; {self.topic}; {self.text}; {self.date}\n"

