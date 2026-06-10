#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

from tkinter import messagebox
from loguru import logger
import sys
import os

#Импорт Компонентов
try:
    from AP import AP
except Exception as e:
    def AP(a=None, b=None, c=None, d=None, e=None, f=None, j=None, q=None, w=None, r=None, t=None, y=None, u=None, i=None, o=None, s=None, h=None, k=None, l=None):
        print(f"CASH - {l["component_import_error"]} AboutProgram")
try:
    from ARM import ARM
except Exception as e:
    def ARM(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} AutoRunMaster")

try:
    from CC import CC
except Exception as e:
    def CC(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} ClearCache")

try:
    from CC22 import CC22
except Exception as e:
    def CC22():
        return "error"

try:
    from config import *
    import config
except Exception as e:
    print(f"CASH - {l["component_import_error"]} config")

try:
    from E import E
except Exception as e:
    def E():
        print(f"CASH - {l["component_import_error"]} Exit")

try:
    from EC import EC
except Exception as e:
    def EC(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} EditCritical")

try:
    from FE import FE
except Exception as e:
    def FE(a=None):
        print(f"CASH - {l["component_import_error"]} FileEditor")

try:
    from FM import FM
except Exception as e:
    def FM(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} FileManager")

try:
    from FR import FR
except Exception as e:
    def FR(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} FileReplacer")

try:
    from GFA import GFA
except Exception as e:
    def GFA(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} GetFullAccess")

try:
    from RLP import RLP
except Exception as e:
    def RLP(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} RealTimeProtect")

try:
    from CM import CM
except Exception as e:
    def CM(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} CrowbarMenu")

try:
    from OF import pac, apply_global_theme, get_offline_reg_path, Psutil, run_component, run_component_process, get_user_name, restart_ca, reg_file, run_command, open_with, get_current_disc, load_bush, unload_bush
except Exception as e:
    def of_error():
        print(f"CASH - {l["component_import_error"]} OtherFunction")
    def restart_ca():
        of_error()
    def open_with():
        of_error()
    def pac():
        messagebox.showerror(random_string(), f"{l["pac"]} {l["not_available"]}!")
    def apply_global_theme(a=None, b=None):
        of_error()
    def get_offline_reg_path(a=None, b=None):
        of_error()
    def run_component(a=None, b=None):
        of_error()
    def run_component_process(a=None, b=None):
        of_error()
    def run_command(a=None, b=None):
        of_error()
    def load_bush(a=None, b=None):
        of_error()
    def unload_bush(a=None, b=None):
        of_error()
    def get_current_disc(a=None, b=None):
        of_error()
    def get_user_name(a=None, b=None):
        of_error()

try:
    from PM import PM
except Exception as e:
    def PM(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} ProcessManager")

try:
    from R import R
except Exception as e:
    def R():
        print(f"CASH - {l["component_import_error"]} Restart")

try:
    from RS import random_string
except Exception as e:
    def random_string():
        return "error"

try:
    from Run import Run
except Exception as e:
    def Run(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} Run")

try:
    from SAU import SAU
except Exception as e:
    def SAU(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} SettingsAndUpdate")

try:
    from SP import SP, scarecrow_protection_version
except Exception as e:
    def SP(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} ScarecrowProtection")

try:
    from UA import UA, check_and_restore_fonts_if_needed
except Exception as e:
    def check_and_restore_fonts_if_needed(a=None):
        print(f"CASH - {l["component_import_error"]} UA/check_and_restore_fonts_if_needed")
    def UA(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} UA")

try:
    from UM import UM
except Exception as e:
    def UM(a=None, b=None):
        print(f"CASH - {l["component_import_error"]} UserManager")

crowbar_antivirus_scripts_handler_version = "0.4.2 Alpha"

current_theme = theme[default_theme]

