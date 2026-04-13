#Обучение
from tkinter import messagebox
import tkinter as tk
#Рисование иконки в трее и вставка картинок
from PIL import Image, ImageDraw, ImageFont
#Логирование Ошибок
from loguru import logger
#Получение прав Администратора
from elevate import elevate
#Движок иконки в трее
from pystray import MenuItem, Menu
import pystray
#Работа с потоками
from io import BytesIO
import multiprocessing
import threading
import signal
#Работа со временим
import time
#Работа с файлами и ОС
import os
#Рандом
import random


#Глобализируем версии компонентов
global autorun_master_version, clear_cache_version, exit_version, file_manager_version, load_protection_version, unlocker_version, on_board_pc_version, other_komponents_version, restart_version, random_string_version, run_version, scarecrow_protection_verison

#Импорт Компонентов
from AP import AP
from ARM import ARM, autorun_master_version
from CC import CC, clear_cache_version
from config import *
from E import ask_exit, exit_version
from EC import edit_criticality_version
from FM import FM, file_manager_version
from FR import FR, file_replacer_version
#from K import knot_version
from RLP import RLP, real_time_protect_version
from MU import MU, unlocker_version
#from OBPC import OBPC, on_board_pc_version
from OF import run_component, restart_ca, open_with, get_current_disc, load_bush, other_components_version
from PM import PM, process_manager_version
from R import R, restart_version
from RS import random_string, random_string_version
from Run import Run, run_version
from SAU import SAU, settings_and_update_version
from SP import SP, scarecrow_protection_version
from UA import UA, unlock_all_version
from UM import UM, users_manager_version

#Импорт консоли
from Console import open_console

if __name__ == '__main__':
    multiprocessing.freeze_support()


try:
    elevate()
    pass
except Exception as e:
    admin_error = f"T - Ошибка при получении прав администратора:\n{e}"
    logger.critical(admin_error)
    messagebox.showerror(random_string(), admin_error)

#Глобальные Переменные
global T_log_txt, start_interface, run_in_recovery, current_theme
font_trey = "arial.ttf"
trey_version = "2.2.2 Beta build 12"
on_board_pc_version = ""

