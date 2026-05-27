#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

try:
    from config import current_localization
except Exception as e:
    current_localization = "ru"

#Локализация
from languages import localizations
l = localizations[current_localization]


import ctypes
import time
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
                formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
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

    logger.exception(f"T - {l["import_error"]} loguru! {l["replacement_is_used"]}", e)

#Интерфейс
try:
    from tkinter import messagebox, simpledialog
    import tkinter as tk
except Exception as e:
    not_tkinter = True
    logger.exception(f"T - {l["import_error"]} tkinter", e)

try:
    #Рисование иконки в трее и вставка картинок
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    not_pillow = True
    logger.exception(f"T - {l["import_error"]} Pillow", e)

#Получение прав Администратора
try:
    from elevate import elevate
except Exception as e:
    not_elevate = True
    logger.exception(f"T - {l["import_error"]} elevate", e)

#Движок иконки в трее
try:
    from pystray import MenuItem, Menu
    import pystray
except Exception as e:
    not_pystray = True
    logger.exception(f"T - {l["import_error"]} pystray", e)

#Работа с потоками
try:
    from io import BytesIO
except Exception as e:
    not_bytesio = True
    logger.exception(f"T - {l["import_error"]} BytesIO", e)

try:
    import multiprocessing
except Exception as e:
    not_multiprocessing = True
    logger.exception(f"T - {l["import_error"]} multiprocessing", e)

try:
    import threading
except Exception as e:
    not_threading = True
    logger.exception(f"T - {l["import_error"]} threading", e)

try:
    import signal
except Exception as e:
    not_signal = True
    logger.exception(f"T - {l["import_error"]} signal", e)

not_ap = False
not_arm = False
not_cc = False
not_config = False
not_e = False
not_ec = False
not_fe = False
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
    logger.exception(f"T - {l["component_import_error"]} AboutImage", e)

try:
    from ARM import ARM, autorun_master_version
except Exception as e:
    not_arm = True
    logger.exception(f"T - {l["component_import_error"]} AutoRunMaster", e)

try:
    from CC import CC, clear_cache_version
except Exception as e:
    not_cc = True
    logger.exception(f"T - {l["component_import_error"]} ClearCache", e)

try:
    from CC22 import CC22
except Exception as e:
    not_cc2 = True
    def CC22():
        return "error"
    logger.exception(f"T - {l["component_import_error"]} CC22", e)

try:
    from config import *
    import config
except Exception as e:
    not_config = True
    logger.exception(f"T - {l["import_error"]} config!", e)

try:
    from E import E, exit_version
except Exception as e:
    not_e = True
    def E():
        pass
    logger.exception(f"T - {l["component_import_error"]} Exit", e)

try:
    from EC import EC, edit_criticality_version
except Exception as e:
    not_ec = True
    def EC():
        pass
    logger.exception(f"T - {l["component_import_error"]} EditCritical", e)

try:
    from FE import FE, file_editor_version
except Exception as e:
    not_fe = True
    logger.exception(f"T - {l["component_import_error"]} FileEditor", e)

try:
    from FM import FM, file_manager_version
except Exception as e:
    not_fm = True
    logger.critical(f"T - {l["component_import_error"]} FileManager", e)

try:
    from FR import FR, file_replacer_version
except Exception as e:
    not_fr = True
    logger.exception(f"T - {l["component_import_error"]} FileReplacer", e)

try:
    from GFA import GFA, get_full_access_version
except Exception as e:
    def GFA():
        pass
    logger.exception(f"T - {l["component_import_error"]} GetFullAccess", e)

try:
    from RLP import RLP, real_time_protect_version
except Exception as e:
    not_rlp = True
    logger.exception(f"T - {l["component_import_error"]} RealTimeProtection", e)

try:
    from CM import CM, crowbar_menu_version
except Exception as e:
    not_cm = True
    crowbar_menu_version = "error"
    def CM(a=None, b=None, c=None):
        pass
    logger.exception(f"T - {l["component_import_error"]} MountUnlocker", e)

try:
    from OF import pac, apply_global_theme, get_offline_reg_path, Psutil, run_component, run_component_process, get_user_name, restart_ca, reg_file, run_command, open_with, get_current_disc, load_bush, unload_bush, other_function_version
except Exception as e:
    not_of = True
    def restart_ca():
        pass
    def open_with():
        pass
    def pac():
        messagebox.showerror(random_string(), f"{l["pac"]} {l["not_available"]}!")
    logger.exception(f"T - {l["component_import_error"]} OtherFunction", e)

