import json
import re

class Note:
    def __init__(self, content: str):
        self.content = content
        self.tags = self.extract_tags()

    def extract_tags(self):
        # Знаходимо всі слова, що починаються на "#" і використовуємо їх як теги
        return re.findall(r"#\w+", self.content)

    def update(self, new_content: str):
        # Оновлюємо зміст нотатки і теги
        self.content = new_content
        self.tags = self.extract_tags()

class NoteManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.notes = []
        self.load()

    def add_note(self, content: str):
        self.notes.append(Note(content))
        self.save()

    def edit_note(self, note_index: int, new_content: str):
        # Перевіряємо, чи індекс нотатки в межах допустимого діапазону
        if 0 <= note_index < len(self.notes):
            self.notes[note_index].update(new_content)
            self.save()

    def delete_note(self, note_index: int):
        # Видаляємо нотатку за індексом, якщо індекс коректний
        if 0 <= note_index < len(self.notes):
            del self.notes[note_index]
            self.save()

    def find_notes(self, query: str):
        # Пошук нотаток, які містять заданий текст або тег
        return [note for note in self.notes if query in note.content or query in note.tags]

    def sort_notes_by_tag(self, tag: str):
        # Сортуємо нотатки за кількістю згадок тега
        return sorted(self.notes, key=lambda note: note.tags.count(tag), reverse=True)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([{'content': note.content, 'tags': note.tags} for note in self.notes], f)

    def load(self):
        try:
            with open(self.filename) as f:
                self.notes = [Note(note_data['content']) for note_data in json.load(f)]
        except FileNotFoundError:
            pass

noteManager = NoteManager('notes.json')
# Додавання нотаток
noteManager.add_note('Learn Python #programming #python')
noteManager.add_note('Go shopping #errands')

# Редагування нотатки
noteManager.edit_note(0, 'Learn Python in-depth #programming #python #learning')

# Видалення нотатки
noteManager.delete_note(1)

# Пошук нотаток за тегом
found_notes = noteManager.find_notes('#python')
print("Found notes:", [note.content for note in found_notes])

# Сортування нотаток за тегом
sorted_notes = noteManager.sort_notes_by_tag('#python')
print("Sorted notes by #python:", [note.content for note in sorted_notes])

# Збереження та завантаження виконується автоматично
