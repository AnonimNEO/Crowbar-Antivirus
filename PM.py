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
from tkinter import ttk, messagebox
import tkinter as tk
#Логирование
from loguru import logger

from config import *
from OF import Psutil, apply_global_theme
from RS import random_string

process_manager_version = "1.6.10 Beta"

def PM(run_in_recovery, current_theme):
    PM_GUI_ELEMENTS = {
        "manager": None,
        "notebook": None,
        "tree": None,
        "tabs": {},
        "vsb": None,
        "current_tab": "Все Процессы",
        "treeview_data": [],
        "update_interval": time_to_update_process_list * 1000,
        "sort_column": "PID",
        "sort_direction": "asc",
        "search_query": "",
        #Начальные значения ширины колонок
        "column_widths": {"PID": 50, "Имя Процесса": 150, "Путь к файлу": 250, "Критичность": 80, "Статус": 80, "Пользователь": 150}
    }

    if not run_in_recovery:
        import psutil
        from EC import EC, get_process_critical_status
    else:
        psutil = Psutil()
        def EC(i, c, d):
            pass
        def get_process_critical_status(i, r):
            return False



    try:
        #Обновляем таблицу
        def update_list():
            set_treeview_columns(PM_GUI_ELEMENTS)
            load_current_tab_data(PM_GUI_ELEMENTS)



        #Получаем имя процесса
        def get_process_name(process_id):
            process = psutil.Process(process_id)
            return process.name()



        #Получаем информацию о процессе
        def get_process_info(proc):
            try:
                status = "Заморожен" if proc.status() == psutil.STATUS_STOPPED else "Запущен"

                #РЕАЛИЗОВАТЬ ПРОВЕРКУ НА АДМИНИСТРАТОРА
                is_elevated = False

                return {
                    "PID": proc.pid,
                    "Имя Процесса": proc.name(),
                    "Путь к файлу": proc.exe() if proc.exe() else "Н/Д",
                    "Пользователь": proc.username() if proc.username() else "Н/Д",
                    "Критичность": get_process_critical_status(proc.pid, run_in_recovery),
                    "Статус": status,
                    "Администратор": is_elevated,
                }
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return None
            except Exception as e:
                process_name = get_process_name(proc.pid)
                logger.error(f"PM - Ошибка при получении информации о процессе {process_name} (pid:{proc.pid}):\n{e}")
                return None



        #Получаем список процессов
        def get_process_list(list_type):
            all_processes = []
            for proc in psutil.process_iter(["pid", "name", "exe", "username", "status"]):
                info = get_process_info(proc)
                if info:
                    all_processes.append(info)

            if list_type == "all_list":
                return all_processes
            elif list_type == "critical_list":
                return [p for p in all_processes if p["Критичность"]]
            elif list_type == "suspend_list":
                return [p for p in all_processes if p["Статус"] == "Заморожен"]
            return []



        def filter_data_by_search(data, query):
            if not query:
                return data #Если строка поиска пустая, возвращаем все данные

            lower_query = query.lower()
            filtered_data = []

            #Перебираем каждый процесс
            for item in data:
                found = False
                #Перебираем все значения в процессе
                for value in item.values():
                    #Проверяем, есть ли совпадение в любом столбце
                    if lower_query in str(value).lower():
                        found = True
                        break
                if found:
                    filtered_data.append(item)

            return filtered_data



        #Диалог Поиска
        def open_search_dialog(PM_GUI_ELEMENTS):
            manager = PM_GUI_ELEMENTS["manager"]

            #Создаем дочернее окно (Toplevel)
            search_window = tk.Toplevel(manager)
            search_window.title("Поиск")
            search_window.geometry("300x100")
            search_window.resizable(False, False)
            #Делаем окно модальным (пока оно открыто, нельзя взаимодействовать с основным окном
            search_window.grab_set()

            #Устанавливаем положение окна по центру
            #manager_x = manager.winfo_x()
            #manager_y = manager.winfo_y()
            #manager_width = manager.winfo_width()
            #manager_height = manager.winfo_height()
            manager.winfo_x()
            manager.winfo_y()
            manager.winfo_width()
            manager.winfo_height()

            search_window.geometry("250x125")

            ttk.Label(search_window, text="Введите текст для поиска:").pack(pady=5, padx=10, anchor="w")

            #Текстовое поле с начальным значением
            search_text = tk.StringVar(value=PM_GUI_ELEMENTS["search_query"])
            search_entry = ttk.Entry(search_window, textvariable=search_text, width=40)
            search_entry.pack(pady=5, padx=10)

            #Устанавливаем фокус на поле ввода
            search_entry.focus_set()

            def perform_search():
                #Сохраняем строку поиска в глобальном состоянии PM_GUI_ELEMENTS
                PM_GUI_ELEMENTS["search_query"] = search_text.get()
                #Закрываем окно поиска
                search_window.destroy()
                #Перезагружаем данные для применения фильтра
                load_current_tab_data(PM_GUI_ELEMENTS)

            def cancel_search():
                search_window.destroy()

            button_frame = ttk.Frame(search_window)
            button_frame.pack(pady=10)

            ttk.Button(button_frame, text="Отмена", command=cancel_search).pack(side="left", padx=5)
            ttk.Button(button_frame, text="ОК", command=perform_search).pack(side="left", padx=5)

            #Привязка Enter к кнопке "ОК"
            search_window.bind("<Return>", lambda e: perform_search())
            #Привязка Esc к кнопке "Отмена"
            search_window.bind("<Escape>", lambda e: cancel_search())

            #Ожидаем закрытия окна
            manager.wait_window(search_window)



        #Останавливаем Поиск
        def stop_search(PM_GUI_ELEMENTS):
            #Проверяем, активен ли поиск вообще
            if PM_GUI_ELEMENTS["search_query"] == "":
                return #Ничего не делаем, если поиск и так пуст

            #Сбрасываем строку поиска
            PM_GUI_ELEMENTS["search_query"] = ""
            #Перезагружаем данные для отображения полного списка
            load_current_tab_data(PM_GUI_ELEMENTS)



        #Действие с процессами
        def action_process(PM_GUI_ELEMENTS, action, process_ids):
            if not isinstance(process_ids, (list, tuple)):
                process_ids = [process_ids]

            for pid in process_ids:
                try:
                    proc = psutil.Process(int(pid))

                    if action == "kill":
                        proc.terminate()
                    elif action == "suspend":
                        proc.suspend()
                    elif action == "resume":
                        proc.resume()
                    elif action == "edit_critical_to_false":
                        EC(int(pid), False)
                    elif action == "edit_critical_to_true":
                        EC(int(pid), True)

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
                except Exception as e:
                    logger.critical(f"PM - Ошибка при {action} для PID {pid}: {e}")

            #Обновляем таблицу один раз после обработки всех процессов
            PM_GUI_ELEMENTS["manager"].after(200, lambda: load_current_tab_data(PM_GUI_ELEMENTS))



        #О Программе
        def about_PM():
            messagebox.showinfo(random_string(), f"Менеджер Процессов - {process_manager_version}")



        #Сортируем данные
        def sort_data(data, col, direction):
            #Словарь для преобразования столбцов в ключи, по которым нужно сортировать
            key_map = {
                "PID": "PID",
                "Имя Процесса": "Имя Процесса",
                "Путь к файлу": "Путь к файлу",
                "Пользователь": "Пользователь",
                "Критичность": "Критичность",
                "Статус": "Статус",
            }

            #Получаем фактический ключ для сортировки
            sort_key = key_map.get(col)

            if not sort_key:
                return data

            #Определяем, является ли ключ числовым, чтобы сортировать правильно
            is_numeric = sort_key in ["PID"]

            def sort_func(item):
                value = item.get(sort_key, "")
                if is_numeric:
                    try:
                        return int(value)
                    except ValueError:
                        return 0 #Возвращаем 0, если не удается преобразовать в число
                return value

            #Сортируем данные. reverse=True, если направление 'desc' (по убыванию)
            data.sort(key=sort_func, reverse=(direction == "desc"))
            return data



        #Обработка смены вкладки
        def on_tab_change(event, PM_GUI_ELEMENTS):
            selected_tab = PM_GUI_ELEMENTS["notebook"].tab(PM_GUI_ELEMENTS["notebook"].select(), "text")
            if selected_tab != PM_GUI_ELEMENTS["current_tab"]:
                PM_GUI_ELEMENTS["current_tab"] = selected_tab
                #Сбрасываем состояние сортировки для новой вкладки
                #PM_GUI_ELEMENTS["sort_column"] = "PID"
                #PM_GUI_ELEMENTS["sort_direction"] = "asc"
                set_treeview_columns(PM_GUI_ELEMENTS)

                #Отменяем текущее запланированное обновление и запускаем загрузку данных
                if "after_id" in PM_GUI_ELEMENTS and PM_GUI_ELEMENTS["after_id"] is not None:
                    PM_GUI_ELEMENTS["manager"].after_cancel(PM_GUI_ELEMENTS["after_id"])
                load_current_tab_data(PM_GUI_ELEMENTS)



        #Установка столбиков, в зависимости от вкладки
        def set_treeview_columns(PM_GUI_ELEMENTS):
            if PM_GUI_ELEMENTS["tree"] and PM_GUI_ELEMENTS["tree"].winfo_exists():
                for col in PM_GUI_ELEMENTS["tree"]["columns"]:
                    #Запоминаем ширину каждой колонки
                    PM_GUI_ELEMENTS["column_widths"][col] = PM_GUI_ELEMENTS["tree"].column(col, width=None)

            if PM_GUI_ELEMENTS["tree"] and PM_GUI_ELEMENTS["tree"].winfo_exists():
                PM_GUI_ELEMENTS["tree"].destroy()
            if PM_GUI_ELEMENTS["vsb"] and PM_GUI_ELEMENTS["vsb"].winfo_exists():
                PM_GUI_ELEMENTS["vsb"].pack_forget()

            current_frame = PM_GUI_ELEMENTS["tabs"][PM_GUI_ELEMENTS["current_tab"]]

            PM_GUI_ELEMENTS["tree"] = ttk.Treeview(current_frame, selectmode="extended")
            PM_GUI_ELEMENTS["tree"].pack(side="left", fill="both", expand=True)

            PM_GUI_ELEMENTS["vsb"] = ttk.Scrollbar(current_frame, orient="vertical", command=PM_GUI_ELEMENTS["tree"].yview)
            PM_GUI_ELEMENTS["vsb"].pack(side="right", fill="y")
            PM_GUI_ELEMENTS["tree"].configure(yscrollcommand=PM_GUI_ELEMENTS["vsb"].set)

            PM_GUI_ELEMENTS["tree"].bind("<Button-3>", lambda e: handle_right_click(e, PM_GUI_ELEMENTS))

            style = ttk.Style()
            style.configure("Treeview", rowheight=25)
            PM_GUI_ELEMENTS["tree"].tag_configure("critical", background="red", foreground="white")
            PM_GUI_ELEMENTS["tree"].tag_configure("suspended", background="gray", foreground="white")
            PM_GUI_ELEMENTS["tree"].tag_configure("admin", background="orange", foreground="black")

            columns = ("PID", "Имя Процесса", "Путь к файлу", "Пользователь", "Критичность", "Статус")
            PM_GUI_ELEMENTS["tree"]["columns"] = columns
            PM_GUI_ELEMENTS["tree"]["show"] = "headings"

            def sort_column_data(col):
                if PM_GUI_ELEMENTS["sort_column"] == col:
                    PM_GUI_ELEMENTS["sort_direction"] = "desc" if PM_GUI_ELEMENTS["sort_direction"] == "asc" else "asc"
                else:
                    PM_GUI_ELEMENTS["sort_column"] = col
                    PM_GUI_ELEMENTS["sort_direction"] = "asc"
                load_current_tab_data(PM_GUI_ELEMENTS)

            for col in columns:
                heading_text = col
                if col == PM_GUI_ELEMENTS["sort_column"]:
                    heading_text += " ▼" if PM_GUI_ELEMENTS["sort_direction"] == "desc" else " ▲"

                PM_GUI_ELEMENTS["tree"].heading(col, text=heading_text, command=lambda c=col: sort_column_data(c))

                w = PM_GUI_ELEMENTS["column_widths"].get(col, 150)
                PM_GUI_ELEMENTS["tree"].column(col, width=w, anchor=tk.W)

        #Загружаем данные для активной вкладки и заполняем таблицу
        def load_current_tab_data(PM_GUI_ELEMENTS):
            tree = PM_GUI_ELEMENTS["tree"]
            current_tab = PM_GUI_ELEMENTS["current_tab"]

            #сохраняем текущий фокус, выделение и позицию скролла
            #Получаем PID процесса, который в данный момент в фокусе/выбран
            saved_pid = None
            saved_scroll_pos = None #переменная для сохранения позиции скролла
            try:
                #focus() возвращает PID элемента, который в фокусе
                focused_item_id = tree.focus()
                #selection() возвращает список выделенных iid
                selected_item_ids = tree.selection()

                #Сохраняем PID, который нужно восстановить
                if focused_item_id:
                    saved_pid = int(focused_item_id)
                elif selected_item_ids:
                    saved_pid = int(selected_item_ids[0])

                #Сохраняем позицию скроллбара
                saved_scroll_pos = tree.yview()[0]

            except Exception:
                pass

            #Загрузка исходных данных
            raw_data = []
            if current_tab == "Все Процессы":
                raw_data = get_process_list("all_list")
            elif current_tab == "Критичные Процессы":
                raw_data = get_process_list("critical_list")
            elif current_tab == "Замороженные Процессы":
                raw_data = get_process_list("suspend_list")

            if raw_data is None:
                raw_data = []

            PM_GUI_ELEMENTS["treeview_data"] = filter_data_by_search(raw_data, PM_GUI_ELEMENTS["search_query"])

            PM_GUI_ELEMENTS["treeview_data"] = filter_data_by_search(raw_data, PM_GUI_ELEMENTS["search_query"])
            #применяем сортировку перед заполнением таблицы
            PM_GUI_ELEMENTS["treeview_data"] = sort_data(
                PM_GUI_ELEMENTS["treeview_data"],
                PM_GUI_ELEMENTS["sort_column"],
                PM_GUI_ELEMENTS["sort_direction"]
            )
            #Перезагружаем колонки для обновления символа сортировки
            set_treeview_columns(PM_GUI_ELEMENTS)

            tree = PM_GUI_ELEMENTS["tree"]

            columns = PM_GUI_ELEMENTS["tree"]["columns"]

            #Заполнение таблицы
            all_pids = []
            for PM_data in PM_GUI_ELEMENTS["treeview_data"]:
                values = [str(PM_data.get(col, "")) for col in columns]
                unique_id = str(PM_data["PID"])
                all_pids.append(PM_data["PID"])

                tags = []
                if PM_data.get("Критичность"):
                    tags.append("critical")
                if PM_data.get("Статус") == "Заморожен":
                    tags.append("suspended")
                if PM_data.get("Администратор"):
                    tags.append("admin")

                #iid (идентификатор элемента) устанавливаем как PID
                tree.insert("", "end", values=values, tags=tuple(tags), iid=unique_id, open=True)

            focus_restored = False

            if saved_pid is not None:
                new_focus_id = str(saved_pid)

                #Если PID все еще в списке доступных процессов
                if new_focus_id in tree.get_children():
                    #Восстанавливаем фокус и выделение
                    tree.focus(new_focus_id)
                    tree.selection_set(new_focus_id)
                    tree.see(new_focus_id) #Прокручиваем до него
                    tree.focus_set()
                    focus_restored = False
                else:
                    #Элемент пропал. Ищем ближайший.
                    try:
                        insertion_index = next(i for i, pid in enumerate(all_pids) if pid > saved_pid)

                        if insertion_index > 0:
                            #Берем предыдущий элемент (ближайший меньший PID)
                            focus_pid = all_pids[insertion_index - 1]
                        else:
                            #Берем первый доступный
                            focus_pid = all_pids[0]

                        new_focus_id = str(focus_pid)

                        tree.focus(new_focus_id)
                        tree.selection_set(new_focus_id)
                        tree.see(new_focus_id)
                        tree.focus_set()
                        focus_restored = False

                    except (StopIteration, IndexError):
                        #Если список пуст или saved_pid был больше всех, восстанавливаем скролл, если есть
                        if all_pids:
                            #Берем последний
                            last_pid = all_pids[-1]
                            new_focus_id = str(last_pid)
                            tree.focus(new_focus_id)
                            tree.selection_set(new_focus_id)
                            tree.see(new_focus_id)
                            tree.focus_set()
                            focus_restored = False

            if not focus_restored and saved_scroll_pos is not None:
                tree.yview_moveto(saved_scroll_pos)

            #Если фокуса нет (например, первый запуск или сброс), устанавливаем на первый элемент
            if not tree.focus() and tree.get_children():
                first_item = tree.get_children()[0]
                tree.focus(first_item)
                tree.selection_set(first_item)
                tree.see(first_item) #Прокручиваем к первому элементу
                tree.focus_set()

            #Планируем следующие обновление таблицы
            #Это обновление автоматически повторно применит фильтр, если он установлен
            if "after_id" in PM_GUI_ELEMENTS and PM_GUI_ELEMENTS["after_id"] is not None:
                PM_GUI_ELEMENTS["manager"].after_cancel(PM_GUI_ELEMENTS["after_id"])

            PM_GUI_ELEMENTS["after_id"] = PM_GUI_ELEMENTS["manager"].after(
            PM_GUI_ELEMENTS["update_interval"],
            lambda: load_current_tab_data(PM_GUI_ELEMENTS)
            )



        #Контекстное Меню
        def show_context_menu(event, PM_GUI_ELEMENTS, selected_pids):
            manager = PM_GUI_ELEMENTS["manager"]
            tree = PM_GUI_ELEMENTS["tree"]
            menu = tk.Menu(manager, tearoff=0)

            count = len(selected_pids)
            suffix = f" ({count} шт.)" if count > 1 else ""

            if selected_pids:
                #Стандартные действия
                menu.add_command(label=f"Убить процессы{suffix}",
                                 command=lambda: action_process(PM_GUI_ELEMENTS, "kill", selected_pids))
                menu.add_command(label=f"Заморозить{suffix}",
                                 command=lambda: action_process(PM_GUI_ELEMENTS, "suspend", selected_pids))
                menu.add_command(label=f"Разморозить{suffix}",
                                 command=lambda: action_process(PM_GUI_ELEMENTS, "resume", selected_pids))
                menu.add_separator()
                menu.add_command(label=f"Сделать критичными{suffix}",
                                 command=lambda: action_process(PM_GUI_ELEMENTS, "edit_critical_to_true", selected_pids))
                menu.add_command(label=f"Снять критичность{suffix}",
                                 command=lambda: action_process(PM_GUI_ELEMENTS, "edit_critical_to_false", selected_pids))

                #если выбран ровно один процесс
                if count == 1:
                    menu.add_separator()
                    item_values = tree.item(selected_pids[0], "values")
                    file_path = item_values[2] if len(item_values) > 2 else ""

                    if file_path and file_path != "Н/Д":
                        menu.add_command(
                            label="Скопировать путь к файлу",
                            command=lambda: copy_to_clipboard(manager, file_path)
                        )

            try:
                menu.tk_popup(event.x_root, event.y_root)
            finally:
                menu.grab_release()



        #Обработчик ПКМ
        def handle_right_click(event, PM_GUI_ELEMENTS):
            tree = PM_GUI_ELEMENTS["tree"]
            item_under_cursor = tree.identify_row(event.y)

            selected_items = list(tree.selection())

            #Если мы нажали ПКМ на элемент, который не выделен — выделяем только его
            if item_under_cursor and item_under_cursor not in selected_items:
                tree.selection_set(item_under_cursor)
                selected_items = [item_under_cursor]

            if selected_items:
                show_context_menu(event, PM_GUI_ELEMENTS, selected_items)



        #Копируем текст в буфер обмена
        def copy_to_clipboard(manager, text):
            manager.clipboard_clear()
            manager.clipboard_append(text)



        #Обработчик клавиш
        def handle_key_action(event, PM_GUI_ELEMENTS):
            tree = PM_GUI_ELEMENTS["tree"]
            selected_items = tree.selection() #Получаем все выделенные ID

            if not selected_items:
                return

            action = None
            key = event.keysym

            if key in ["Delete", "Delete_Last"]:
                action = "kill"
            elif key in ["s", "S"]:
                action = "suspend"
            elif key in ["u", "U"]:
                action = "resume"
            elif key in ["c", "C"]:
                #Для массового изменения берем статус первого элемента как образец
                first_pid = int(selected_items[0])
                is_critical = get_process_critical_status(first_pid, False)
                action = "edit_critical_to_false" if is_critical else "edit_critical_to_true"

            if action:
                action_process(PM_GUI_ELEMENTS, action, list(selected_items))

        def help_pm():
            messagebox.showinfo(random_string(), "Добро пожаловать в Менеджер Процессов, он поддерживает:\n1)Выделение нескольких процессов и работу с ними\n2)Поиск - чтобы его вызвать нажмите на пункт вверху левой части окна.\n3)Замороженные процессы - помечены серым цветом, а критические - красным. Также есть вкладки для удобной навигации.\n\nУчтите, что windows создаёт свои 4 критических процессов svhost.exe, но вирус может изменить эти значения, будьте бдительны!")

        def restart_pm(user_theme):
            global current_theme
            current_theme = theme[user_theme]
            #PM_GUI.destroy()
            #PM(run_in_recovery, current_theme)
            apply_global_theme(PM_GUI, current_theme)

        PM_GUI = tk.Tk()
        PM_GUI_ELEMENTS["manager"] = PM_GUI
        PM_GUI.title(random_string())
        PM_GUI.geometry("810x450")

        apply_global_theme(PM_GUI, current_theme)

        #Меню
        menubar = tk.Menu(PM_GUI)
        #Создаем выпадающее меню "Действия"
        actions_menu = tk.Menu(menubar, tearoff=0)
        actions_menu.add_command(label="Поиск", accelerator="Ctrl+F", command=lambda: open_search_dialog(PM_GUI_ELEMENTS))
        actions_menu.add_command(label="Прекратить поиск", accelerator="Esc", command=lambda: stop_search(PM_GUI_ELEMENTS))
        menubar.add_cascade(label="Действия", menu=actions_menu)

        #Пункт "Помощь"
        menubar.add_command(label="Помощь", command=help_pm)

        #Меню
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_checkbutton(label="Тёмная", command=lambda: restart_pm("dark"))
        theme_menu.add_checkbutton(label="Светлая", command=lambda: restart_pm("white"))
        theme_menu.add_checkbutton(label="Красная", command=lambda: restart_pm("red"))
        theme_menu.add_checkbutton(label="Зелёная", command=lambda: restart_pm("lime"))
        theme_menu.add_checkbutton(label="Контрастная", command=lambda: restart_pm("black"))
        theme_menu.add_checkbutton(label="Серая", command=lambda: restart_pm("gray"))
        theme_menu.add_checkbutton(label="Оранжевая", command=lambda: restart_pm("orange"))

        #Пункт "Темы"
        menubar.add_cascade(label="Темы", menu=theme_menu)

        #Пункт "О Программе"
        menubar.add_command(label="О программе", command=about_PM)

        PM_GUI.attributes("-topmost", True) 

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

        menubar.add_command(label="Поверх всех окон: вкл", command=lambda: toggle_topmost(PM_GUI))
        update_topmost_label(menubar, PM_GUI)

        PM_GUI.config(menu=menubar)

        #Добавляем привязку клавиш Ctrl+F, Esc, Delete, S, U, C
        #Поиск
        PM_GUI.bind_all("<Control-f>", lambda e: open_search_dialog(PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<Control-F>", lambda e: open_search_dialog(PM_GUI_ELEMENTS))

        #Прекратить поиск
        PM_GUI.bind_all("<Escape>", lambda e: stop_search(PM_GUI_ELEMENTS))

        #Горячие клавиши действий
        PM_GUI.bind_all("<Delete>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<s>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<S>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<u>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<U>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<c>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))
        PM_GUI.bind_all("<C>", lambda e: handle_key_action(e, PM_GUI_ELEMENTS))

        #Панель вкладок
        PM_GUI_ELEMENTS["notebook"] = ttk.Notebook(PM_GUI)
        PM_GUI_ELEMENTS["notebook"].pack(pady=10, padx=10, fill="both", expand=True)
        PM_GUI_ELEMENTS["notebook"].bind("<<NotebookTabChanged>>", lambda e: on_tab_change(e, PM_GUI_ELEMENTS))

        #Создаём вкладки
        tab_names = ["Все Процессы", "Критичные Процессы", "Замороженные Процессы"]
        for tab_name in tab_names:
            frame = ttk.Frame(PM_GUI_ELEMENTS["notebook"], padding="5 5 5 5")
            PM_GUI_ELEMENTS["notebook"].add(frame, text=tab_name)
            PM_GUI_ELEMENTS["tabs"][tab_name] = frame

        #Создание начальной Таблицы и Скроллбара
        initial_frame = PM_GUI_ELEMENTS["tabs"]["Все Процессы"]
        PM_GUI_ELEMENTS["tree"] = ttk.Treeview(initial_frame, selectmode="browse")
        PM_GUI_ELEMENTS["vsb"] = ttk.Scrollbar(initial_frame, orient="vertical", command=PM_GUI_ELEMENTS["tree"].yview)
        PM_GUI_ELEMENTS["tree"].configure(yscrollcommand=PM_GUI_ELEMENTS["vsb"].set)
        PM_GUI_ELEMENTS["tree"].pack(side="left", fill="both", expand=True)
        PM_GUI_ELEMENTS["vsb"].pack(side="right", fill="y")

        #Привязка ПКМ
        PM_GUI_ELEMENTS["tree"].bind("<Button-3>", lambda e: handle_right_click(e, PM_GUI_ELEMENTS))

        #Инициализация и загрузка первой вкладки
        update_list()

        PM_GUI.mainloop()
    except Exception as e:
        logger.critical(f"В Компоненте ProcessManager произошла неизвестная ошибка!\n{e}")

if __name__ == "__main__":
    current_theme = theme[default_theme]
    PM(False, current_theme)
