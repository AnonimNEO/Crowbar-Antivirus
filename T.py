#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

import ctypes
import random
import sys
import os

not_loguru = False
not_tkinter = False
not_pillow = False
not_elevate = False
not_pystray = False
not_bytesio = False
not_multiprocessing = False
not_threading = False
not_signal = False

try:
    #Логирование Ошибок
    from loguru import logger
except Exception as e:
    import logging
    not_loguru = True
    #Создаём заглушку логгера
    class Loggers:
        def __init__(self):
            self.setup_fallback_logger()

        #Настраиваем стандартный логгер как замену
        def setup_fallback_logger(self):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.ERROR)

            #Если логгер уже имеет обработчики, не добавляем новые
            if not self.logger.handlers:
                handler = logging.StreamHandler(sys.stdout)
                formatter = logging.Formatter(
                    "%(asctime)s | %(levelname)-8s | %(message)s",
                    datefmt="%d-%m-%Y %H:%M:%S"
                )
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)

        def debug(self, message):
            self.logger.debug(message)

        def info(self, message):
            self.logger.info(message)

        def warning(self, message):
            self.logger.warning(message)

        def error(self, message):
            self.logger.error(message)

        def critical(self, message):
            self.logger.critical(message)

        def success(self, message):
            self.logger.info(f"[SUCCESS] {message}")

        def exception(self, message):
            self.logger.exception(message)

        def add(self, *args, **kwargs):
            pass

    logger = Loggers()

    logger.critical(f"T - Ошибка импорта loguru! Используется замена\n{e}")

#Интерфейс
try:
    from tkinter import messagebox
    import tkinter as tk
except Exception as e:
    not_tkinter = True
    logger.critical(f"T - Ошибка импорта tkinter\n{e}")

try:
    #Рисование иконки в трее и вставка картинок
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    not_pillow = True
    logger.critical(f"T - Ошибка импорта Pillow\n{e}")

#Получение прав Администратора
try:
    from elevate import elevate
except Exception as e:
    not_elevate = True
    logger.critical(f"T - Ошибка импорта elevate\n{e}")

#Движок иконки в трее
try:
    from pystray import MenuItem, Menu
    import pystray
except Exception as e:
    not_pystray = True
    logger.critical(f"T - Ошибка импорта pystray\n{e}")

#Работа с потоками
try:
    from io import BytesIO
except Exception as e:
    not_bytesio = True
    logger.critical(f"T - Ошибка импорта BytesIO\n{e}")

try:
    import multiprocessing
except Exception as e:
    not_multiprocessing = True
    logger.critical(f"T - Ошибка импорта multiprocessing\n{e}")

try:
    import threading
except Exception as e:
    not_threading = True
    logger.critical(f"T - Ошибка импорта threading\n{e}")

try:
    import signal
except Exception as e:
    not_signal = True
    logger.critical(f"T - Ошибка импорта signal\n{e}")

not_ap = False
not_arm = False
not_cc = False
not_config = False
not_e = False
not_ec = False
not_fm = False
not_fr = False
not_rlp = False
not_cm = False
not_of = False
not_pm = False
not_r = False
not_rs = False
not_run = False
not_sau = False
not_sp = False
not_ua = False
not_um = False
not_console = False

#Импорт Компонентов
#from OBPC import OBPC, on_board_pc_version
try:
    from AP import AP
except Exception as e:
    not_ap = True
    logger.critical(f"T - Ошибка импорта Компонента AboutImage\n{e}")

try:
    from ARM import ARM, autorun_master_version
except Exception as e:
    not_arm = True
    logger.critical(f"T - Ошибка импорта Компонента AutoRunMaster\n{e}")

try:
    from CC import CC, clear_cache_version
except Exception as e:
    not_cc = True
    logger.critical(f"T - Ошибка импорта Компонента ClearCache\n{e}")

try:
    from config import *
except Exception as e:
    not_config = True
    logger.critical(f"T - Ошибка импорта конфига!\n{e}")

try:
    from E import ask_exit, exit_version
