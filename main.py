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

# Фрейм для фильтров
filter_frame = tk.LabelFrame(root, text="Фильтры", font=("Arial", 12))
filter_frame.pack(pady=10, padx=20, fill="x")

tk.Label(filter_frame, text="Фильтры будут здесь").pack(pady=10)

# Фрейм для таблицы книг
table_frame = tk.Frame(root)
table_frame.pack(pady=10, padx=20, fill="both", expand=True)

tk.Label(table_frame, text="Таблица книг будет здесь").pack(pady=20)

# Запуск приложения
root.mainloop()
