#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Логирование Ошибок
from loguru import logger
#Работа с ОС
import ctypes
from ctypes import wintypes
import psutil

from OF import Psutil
from languages import l
from config import current_localization

edit_criticality_version = "0.4.4 Beta"

#Загрузка необходимых библиотек windows
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
ntdll = ctypes.WinDLL("ntdll", use_last_error=True)

#Определение структур и констант
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_SET_INFORMATION = 0x0200
STATUS_SUCCESS = 0

#0x1D (29) - ProcessBreakOnTermination: используется для установки/запроса критичности.
#Значение (ULONG): 1 - критический, 0 - некритический
PROCESS_INFORMATION_CLASS_CRITICAL = 0x1D

#Определяем функции windows API
def define_functions():
    #kernel32.OpenProcess
    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel32.OpenProcess.restype = wintypes.HANDLE

    #kernel32.CloseHandle
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL

    #ntdll.NtSetInformationProcess (Для установки критичности)
    ntdll.NtSetInformationProcess.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.ULONG]
    ntdll.NtSetInformationProcess.restype = wintypes.LONG

    #ntdll.NtQueryInformationProcess (Для запроса критичности)
    ntdll.NtQueryInformationProcess.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.ULONG, ctypes.POINTER(wintypes.ULONG)]
    ntdll.NtQueryInformationProcess.restype = wintypes.LONG


#Получаем имя процесса
def get_process_name(process_id):
    try:
        process = psutil.Process(process_id)
        return process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return f"Unknown_PID_{process_id}"


#Получаем текущий статус критичности процесса
def get_process_critical_status(process_id, debug_mode=False):
    process_handle = None
    try:
        define_functions()

        #Открываем процесс с правом на запрос информации
        process_handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, process_id)

        if not process_handle:
            error_code = ctypes.get_last_error()
            if debug_mode:
                logger.error(f"EC - {l("open_process_error")} (pid: {process_id}). {l("error_code")}: {error_code}")
            return None

        #Переменная для хранения результата
        critical_value = ctypes.c_ulong(0)
        return_length = ctypes.c_ulong(0)

        #Вызываем NtQueryInformationProcess с классом 0x1D
        result = ntdll.NtQueryInformationProcess(process_handle, PROCESS_INFORMATION_CLASS_CRITICAL, ctypes.byref(critical_value), ctypes.sizeof(critical_value), ctypes.byref(return_length))

        if result == STATUS_SUCCESS:
            is_critical = bool(critical_value.value)
            if debug_mode:
                logger.info(f"EC - {l("process")} (pid: {process_id}) {l("criticality_status")}: {is_critical}")
            return is_critical
        else:
            logger.error(f"EC - {l("query_critical_error")}. {l("error_code")}: {hex(result)}")
            return None

    except:
        logger.exception(f"EC - {l("get_critical_unknown_error")}")
        return None
    finally:
        if process_handle:
            kernel32.CloseHandle(process_handle)


#Меняем значение критичности на процессе
def set_process_critical(process_id, critical):
    process_handle = None
    try:
        define_functions()

        #Получаем handle процесса с правами на изменение и запрос информации
        process_handle = kernel32.OpenProcess(PROCESS_SET_INFORMATION | PROCESS_QUERY_INFORMATION, False, process_id)

        if not process_handle:
            error_code = ctypes.get_last_error()
            process_name = get_process_name(process_id)
            logger.error(f"EC - {l("open_process_error")} {process_name} (pid: {process_id}). {l("error_code")}: {error_code}")
            return False

        #Значение 1 для True (критический), 0 для False (некритический)
        critical_value = ctypes.c_ulong(1 if critical else 0)

        #Вызываем NtSetInformationProcess с классом 0x1D
        result = ntdll.NtSetInformationProcess(process_handle, PROCESS_INFORMATION_CLASS_CRITICAL, ctypes.byref(critical_value), ctypes.sizeof(critical_value))

        if result == STATUS_SUCCESS:
            status = l("installed") if critical else l("removed")
            logger.success(f"EC - {l("process_critical")} {process_id} {status} ({l("target")}: {critical})")
            return True
        else:
            logger.error(f"EC - {l("edit_critical_error")}. {l("error_code")}: {hex(result)}")
            return False

    except:
        logger.exception(f"EC - {l("edit_critical_unknown_error")}")
        return False
    finally:
        if process_handle:
            kernel32.CloseHandle(process_handle)



def EC(process_id, critical=None, debug_mode=False):
    try:
        process_name = get_process_name(process_id)

        if not psutil.pid_exists(process_id):
            if debug_mode:
                logger.debug(f"EC - {l("process")} {process_name} (pid: {process_id}) {l("not_found")}!")
            return None

        #Если critical=None, только считываем статус
        if critical is None:
            current_status = get_process_critical_status(process_id)
            return current_status

        #Иначе устанавливаем новое значение и проверяем результат
        if set_process_critical(process_id, critical):
            #Проверяем, успешно ли изменилось значение
            verified_status = get_process_critical_status(process_id)

            if verified_status == critical:
                logger.success(f"EC - {l("criticality_status")} {process_name} (pid: {process_id}) {l("changed_to")} {critical}")
                return True
            else:
                logger.warning(f"EC - {l("criticality_status")} {process_name} (pid: {process_id}) {l("change_verify_failed")}")
                return False
        else:
            logger.error(f"EC - {l("criticality_status")} {process_name} (pid: {process_id}) {l("no_changed")}")
            return False

    except:
        logger.exception(f"{l("ec_critical_error")}")
        return None