try:
    from PM import PM, process_manager_version
except Exception as e:
    not_pm = True
    logger.exception(f"T - {l["component_import_error"]} ProcessManager", e)

try:
    from R import R, restart_version
except Exception as e:
    not_r = True
    def R():
        pass
    logger.exception(f"T - {l["component_import_error"]} Restart", e)

try:
    from RS import random_string, random_string_version
except Exception as e:
    def random_string():
        return "error"
    not_rs = True
    logger.exception(f"T - {l["component_import_error"]} RandomString", e)

try:
    from Run import Run, run_version
except Exception as e:
    not_run = True
    logger.exception(f"T - {l["component_import_error"]} Run", e)

try:
    from SAU import SAU, settings_and_update_version
except Exception as e:
    not_sau = True
    logger.exception(f"T - {l["component_import_error"]} SettingsAndUpdate", e)

try:
    from SP import SP, scarecrow_protection_version
except Exception as e:
    not_sp = True
    logger.exception(f"T - {l["component_import_error"]} ScarecrowProtection", e)

try:
    from UA import UA, check_and_restore_fonts_if_needed, unlock_all_version
except Exception as e:
    not_ua = True
    def check_and_restore_fonts_if_needed(a=None):
        pass
    logger.exception(f"T - {l["component_import_error"]} UnlockAll", e)

try:
    from UM import UM, users_manager_version
except Exception as e:
    not_um = True
    logger.exception(f"T - {l["component_import_error"]} UserManager", e)

#Импорт консоли разработчика
try:
    from Console import open_console, crowbar_console_version
except Exception as e:
    not_console = True
    logger.exception(f"T - {l["component_import_error"]} Console", e)

from CASH import CASH

try:
    if not_pystray and not_cm and not not_tkinter:
        #def check_component(is_broken):
        #    return "не доступен" if is_broken else "доступен"

        broken_components = []
        if not_ap:
            broken_components.append(f"{l["component"]} AP: {l["not_available"]}")
        if not_arm:
            broken_components.append(f"{l["component"]} ARM: {l["not_available"]}")
        if not_cc:
            broken_components.append(f"{l["component"]} CC: {l["not_available"]}")
        if not_e:
            broken_components.append(f"{l["component"]} E: {l["not_available"]}")
        if not_ec:
            broken_components.append(f"{l["component"]} EC: {l["not_available"]}")
        if not_fm:
            broken_components.append(f"{l["component"]} FM: {l["not_available"]}")
        if not_fr:
            broken_components.append(f"{l["component"]} FR: {l["not_available"]}")
        if not_rlp:
            broken_components.append(f"{l["component"]} RLP: {l["not_available"]}")
        if not_cm:
            broken_components.append(f"{l["component"]} CM: {l["not_available"]}")
        if not_of:
            broken_components.append(f"{l["component"]} OF: {l["not_available"]}")
        if not_pm:
            broken_components.append(f"{l["component"]} PM: {l["not_available"]}")
        if not_r:
            broken_components.append(f"{l["component"]} R: {l["not_available"]}")
        if not_rs:
            broken_components.append(f"{l["component"]} RS: {l["not_available"]}")
        if not_run:
            broken_components.append(f"{l["component"]} Run: {l["not_available"]}")
        if not_sau:
            broken_components.append(f"{l["component"]} SAU: {l["not_available"]}")
        if not_sp:
            broken_components.append(f"{l["component"]} SP: {l["not_available"]}")
        if not_ua:
            broken_components.append(f"{l["component"]} UA: {l["not_available"]}")
        if not_um:
            broken_components.append(f"{l["component"]} UM: {l["not_available"]}")
        if not_console:
            broken_components.append(f"{l["component"]} Console: {l["not_available"]}")
        if not_loguru:
            broken_components.append(f"{l["library"]} loguru: {l["not_available2"]}")
        if not_tkinter:
            broken_components.append(f"{l["library"]} tkinter: {l["not_available2"]}")
        if not_pillow:
            broken_components.append(f"{l["library"]} pillow: {l["not_available2"]}")
        if not_elevate:
            broken_components.append(f"{l["library"]} elevate: {l["not_available2"]}")
        if not_pystray:
            broken_components.append(f"{l["library"]} pystray: {l["not_available2"]}")
        if not_bytesio:
            broken_components.append(f"{l["library"]} bytesio: {l["not_available2"]}")
        if not_multiprocessing:
            broken_components.append(f"{l["library"]} multiprocessing: {l["not_available2"]}")
        if not_threading:
            broken_components.append(f"{l["library"]} threading: {l["not_available2"]}")
        if not_signal:
            broken_components.append(f"{l["library"]} signal: {l["not_available2"]}")

        critical_error = (
            f"{l["critical_fail_detect"]}.\n"
            f"{l["damage"]}:\n" +
            "\n".join(broken_components)
        )
        messagebox.showerror(random_string(), critical_error)
