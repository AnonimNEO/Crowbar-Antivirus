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
from tkinter import ttk, Menu, simpledialog
import tkinter as tk
#Логирование Ошибок
from loguru import logger

#Импорт Компонентов
from ARM import ARM
from CC import CC
from FM import FM
from FR import FR
from RLP import RLP
from OF import run_component, load_bush, get_current_disc, open_with, get_current_disc, apply_global_theme
from PM import PM
from R import R
from RS import random_string
from Run import Run
from SP import SP
from UA import UA
from UM import UM

from config import theme, default_theme

global run_in_recovery, current_theme, unlocker_version
unlocker_version = "2.2.3 Beta"

@logger.catch
def MU(run_in_recovery, current_theme, current_disc=None):
    try:
        def restart_mu(user_theme):
            global current_theme
            current_theme = theme[user_theme]
            apply_global_theme(MU_GUI, current_theme)
            #MU_GUI.destroy()
            #MU(run_in_recovery, current_theme)

        #Обновляем размер шрифта и кнопок при изменении размера окна
        def on_window_resize(event):
            #Проверяем, что событие вызвано именно окном MU_GUI
            if event.widget != MU_GUI:
                return

            width = event.width
            height = event.height

            #Базовые размеры
            base_width = 750
            base_height = 300

            #Вычисляем коэффициенты
            scale_w = width / base_width
            scale_h = height / base_height

            #Снижаем интенсивность вертикального масштабирования.
            #Берём ширину как основной фактор и высоту как вспомогательный.
            #Это предотвратит раздувание шрифта на квадратных мониторах.
            scale = (scale_w * 0.8) + (scale_h * 0.2)

            #Замедляем общий рост, чтобы на 4К или полном экране шрифт не становился огромным.
            #Я честно не знаю, работает ли это у меня FullHD
            if scale > 1.2:
                scale = 1.2 + (scale - 1.2) * 0.5

            #Рассчитываем новые размеры шрифтов
            header_font_size = int(32 * scale)
            button_font_size = int(18 * scale)
            small_button_font_size = int(10 * scale)

            #Применяем шрифты с лимитом сверху
            update_fonts(
                min(48, max(14, header_font_size)), 
                min(24, max(10, button_font_size)), 
                min(14, max(8, small_button_font_size)), 
                scale
            )

        #Обновляем шрифты всех элементов интерфейса
        def update_fonts(header_size, button_size, small_size, scale):
            try:
                #Шрифт для заголовков
                header_f = ("Default", header_size, "bold")
                for label in header_labels:
                    label.configure(font=header_f)

                #Шрифт для кнопок
                button_f = ("Default", button_size)
                for btn in regular_buttons:
                    btn.configure(style="TButton")
                    style.configure("TButton", font=button_f) 
                    btn.configure(font=button_f)

                #Маленькие кнопки
                small_f = ("Default", small_size)
                for btn in small_buttons:
                    btn.configure(font=small_f)

                #Версия внизу
                copyleft_label.configure(font=("Default", max(8, int(10 * scale))))
            except:
                pass

        MU_GUI = tk.Tk()
        MU_GUI.geometry("750x350")
        MU_GUI.minsize(750, 300)
        MU_GUI.resizable(True, True)
        MU_GUI.title(random_string())

        MU_GUI.attributes("-topmost", True)
        #MU_GUI.attributes("-topmost", False)

        MU_GUI.lift()
        MU_GUI.focus_set()

        apply_global_theme(MU_GUI, current_theme)

        #MU_GUI.configure(background=current_theme["bg"])
        style = ttk.Style()
        #style.theme_use("clam")
        #style.configure("TNotebook", background=current_theme["bg"])
        #style.configure("TNotebook.Tab", background=current_theme["tbg"], foreground=current_theme["tfg"])
        #style.map("TNotebook.Tab", background=[("selected", current_theme["stb"])])

        #Настройка стиля для вкладок
        #style.configure("TFrame", background=current_theme["bg"])
        #style.configure("TLabel", background=current_theme["bg"], foreground=current_theme["fg"])
        #style.configure("TButton", background=current_theme["bbg"], foreground=current_theme["bfg"])

        tab_control = ttk.Notebook(MU_GUI)

        tab_components = ttk.Frame(tab_control)
        tab_control.add(tab_components, text="Компоненты")
        tab_utilities = ttk.Frame(tab_control)
        tab_control.add(tab_utilities, text="Утилиты")
        tab_protect = ttk.Frame(tab_control)
        tab_control.add(tab_protect, text="Защита")
        tab_manage = ttk.Frame(tab_control)
        tab_control.add(tab_manage, text="Управление")

        tab_components.configure(style="TFrame")
        tab_utilities.configure(style="TFrame")
        tab_protect.configure(style="TFrame")
        tab_manage.configure(style="TFrame")

        #Списки для отслеживания элементов при изменении размера
        header_labels = []
        regular_buttons = []
        small_buttons = []

        #Вкладка "Компоненты"
        label_comp = ttk.Label(tab_components, text="Компоненты", font="Default 24")
        label_comp.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_labels.append(label_comp)

        arm_btn = ttk.Button(tab_components, text="Мастер Автозагрузки",
                     command=lambda:run_component(ARM, run_in_recovery, current_theme))
        arm_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(arm_btn)

        pm_btn = ttk.Button(tab_components, text="Менеджер Процессов",
                     command=lambda:run_component(PM, run_in_recovery, current_theme))
        pm_btn.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(pm_btn)

        fm_btn = ttk.Button(tab_components, text="Файловый Менеджер",
                     command=lambda:run_component(FM, run_in_recovery, current_theme))
        fm_btn.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(fm_btn)

        ua_btn = ttk.Button(tab_components, text="Разблокировка Всего",
                     command=lambda:UA(run_in_recovery))
        ua_btn.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(ua_btn)



        #Вкладка "Утилиты"
        label_util = ttk.Label(tab_utilities, text="Утилиты")
        label_util.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_labels.append(label_util)

        fr_btn = ttk.Button(tab_utilities, text="Замена редких файлов",
                     command=lambda:run_component(FR, run_in_recovery, current_theme))
        fr_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(fr_btn)

        cc_btn = ttk.Button(tab_utilities, text="Очистка Temp",
                     command=lambda:CC(run_in_recovery))
        cc_btn.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(cc_btn)

        run_btn = ttk.Button(tab_utilities, text="Запуск от имени администратора",
                     command=lambda:run_component(Run, current_theme))
        run_btn.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        small_buttons.append(run_btn)

        r_btn = ttk.Button(tab_utilities, text="Перезапустить ПК",
                     command=R)
        r_btn.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(r_btn)

        ow_btn = ttk.Button(tab_utilities, text="Открыть с помощью",
                     command=lambda:open_with())
        ow_btn.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(ow_btn)



        #Вкладка "Защита"
        label_prot = ttk.Label(tab_protect, text="Защита")
        label_prot.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_labels.append(label_prot)

        #rlp_btn = ttk.Button(tab_protect, text="Защита Нагрузки",
        #              command=lambda:run_component(RLP, run_in_recovery))
        #rlp_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        #regular_buttons.append(lp_btn)

        sp_btn = ttk.Button(tab_protect, text="Пугало от вирусов",
                      command=lambda:run_component(SP, run_in_recovery, current_disc_r, current_theme))
        sp_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(sp_btn)



        #Вкладка "Управление"
        label_manage = ttk.Label(tab_manage, text="Управление")
        label_manage.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_labels.append(label_manage)

        um_btn = ttk.Button(tab_manage, text="Менеджер Пользователей",
                      command=lambda:run_component(UM, current_theme))
        um_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        regular_buttons.append(um_btn)

        #Настройка сетки для адаптивности
        for tab in [tab_components, tab_utilities, tab_protect, tab_manage]:
            tab.columnconfigure(0, weight=1)
            tab.columnconfigure(1, weight=1)
            tab.rowconfigure(1, weight=1)
            tab.rowconfigure(2, weight=1)
            tab.rowconfigure(3, weight=1)
            tab.rowconfigure(4, weight=1)

        if run_in_recovery:
            current_disc_r, found_disc = get_current_disc(run_in_recovery)
        else:
            current_disc_r = "C:\\"

        tab_control.pack(fill="both", expand=True)

        copyleft_label = ttk.Label(MU_GUI, text=f"Mount Unlocker {unlocker_version}", anchor="w")
        copyleft_label.pack(side="bottom", anchor="w", padx=10, pady=10)

        #Меню
        menubar = Menu(MU_GUI)
        theme_menu = Menu(menubar, tearoff=0)
        theme_menu.add_checkbutton(label="Тёмная", command=lambda: restart_mu("dark"))
        theme_menu.add_checkbutton(label="Светлая", command=lambda: restart_mu("white"))
        theme_menu.add_checkbutton(label="Красная", command=lambda: restart_mu("red"))
        theme_menu.add_checkbutton(label="Зелёная", command=lambda: restart_mu("lime"))
        theme_menu.add_checkbutton(label="Контрастная", command=lambda: restart_mu("black"))
        theme_menu.add_checkbutton(label="Серая", command=lambda: restart_mu("gray"))
        theme_menu.add_checkbutton(label="Оранжевая", command=lambda: restart_mu("orange"))

        #Пункт "Темы"
        menubar.add_cascade(label="Темы", menu=theme_menu)

        if run_in_recovery:
            higher = tk.BooleanVar(value=False)
        else:
            higher = tk.BooleanVar(value=True)

        #Включаем или выключаем режим "поверх всех окон"
        def toggle_topmost(GUI):
            higher.set(not higher.get())
            GUI.attributes("-topmost", higher.get())

        menubar.add_command(label=f"Поверх всех окон: вкл", command=lambda:toggle_topmost(MU_GUI))

        def update_topmost_label(menubar, GUI):
            status = "вкл" if higher.get() else "выкл"
            menubar.entryconfig(2, label=f"Поверх всех окон: {status}")
            GUI.after(100, lambda:update_topmost_label(menubar, GUI))

        #if run_in_recovery:
        #    def change_user():
        #       user = simpledialog.askstring(title=random_string(), prompt=f"Введите имя пользователя: ")
        #        load_bush(current_disc, user)

        #    menubar.add_command(label=f"Пользователь: {user_name}", command=lambda:change_user)

        MU_GUI.config(menu=menubar)
        update_topmost_label(menubar, MU_GUI)


        #Привязываем событие изменения размера окна
        MU_GUI.bind("<Configure>", on_window_resize)

        MU_GUI.mainloop()
    except Exception as e:
        logger.critical(f"В Компоненте MountUnlocker произошла неизвестная ошибка!\n{e}")

if __name__ == "__main__":
    current_theme = theme[default_theme]
    MU(False, current_theme)
