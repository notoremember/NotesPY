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