#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Логирование ошибок
from loguru import logger
#Интерфейс
import tkinter as tk
from tkinter import ttk, Menu
#Работа с процессами и файлами
import subprocess
import os
import re

from OF import apply_global_theme
from RS import random_string
from config import theme, default_theme

run_version = "1.0.5 beta"
run_width_window = 400
run_height_window = 200
run_size_window = f"{run_width_window}x{run_height_window}"

class ApplicationLauncher:
    def __init__(self, RUN_GUI):
        self.RUN_GUI = RUN_GUI
        self.RUN_GUI.title(random_string())
        self.RUN_GUI.geometry(run_size_window)
        self.RUN_GUI.minsize(run_width_window, run_height_window)

        #Пресеты
        self.presets = [
            {"name": "---Стандартные утилиты---", "command": ""},
            {"name": "редактор реестра", "command": "regedit.exe"},
            {"name": "диспетчер задач", "command": "taskmgr.exe"},
            {"name": "блокнот", "command": "notepad.exe"},
            {"name": "проводник", "command": "explorer.exe"},
            {"name": "командная строка", "command": "cmd.exe"},
            {"name": "PowerShell", "command": "powershell.exe"},
            {"name": "---Команды---", "command": ""},
            {"name": "SFC /SCANNOW", "command": "SFC /SCANNOW"},
            {"name": "Отменить перезагрузки/выключение", "command": "shutdown /a"},
            {"name": "Перезагрузить ПК", "command": "shutdown /r"},
            {"name": "Выключить ПК", "command": "shutdown /s"},
            {"name": "завершить сеанс", "command": "shutdown /l"}
        ]

        self.mode = tk.StringVar(value="professional")
        self.current_buttons = []

        self.create_menu()

        self.professional_frame = tk.Frame(RUN_GUI)
        self.professional_frame.pack(fill=tk.BOTH, expand=True)
        self.create_professional_mode()

        self.simplified_frame = tk.Frame(RUN_GUI)
        self.create_simplified_mode()

        #Переключение на профессиональный режим по умолчанию
        self.switch_mode("professional")

        #Привязка события изменения размера окна
        self.RUN_GUI.bind("<Configure>", self.on_window_resize)



    #Создание меню с выбором режима
    def create_menu(self):
        menu_frame = tk.Frame(self.RUN_GUI, height=40)
        menu_frame.pack(side=tk.TOP, fill=tk.X)
        menu_frame.pack_propagate(False)

        label = tk.Label(menu_frame, text="Режим:", font=("Default", 10))
        label.pack(side=tk.LEFT, padx=10, pady=8)

        mode_combo = ttk.Combobox(
            menu_frame,
            textvariable=self.mode,
            values=["профессиональный", "упрощённый"],
            state="readonly",
            width=20
        )
        mode_combo.pack(side=tk.LEFT, padx=5, pady=8)
        mode_combo.bind("<<ComboboxSelected>>", lambda e: self.switch_mode(
            "professional" if self.mode.get() == "профессиональный" else "simplified"
        ))



    def create_professional_mode(self):
        #Поле для ввода команды
        input_frame = tk.Frame(self.professional_frame)
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.input_field = tk.Entry(input_frame, font=("Default", 11))
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.input_field.bind("<Return>", lambda e: self.run_command())

        ok_button = tk.Button(
            input_frame,
            text="OK",
            command=self.run_command,
            width=5,
            font=("Default", 11)
        )
        ok_button.pack(side=tk.LEFT)

        #Меню пресетов
        self.preset_combo = ttk.Combobox(
            self.professional_frame,
            values=[p["name"] for p in self.presets],
            state="readonly",
            font=("Default", 10),
            height=8
        )
        self.preset_combo.pack(fill=tk.X, padx=5, pady=5)
        self.preset_combo.bind("<<ComboboxSelected>>", self.on_preset_selected)

        #Текстовое поле для отображения ошибок
        log_frame = tk.Frame(self.professional_frame)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        tk.Label(log_frame, text="Ошибки:", font=("Default", 9)).pack(anchor=tk.W)

        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(
            log_frame,
            font=("Default", 9),
            yscrollcommand=scrollbar.set,
            height=10
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)

        #Блокируем изменение размера окна в профессиональном режиме
        self.RUN_GUI.resizable(False, False)



    def create_simplified_mode(self):
        self.simplified_frame.pack_propagate(False)

        #Очистка предыдущего интерфейса
        for widget in self.simplified_frame.winfo_children():
            widget.destroy()

        self.current_buttons = []

        #Пропускаем пресеты начинающиеся с "-"
        row = 0
        col = 0
        for preset in self.presets:
            if preset["name"].startswith("-"):
                continue
                
            btn = tk.Button(
                self.simplified_frame,
                text=preset["name"],
                command=lambda cmd=preset["command"]: self.run_command_from_button(cmd),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.current_buttons.append(btn)
            
            col += 1
            if col > 1:
                col = 0
                row += 1

        for i in range(row + 1):
            self.simplified_frame.grid_rowconfigure(i, weight=1)
        self.simplified_frame.grid_columnconfigure(0, weight=1)
        self.simplified_frame.grid_columnconfigure(1, weight=1)



    #Переключаем режим
    def switch_mode(self, mode):
        if mode == "professional":
            self.professional_frame.pack(fill=tk.BOTH, expand=True)
            self.simplified_frame.pack_forget()
            self.RUN_GUI.resizable(False, False)
            self.RUN_GUI.geometry(run_size_window)
        else:
            self.RUN_GUI.minsize(600, 275)
            #self.RUN_GUI.geometry(run_)
            self.professional_frame.pack_forget()
            self.simplified_frame.pack(fill=tk.BOTH, expand=True)
            self.RUN_GUI.resizable(True, True)



    def on_preset_selected(self, event=None):
        selected = self.preset_combo.get()
        for preset in self.presets:
            if preset["name"] == selected:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, preset["command"])
                break



    #Проверяем является ли текст командой или путём к файлу
    def is_command_or_dir(self, text):
        #Если начинается с буквы и двоеточия, то это путь
        if re.match(r"^[A-Za-z]:", text):
            return False
        return True



    #Выполняем команду или запускаем файл
    def run_command(self):
        command = self.input_field.get().strip()
        if command == "" or command == None:
            return

        try:
            if self.is_command_or_dir(command):
                #Это команда
                subprocess.Popen(command, shell=True)
                logger.info(f"Run - запуск команды: {command}")
            else:
                #Это путь к файлу
                if os.path.exists(command):
                    os.startfile(command)
                    logger.info(f"Run - запуск файла: {command}")
                else:
                    comment = f"Run - Не найден файл: {command}"
                    logger.error(comment)
                    self.log(comment)
        except Exception as e:
            comment = f"Run - Ошибка при запуске файла:\n{e}"
            logger.error(comment)
            self.log(comment)



    #Выполняем команду кнопки
    def run_command_from_button(self, command):
        if command == "":
            return
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            comment = f"Run - Ошибка при выполнении команды {command}:\n{e}"
            logger.error(comment)
            self.log(comment)



    def on_window_resize(self, event=None):
        if self.mode.get() == "упрощённый":
            #Динамическое изменение размера шрифта в зависимости от размера окна
            width = self.RUN_GUI.winfo_width()
            height = self.RUN_GUI.winfo_height()

            if width > 0 and height > 0:
                font_size = max(14, min(width, height) // 32)
                for btn in self.current_buttons:
                    btn.config(font=("Default", font_size, "bold"))



    #Отображение ошибок в интерфейсе
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)