except Exception as e:
    not_e = True
    def ask_exit():
        pass
    logger.critical(f"T - Ошибка импорта Компонента Exit\n{e}")

try:
    from EC import edit_criticality_version
except Exception as e:
    not_ec = True
    logger.critical(f"T - Ошибка импорта Компонента EditCritical\n{e}")

try:
    from FM import FM, file_manager_version
except Exception as e:
    not_fm = True
    logger.critical(f"T - Ошибка импорта Компонента FileManager\n{e}")

try:
    from FR import FR, file_replacer_version
except Exception as e:
    not_fr = True
    logger.critical(f"T - Ошибка импорта Компонента FileReplacer\n{e}")

try:
    from RLP import RLP, real_time_protect_version
except Exception as e:
    not_rlp = True
    logger.critical(f"T - Ошибка импорта Компонента RealTimeProtection\n{e}")

try:
    from CM import CM, unlocker_version
except Exception as e:
    not_cm = True
    def CM(a=None, b=None, c=None):
        pass
    logger.critical(f"T - Ошибка импорта Компонента CrowbarMenu\n{e}")

try:
    from OF import run_component, restart_ca, open_with, get_current_disc, load_bush, other_components_version
except Exception as e:
    not_of = True
    def restart_ca():
        pass
    def open_with():
        pass
    logger.critical(f"T - Ошибка импорта Компонента OtherFunction\n{e}")

try:
    from PM import PM, process_manager_version
except Exception as e:
    not_pm = True
    logger.critical(f"T - Ошибка импорта Компонента ProcessManager\n{e}")

try:
    from R import R, restart_version
except Exception as e:
    not_r = True
    def R():
        pass
    logger.critical(f"T - Ошибка импорта Компонента Restart\n{e}")

try:
    from RS import random_string, random_string_version
except Exception as e:
    def random_string():
        return "error"
    not_rs = True
    logger.critical(f"T - Ошибка импорта Компонента RandomString\n{e}")

try:
    from Run import Run, run_version
except Exception as e:
    not_run = True
    logger.critical(f"T - Ошибка импорта Компонента Run\n{e}")

try:
    from SAU import SAU, settings_and_update_version
except Exception as e:
    not_sau = True
    logger.critical(f"T - Ошибка импорта Компонента SettingsAndUpdate\n{e}")

try:
    from SP import SP, scarecrow_protection_version
except Exception as e:
    not_sp = True
    logger.critical(f"T - Ошибка импорта Компонента ScarecrowProtection\n{e}")

try:
    from UA import UA, unlock_all_version
except Exception as e:
    not_ua = True
    logger.critical(f"T - Ошибка импорта Компонента UnlockAll\n{e}")

try:
    from UM import UM, users_manager_version
except Exception as e:
    not_um = True
    logger.critical(f"T - Ошибка импорта Компонента UserManager\n{e}")

#Импорт консоли разработчика
try:
    from Console import open_console
except Exception as e:
    not_console = True
    logger.critical(f"T - Ошибка импорта Компонента Console\n{e}")

