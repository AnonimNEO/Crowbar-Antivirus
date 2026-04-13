#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Обучение
from tkinter import messagebox
from RS import random_string
#Работа с реестром и списками
from typing import Tuple, Any
import winreg
#Логирование
from loguru import logger

#from OF2 import get_offline_reg_path, loaded_hive_names
from OF import get_offline_reg_path, loaded_hive_names

unlock_all_version = "1.1.4 Beta"

#Возвращает безопасное "нулевое" значение для сброса параметра
def get_new_value_for_type(reg_type: int) -> Tuple[Any, int]:
    if reg_type in (winreg.REG_DWORD, winreg.REG_QWORD):
        return 0, reg_type
    elif reg_type in (winreg.REG_SZ, winreg.REG_EXPAND_SZ):
        return "", reg_type
    elif reg_type == winreg.REG_MULTI_SZ:
        return [], reg_type
    elif reg_type == winreg.REG_BINARY:
        return b"", reg_type
    return None, reg_type



#Сбрасывает указанные параметры в разделе реестра с учетом оффлайн-режима
def reset_reg_values(hkey_const, chapter, params, ua_globals, is_exception, run_in_recovery):
    key_handle = None
    hive_name = ua_globals["HKEY_MAP"].get(hkey_const, str(hkey_const))

    #Получаем корректный путь в зависимости от среды
    final_hkey, final_subkey = get_offline_reg_path(hkey_const, chapter, ua_globals, run_in_recovery)

    logger.info(f"UA - Обработка раздела: {hive_name}\\{chapter} (Режим исключений: {is_exception})")

    try:
        #Открываем ключ с правами на чтение и запись
        #KEY_QUERY_VALUE нужен для перечисления параметров, KEY_SET_VALUE для изменения
        key_handle = winreg.OpenKey(final_hkey, final_subkey, 0, winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE | winreg.KEY_ENUMERATE_SUB_KEYS)

        targets = []

        if is_exception:
            #получаем список всех параметров в разделе
            try:
                i = 0
                while True:
                    #Получаем имя параметра по индексу
                    param_name, _, _ = winreg.EnumValue(key_handle, i)
                    #Если имени нет в списке исключений — добавляем в очередь на сброс
                    if param_name not in params:
                        targets.append(param_name)
                    i += 1
            except OSError:
                #OSError возникает, когда параметры для перечисления закончились
                pass
        else:
            #работаем только с тем, что передали в списке
            targets = params

        #Процесс сброса
        for param in targets:
            try:
                #Уточняем текущий тип параметра
                _, reg_type = winreg.QueryValueEx(key_handle, param)
                new_val, r_type = get_new_value_for_type(reg_type)

                if new_val is not None:
                    winreg.SetValueEx(key_handle, param, 0, r_type, new_val)
                    logger.success(f'UA - Параметр "{param}" успешно сброшен в {hive_name}\\{chapter}')
                else:
                    logger.warning(f'UA - Неподдерживаемый тип для "{param}" в {hive_name}\\{chapter}')

            except FileNotFoundError:
                logger.debug(f'UA - Параметр "{param}" не найден, пропуск.')
            except Exception as e:
                logger.error(f'UA - Ошибка при сбросе "{param}": {e}')

    except FileNotFoundError:
        logger.warning(f"UA - Раздел не найден: {hive_name}\\{chapter}")
    except PermissionError:
        logger.critical(f"UA - Ошибка прав доступа к разделу: {hive_name}\\{chapter}")
    except Exception as e:
        logger.error(f"UA - Неизвестная ошибка в разделе {chapter}: {e}")
    finally:
        if key_handle:
            winreg.CloseKey(key_handle)



#Разблокировка всего
def UA(run_in_recovery):
    try:
        #system_hive = loaded_hive_names.get("SYSTEM", "Offline_SYSTEM")
        software_hive = loaded_hive_names.get("SOFTWARE", "Offline_SOFTWARE")
        user_hive = loaded_hive_names.get("USER", "Offline_USER")

        ua_globals = {
            "OFFLINE_HKEY_MAP": {
                winreg.HKEY_LOCAL_MACHINE: (winreg.HKEY_LOCAL_MACHINE, software_hive, r"Software"),
                winreg.HKEY_CURRENT_USER: (winreg.HKEY_LOCAL_MACHINE, user_hive, None)
            },
            "HKEY_MAP": {
                winreg.HKEY_LOCAL_MACHINE: "HKEY_LOCAL_MACHINE",
                winreg.HKEY_CURRENT_USER: "HKEY_CURRENT_USER"
            }
        }

        #Мышь
        #reset_reg_values(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", ["SwapMouseButtons"], ua_globals, run_in_recovery)

        #Ограничения проводника
        #explorer_policies = ["NoRun", "NoClose", "NoDriveTypeAutoRun", "NoLogopent", "NoControlPanel", "NoDesktop"]
        #reset_reg_values(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer", explorer_policies, ua_globals, run_in_recovery)

        #Системные политики (HKCU)
        #system_policies = ["DisableTaskMgr", "DisableRegistryTools", "DisableCMD"]
        #reset_reg_values(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", system_policies, ua_globals, run_in_recovery)

        #Системные политики (HKLM)
        #reset_reg_values(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", ["DisableTaskMgr", "ConsentPromptBehaviorAdmin"], ua_globals, run_in_recovery)

        #Список политик для сброса
        #Мышь
        reset_reg_values(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", ["SwapMouseButtons"], ua_globals, False, run_in_recovery)

        #Ограничения проводника
        reset_reg_values(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer", [], ua_globals, True, run_in_recovery)

        #Системные политики (HKCU)
        reset_reg_values(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", [], ua_globals, True, run_in_recovery)

        #Системные политики (HKLM)
        reset_reg_values(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", [], ua_globals, True, run_in_recovery)

        messagebox.showinfo(random_string(), "Разблокировка всего завершила свою работу, ошибок вроде не возникло, подробнее в лог файле.")
    except Exception as e:
        ua_error_text = f"В Компоненте UnlockAll произошла неизвестная ошибка:\n{e}"
        logger.critical(ua_error_text)
        messagebox.showerror(random_string(), ua_error_text)

    logger.info("UA - Работа компонента завершена.")
