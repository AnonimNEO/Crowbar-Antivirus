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
from tkinter import messagebox, simpledialog
import tkinter as tk
#Логирование Ошибок
from loguru import logger
#Капча
import random
import os

from RS import random_string
from config import program_authentication_clyth
from languages import localizations, current_localization

exit_version = "1.1.0 Beta"
l = localizations[current_localization]
dyrachok_path = r"C:\ProgramData\dyrachok.txt"

@logger.catch
def check_access_file():
    try:
        with open(dyrachok_path, "r") as f:
            content = f.read()
        if "debil" in content:
            logger.critical(f"E - {l["dyrachok_test_log_text"]}.")
            messagebox.showwarning(random_string(), l["dyrachok_test_text"])
            return False
        else:
            #logger.success("E - Проверка на дурочка прошла успешно.")
            return True
    except FileNotFoundError:
        return True



@logger.catch
def tiktok_question():
    if messagebox.askyesno(random_string(), l["watch_tiktok?"]):
        try:
            with open(dyrachok_path, "w") as f:
                f.write("debil")
            messagebox.showinfo(random_string(), l["dyrachok_test_text"])
        except Exception as e:
            comment = f"E - {l["exit_error"]}"
            logger.exception(comment, e)
            messagebox.showerror(random_string(), f"{comment}\n{e}")
            return False
    else:
        logger.info(l["exit_program"])
        os._exit(0)



def bad_capcha():
    messagebox.showerror(random_string(), l["bad_capcha"])



def math_window():
    n = random.randint(256, 1024)
    number_input = tk.simpledialog.askinteger(random_string(), f"{l["enter_result_example"]}: √({n} * {n})")

    if number_input == n:
        #logger.info("E - ввод примера верен.")
        tiktok_question()
    else:
        logger.critical(f"E - {l["bad_result_example"]}.")
        bad_capcha()



def captcha_window():
    n = random.randint(256, 1024)
    captcha_input = tk.simpledialog.askinteger(random_string(), f"{l["enter_number"]}: {n}")

    if captcha_input == n:
        #logger.info("E - ввод числа верен.")
        math_window()
    else:
        logger.critical(f"E - {l["bad_enter_number"]}")
        bad_capcha()



def E():
    try:
        if check_access_file():
            if messagebox.askyesno(random_string(), f"{l["pac"]} - {program_authentication_clyth}\n\n{l["want_exit?"]}"):
                logger.info(f"E - {l["attempting_to_exit"]}.")
                captcha_window()
            else:
                logger.info(f"E - {l["cancel_exit"]}.")
    except Exception as e:
        logger.exception(f"{e_critical_error}\n{e}")
