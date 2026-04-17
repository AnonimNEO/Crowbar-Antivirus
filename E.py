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

exit_version = "1.0.16 Beta"

dyrachok_path = r"C:\ProgramData\dyrachok.txt"

try:
    @logger.catch
    def check_access_file():
        try:
            with open(dyrachok_path, "r") as f:
                content = f.read()
            if "debil" in content:
                logger.critical("E - Проверка на дурочка не прошла.")
                messagebox.showwarning(random_string(), "Вы смотрите тикток!\nПрограмма не будет закрыта.")
                return False
            else:
                logger.succes("E - Проверка на дурочка прошла успешно.")
                return True
        except FileNotFoundError:
            return True



    @logger.catch
    def tiktok_question():
        if messagebox.askyesno(random_string(), "Смотрите ли вы тикток?"):
            try:
                with open(dyrachok_path, "w") as f:
                    f.write("debil")
                messagebox.showinfo(random_string(), "Вы смотрите тикток!\nПрограмма не будет закрыта.")
            except Exception as e:
                comment = f"E - Ошибка при выходе\n{e}"
                logger.critical(comment)
                messagebox.showerror(random_string(), comment)
                return False
        else:
            logger.info("Завершение работы программы...")
            os._exit(0)



    def bad_capcha():
        messagebox.showerror(random_string(), "Неправильный ввод капчи.\nПрограмма не будет закрыта.")



    def math_window():
        n = random.randint(256, 1024)
        number_input = tk.simpledialog.askinteger(random_string(), f"Введите результат данного примера: √({n} * {n})")

        if number_input == n:
            logger.info("E - ввод примера верен.")
            tiktok_question()
        else:
            logger.critical("E - ввод примера не верен.")
            bad_capcha()



    def captcha_window():
        n = random.randint(256, 1024)
        captcha_input = tk.simpledialog.askinteger(random_string(), f"Введите число: {n}")

        if captcha_input == n:
            logger.info("E - ввод числа верен.")
            math_window()
        else:
            logger.critical("E - Неправильный ввод числа")
            bad_capcha()



    def ask_exit():
        if check_access_file():
            if messagebox.askyesno(random_string(), "Вы действительно хотите выйти из данного программного обеспечения?"):
                logger.info("E - Попытка выхода из программы.")
                captcha_window()
            else:
                logger.info("E - Отмена выхода.")
                messagebox.showerror(random_string(), "Данное программное обеспечение не будет закрыто.")

except Exception as e:
    logger.critical(f"В Компоненте Exit произошла неизвестная ошибка!\n{e}")
