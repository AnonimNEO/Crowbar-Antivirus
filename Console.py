#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

import tkinter as tk
from tkinter import scrolledtext, messagebox
from io import StringIO
#Логирование Ошибок
from loguru import logger
import threading
import random
import sys

from config import program_authentication_clyth, current_localization
from languages import localizations
from RS import random_string
import config

crowbar_console_version = "0.1.1 Pre-Alpha"
l = localizations[current_localization]

class CrowbarConsole:
    def __init__(self, globals_dict=None):
        self.globals_dict = globals_dict if globals_dict else {}
        self.window = None
        self.output_text = None
        self.input_entry = None
        
    def create_console(self):
        self.window = tk.Tk()
        self.window.title(random_string())
        self.window.geometry("650x400")
        
        #Вывод консоли
        self.output_text = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            bg="#1e1e1e",
            fg="#00ff00",
            font=("Default", 10),
            height=20
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.output_text.insert(tk.END, f"=== {l["crowbar_console"]} {crowbar_console_version} ===\n")
        self.output_text.insert(tk.END, f"{l["pac"]} - {program_authentication_clyth}\n")
        self.output_text.insert(tk.END, l["crowbar_console_text"])
        
        self.output_text.config(state=tk.DISABLED)
        
        #Поле ввода
        input_frame = tk.Frame(self.window)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(input_frame, text=">>>", fg="#00ff00", bg="black").pack(side=tk.LEFT, padx=5)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=("Default", 10),
            bg="#1e1e1e",
            fg="#00ff00",
            insertbackground="black"
        )
        self.input_entry.pack(fill=tk.X, expand=True, padx=5)
        self.input_entry.bind("<Return>", self.execute_command)
        self.input_entry.focus()
        
        self.window.mainloop()
    
    def execute_command(self, event=None):
        command = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        
        if not command.strip():
            return

        logger.info(f"Console - {l["attempt_command"]}: {command}")

        if any(x in command for x in ("exit", "quit", "os._exit")):
            self.output_text.config(state=tk.NORMAL)
            comment = f"{l["exit_with_console_text"]}\n"
            logger.info(f"Console - {comment}")
            self.output_text.insert(tk.END, comment)
            self.output_text.config(state=tk.DISABLED)
            return
        
        #Вывод команды
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"> {command}\n")
        self.output_text.config(state=tk.DISABLED)
        
        try:
            #Перенаправляем stdout для захвата print
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            #Выполняем команду
            exec(command, self.globals_dict)
            
            #Получаем вывод
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            if output:
                self.output_text.config(state=tk.NORMAL)
                self.output_text.insert(tk.END, output)
                self.output_text.config(state=tk.DISABLED)
        
        except SyntaxError as e:
            self.output_text.config(state=tk.NORMAL)
            comment = f"SyntaxError: {e}\n"
            logger.error(f"Console - {comment[:-5]}\n{e}")
            self.output_text.insert(tk.END, comment)
            self.output_text.config(state=tk.DISABLED)
        
        except Exception as e:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.insert(tk.END, f"Error: {type(e).__name__}: {e}\n")
            self.output_text.config(state=tk.DISABLED)
        
        finally:
            sys.stdout = old_stdout
        
        #Прокручиваем в конец
        self.output_text.config(state=tk.NORMAL)
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)

def open_console(globals_dict=None):
    n = random.randint(128, 2048)
    captcha_input = tk.simpledialog.askinteger(random_string(), f"{l["enter_number"]}: {n}")

    if captcha_input == n:
        pass
    else:
        messagebox.showerror(random_string(), l["bad_password_for_console"])
        return
    console = CrowbarConsole(globals_dict)
    console.create_console()