def Crowbar():
    global start_obpc, start_lp, start_interface, current_theme, run_in_recovery, current_disc
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logger.add(f"{log_path}\\{T_log_txt}", format="{time} {level} {message}", rotation="100 KB", compression="zip")

    def check_is_recovery():
        if os.path.exists("X:\\Windows\\"):
            return True
        return False

    run_in_recovery = False
    current_disc = "C:\\"  # ← ИНИЦИАЛИЗИРУЕМ В НАЧАЛЕ
    
    try:
        try:
            run_in_recovery = check_is_recovery()
            if run_in_recovery:
                logger.warning("T - Запуск в среде восстановления Шindows")
            else:
                logger.info("T - Запуск в стандартной среде Шindows")
        except Exception as e:
            run_in_recovery = True
            logger.error(f"T - Ошибка при определении среды:\n{e}")

        if run_in_recovery:
            current_disc, found_disc = get_current_disc(run_in_recovery)
            if found_disc:
                logger.info(f"T - Загрузка кустов реестра с диска {current_disc}...")
                load_bush(current_disc)

    except Exception as e:
        logger.error(f"T - Критическая ошибка: {e}")

    #Основная программа
    try:
        current_theme = theme[default_theme]
        if not run_in_recovery:
            try:
                #Создание Иконки
                def create_image(width, height):
                    icon_trey = Image.new("RGB", (width, height), (255, 0, 0))
                    square = ImageDraw.Draw(icon_trey)
                    square.rectangle(
                        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
                        fill=(0, 0, 255)
                    )

                    font = None
                    font_paths = [font_trey, "C:\\Windows\\Fonts\\arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]

                    for path in font_paths:
                        try:
                            font = ImageFont.truetype(path, 24)
                            break
                        except:
                            continue

                    if font is None:
                        font = ImageFont.load_default()
                        logger.warning("T - Используется шрифт по умолчанию")

                    text = "=]"
                    text_bbox = square.textbbox((0, 0), text, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                    text_position = (width // 2 - text_width // 2, height // 2 - text_height // 2)
                    square.text(text_position, text, fill=(255, 0, 0), font=font)

                    buf = BytesIO()
                    icon_trey.save(buf, format='PNG')
                    buf.seek(0)
                    return Image.open(buf)

                def start_icon():
                    if run_in_recovery:
                        logger.warning("T - Режим восстановления: Трей отключен.")
                        return
                    try:
                        icon.visible = True
                    except Exception as e:
                        logger.error(f"T - Ошибка трея:\n{e}")

                if run_in_recovery:
                    current_disc_r, found_disc = get_current_disc(run_in_recovery)
                else:
                    current_disc_r = "C:\\"

                #Создаем выпадающий список с функциями Анлокера
                unlocker_menu = Menu(
                    MenuItem("Мастер Автозагрузки", lambda:run_component(ARM, run_in_recovery, current_theme)),
                    MenuItem("Менеджер Процессов", lambda: run_component(PM, run_in_recovery, current_theme)),
                    MenuItem("Файловый Менеджер", lambda: run_component(FM, run_in_recovery, current_theme)),
                    MenuItem("Замена Редких Файлов", lambda:run_component(FR, run_in_recovery, current_theme)),
                    MenuItem("Менеджер Пользователей", lambda:run_component(UM, current_theme)),
                    MenuItem("Scarecrow Protection", lambda:run_component(SP, run_in_recovery, current_disc_r, current_theme)),
                    MenuItem("Запустить Очистку Temp", lambda:CC(run_in_recovery)),
                    MenuItem("Открыть с Помощью", open_with),
                    MenuItem("Перезапустить ПК", R)
                )

                #Определяем компоненты и запускаем консоль в отдельном потоке
                def open_console_on_thread():
                    n = random.randint(128, 2048)
                    captcha_input = tk.simpledialog.askinteger(random_string(), f"Введите число: {n}")

                    if captcha_input == n:
                        pass
                    else:
                        messagebox.showerror(random_string(), "Неправильный ввод капчи.\nКонсоль разработчика не будет запущена.")
                        return

                    console_globals = {
                        "run_component": run_component,
                        "run_in_recovery": run_in_recovery,
                        "current_theme": current_theme,
                        "AP": AP,
                        "ARM": ARM,
                        "PM": PM,
                        "FM": FM,
                        "FR": FR,
                        "UM": UM,
                        "SP": SP,
                        "CC": CC,
                        "UA": UA,
                        "Run": Run,
                        "SAU": SAU,
                        "RLP": RLP,
                        "MU": MU,
                        "icon": icon if "icon" in locals() else None,
                        "logger": logger,
                    }
                    thread = threading.Thread(target=open_console, args=(console_globals,), daemon=True)
                    thread.start()

                #Меню По ПКМ
                image = create_image(20, 20)
                menu = Menu(
                    MenuItem("Открыть Монтировка Анлокер", lambda:MU(run_in_recovery, current_theme)),
                    MenuItem("Утилиты", unlocker_menu),
                    MenuItem("Разблокировка Всего", lambda:UA(run_in_recovery)),
                    MenuItem("Запустить От Имени Админа", lambda:run_component(Run, current_theme)),
                    MenuItem("О Программе", lambda:AP(autorun_master_version, clear_cache_version, exit_version, edit_criticality_version, file_manager_version, real_time_protect_version, unlocker_version, other_components_version, process_manager_version, restart_version, random_string_version, run_version, scarecrow_protection_version, settings_and_update_version, trey_version, unlock_all_version, users_manager_version)),
                    MenuItem("Консоль Разработчика", open_console_on_thread),
                    MenuItem("Настройки", lambda:run_component(SAU, current_theme)),
                    MenuItem("Выход", ask_exit)
                )

                icon = pystray.Icon("Crowbar_Antivirus_Icon", image, "Crowbar Antivirus", menu)

                if start_interface == "icon" or start_interface == "window":
                    try:
                        thread_icon = threading.Thread(target=icon.run)
                        thread_icon.daemon = True
                        thread_icon.start()

                        start_icon()
                    except Exception as e:
                        logger.critical(f"T - Ошибка запуска иконки! Аварийный перезапуск!\n{e}")

                if start_lp:
                    run_component(RLP)

                if start_interface == "window" or start_interface == "only-windows":
                    run_component(MU, run_in_recovery, current_theme)

                while True:
                    time.sleep(1)
            except Exception as e:
                logger.warning(f"T - Ошибка при запуске иконки\n{e}")
                MU(run_in_recovery, current_theme, current_disc)

        if run_in_recovery:
            logger.info("T - Запуск в режиме рекавери...")
            MU(run_in_recovery, current_theme, current_disc)

    except Exception as e:
        logger.critical(f"В Компоненте Trey произошла неизвестная ошибка!\n{e}")
        MU(run_in_recovery, current_theme, current_disc)
    finally:
        if run_in_recovery:
            logger.info("T - Завершение работы, выгрузка кустов реестра...")

        if not run_in_recovery:
            signal.signal(signal.SIGTERM, restart_ca)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    Crowbar()