#Получаем настройки скрипта
def get_script_config(code):
    config = {
        "delete_script_after_exec": False,
        "launch_when_program_starts": False,
        "enable_while": False,
    }

    #Ищем строки с переменными конфигурации
    for line in code.split("\n"):
        line = line.strip()

        #Пропускаем комментарии и пустые строки
        if not line or line.startswith("#"):
            continue

        if "delete_script_after_exec" in line and "=" in line:
            try:
                value = line.split("=")[1].strip()
                config["delete_script_after_exec"] = value.lower() == "true"
            except:
                pass

        elif "launch_when_program_starts" in line and "=" in line:
            try:
                value = line.split("=")[1].strip()
                config["launch_when_program_starts"] = value.lower() == "true"
            except:
                pass

        elif "enable_while" in line and "=" in line:
            try:
                value = line.split("=")[1].strip()
                config["enable_while"] = value.lower() == "true"
            except:
                pass

        #Выходим, если начался код скрипта
        if line and not line.startswith("#") and not any(var in line for var in
            ["delete_script_after_exec", "launch_when_program_starts", "enable_while", "valid_version"]):
            break

    return config



def CASH(run_in_recovery, debug_mode=False):
    while True:
        if len(sys.argv) > 1:
            #Был передан файл
            file_path = sys.argv[1]
            if debug_mode:
                logger.debug(f"CASH - {l("file_transferred")}: {file_path}")
            #Получаем расширение файла
            _, file_extension = os.path.splitext(file_path)
            f_e = file_extension.lower() #Преобразуем в нижний регистр
            if f_e == ".txt" or f_e == ".md" or f_e == ".py":
                FE(file_path)
                break
            elif f_e == ".cas":
                try:
                    with open(file_path, "r", encoding="utf-8-sig") as script:
                        code = script.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, "r", encoding="cp1251") as script:
                            code = script.read()
                    except UnicodeDecodeError:
                        #Попытка с игнорированием ошибок
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as script:
                            code = script.read()

                #code = CC22(code, clyth, True)

                config = get_script_config(code)
                
                if debug_mode:
                    logger.debug(f"CASH - {l("script_config")}: {config}")

                #Создаём контекст выполнения с доступными функциями программы
                exec_globals = {
                    #"__builtins__": __builtins__,
                    "logger": logger,
                    "sys": sys,
                    "os": os,
                    "messagebox": "messagebox",
                    "run_in_recovery": run_in_recovery,
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
                    "reg_file": reg_file,
                    "run_command": run_command,
                    "PM": PM,
                    "RLP": RLP,
                    "RS": random_string,
                    "Run": Run,
                    "SAU": SAU,
                    "SP": SP,
                    "UA": UA,
                    "UM": UM,
                }

                try:
                    exec(code, exec_globals)
                except Exception as e:
                    logger.exception(f"CASH - {l("exec_script_error")} {file_path}")
                    messagebox.showerror(random_string(), f"{l("exec_script_error")}:\n{e}")

                #Используем полученную конфигурацию
                delete_script_after_exec = config["delete_script_after_exec"]
                launch_when_program_starts = config["launch_when_program_starts"]
                enable_while = config["enable_while"]

                if delete_script_after_exec:
                    try:
                        os.remove(file_path)
                        if debug_mode:
                            logger.debug(f"CASH - {l("script_deleted")}: {file_path}")
                    except Exception as e:
                        logger.exception(f"CASH - {l("script_deleted_error")}: {file_path}")

                #Если enable_while=False или launch_when_program_starts=False, выходим из цикла
                if not enable_while or not launch_when_program_starts:
                    break
                #Если enable_while=True, цикл продолжится и скрипт выполнится снова
                if not enable_while:
                    logger.success(f"CASH - {l("execution_completed")}.")
            else:
                messagebox.showwarning(random_string(), l("command_not_found_for_file"))
                break
        else:
            break #Выход, если файл не был передан

if __name__ == "__main__":
    CASH(False, True)
