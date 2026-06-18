#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Локализация
from languages import l

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
except:
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

    logger.exception(f"T - {l("import_error")} loguru! {l("replacement_is_used")}")

#Интерфейс
try:
    from tkinter import messagebox, simpledialog
    import tkinter as tk
except:
    not_tkinter = True
    logger.exception(f"T - {l("import_error")} tkinter")

try:
    #Рисование иконки в трее и вставка картинок
    from PIL import Image, ImageDraw, ImageFont
except:
    not_pillow = True
    logger.exception(f"T - {l("import_error")} Pillow")

#Получение прав Администратора
try:
    from elevate import elevate
except:
    not_elevate = True
    logger.exception(f"T - {l("import_error")} elevate")

#Движок иконки в трее
try:
    from pystray import MenuItem, Menu
    import pystray
except:
    not_pystray = True
    logger.exception(f"T - {l("import_error")} pystray", e)

#Работа с потоками
try:
    from io import BytesIO
except:
    not_bytesio = True
    logger.exception(f"T - {l("import_error")} BytesIO")

try:
    import multiprocessing
except:
    not_multiprocessing = True
    logger.exception(f"T - {l("import_error")} multiprocessing")

try:
    import threading
except:
    not_threading = True
    logger.exception(f"T - {l("import_error")} threading")

try:
    import signal
except:
    not_signal = True
    logger.exception(f"T - {l("import_error")} signal")

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
not_rm = False
not_sim = False

#Импорт Компонентов
#from OBPC import OBPC, on_board_pc_version
try:
    from AP import AP
except:
    not_ap = True
    logger.exception(f"T - {l("component_import_error")} AboutImage")

try:
    from ARM import ARM, autorun_master_version
except:
    not_arm = True
    logger.exception(f"T - {l("component_import_error")} AutoRunMaster")

try:
    from CC import CC, clear_cache_version
except:
    not_cc = True
    logger.exception(f"T - {l("component_import_error")} ClearCache")

try:
    from AES import AES
except:
    not_cc2 = True
    def AES(a=None, b=None, c=None):
        return "error"
    logger.exception(f"T - {l("component_import_error")} AES")

try:
    from config import log_path, T_log_txt, theme, default_theme, program_authentication_clyth, start_interface, start_cash, start_lp
    import config
except:
    not_config = True
    logger.exception(f"T - {l("import_error")} config!")

try:
    from E import E, exit_version
except:
    not_e = True
    def E():
        pass
    logger.exception(f"T - {l("component_import_error")} Exit")

try:
    from EC import EC, edit_criticality_version
except:
    not_ec = True
    def EC():
        pass
    logger.exception(f"T - {l("component_import_error")} EditCritical")

try:
    from FE import FE, file_editor_version
except:
    not_fe = True
    logger.exception(f"T - {l("component_import_error")} FileEditor")

try:
    from FM import FM, file_manager_version
except:
    not_fm = True
    logger.critical(f"T - {l("component_import_error")} FileManager")

try:
    from FR import FR, file_replacer_version
except:
    not_fr = True
    logger.exception(f"T - {l("component_import_error")} FileReplacer")

try:
    from GFA import GFA, get_full_access_version
except:
    def GFA():
        pass
    logger.exception(f"T - {l("component_import_error")} GetFullAccess")

try:
    from RLP import RLP, real_time_protect_version
except:
    not_rlp = True
    logger.exception(f"T - {l("component_import_error")} RealTimeProtection")

try:
    from CM import CM, crowbar_menu_version
except:
    not_cm = True
    crowbar_menu_version = "error"
    def CM(a=None, b=None, c=None):
        pass
    logger.exception(f"T - {l("component_import_error")} MountUnlocker")

try:
    from RS import RS, random_string_version
except:
    def RS(a=None):
        return "error"
    not_rs = True
    logger.exception(f"T - {l("component_import_error")} RandomString")

try:
    from OF import pac, apply_global_theme, get_offline_reg_path, Psutil, run_component, run_component_process, get_user_name, restart_ca, reg_file, run_command, open_with, get_current_disc, load_bush, unload_bush, enable_debug_mode, other_function_version, CMD, decoy_mode, extract_filename_from_path, launch_ghost