try:
    if not_pystray and not_mu and not not_tkinter:
        def check_component(is_broken):
            return "не доступен" if is_broken else "доступен"

        broken_components = []
        if not_ap:
            broken_components.append(f"Компонент AP: не доступен")
        if not_arm:
            broken_components.append(f"Компонент ARM: не доступен")
        if not_cc:
            broken_components.append(f"Компонент CC: не доступен")
        if not_config:
            broken_components.append(f"config: не доступен")
        if not_e:
            broken_components.append(f"Компонент E: не доступен")
        if not_ec:
            broken_components.append(f"Компонент EC: не доступен")
        if not_fm:
            broken_components.append(f"Компонент FM: не доступен")
        if not_fr:
            broken_components.append(f"Компонент FR: не доступен")
        if not_rlp:
            broken_components.append(f"Компонент RLP: не доступен")
        if not_mu:
            broken_components.append(f"Компонент MU: не доступен")
        if not_of:
            broken_components.append(f"Компонент OF: не доступен")
        if not_pm:
            broken_components.append(f"Компонент PM: не доступен")
        if not_r:
            broken_components.append(f"Компонент R: не доступен")
        if not_rs:
            broken_components.append(f"Компонент RS: не доступен")
        if not_run:
            broken_components.append(f"Компонент Run: не доступен")
        if not_sau:
            broken_components.append(f"Компонент SAU: не доступен")
        if not_sp:
            broken_components.append(f"Компонент SP: не доступен")
        if not_ua:
            broken_components.append(f"Компонент UA: не доступен")
        if not_um:
            broken_components.append(f"Компонент UM: не доступен")
        if not_console:
            broken_components.append(f"Компонент Console: не доступен")
        if not_loguru:
            broken_components.append(f"Библиотека loguru: не доступна")
        if not_tkinter:
            broken_components.append(f"Библиотека tkinter: не доступна")
        if not_pillow:
            broken_components.append(f"Библиотека pillow: не доступна")
        if not_elevate:
            broken_components.append(f"Библиотека elevate: не доступна")
        if not_pystray:
            broken_components.append(f"Библиотека pystray: не доступна")
        if not_bytesio:
            broken_components.append(f"Библиотека bytesio: не доступна")
        if not_multiprocessing:
            broken_components.append(f"Библиотека multiprocessing: не доступна")
        if not_threading:
            broken_components.append(f"Библиотека threading: не доступна")
        if not_signal:
            broken_components.append(f"Библиотека signal: не доступна")
        
        critical_error = (
            "Ядро программы не может быть запущено, обнаружены критические повреждения программы!\n"
            "Повреждения:\n" +
            "\n".join(broken_components)
        )
        messagebox.showerror(random_string(), critical_error)
except Exception as e:
    logger.error(f"T - ошибка при проверке критических повреждений\n{e}")


#Глобальные Переменные
global T_log_txt, start_interface, run_in_recovery, current_theme
font_trey = "arial.ttf"
trey_version = "2.3.2 Beta build 12"
on_board_pc_version = ""

