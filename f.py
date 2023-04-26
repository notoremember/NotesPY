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