except:
    not_of = True
    def restart_ca():
        while True:
            input(">>> Fatal error")
    def open_with():
        pass
    def enable_debug_mode():
        pass
    def pac():
        messagebox.showerror(RS(), f"{l("pac")} {l("not_available")}!")
    def CMD():
        pass
    def decoy_mode(a=None, b=None):
        pass
    def extract_filename_from_path(a=None, b=None):
        pass
    def launch_ghost(a=None):
        pass
    logger.exception(f"T - {l("component_import_error")} OtherFunction")

try:
    from PM import PM, process_manager_version
except:
    not_pm = True
    logger.exception(f"T - {l("component_import_error")} ProcessManager")

try:
    from R import R, restart_version
except:
    not_r = True
    def R():
        pass
    logger.exception(f"T - {l("component_import_error")} Restart")

try:
    from Run import Run, run_version
except:
    not_run = True
    logger.exception(f"T - {l("component_import_error")} Run")

try:
    from SAU import SAU, settings_and_update_version
except:
    not_sau = True
    logger.exception(f"T - {l("component_import_error")} SettingsAndUpdate")

try:
    from SP import SP, scarecrow_protection_version
except:
    not_sp = True
    logger.exception(f"T - {l("component_import_error")} ScarecrowProtection")

try:
    from UA import UA, check_and_restore_fonts_if_needed, unlock_all_version
except:
    not_ua = True
    def check_and_restore_fonts_if_needed(a=None, b=None):
        pass
    logger.exception(f"T - {l("component_import_error")} UnlockAll")

try:
    from UM import UM, users_manager_version
except:
    not_um = True
    logger.exception(f"T - {l("component_import_error")} UserManager")

try:
    from SIM import SIM, software_installation_manager
except:
    nor_sim = True
    logger.exception(f"T - {l("component_import_error")} SoftwareInstallationManager")

try:
    from RM import registry_monitor
except:
    not_rm = True
    logger.exception(f"T - {l("component_import_error")} RegistryMonitor")

#Импорт консоли разработчика
try:
    from Console import open_console, crowbar_console_version
except:
    not_console = True
    logger.exception(f"T - {l("component_import_error")} Console")

#Импорт движка скриптов
try:
    from CASH import CASH, crowbar_antivirus_scripts_handler_version
except:
    not_cash = True
    logger.exception(f"T - {l("component_import_error")} CASH")

try:
    if not_pystray and not_cm and not not_tkinter:
        broken_components = []
        c = l("component")
        li = l("library")
        na = l("not_available")
        na2 = l("not_available2")

        if not_ap:
            broken_components.append(f"{c} AP: {na}")
        if not_arm:
            broken_components.append(f"{c} ARM: {na}")
        if not_cc:
            broken_components.append(f"{c} CC: {na}")
        if not_e:
            broken_components.append(f"{c} E: {na}")
        if not_ec:
            broken_components.append(f"{c} EC: {na}")
        if not_fm:
            broken_components.append(f"{c} FM: {na}")
        if not_fr:
            broken_components.append(f"{c} FR: {na}")
        if not_rlp:
            broken_components.append(f"{c} RLP: {na}")
        if not_cm:
            broken_components.append(f"{c} CM: {na}")
        if not_of:
            broken_components.append(f"{c} OF: {na}")
        if not_pm:
            broken_components.append(f"{c} PM: {na}")
        if not_r:
            broken_components.append(f"{c} R: {na}")
        if not_rs:
            broken_components.append(f"{c} RS: {na}")
        if not_run:
            broken_components.append(f"{c} Run: {na}")
        if not_sau:
            broken_components.append(f"{c} SAU: {na}")
        if not_sp:
            broken_components.append(f"{c} SP: {na}")
        if not_ua:
            broken_components.append(f"{c} UA: {na}")
        if not_um:
            broken_components.append(f"{c} UM: {na}")
        if not_console:
            broken_components.append(f"{c} Console: {na}")
        if not_cash:
            broken_components.append(f"{c} CASH: {na}")
        if not_sim:
            broken_components.append(f"{c} SIM: {na}")
        if not_rm:
            broken_components.append(f"{c} RM: {na}")
        if not_loguru:
            broken_components.append(f"{li} loguru: {na2}")
        if not_tkinter:
            broken_components.append(f"{li} tkinter: {na2}")
        if not_pillow:
            broken_components.append(f"{li} pillow: {na2}")
        if not_elevate:
            broken_components.append(f"{li} elevate: {na2}")
        if not_pystray:
            broken_components.append(f"{li} pystray: {na2}")
        if not_bytesio:
            broken_components.append(f"{li} bytesio: {na2}")
        if not_multiprocessing:
            broken_components.append(f"{li} multiprocessing: {na2}")
        if not_threading:
            broken_components.append(f"{li} threading: {na2}")
        if not_signal:
            broken_components.append(f"{li} signal: {na2}")

        critical_error = (
            f"{l("critical_fail_detect")}.\n"
            f"{l("damage")}:\n" +
            "\n".join(broken_components)
        )
        messagebox.showerror(RS(), critical_error)
