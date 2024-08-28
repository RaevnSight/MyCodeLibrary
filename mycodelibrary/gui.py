# mycodelibrary/gui.py

import sys
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
sys.path.append(str(Path(__file__).parent.parent))
from mycodelibrary.code_store import CodeStore

class MyCodeLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MyCodeLibrary")
        self.root.geometry("500x500")
        self.root.configure(bg="#2c3e50")  # Set background color

        # Initialize CodeStore
        self.store = CodeStore()

        # Create a style for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Set the theme

        # Customize ttk styles
        self.style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12))
        self.style.configure("TButton", background="#3498db", foreground="#ecf0f1", font=("Helvetica", 10))
        self.style.configure("TEntry", font=("Helvetica", 10))

        # Language input
        self.language_label = ttk.Label(root, text="Language:")
        self.language_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.language_entry = ttk.Entry(root, width=30)
        self.language_entry.grid(row=0, column=1, padx=10, pady=10)

        # Description input
        self.desc_label = ttk.Label(root, text="Description:")
        self.desc_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.desc_entry = ttk.Entry(root, width=30)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=10)

        # Code input
        self.code_label = ttk.Label(root, text="Code Snippet:")
        self.code_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.code_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD, font=("Courier New", 10))
        self.code_text.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = ttk.Button(root, text="Add Code", command=self.add_code)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)
        self.get_button = ttk.Button(root, text="Get Code", command=self.get_code)
        self.get_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.list_button = ttk.Button(root, text="List Languages", command=self.list_languages)
        self.list_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        # Output area
        self.output_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD, font=("Courier New", 10), bg="#ecf0f1", fg="#2c3e50")
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_code(self):
        language = self.language_entry.get()
        description = self.desc_entry.get()
        code = self.code_text.get("1.0", tk.END).strip()
        
        if not language or not description or not code:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return
        
        self.store.add_code(language, description, code)
        messagebox.showinfo("Success", "Code snippet added successfully.")
        self.clear_inputs()

    def get_code(self):
        language = self.language_entry.get()
        snippets = self.store.get_code(language)
        
        if not snippets:
            messagebox.showinfo("No Snippets", f"No code snippets found for language: {language}")
            return
        
        self.output_text.delete("1.0", tk.END)
        for idx, snippet in enumerate(snippets, start=1):
            self.output_text.insert(tk.END, f"Snippet {idx}:\nDescription: {snippet['description']}\nCode:\n{snippet['code']}\n\n")

    def list_languages(self):
        languages = self.store.list_languages()
        
        if not languages:
            messagebox.showinfo("No Languages", "No languages found in the code store.")
            return
        
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Languages available in the code store:\n")
        for language in languages:
            self.output_text.insert(tk.END, f"- {language}\n")
    
    def clear_inputs(self):
        self.language_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.code_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyCodeLibraryApp(root)
    root.mainloop()
