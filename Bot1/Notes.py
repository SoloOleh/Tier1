import re
import json
from collections import UserDict

class Notebook(UserDict):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_note(self, note):
        self.data[note.id] = note

    def dump(self, file):
        with open(file, 'w+') as write_file:
            dump_dict = {self.name: {}}
            for id, note in self.data.items():
                dump_dict[self.name][str(id)] = {
                    "keyword": note.keyword,
                    "note": note.note
                }
            json.dump(dump_dict, write_file)

    def load(self, file):
        with open(file, 'r') as read_file:
            data = json.load(read_file)
            self.name = list(data.keys())[0]
            for id, note_info in data[self.name].items():
                note_ = Note(note_info["note"])
                note_.keyword = note_info.get("keyword", [])
                self.add_note(note_)

    def delete(self, id):
        if id in self.data:
            del self.data[id]

    def find(self, request_lst):
        if isinstance(request_lst, str):
            request_lst = request_lst.split(" ")
        res_lst = []
        for tag in request_lst:
            for id, note in self.data.items():
                if re.search(tag, " ".join(note.keyword).lower()) or re.search(tag, note.note.lower()):
                    if note not in res_lst:
                        res_lst.append(note)
        return res_lst

class Note:
    id_counter = 0

    def __init__(self, note):
        Note.id_counter += 1
        self.id = Note.id_counter
        self.note = note
        self.keyword = self.get_keywords(note)

    def get_keywords(self, note):
        keywords = re.findall("#[a-zA-Zа-яА-Я0-9_\-]+", note)
        return [keyword.strip("#") for keyword in keywords]

# Example of usage:
# Create a notebook
notebook = Notebook("My Notebook")

# Add a note
note = Note("This is a test note #example #test")
notebook.add_note(note)

# Find notes by keywords
found_notes = notebook.find("example")

# Dump notebook to a file
notebook.dump("notebook.json")

# Load notebook from a file
notebook.load("notebook.json")

# Delete a note by id
notebook.delete(note.id)