except Exception as e:
    logger.exception(f"T - {l["checking_damage_error"]}", e)

#Глобальные Переменные
global T_log_txt, start_interface, run_in_recovery, current_theme
font_trey = "Default"
trey_version = "2.4.3 Beta build 6"
on_board_pc_version = l["not_stable"]

def Crowbar():
    global start_lp, start_interface, current_theme, run_in_recovery, current_disc

    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logger.add(f"{log_path}\\{T_log_txt}", format="{time} {level} {message}", rotation="100 KB", compression="zip")

    current_disc = None

    def check_is_recovery():
        if os.environ.get("WINPE") == "1":
            return True
        return False

    try:
        try:
            run_in_recovery = check_is_recovery()
            if run_in_recovery:
                logger.warning(f"T - {l["run_in_recovery"]}")
            else:
                logger.info(f"T - {l["run_in_normal"]}")
        except Exception as e:
            run_in_recovery = True
            logger.exception(f"T - {l["environment_error"]}", e)

        if run_in_recovery:
            current_disc, found_disc = get_current_disc(run_in_recovery)
            if found_disc:
                logger.info(f"T - {l["load_bush"]} {current_disc}...")
                load_bush(current_disc)

    except Exception as e:
        comment = f"T -{runtime_error}"
        logger.exception(comment, e)
        messagebox.showerror(random_string(), f"{comment}:\n{e}")

    check_and_restore_fonts_if_needed(run_in_recovery)

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

                    font_paths = r"C:\Windows\Fonts\arial.ttf"

                    font = ImageFont.truetype(font_paths, 24)

                    if font is None:
                        font = ImageFont.load_default()
                        logger.warning(f"T - {l["use_default_font"]}.")

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
                        #logger.warning("T - Режим восстановления: Трей отключен.")
                        return
                    try:
                        icon.visible = True
                    except Exception as e:
                        logger.exception(f"T - {l["trey_error"]}", e)

                if run_in_recovery:
                    current_disc_r, found_disc = get_current_disc(run_in_recovery)
                else:
                    current_disc_r = "C:\\"

                #Создаём меню в зависимости от условия доступности компонента
                def create_menu_item(condition, enabled_text, enabled_func, component_name):
                    if condition:
                        disabled_text = f"[!] {l["component"]} {component_name} {l["not_available"]}""."
                        return MenuItem(disabled_text, lambda: None)
                    else:
                        return MenuItem(enabled_text, enabled_func)

                unlocker_menu = Menu(
                    create_menu_item(not_arm, l["ARM"], lambda: run_component_process(ARM, run_in_recovery, current_theme), "ARM"),
                    create_menu_item(not_pm, l["PM"], lambda: run_component_process(PM, run_in_recovery, current_theme), "PM"),
                    create_menu_item(not_fm, l["FM"], lambda: run_component_process(FM, run_in_recovery, current_theme), "FM"),
                    create_menu_item(not_fr, l["FR"], lambda: run_component(FR, run_in_recovery, current_theme), "FR"),
                    create_menu_item(not_um, l["UM"], lambda: run_component(UM, current_theme), "UM"),
                    create_menu_item(not_fe, l["FE"], lambda: run_component(FE), "FE"),
                    create_menu_item(not_sp, l["SP"], lambda: run_component(SP, run_in_recovery, current_disc_r, current_theme), "SP"),
                    create_menu_item(not_cc, l["CC"], lambda: CC(run_in_recovery), "CC"),
                    create_menu_item(not_of, l["open_with"], open_with, "OF"),
                    create_menu_item(not_r, l["R"], R, "R")
                )

                #Меню По ПКМ
                image = create_image(20, 20)
                menu = Menu(
                    create_menu_item(not_cm, f"{l["open"]} {l["CM"]}", lambda: run_component(CM, run_in_recovery, current_theme), "CM"),
                    MenuItem(l["utilities"], unlocker_menu),
                    create_menu_item(not_ua, l["UA"], lambda: UA(run_in_recovery), "UA"),
                    create_menu_item(not_run, l["Run"], lambda: run_component_process(Run, current_theme), "Run"),
                    create_menu_item(not_ap, l["AP"], lambda: run_component(AP,
                        autorun_master_version,
                        anti_xyina_version,
                        clear_cache_version,
                        crowbar_menu_version,
                        crowbar_console_version,
                        exit_version,
                        edit_criticality_version,
                        file_editor_version,
                        file_manager_version,
                        file_replacer_version,
                        get_full_access_version,
                        on_board_pc_version,
                        other_function_version,
                        process_manager_version,
                        restart_version,
                        real_time_protect_version,
                        random_string_version,
                        run_version,
                        settings_and_update_version,
                        scarecrow_protection_version,
                        trey_version,
                        unlock_all_version,
                        users_manager_version
                    ), "AP"),
                    create_menu_item(not_console, l["Console"], lambda: open_console({
                        "run_component": run_component,
                        "run_component_process": run_component_process,
                        "run_in_recovery": run_in_recovery,
                        "current_theme": current_theme,
                        "AP": AP,
                        "ARM": ARM,
                        "CC": CC,
                        "CC22": CC22,
                        "CM": CM,
                        "config": config,
                        "EC": EC,
                        "FE": FE,
                        "FM": FM,
                        "FR": FR,
                        "GFA": GFA,
                        #OF
                        "Psutil": Psutil,
                        "run_component": run_component,
                        "apply_global_theme": apply_global_theme,
                        "get_offline_reg_path": get_offline_reg_path,
                        "get_current_disc": get_current_disc,
                        "load_bush": load_bush,
                        "unload_bush": unload_bush,
                        "get_user_name": get_user_name,
                        "open_with": open_with,
                        "reg_path": reg_file,
                        "run_command": run_command,
                        "PM": PM,
                        "RLP": RLP,
                        "RS": random_string,
                        "Run": Run,
                        "SAU": SAU,
                        "SP": SP,
                        "UA": UA,
                        "UM": UM,
                        "icon": icon if "icon" in locals() else None,
                        "logger": logger,
                    }), "Console"),
                    create_menu_item(not_sau, l["SAU"], lambda: run_component(SAU, current_theme), "SAU"),
                    create_menu_item(not_config, f"{l["pac"]} - {program_authentication_clyth}", pac, "config"),
                    create_menu_item(not_e, l["E"], E, "Exit")
                )

                icon = pystray.Icon("Crowbar_Antivirus_Icon", image, "Crowbar Antivirus", menu)

                if start_interface == "icon" or start_interface == "window":
                    try:
                        thread_icon = threading.Thread(target=icon.run)
                        thread_icon.daemon = True
                        thread_icon.start()

                        start_icon()
                    except Exception as e:
                        logger.exception(f"T - {l["icon_start_error"]}!", e)
                if start_lp:
                    run_component(RLP)

                if start_interface == "window" or start_interface == "only-windows":
                    run_component(CM, run_in_recovery, current_theme)

                if start_cash:
                    hcas_thread = threading.Thread(target=CASH, args=(run_in_recovery,), daemon=True)
                    hcas_thread.start()

                while True:
                    time.sleep(1)
            except Exception as e:
                logger.exception(f"T - {l["icon_start_error"]}!", e)
                CM(run_in_recovery, current_theme, current_disc)

        if run_in_recovery:
            CM(run_in_recovery, current_theme, current_disc)

    except Exception as e:
        logger.exception(l["t_critical_error"], e)
        CM(run_in_recovery, current_theme, current_disc)
    finally:
        if run_in_recovery:
            logger.infof(f"T - {l["unload_bush"]}")

        if not run_in_recovery:
            signal.signal(signal.SIGTERM, restart_ca)

if __name__ == "__main__":
    try:
        multiprocessing.freeze_support()
    except Exception as e:
        logger.exception(f"T - {l["multiprocessing_error"]}", e)

    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            try:
                Crowbar()
            except Exception as e:
                comment = f"T - {l["t_critical_error"]}"
                logger.exception(comment, e)
                if messagebox.askyesno(random_string(), f"{comment}:\n{e}\n\n{l["restart_program"]}?"):
                    Crowbar()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except Exception as e:
        admin_error = f"T - {l["admin_error"]}"
        logger.exception(admin_error, e)
        messagebox.showerror(random_string(), f"{admin_error}:\n{e}")
