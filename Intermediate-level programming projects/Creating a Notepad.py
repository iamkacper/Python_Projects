""" 
Creating a Notepad
An application that allows users to write, save, and edit notes in plain text format. The script stores the notes in a text file and allows reading or updating them later. 
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

# Główne okno aplikacji
root = tk.Tk()
root.title("📝 Simple Notepad")
root.geometry("600x500")

# Pole tekstowe z przewijaniem
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill='both')

# Funkcja zapisu do pliku
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Funkcja otwierania pliku
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding='utf-8') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

# Pasek menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="📂 Open", command=open_file)
file_menu.add_command(label="💾 Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="❌ Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Uruchomienie pętli aplikacji
root.mainloop()
