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
#Логирование Ошибок
from loguru import logger
import datetime
#Работа с ОС и файлами
import getpass
import shutil
import os

from OF import get_current_disc
from RS import random_string
from config import *

global log_path, clear_temp_log
clear_cache_version = "0.6.10 Beta"

@logger.catch
def CC(run_in_recovery):
    try:
        logger.info("CC - Запуск Очистки...")
        #Получаем имя пользователя
        username = getpass.getuser()
        if run_in_recovery:
            current_disc = get_current_disc()
        else:
            current_disc = "C:\\"
        temp_path = f"{current_disc}\\Users\\{username}\\AppData\\Local\\Temp\\"

        #Переменные для логирования
        files_not_deleted = []
        files_deleted = []

        #Проходим по содержимому папки Temp
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    files_deleted.append(item)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    files_deleted.append(item)
            except Exception as e:
                files_not_deleted.append(item)
                logger.error(f"CC - Ошибка при удалении файла из %Temp% - {item}\n{e}")

        #Получаем текущее время и дату для имени лог-файла
        current_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        log_filename = f"{log_path}\\{clear_temp_log}_{current_time}.txt"
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        with open(log_filename, "w") as log_file:
            log_file.write("Ошибка при удалении следующих файлов:\n")
            for file in files_not_deleted:
                log_file.write(f"{file}\n")
            log_file.write("\nУспешно удалённые файлы:\n")
            for file in files_deleted:
                log_file.write(f"{file}\n")

        cc_log_text = f"Лог файл был создан по пути - {log_path}\\{log_filename}"
        logger.info(cc_log_text)
        messagebox.showinfo(random_string(), cc_log_text)

    except Exception as e:
        logger.critical(f"В Компоненте ClearCache произошла неизвестная ошибка!\n{e}")