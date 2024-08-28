# tests/test_code_store.py

import unittest
from mycodelibrary.code_store import CodeStore

class TestCodeStore(unittest.TestCase):
    def test_add_and_get_code(self):
        store = CodeStore()
        store.add_code("Python", "Example of print", "print('Hello World')")
        code_snippets = store.get_code("Python")
        self.assertEqual(len(code_snippets), 1)
        self.assertEqual(code_snippets[0]['description'], "Example of print")
        self.assertEqual(code_snippets[0]['code'], "print('Hello World')")

if __name__ == '__main__':
    unittest.main()
