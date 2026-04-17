#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Интерфейс
from tkinter import filedialog, messagebox, ttk, Menu
import tkinter as tk
#Логирование
from loguru import logger
#Работа с файлами
import subprocess
import shutil
import os

from RS import random_string
from OF import apply_global_theme, get_current_disc
from config import theme, default_theme

file_replacer_version = "0.2.6 Beta"

def FR(run_in_recovery, current_theme):
    def browse_source(source_var):
        path = filedialog.askopenfilename(title=random_string())
        if path:
            source_var.set(path)

    def browse_target(target_var):
        path = filedialog.askopenfilename(title=random_string())
        if path:
            target_var.set(path)

    def on_preset_select(event, combo, target_var, presets_dict):
        selected = combo.get()
        path = presets_dict.get(selected, "")
        if path:
            target_var.set(path)

    def replace_file(source_var, target_var):
        final_src = source_var.get()
        raw_target = target_var.get()

        current_disc, found_disc = get_current_disc(run_in_recovery)

        if not found_disc:
            current_disc = "C:\\"

        if raw_target.startswith("C:"):
            final_tgt = raw_target.replace("C:", current_disc)
        else:
            final_tgt = raw_target

        if not final_src or not os.path.exists(final_src):
            messagebox.showerror(random_string(), "Файл-источник не найден!")
            return

        try:
            #Получаем права собственности (для WinRE)
            #/F - путь к файлу, /A - передать права группе администраторов
            subprocess.run(f'takeown /f "{final_tgt}" /a', shell=True, check=False)
            
            #Даем полные права администраторам
            #/grant - предоставить права, :F - Full access (полный доступ)
            subprocess.run(f'icacls "{final_tgt}" /grant administrators:F', shell=True, check=False)

            #Создаем бэкап
            backup_path = final_tgt + ".backup"
            if os.path.exists(final_tgt):
                shutil.copy2(final_tgt, backup_path)
                logger.info(f"FR - Создан бэкап: {backup_path}")

            #Копируем новый файл
            shutil.copy2(final_src, final_tgt)
            logger.success(f"FR - Успешно заменено: {final_tgt}")
            messagebox.showinfo(random_string(), f"Файл заменен на диске {current_disc}")

        except Exception as e:
            logger.error(f"FR - Ошибка:\n{e}")
            messagebox.showerror(random_string(), f"Не удалось заменить файл:\n{e}")

    def restore_file(target_var):
        final_tgt = target_var.get()
        current_disc, found_disc = get_current_disc(run_in_recovery)
        if not found_disc:
            current_disc = "C:\\"
        final_tgt = final_tgt.replace("C:", f"{current_disc}")
        if not final_tgt:
            messagebox.showwarning(random_string(), "Сначала выберите или укажите путь к файлу!")
            return
        
        backup_path = final_tgt + ".backup"
        if not os.path.exists(backup_path):
            messagebox.showwarning(random_string(), f"Бэкап не найден по пути:\n{backup_path}")
            return

        if messagebox.askyesno(random_string(), f"Восстановить {os.path.basename(final_tgt)} из бэкапа?"):
            try:
                #Возвращаем бэкап на место основного файла
                shutil.move(backup_path, final_tgt)
                logger.success(f"FR - Восстановлено из бэкапа: {final_tgt}")
                messagebox.showinfo(random_string(), "Файл успешно восстановлен.")
            except Exception as e:
                logger.error(f"FR - Ошибка при восстановлении файла:\n{e}")
                messagebox.showerror(random_string(), str(e))

    def restart_fr(user_theme):
        global current_theme
        current_theme = theme[user_theme]
        #FR_GUI.destroy()
        #FR(current_theme)
        apply_global_theme(FR_GUI, current_theme)

    FR_GUI = tk.Tk()
    FR_GUI.title(random_string())
    FR_GUI.geometry("400x235")

    apply_global_theme(FR_GUI, current_theme)

    source_path = tk.StringVar()
    target_path = tk.StringVar()

    presets = {
        "Свой путь": "",
        "Sethc (Залипание клавиш)": "C:\\Windows\\System32\\sethc.exe",
        "Utilman (Спец. возможности)": "C:\\Windows\\System32\\utilman.exe",
        "Taskmgr (Диспетчер задач)": "C:\\Windows\\System32\\taskmgr.exe",
        "Explorer (Проводник)": "C:\\Windows\\explorer.exe"
    }

    #GUI элементы
    tk.Label(FR_GUI, text="1)На, что заменить:", bg=current_theme["lbg"], fg=current_theme["lfg"], font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
    src_frame = tk.Frame(FR_GUI)
    src_frame.pack(fill="x", padx=10)
    tk.Entry(src_frame, bg=current_theme["lbg"], fg=current_theme["fg"], textvariable=source_path).pack(side="left", expand=True, fill="x")
    tk.Button(src_frame, text="Обзор", bg=current_theme["bbg"], fg=current_theme["bfg"], activebackground=current_theme["abg"], activeforeground=current_theme["afg"], command=lambda: browse_source(source_path)).pack(side="right", padx=5)

    tk.Label(FR_GUI, text="2)Что заменяем:", bg=current_theme["lbg"], fg=current_theme["lfg"]).pack(anchor="w", padx=10, pady=(10, 0))
    combo_presets = ttk.Combobox(FR_GUI, values=list(presets.keys()), state="readonly")
    combo_presets.pack(fill="x", padx=10)
    combo_presets.set("Выберите пресет...")
    combo_presets.bind("<<ComboboxSelected>>", lambda e: on_preset_select(e, combo_presets, target_path, presets))

    tgt_frame = tk.Frame(FR_GUI)
    tgt_frame.pack(fill="x", padx=10, pady=5)
    tk.Entry(tgt_frame, bg=current_theme["lbg"], fg=current_theme["fg"], textvariable=target_path).pack(side="left", expand=True, fill="x")
    tk.Button(tgt_frame, text="Обзор", bg=current_theme["bbg"], fg=current_theme["bfg"], activebackground=current_theme["abg"], activeforeground=current_theme["afg"], command=lambda: browse_target(target_path)).pack(side="right", padx=5)

    #Кнопки действий
    btn_frame = tk.Frame(FR_GUI)
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Заменить",
              command=lambda: replace_file(source_path, target_path),
              bg="red", width=15, font=('Segoe UI', 9, 'bold')).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Восстановить",
              command=lambda: restore_file(target_path), 
              bg="lime", width=15).pack(side="left", padx=10)

    #Меню
    menubar = Menu(FR_GUI)
    theme_menu = Menu(menubar, tearoff=0)
    theme_menu.add_checkbutton(label="Тёмная", command=lambda: restart_fr("dark"))
    theme_menu.add_checkbutton(label="Светлая", command=lambda: restart_fr("white"))
    theme_menu.add_checkbutton(label="Красная", command=lambda: restart_fr("red"))
    theme_menu.add_checkbutton(label="Контрастная", command=lambda: restart_fr("black"))
    theme_menu.add_checkbutton(label="Серая", command=lambda: restart_fr("gray"))
    theme_menu.add_checkbutton(label="Оранжевая", command=lambda: restart_fr("orange"))

    #Пункт "Темы"
    menubar.add_cascade(label="Темы", menu=theme_menu)

    FR_GUI.attributes("-topmost", True) 

    higher = tk.BooleanVar(value=True)

    def toggle_topmost(GUI):
        new_state = not higher.get()
        higher.set(new_state)
        GUI.attributes("-topmost", new_state)

    def update_topmost_label(menubar, GUI):
        status = "вкл" if higher.get() else "выкл"
        #Индекс command в menubar
        menubar.entryconfig(5, label=f"Поверх всех окон: {status}")
        GUI.after(200, lambda: update_topmost_label(menubar, GUI))

    menubar.add_command(label="Поверх всех окон: вкл", command=lambda: toggle_topmost(FR_GUI))
    update_topmost_label(menubar, FR_GUI)

    FR_GUI.config(menu=menubar)

    FR_GUI.mainloop()

if __name__ == "__main__":
    current_theme = theme[default_theme]
    FR(current_theme)
