import json
import os
import re
from typing import Dict, List

class Note:
    id_counter = 0

    def __init__(self, content: str):
        Note.id_counter += 1
        self.id = Note.id_counter
        self.content = content
        self.tags = self.extract_tags()

    def extract_tags(self) -> List[str]:
        # Витягуємо всі слова, що починаються на "#"
        return re.findall(r"#\w+", self.content)

    def to_dict(self):
        return {'id': self.id, 'content': self.content, 'tags': self.tags}

    @classmethod
    def from_dict(cls, data: Dict):
        note = cls(data['content'])
        note.id = data['id']
        note.tags = data['tags']
        Note.id_counter = max(Note.id_counter, note.id)
        return note

class NoteManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.notes: Dict[int, Note] = {}
        self.load()

    def add_note(self, content: str):
        note = Note(content)
        self.notes[note.id] = note
        self.save()

    def delete_note(self, note_id: int):
        if note_id in self.notes:
            del self.notes[note_id]
            self.save()

    def edit_note(self, note_id: int, new_content: str):
        if note_id in self.notes:
            self.notes[note_id].content = new_content
            self.notes[note_id].tags = self.notes[note_id].extract_tags()
            self.save()

    def find_notes(self, query: str) -> List[Note]:
        query = query.lower()
        return [note for note in self.notes.values() if query in note.content.lower() or any(query in tag.lower() for tag in note.tags)]

    def sort_notes_by_tags(self, notes: List[Note], query: str) -> List[Note]:
        query_tags = set(query.lower().split())
        # Сортуємо нотатки за кількістю співпадінь тегів із запитом
        sorted_notes = sorted(notes, key=lambda note: len(set(note.tags) & query_tags), reverse=True)
        return sorted_notes

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([note.to_dict() for note in self.notes.values()], f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as f:
            notes = json.load(f)
            for note_data in notes:
                note = Note.from_dict(note_data)
                self.notes[note.id] = note

# Використання
noteManager = NoteManager('notes.json')
noteManager.add_note('Learn Python #programming #python #learning')
noteManager.add_note('Buy milk #shopping')
noteManager.edit_note(1, 'Learn Python in-depth #programming #python #learning')

found_notes = noteManager.find_notes('#python')
sorted_notes = noteManager.sort_notes_by_tags(found_notes, '#python #learning')
for note in sorted_notes:
    print(note.content, note.tags)
