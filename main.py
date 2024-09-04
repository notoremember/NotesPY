import csv
import datetime
import os
import sys


class Note:
    def __init__(self, id, title, body, created, updated):
        self.id = id
        self.title = title
        self.body = body
        self.created = created
        self.updated = updated

    def __str__(self):
        created_str = self.created.strftime("%Y-%m-%d %H:%M:%S")
        updated_str = self.updated.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.id};{self.title};{self.body};{created_str};{updated_str}"

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", newline="") as f:
                reader = csv.reader(f, delimiter=";")
                for row in reader:
                    id = int(row[0])
                    title = row[1]
                    body = row[2]
                    created = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                    updated = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
                    note = Note(id, title, body, created, updated)
                    self.notes.append(note)
                    
    def save_notes(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.created, note.updated])

    def create_note(self, title, body):
        id = max([note.id for note in self.notes]) + 1 if self.notes else 1
        created = datetime.datetime.now()
        updated = datetime.datetime.now()
        note = Note(id, title, body, created, updated)
        self.notes.append(note)
        return note

    def read_notes(self):
        return self.notes

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def update_note(self, id, title=None, body=None):
        note = self.get_note_by_id(id)
        if note:
            note.title = title if title is not None else note.title
            note.body = body if body is not None else note.body
            note.updated = datetime.datetime.now()
            return note
        else:
            return None

    def delete_note(self, id):
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)

def create():
    title = input("Введите заголовок заметки ")
    body = input("Введите тело заметки ")
    note = note_manager.create_note(title, body)
    print("Заметка сохранена")


def read_notes():
    notes = note_manager.read_notes()
    if notes:
        for note in notes:
            print(f"{note.id}: {note.title}\n{note.body}\n")
    else:
        print("заметок пока нет")

def update_note():
    id = int(input("ведите ID/номер заметки для редактирования "))
    note = note_manager.get_note_by_id(id)
    if note:
        title = input(f"текущий заголовок заметки: {note.title}\nвведите новый заголовок заметки (оставьте пустым, чтобы оставить текущий): ")
        body = input(f"текущее тело заметки: {note.body}\nвведите новое тело заметки (оставьте пустым, чтобы оставить текущее): ")
        updated_note = note_manager.update_note(id, title, body)
        if updated_note:
            print(f"заметка с ID/номером {id} успешно обновлена")
        else:
            print(f"не удалось обновить заметку с ID {id}")
    else:
        print(f"заметка с ID {id} не найдена")


def delete_note():
    id = int(input("введите ID заметки для удаления: "))
    note_manager.delete_note(id)
    print(f"заметка с ID {id} успешно удалена")

if __name__ == "__main__":
    print("Добро пожаловать в менеджер заметок!\n\
    Список команд: \n\
    create - создать/добавить заметку\n\
    read - просмотреть заметку\n\
    update - обновить/добавить что-то в заметку\n\
    delete - удалить заметку \n\
    exit - завершить работу менеждера\n")
    note_manager = NoteManager("notes.csv")

    while True:
        command = input("Введите команду: ")

        if command == "create":
            create()
        elif command == "read":
            read_notes()
        elif command == "update":
            update_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            sys.exit()
        else:
            print("Некорректная команда")