def Crowbar():
    global start_obpc, start_lp, start_interface, current_theme, run_in_recovery, current_disc
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logger.add(f"{log_path}\\{T_log_txt}", format="{time} {level} {message}", rotation="100 KB", compression="zip")

    current_disc = None

    def check_is_recovery():
        #Проверка на безопасный режим
        #try:
        #    import winreg
        #    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        #    key = winreg.OpenKey(reg, r'System\CurrentControlSet\Control\SafeBoot')
        #    is_safe_mode = True
        #except Exception:
        #    pass

        #Проверка на среду восстановления
        if os.environ.get("WINPE") == "1":
            return True

        return False

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
                _icon_buffer = None

                def create_image(width, height):
                    global _icon_buffer

                    icon_trey = Image.new("RGB", (width, height), (255, 0, 0))
                    square = ImageDraw.Draw(icon_trey)
                    square.rectangle((width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10), fill=(0, 0, 255))

                    font_paths = "C:\\Windows\\Fonts\\arial.ttf"

                    font = ImageFont.truetype(font_paths, 24)

                    if font is None:
                        font = ImageFont.load_default()
                        logger.warning("T - Используется шрифт по умолчанию")

                    text = "=]"
                    text_bbox = square.textbbox((0, 0), text, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                    text_position = (width // 2 - text_width // 2, height // 2 - text_height // 2)
                    square.text(text_position, text, fill=(255, 0, 0), font=font)

                    #Сохраняем буфер в глобальной переменной
                    _icon_buffer = BytesIO()
                    icon_trey.save(_icon_buffer, format="PNG")
                    _icon_buffer.seek(0)

                    return Image.open(_icon_buffer)

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

                def create_menu_item(condition, enabled_text, enabled_func, component_name):
                    """Создает MenuItem в зависимости от условия доступности компонента"""
                    if condition:
                        disabled_text = f"[!] Компонент {component_name} недоступен."
                        return MenuItem(disabled_text, lambda: None)
                    else:
                        return MenuItem(enabled_text, enabled_func)

                unlocker_menu = Menu(
                    create_menu_item(not_arm, "Мастер Автозагрузки", lambda: run_component(ARM, run_in_recovery, current_theme), "ARM"),
                    create_menu_item(not_pm, "Менеджер Процессов", lambda: run_component(PM, run_in_recovery, current_theme), "PM"),
                    create_menu_item(not_fm, "Файловый Менеджер", lambda: run_component(FM, run_in_recovery, current_theme), "FM"),
                    create_menu_item(not_fr, "Замена Редких Файлов", lambda: run_component(FR, run_in_recovery, current_theme), "FR"),
                    create_menu_item(not_um, "Менеджер Пользователей", lambda: run_component(UM, current_theme), "UM"),
                    create_menu_item(not_sp, "Scarecrow Protection", lambda: run_component(SP, run_in_recovery, current_disc_r, current_theme), "SP"),
                    create_menu_item(not_cc, "Запустить Очистку Temp", lambda: CC(run_in_recovery), "CC"),
                    create_menu_item(not_of, "Открыть с Помощью", open_with, "OF"),
                    create_menu_item(not_r, "Перезапустить ПК", R, "R")
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
                        "CM": CM,
                        "icon": icon if "icon" in locals() else None,
                        "logger": logger,
                    }
                    thread = threading.Thread(target=open_console, args=(console_globals,), daemon=True)
                    thread.start()

                #Меню По ПКМ
                image = create_image(20, 20)
                menu = Menu(
                    create_menu_item(not_cm, "Открыть Монтировка Анлокер", lambda: CM(run_in_recovery, current_theme), "CM"),
                    MenuItem("Утилиты", unlocker_menu),
                    create_menu_item(not_ua, "Разблокировка Всего", lambda: UA(run_in_recovery), "UA"),
                    create_menu_item(not_run, "Запустить От Имени Админа", lambda: run_component(Run, current_theme), "Run"),
                    create_menu_item(not_ap, "О Программе", lambda: AP(autorun_master_version, clear_cache_version, exit_version, edit_criticality_version, file_manager_version, real_time_protect_version, unlocker_version, other_components_version, process_manager_version, restart_version, random_string_version, run_version, scarecrow_protection_version, settings_and_update_version, trey_version, unlock_all_version, users_manager_version), "AP"),
                    create_menu_item(not_console, "Консоль Разработчика", open_console_on_thread, "Console"),
                    create_menu_item(not_sau, "Настройки", lambda: run_component(SAU, current_theme), "SAU"),
                    create_menu_item(not_e, "Выход", ask_exit, "Exit")
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
                    run_component(CM, run_in_recovery, current_theme)

                #while True:
                #    time.sleep(1)
            except Exception as e:
                logger.warning(f"T - Ошибка при запуске иконки\n{e}")
                CM(run_in_recovery, current_theme, current_disc)

        if run_in_recovery:
            logger.info("T - Запуск в режиме рекавери...")
            CM(run_in_recovery, current_theme, current_disc)

    except Exception as e:
        logger.critical(f"В Компоненте Trey произошла неизвестная ошибка!\n{e}")
        CM(run_in_recovery, current_theme, current_disc)
    finally:
        if run_in_recovery:
            logger.info("T - Завершение работы, выгрузка кустов реестра...")

        if not run_in_recovery:
            signal.signal(signal.SIGTERM, restart_ca)

if __name__ == "__main__":
    try:
        multiprocessing.freeze_support()
    except Exception as e:
        logger.critical(f"T - Критическая ошибка при многопоточности\n{e}")

    try:
        #elevate()
        if ctypes.windll.shell32.IsUserAnAdmin():
            try:
                Crowbar()
            except Exception as e:
                comment = f"T - Фатальная ошибка при работе ядра программы\n{e}"
                logger.critical(comment)
                if messagebox.askyesno(random_string(),f"{comment}\n\nПерезапустить программу?"):
                    Crowbar()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except Exception as e:
        admin_error = f"T - Ошибка при получении прав администратора:\n{e}"
        logger.critical(admin_error)
        messagebox.showerror(random_string(), admin_error)
