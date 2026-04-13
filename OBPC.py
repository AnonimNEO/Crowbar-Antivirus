#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Данный Компонент сильно конфликтует (вызывает цикличные импорты, он отключен на неизвестное время)

#Распознание речи
import speech_recognition as sr
#Интерфейс
from tkinter import messagebox
#Логирование
from loguru import logger
#Паузы
import time

from RS import random_string
#from LP import LP
from SP import SP
from UA import UA
from E import ask_exit
#from ARM import ARM
#from MU import MU
#from CC import CC
#from FM import FM
#from PM import PM
from R import R

on_board_pc_version = "0.3.16 Beta"

#Список Команд
def execute_command(text, run_in_recovery):
    if "список всех команд" in text or "помощь" in text or "команды" in text:
        messagebox.showinfo(random_string(), "Доступные Команды:\n1)файловый менеджер - проводник - диспетчер файлов\n2)мастер автозагрузки - мастер автозапуска - автозапуск - автозапуска - управление автозапуском - управление автозагрузкой\n3)менеджер процессов - мастре процессов - процессы - процесы - менеджер процесов - мастер процесов - запусти менеджер процессов - запусти менеджер процесов - запусти мастер процессов - запусти мастер процесов\n4)очистка кэша - очистить кэш - кэш - удалить кэш - запусти удаление кэша - запустить удаление кэша - запусти очистку кэша - запусти удаление кэша\n5)перезапусти пк - перезапусти компьютер - перезапусти ноут - перезапусти ноутбук - перезагрузи пк - перезагрузи компьютер - перезагрузи комп - перезапусти комп - перезагрузи ноут - перезагрузи ноутбук - перезапуск - перезагрузка\n6)монтировка анлокер - анлокер - окно - окошко - открой монтировка анлокер - запусти монтировка анлокер - открой анлокер - запусти анлокер\n7)лоад протект - лоад протектион - лп - запусти лоад протект - запусти лоад протектион - запусти лп - открой лоад протект - открой лоад протектион - открой лп\n8)выйти - выход - завершить работу - остановить работу - закрыться")

    #elif "файловый менеджер" in text or "проводник" in text or "диспетчер файлов" in text:
    #    logger.info("OBPC - Запуск Компонента FileManager...")
    #FM(run_in_recovery)

    #elif "мастер автозагрузки" in text or "мастер автозапуска" in text or "автозапуск" in text or "автозапуска" in text or "управление автозапуском" in text or "управление автозагрузкой" in text:
    #    logger.info("OBPC - Запуск Компонента AutoRunMaster...")
    #    ARM(run_in_recovery)

    #elif "менеджер процессов" in text or "мастре процессов" in text or "процессы" in text or "процесы" in text or "менеджер процесов" in text or "мастер процесов" in text or "запусти менеджер процессов" in text or "запусти менеджер процесов" in text or "запусти мастер процессов" in text or "запусти мастер процесов" in text:
    #    logger.info("OBPC - Запуск Компонента ProcessManager...")
    #    PM(run_in_recovery)

    elif "разблокировка" in text or "разблокировка всего" in text or "разблокируй всё" in text or "разблокируй" in text or "разблочь" in text or "разблоч" in text:
        UA(run_in_recovery)

    #elif "очистка кэша" in text or "очистить кэш" in text or "кэш" in text or "удалить кэш" in text or "запусти удаление кэша" in text or "запустить удаление кэша" in text or "запусти очистку кэша" in text or "запусти удаление кэша" in text:
    #    logger.info("OBPC - Запуск очистки кэша...")
    #    CC(run_in_recovery)

    elif "перезапусти пк" in text or "перезапусти компьютер" in text or "перезапусти ноут" in text or "перезапусти ноутбук" in text or "перезагрузи пк" in text or "перезагрузи компьютер" in text or "перезагрузи комп" in text or "перезапусти комп" in text or "перезагрузи ноут" in text or "перезагрузи ноутбук" in text or "перезапуск" in text or "перезагрузка" in text:
        logger.info("OBPC - Перезапуск ПК...")
        R()

    #elif "монтировка анлокер" in text or "анлокер" in text or "окно" in text or "окошко" in text or "открой монтировка анлокер" in text or "запусти монтировка анлокер" in text or "открой анлокер" in text or "запусти анлокер" in text:
        #logger.info("OBPC - Запуск Компонента MountUnlocker...")
        #MU(run_in_recovery)

    #elif "лоад протект" in text or "лоад протектион" in text or "лп" in text or "запусти лоад протект" in text or "запусти лоад протектион" in text or "запусти лп" in text or "открой лоад протект" in text or "открой лоад протектион" in text or "открой лп" in text:
    #    logger.info("OBPC - Запуск Компонента LoadProtection...")
    #    LP(run_in_recovery)

    elif "пугало" in text or "запусти пугало" in text or "открой пугало" in text:
        logger.info("OBPC - Запуск Компонента ScarecrowProtection...")
        SP(run_in_recovery)

    elif "выйти" in text or "выход" in text or "завершить работу" in text or "остановить работу" in text or "закрыться" in text:
        logger.info("OBPC - Выход из программы...")
        ask_exit()



def OBPC(run_in_recovery):
    recognizer = sr.Recognizer()
    #engine = pyttsx3.init()

    #Список ключевых слов для активации
    activation_words = ["бортовой компьютер", "бортовой пк", "бортовой комп", "монтировка", "антивирус", "пк", "комп", "компьютер"]

    while True:
        try:
            with sr.Microphone() as source:
                #Адаптация под шум (помогает избежать ошибок распознавания)
                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                print("OBPC - Ожидаю одну из фраз активации...")
                audio = recognizer.listen(source)

                phrase = recognizer.recognize_google(audio, language="ru-RU").lower()
                logger.info(f"Вы сказали: {phrase}")

                #Правильная проверка наличия любого слова из списка
                if any(word in phrase for word in activation_words):
                    print("OBPC - Слушаю команду...")

                    #Слушаем саму команду сразу после активации
                    audio_cmd = recognizer.listen(source)
                    text = recognizer.recognize_google(audio_cmd, language="ru-RU").lower()

                    logger.info(f"OBPC - Распознана команда: {text}")
                    execute_command(text, run_in_recovery)

        except sr.UnknownValueError:
            pass #Ничего не сказано
        except sr.RequestError as e:
            logger.error(f"OBPC - Ошибка сервиса распознавания:\n{e}")
            time.sleep(5)
        except Exception as e:
            logger.critical(f"В Компоненте OnBoardPC произошла неизвестная ошибка:\n{e}")
            time.sleep(1)
