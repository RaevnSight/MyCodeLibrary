# mycodelibrary/code_store.py

class CodeStore:
    def __init__(self):
        self.store = {}

    def add_code(self, language: str, description: str, code: str):
        if language not in self.store:
            self.store[language] = []
        self.store[language].append({
            'description': description,
            'code': code
        })

    def get_code(self, language: str):
        return self.store.get(language, [])

    def list_languages(self):
        return list(self.store.keys())
