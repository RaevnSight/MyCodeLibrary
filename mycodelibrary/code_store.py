# mycodelibrary/code_store.py

import json
import os

class CodeStore:
    def __init__(self, storage_file='code_store.json'):
        self.storage_file = storage_file
        self.store = self.load_data()

    def load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.store, file, indent=4)

    def add_code(self, language: str, description: str, code: str):
        if language not in self.store:
            self.store[language] = []
        self.store[language].append({
            'description': description,
            'code': code
        })
        self.save_data()

    def get_code(self, language: str):
        return self.store.get(language, [])

    def list_languages(self):
        return list(self.store.keys())
