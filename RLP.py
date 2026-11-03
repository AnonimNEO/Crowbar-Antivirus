# Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
# Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
# ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
# В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
# ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
# Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
# Или в файле COPYING.txt в архиве с установщиком
# Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
# Coded by AnonimNEO (Github)



# ДАННЫЙ КОМПОНЕНТ НЕ ДОДЕЛАН, НЕ ГАРАНТИРОВАН ДАЖЕ ЗАПУСК


# Интерфейс
from tkinter import messagebox
# Логирование
from loguru import logger
# работал с каталогами
from pathlib import Path
# Работа с процессами
import psutil

from RS import RS
from EC import get_process_critical_status
from PM import action_process, get_process_name, get_process_info, get_process_list

REAL_TIME_PROTECT_VERSION = "0.1.7 Pre-Alpha"

def RLP(RUN_IN_RECOVERY=False, DEBUG_MODE=False):
    if RUN_IN_RECOVERY:
        messagebox.showwarning(RS(), "RealTimeProtect невозможно запустить в среде восстановления")

    SUSPEND_PROCESS = []
    SYSTEM_PROCESS = (
        (r"C:\Windows\System32\cmd.exe", 0),
        (r"C:\Windows\notepad.exe", 0),
        (r"C:\Windows\System32\calc.exe", 0),
        (r"C:\Windows\explorer.exe", 0),
        (r"C:\Windows\System32\powershell.exe", 0),
        (r"C:\Windows\System32\taskmgr.exe", 0),
        (r"C:\Windows\regedit.exe", 0),
        (r"C:\Windows\System32\mspaint.exe", 0),
    )
    EXCEPTION = [[r"C:\Users\Adminus\Desktop\calc.exe", 0], [r"C:\Windows\explorer.exe", 0]]

    def warning_dialog(cause, p):
        if cause == "fake_system":
            cause_text = f'Процесс {p["Имя Процесса"]}({p["PID"]}), притворяется системным с помощью имению, но его файл расположен в: {p["Путь к файлу"]} и поэтому был замрожен'

  
    def stop_process(cause, p):
        action_process("suspend", p["PID"])
        SUSPEND_PROCESS.append(p["PID"])
        warning_dialog(cause, p)

    def check_system_process(PROCESS_LIST):
        if DEBUG_MODE:
            logger.debug("RLP - Проверка системных процессов...")
        for p in PROCESS_LIST:
            p_name = p["Имя"]
            p_exe = p["Путь к файлу"]

            for sys_exe, sys_byte in system_name_process:
                sys_name = Path(p_exe).name
                if p_name == sys_name:
                    if p_exe != sys_exe:
                        stop_process("fake_system", p)

    def filter_process_for_exception(PROCESS_LIST):
        for p in PROCESS_LIST:
            for except_sys_name in system_exception:
                if p["Путь к файлу"] == except_sys_name:
                    PROCESS_LIST.remove(p)

        return PROCESS_LIST

    while True:
        PROCESS_LIST = get_process_list("all_list", RUN_IN_RECOVERY)

        PROCESS_LIST = filter_process_for_exception(PROCESS_LIST)

        check_system_process(PROCESS_LIST)

if __name__ == "__main__":
    RLP(False, True)