def Run(current_theme):
    RUN_GUI = tk.Tk()
    apply_global_theme(RUN_GUI, current_theme)
    ApplicationLauncher(RUN_GUI)

    def restart_run(user_theme):
        global current_theme
        current_theme = theme[user_theme]

    menubar = tk.Menu(RUN_GUI)

    #Меню
    menubar = Menu(RUN_GUI)
    theme_menu = Menu(menubar, tearoff=0)
    theme_menu.add_checkbutton(label="Тёмная", command=lambda: restart_run("dark"))
    theme_menu.add_checkbutton(label="Светлая", command=lambda: restart_run("white"))
    theme_menu.add_checkbutton(label="Красная", command=lambda: restart_run("red"))
    theme_menu.add_checkbutton(label="Зелёная", command=lambda: restart_run("lime"))
    theme_menu.add_checkbutton(label="Контрастная", command=lambda: restart_run("black"))
    theme_menu.add_checkbutton(label="Серая", command=lambda: restart_run("gray"))
    theme_menu.add_checkbutton(label="Оранжевая", command=lambda: restart_run("orange"))

    #Пункт "Темы"
    menubar.add_cascade(label="Темы", menu=theme_menu)

    RUN_GUI.attributes("-topmost", True) 

    higher = tk.BooleanVar(value=True)

    def toggle_topmost(GUI):
        new_state = not higher.get()
        higher.set(new_state)
        GUI.attributes("-topmost", new_state)

    def update_topmost_label(menubar, GUI):
        status = "вкл" if higher.get() else "выкл"
        #Индекс command в menubar
        menubar.entryconfig(2, label=f"Поверх всех окон: {status}")
        GUI.after(200, lambda: update_topmost_label(menubar, GUI))

    menubar.add_command(label="Поверх всех окон: вкл", command=lambda: toggle_topmost(RUN_GUI))
    update_topmost_label(menubar, RUN_GUI)

    RUN_GUI.config(menu=menubar)

    RUN_GUI.mainloop()

if __name__ == "__main__":
    current_theme = theme[default_theme]
    Run(current_theme)
