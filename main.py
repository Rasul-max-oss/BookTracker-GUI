import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# Главное окно
root = tk.Tk()
root.title("Book Tracker - Трекер прочитанных книг")
root.geometry("800x600")

# Список книг
books = []

# Метка заголовка
title_label = tk.Label(root, text="Book Tracker", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Фрейм для формы ввода
input_frame = tk.LabelFrame(root, text="Добавить новую книгу", font=("Arial", 12))
input_frame.pack(pady=10, padx=20, fill="x")

# Поле: Название книги
tk.Label(input_frame, text="Название книги:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_title = tk.Entry(input_frame, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=5)

# Поле: Автор
tk.Label(input_frame, text="Автор:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_author = tk.Entry(input_frame, width=40)
entry_author.grid(row=1, column=1, padx=10, pady=5)

# Поле: Жанр
tk.Label(input_frame, text="Жанр:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
genre_var = tk.StringVar()
genres = ["Роман", "Фантастика", "Детектив", "Научная литература", "Поэзия", "Биография", "Фэнтези", "Другое"]
combo_genre = ttk.Combobox(input_frame, textvariable=genre_var, values=genres, width=37, state="readonly")
combo_genre.grid(row=2, column=1, padx=10, pady=5)
combo_genre.current(0)

# Поле: Количество страниц
tk.Label(input_frame, text="Количество страниц:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_pages = tk.Entry(input_frame, width=40)
entry_pages.grid(row=3, column=1, padx=10, pady=5)

# Кнопка добавления книги
btn_add = tk.Button(input_frame, text="Добавить книгу", font=("Arial", 11), bg="#4CAF50", fg="white")
btn_add.grid(row=4, column=0, columnspan=2, pady=10)

# Фрейм для фильтров
filter_frame = tk.LabelFrame(root, text="Фильтры", font=("Arial", 12))
filter_frame.pack(pady=10, padx=20, fill="x")

tk.Label(filter_frame, text="Фильтры будут здесь").pack(pady=10)

# Фрейм для списка книг
list_frame = tk.Frame(root)
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Список для отображения книг
book_listbox = tk.Listbox(list_frame, font=("Arial", 11), height=15)

# Полоса прокрутки
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=book_listbox.yview)
book_listbox.configure(yscrollcommand=scrollbar.set)

book_listbox.pack(side=tk.LEFT, fill="both", expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Запуск приложения
root.mainloop()
