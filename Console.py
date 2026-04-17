import tkinter as tk
from tkinter import scrolledtext, messagebox
from io import StringIO
#Логирование Ошибок
from loguru import logger
import threading
import sys

from RS import random_string
import config

crowbar_console_version = "0.0.2 Pre-Alpha"

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
        self.output_text.insert(tk.END, f"=== Crowbar Antivirus Console {crowbar_console_version} ===\n")
        self.output_text.insert(tk.END, f"=== Консоль Антивируса Монтировка {crowbar_console_version} ===\n")
        self.output_text.insert(tk.END, "Будте осторожны, данный компоеннт может быть не стабилен\n")
        self.output_text.insert(tk.END, "Доступно изменение переменных run_in_recovery\n")
        
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

        logger.info(f"Console - попытка выполнить команду: {command}")

        if any(x in command for x in ("exit", "quit", "os._exit")):
            self.output_text.config(state=tk.NORMAL)
            comment = "Не не Я не дам тебе обойти капчю (как минимум попытаюсь)\n"
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
    console = CrowbarConsole(globals_dict)
    console.create_console()
