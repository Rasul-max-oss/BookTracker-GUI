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

tk.Label(input_frame, text="Поля ввода будут здесь").pack(pady=20)

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