except:
    logger.exception(f"T - {l("checking_damage_error")}")

global debug_mode
font_trey = "Default"
trey_version = "2.4.13 Beta"
on_board_pc_version = l("not_stable")
debug_mode = True

def Crowbar():
    if debug_mode:
        messagebox.showwarning(RS(), l("warning_debug_mode_on"))
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
                logger.warning(f"T - {l("run_in_recovery")}")
            else:
                logger.info(f"T - {l("run_in_normal")}")
        except:
            run_in_recovery = True
            logger.exception(f"T - {l("environment_error")}")

        if run_in_recovery:
            current_disc, found_disc = get_current_disc(run_in_recovery)
            if found_disc:
                logger.info(f"T - {l("load_bush")} {current_disc}...")
                load_bush(current_disc)

    except:
        comment = f"T -{l("runtime_error")}"
        logger.exception(comment)
        messagebox.showerror(RS(), f"{comment}:\n{e}")

    check_and_restore_fonts_if_needed(run_in_recovery, debug_mode)

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
                        logger.warning(f"T - {l("use_default_font")}.")

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
                    except:
                        logger.exception(f"T - {l("trey_error")}")

                if run_in_recovery:
                    current_disc_r, found_disc = get_current_disc(run_in_recovery)
                else:
                    current_disc_r = "C:\\"

                #Создаём меню в зависимости от условия доступности компонента
                def create_menu_item(condition, enabled_text, enabled_func, component_name):
                    if condition:
                        disabled_text = f"[!] {l("component")} {component_name} {l("not_available")}."
                        return MenuItem(disabled_text, lambda: None)
                    else:
                        return MenuItem(enabled_text, enabled_func)

                def t_enable_debug_mode():
                    global debug_mode
                    debug_mode = enable_debug_mode()

                unlocker_menu = Menu(
                    create_menu_item(not_arm, l("ARM"), lambda: run_component_process(ARM, run_in_recovery, current_theme, debug_mode), "ARM"),
                    create_menu_item(not_pm, l("PM"), lambda: run_component_process(PM, run_in_recovery, current_theme, debug_mode), "PM"),
                    create_menu_item(not_fm, l("FM"), lambda: run_component_process(FM, run_in_recovery, current_theme, debug_mode), "FM"),
                    create_menu_item(not_fr, l("FR"), lambda: run_component(FR, run_in_recovery, current_theme, debug_mode), "FR"),
                    create_menu_item(not_um, l("UM"), lambda: run_component(UM, current_theme, debug_mode), "UM"),
                    create_menu_item(not_fe, l("FE"), lambda: run_component(FE), "FE"),
                    create_menu_item(not_sp, l("SP"), lambda: run_component(SP, run_in_recovery, current_disc_r, current_theme, debug_mode), "SP"),
                    create_menu_item(not_cc, l("CC"), lambda: run_component(CC, run_in_recovery), "CC"),
                    create_menu_item(not_sim, l("SIM"), lambda: run_component(SIM, run_in_recovery, current_theme, debug_mode), "SIM"),
                    create_menu_item(not_of, "CMD", lambda: run_component(CMD), "OF"),
                    create_menu_item(not_of, l("open_with"), open_with, "OF"),
                    create_menu_item(not_of, l("enable_debug_mode"), t_enable_debug_mode, "OF"),
                    create_menu_item(not_r, l("R"), R, "R")
                )

                #Меню По ПКМ
                image = create_image(20, 20)
                del(_icon_buffer)
                menu = Menu(
                    create_menu_item(not_cm, f"{l("open")} {l("CM")}", lambda: run_component(CM, run_in_recovery, current_theme, debug_mode), "CM"),
                    MenuItem(l("utilities"), unlocker_menu),
                    create_menu_item(not_ua, l("UA"), lambda: UA(run_in_recovery, debug_mode), "UA"),
                    create_menu_item(not_run, l("Run"), lambda: run_component_process(Run, current_theme), "Run"),
                    create_menu_item(not_ap, l("AP"), lambda: run_component(AP,
                        autorun_master_version,
                        crowbar_antivirus_scripts_handler_version,
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
                        registry_monitor,
                        random_string_version,
                        run_version,
                        settings_and_update_version,
                        software_installation_manager,
                        scarecrow_protection_version,
                        trey_version,
                        unlock_all_version,
                        users_manager_version
                    ), "AP"),
                    create_menu_item(not_console, l("Console"), lambda: open_console({
                        "run_component": run_component,
                        "run_component_process": run_component_process,
                        "run_in_recovery": run_in_recovery,
                        "current_theme": current_theme,
                        "debug_mode": debug_mode,
                        "AP": AP,
                        "ARM": ARM,
                        "CC": CC,
                        "AES": AES,
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
                        "reg_file": reg_file,
                        "run_command": run_command,
                        "decoy_mode": decoy_mode,
                        "launch_ghost": launch_ghost,
                        "extract_filename_from_path": extract_filename_from_path,
                        "PM": PM,
                        "RLP": RLP,
                        "RS": RS,
                        "Run": Run,
                        "SAU": SAU,
                        "SP": SP,
                        "UA": UA,
                        "UM": UM,
                        "logger": logger,
                    }, debug_mode), "Console"),
                    create_menu_item(not_sau, l("SAU"), lambda: run_component(SAU, current_theme), "SAU"),
                    create_menu_item(not_config, f"{l("pac")} - {program_authentication_clyth}", pac, "config"),
                    create_menu_item(not_e, l("E"), E, "Exit")
                )

                icon = pystray.Icon("Crowbar_Antivirus_Icon", image, "Crowbar Antivirus", menu)

                if start_interface == "icon" or start_interface == "window":
                    try:
                        thread_icon = threading.Thread(target=icon.run)
                        thread_icon.daemon = True
                        thread_icon.start()

                        start_icon()
                    except:
                        logger.exception(f"T - {l("icon_start_error")}!")
                if start_lp:
                    run_component(RLP)

                if start_interface == "window" or start_interface == "only-windows":
                    run_component(CM, run_in_recovery, current_theme)

                if start_cash:
                    try:
                        hcas_thread = threading.Thread(target=CASH, args=(run_in_recovery, debug_mode), daemon=True)
                        hcas_thread.start()
                    except:
                        logger.exception(f"T - {l("start_cash_error")}!")

                while True:
                    time.sleep(1)
            except:
                logger.exception(f"T - {l("icon_start_error")}!")
                CM(run_in_recovery, current_theme, current_disc)

        if run_in_recovery:
            CM(run_in_recovery, current_theme, current_disc)

    except:
        logger.exception(l("t_critical_error"))
        CM(run_in_recovery, current_theme, current_disc)
    finally:
        if run_in_recovery:
            logger.infof(f"T - {l("unload_bush")}")

        if not run_in_recovery:
            signal.signal(signal.SIGTERM, restart_ca)

if __name__ == "__main__":
    try:
        multiprocessing.freeze_support()
    except:
        logger.exception(f"T - {l("multiprocessing_error")}")

    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            try:
                Crowbar()
            except Exception as e:
                comment = f"T - {l("t_critical_error")}"
                logger.exception(comment)
                if messagebox.askyesno(RS(), f"{comment}:\n{e}\n\n{l("restart_program")}?"):
                    Crowbar()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except Exception as e:
        admin_error = f"T - {l("admin_error")}"
        logger.exception(admin_error)
        messagebox.showerror(RS(), f"{admin_error}:\n{e}")
        restart_ca()
