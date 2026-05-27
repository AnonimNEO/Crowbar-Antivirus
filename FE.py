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
from tkinter import filedialog, messagebox
from loguru import logger
import os

from languages import localizations
from config import program_authentication_clyth, current_localization, clyth
from RS import random_string
#from CC22 import CC22
from OF import pac

file_editor_version = "0.3.0 Beta"
l = localizations[current_localization]

class FileEditor:
    def __init__(self, FE_GUI):
        self.FE_GUI = FE_GUI
        self.FE_GUI.title(random_string())
        self.FE_GUI.geometry("650x400")

        self.current_file = None
        self.is_modified = False

        #Переменные для стилей
        self.font_family = "Courier"
        self.font_size = 11
        self.bg_color = "white"
        self.fg_color = "black"
        self.line_numbers_enabled = False

        #Список для хранения позиций совпадений
        self.matches_positions = []
        self.current_match_index = -1

        #Создаём меню
        self.create_menu()

        #Создаём главный фрейм
        self.main_frame = tk.Frame(self.FE_GUI)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        #Создаём текстовое поле
        self.create_text_widget()

        #Создаём строку состояния
        self.create_status_bar()

        #Создаём панель поиска
        self.create_search_panel()

        #Создаём контекстное меню
        self.create_context_menu()

        #Привязываем сочетания клавиш
        self.bind_shortcuts()

        #Обработчик закрытия окна
        self.FE_GUI.protocol("WM_DELETE_WINDOW", self.on_closing)

    #Создание главного меню
    def create_menu(self):
        menubar = tk.Menu(self.FE_GUI)
        self.FE_GUI.config(menu=menubar)

        #Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=l["file"], menu=file_menu)
        file_menu.add_command(label=l["open"], command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label=l["save"], command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label=l["save_as"], command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label=l["exit"], command=self.on_closing, accelerator="Alt+F4")

        #Меню "Редактирование"
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=l["editing"], menu=edit_menu)
        edit_menu.add_command(label=l["cancel"], command=lambda: self.text_widget.edit_undo(), accelerator="Ctrl+Z")
        edit_menu.add_command(label=l["repeat"], command=lambda: self.text_widget.edit_redo(), accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label=l["cut"], command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label=l["copy"], command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label=l["paste"], command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label=l["select_all"], command=self.select_all, accelerator="Ctrl+A")

        #Меню "Вид"
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=l["view"], menu=view_menu)

        #Подменю "Шрифт"
        font_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label=l["font"], menu=font_menu)

        fonts = ["Courier", "Arial", "Times New Roman", "Helvetica", "Verdana", "Consolas"]
        for font in fonts:
            font_menu.add_command(label=font, command=lambda f=font: self.change_font(f))

        #Подменю "Размер шрифта"
        size_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label=l["font_size"], menu=size_menu)

        sizes = [8, 10, 11, 12, 14, 16, 18, 20, 24]
        for size in sizes:
            size_menu.add_command(label=str(size), command=lambda s=size: self.change_font_size(s))

        view_menu.add_separator()

        #Подменю "Тема"
        theme_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label=l["themes"], menu=theme_menu)

        themes = {
            l["white"]: {"bg": "white", "fg": "black"},
            l["dark"]: {"bg": "#2b2b2b", "fg": "#ffffff"},
            l["green"]: {"bg": "#0a0a0a", "fg": "#00ff00"},
            l["blue"]: {"bg": "#1e1e30", "fg": "#00bfff"},
            l["cuttlefish"]: {"bg": "#f4ebd9", "fg": "#5c4033"}
        }

        for theme_name, colors in themes.items():
            theme_menu.add_command(
                label=theme_name,
                command=lambda bg=colors["bg"], fg=colors["fg"]: self.apply_theme(bg, fg)
            )

        higher = tk.BooleanVar(value=True)

        #Включаем или выключаем режим "поверх всех окон"
        def toggle_topmost(GUI):
            higher.set(not higher.get())
            GUI.attributes("-topmost", higher.get())

        def update_topmost_label(menubar, GUI):
            status = l["on2"] if higher.get() else l["off2"]
            menubar.entryconfig(4, label=f"{l["topmost"]}: {status}")
            GUI.after(100, lambda:update_topmost_label(menubar, GUI))

        menubar.add_command(label=f"{l["topmost"]}: {l["on2"]}", command=lambda:toggle_topmost(self.FE_GUI))
        menubar.add_command(label=f"{l["pac"]} - {program_authentication_clyth}", command=pac)
        update_topmost_label(menubar, self.FE_GUI)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self.FE_GUI, tearoff=0)
        self.context_menu.add_command(label=l["cancel"], command=lambda: self.text_widget.edit_undo())
        self.context_menu.add_command(label=l["repeat"], command=lambda: self.text_widget.edit_redo())
        self.context_menu.add_separator()
        self.context_menu.add_command(label=l["cut"], command=self.cut_text)
        self.context_menu.add_command(label=l["copy"], command=self.copy_text)
        self.context_menu.add_command(label=l["paste"], command=self.paste_text)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=l["select_all"], command=self.select_all)

        #Привязываем показ контекстного меню на ПКМ
        self.text_widget.bind("<Button-3>", self.show_context_menu)



    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_FE_GUI, event.y_FE_GUI)
        finally:
            self.context_menu.grab_release()



    def bind_shortcuts(self):
        self.FE_GUI.bind("<Control-o>", lambda e: self.open_file())
        self.FE_GUI.bind("<Control-s>", lambda e: self.save_file())
        self.FE_GUI.bind("<Control-Shift-S>", lambda e: self.save_as_file())
        self.FE_GUI.bind("<Control-z>", lambda e: self.text_widget.edit_undo())
        self.FE_GUI.bind("<Control-y>", lambda e: self.text_widget.edit_redo())
        self.FE_GUI.bind("<Control-x>", lambda e: self.cut_text())
        self.FE_GUI.bind("<Control-c>", lambda e: self.copy_text())
        self.FE_GUI.bind("<Control-v>", lambda e: self.paste_text())
        self.FE_GUI.bind("<Control-a>", lambda e: self.select_all())
        self.FE_GUI.bind("<Control-f>", lambda e: self.toggle_search_panel())



    def change_font(self, font_name):
        self.font_family = font_name
        self.text_widget.config(font=(self.font_family, self.font_size))



    def change_font_size(self, size):
        self.font_size = size
        self.text_widget.config(font=(self.font_family, self.font_size))



    def apply_theme(self, bg_color, fg_color):
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text_widget.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.FE_GUI.config(bg=bg_color)



    def create_text_widget(self):
        frame = tk.Frame(self.main_frame)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        #Прокрутка
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Текстовое поле
        self.text_widget = tk.Text(
            frame,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD,
            font=(self.font_family, self.font_size),
            undo=True,
            maxundo=-1
        )
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_widget.yview)

        #Отслеживание изменений
        self.text_widget.bind("<KeyRelease>", self.on_text_change)



    def create_status_bar(self):
        self.status_bar = tk.Label(
            self.FE_GUI,
            text=l["new_file"],
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)



    def update_status_bar(self):
        if self.current_file:
            filename = os.path.basename(self.current_file)
            modified_indicator = " *" if self.is_modified else ""
            self.status_bar.config(text=f"{filename}{modified_indicator}")
        else:
            modified_indicator = " *" if self.is_modified else ""
            self.status_bar.config(text=f"{l["new_file"]}{modified_indicator}")



    def on_text_change(self, event=None):
        if not self.is_modified:
            self.is_modified = True
            self.update_status_bar()
        #Обновляем поиск
        if self.search_active:
            self.perform_search()



    def open_file(self):
        file_path = filedialog.askopenfilename(
            title=random_string(),
            filetypes=[(l["text_file"], "*.txt"), ("MarkDown", "*.md"), ("JSON", "*.json"), (l["crowbar_scripts"], "*.cas"), (l["all_files"], "*.*")]
        )
        if file_path:
            self.load_file(file_path)



    def load_file(self, file_path):
        try:
            if not os.path.exists(file_path):
                messagebox.showerror(random_string(), f"{l["file"]} {l["not_found"]}: {file_path}")
                return

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            #file_name = extract_filename_from_path(file_path)
            #if file_name[-4:] == ".cas":
            #    content = CC22(code, clyth, True)

            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(1.0, content)

            self.current_file = file_path
            self.is_modified = False
            self.update_status_bar()
        except Exception as e:
            messagebox.showerror(random_string(), str(e))



    def save_file(self):
        if not self.current_file:
            self.save_as_file()
            return
        try:
            content = self.text_widget.get(1.0, tk.END)
            #file_name = extract_filename_from_path(self.current_file)
            #if file_name[-4:] == ".cas":
            #    content = CC22(code, clyth)
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(content)
            self.is_modified = False
            self.update_status_bar()
            messagebox.showinfo(random_string(), f"{l["file"]} {l["success_saved"]}!")
        except Exception as e:
            messagebox.showerror(random_string(), str(e))



    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            title=random_string(),
            defaultextension=".txt",
            filetypes=[(l["text_file"], "*.txt"), ("MarkDown", "*.md"), ("JSON", "*.json"), (l["all_files"], "*.*")]
        )
        if file_path:
            try:
                content = self.text_widget.get(1.0, tk.END)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                self.current_file = file_path
                self.is_modified = False
                self.update_status_bar()
                messagebox.showinfo(random_string(), f"{l["file"]} {l["success_saved"]}!")
            except Exception as e:
                messagebox.showerror(random_string(), str(e))



    def cut_text(self):
        try:
            self.text_widget.event_generate("<<Cut>>")
        except:
            pass



    def copy_text(self):
        try:
            self.text_widget.event_generate("<<Copy>>")
        except:
            pass



    def paste_text(self):
        try:
            self.text_widget.event_generate("<<Paste>>")
        except:
            pass



    def select_all(self):
        self.text_widget.tag_add(tk.SEL, "1.0", tk.END)
        self.text_widget.mark_set(tk.INSERT, "1.0")
        self.text_widget.see(tk.INSERT)
        return "break"



    def on_closing(self):
        if self.is_modified:
            response = messagebox.askyesnocancel(random_string(), l["save_changes?"])
            if response is None: #Отмена
                return
            elif response: #Да
                self.save_file()
        self.FE_GUI.destroy()



    #Создаём панель поиска
    def create_search_panel(self):
        self.search_active = False
        self.search_panel = tk.Frame(self.FE_GUI, bd=1, relief=tk.RAISED)
        #Текстовое поле поиска
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.search_panel, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.search_entry.bind("<KeyRelease>", lambda e: self.perform_search())

        #Чекбоксы
        self.case_var = tk.BooleanVar(value=True)
        self.word_var = tk.BooleanVar(value=False)

        self.case_check = tk.Checkbutton(self.search_panel, text=l["match_case"], variable=self.case_var, command=self.perform_search)
        self.word_check = tk.Checkbutton(self.search_panel, text=l["whole_words"], variable=self.word_var, command=self.perform_search)

        self.case_check.pack(side=tk.LEFT, padx=5)
        self.word_check.pack(side=tk.LEFT, padx=5)

        #Кнопки навигации
        self.prev_button = tk.Button(self.search_panel, text=l["back"], command=self.search_prev)
        self.next_button = tk.Button(self.search_panel, text=l["next"], command=self.search_next)
        self.prev_button.pack(side=tk.LEFT, padx=2)
        self.next_button.pack(side=tk.LEFT, padx=2)

        #Кнопка закрытия поиска
        self.close_search_button = tk.Button(self.search_panel, text="×", command=self.toggle_search_panel)
        self.close_search_button.pack(side=tk.RIGHT, padx=2)



    #Показываем или скрывает панель поиска
    def toggle_search_panel(self):
        if self.search_active:
            self.search_panel.pack_forget()
            self.search_active = False
            self.clear_search_highlight()
        else:
            self.search_panel.pack(side=tk.TOP, fill=tk.X)
            self.search_active = True
            self.search_var.set('')
            self.matches_positions = []
            self.current_match_index = -1
            self.clear_search_highlight()



    #Выполняем поиск и выделяем совпадения
    def perform_search(self):
        self.clear_search_highlight()
        pattern = self.search_var.get()
        if not pattern:
            return
        content = self.text_widget.get("1.0", tk.END)
        flags = 0
        if not self.case_var.get():
            pattern = pattern.lower()
            content_cmp = content.lower()
        else:
            content_cmp = content

        self.matches_positions = []

        import re
        if self.word_var.get():
            regex = r"\b{}\b".format(re.escape(pattern))
        else:
            regex = re.escape(pattern)

        for match in re.finditer(regex, content_cmp):
            start_idx = match.start()
            end_idx = match.end()
            start = self.text_widget.index(f"1.0+{start_idx}c")
            end = self.text_widget.index(f"1.0+{end_idx}c")
            self.matches_positions.append((start, end))

        #Выделяем все совпадения одним цветом
        self.text_widget.tag_remove("search_highlight", "1.0", tk.END)
        for start, end in self.matches_positions:
            self.text_widget.tag_add("search_highlight", start, end)
        self.text_widget.tag_config("search_highlight", foreground="blue", background="yellow")

        #Выделяем текущее совпадение другим цветом
        self.text_widget.tag_remove("current_match", "1.0", tk.END)
        if self.matches_positions:
            self.current_match_index = 0
            start, end = self.matches_positions[self.current_match_index]
            self.text_widget.tag_add("current_match", start, end)
            self.text_widget.tag_config("current_match", foreground="white", background="red")

            self.focus_match(self.current_match_index)



    #Перемещаем курсор к совпадению по индексу и выделяем его цветом
    def focus_match(self, index):
        if not self.matches_positions:
            return
        if index < 0 or index >= len(self.matches_positions):
            return
        start, end = self.matches_positions[index]
        #Убираем выделение текущего совпадения
        self.text_widget.tag_remove("current_match", "1.0", tk.END)
        self.text_widget.tag_remove(tk.SEL, "1.0", tk.END)
        self.text_widget.tag_add("current_match", start, end)
        self.text_widget.see(start)
        self.text_widget.mark_set(tk.INSERT, start)
        #Выделяем текущее совпадение
        self.text_widget.tag_add(tk.SEL, start, end)



    #Переходим к следующему совпадению
    def search_next(self):
        if not self.matches_positions:
            return
        self.current_match_index = (self.current_match_index + 1) % len(self.matches_positions)
        self.focus_match(self.current_match_index)



    #Переходим к предыдущему совпадению
    def search_prev(self):
        if not self.matches_positions:
            return
        self.current_match_index = (self.current_match_index - 1) % len(self.matches_positions)
        self.focus_match(self.current_match_index)



    #Удаляем выделение от поиска
    def clear_search_highlight(self):
        self.text_widget.tag_remove("search_highlight", "1.0", tk.END)



def FE(file_path=None):
    try:
        FE_GUI = tk.Tk()
        FE_GUI.attributes("-topmost", True)
        editor = FileEditor(FE_GUI)
        if file_path:
            editor.load_file(file_path)
        FE_GUI.mainloop()
    except Exception as e:
        logger.exception(l["fe_critical_error"], e)

if __name__ == "__main__":
    FE()
