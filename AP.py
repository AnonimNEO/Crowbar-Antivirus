#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2024 - 2026
#Coded by @AnonimNEO (Telegram)

#Вставка картинок
from PIL import Image, ImageTk
#Графический Интерфейс
from tkinter import messagebox
import tkinter as tk
#Логирование Ошибок
from loguru import logger
#Обращение к веб-браузеру
import webbrowser
#Обращение к Системным Командам и Значениям
import os

#Импорт Компонентов
from config import *
from RS import random_string

global about_program_version
about_program_version = "0.2.21 Beta"

image_references = {}

def AP(autorun_master_version, clear_cache_version, exit_version, edit_criticality_version, file_manager_version, real_time_protect_version, unlocker_version, other_components_version, process_manager_version, restart_version, random_string_version, run_version, scarecrow_protection_version, settings_and_update_version, trey_version, unlock_all_version, users_manager_version):
    try:
        #Загрузка изображений
        def load_images(master):
            image_labels_container = [] #Список для хранения ссылок на метки изображений
            image_files = [] #Список найденных файлов изображений

            #Проверяем существование каталога
            if not os.path.isdir(images_path):
                return image_labels_container

            #Получаем список файлов в каталоге
            try:
                image_files = [f for f in os.listdir(images_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
            except Exception as e:
                logger.error(f"AP - Ошибка при чтении каталога {images_path}:\n{e}")
                return image_labels_container

            #Проверяем наличие файлов
            if not image_files:
                return image_labels_container

            #Если каталог существует и файлы найдены, создаем фрейм для них
            image_frame = tk.Frame(master, bg="black")
            image_frame.pack(pady=20)

            #Загружаем изображения и создаем метки
            for image_file in image_files:
                img_path = os.path.join(images_path, image_file)
                try:
                    img = Image.open(img_path)
                    #Изменение размера изображения
                    img.thumbnail((100, 100))
                    img_tk = ImageTk.PhotoImage(img)

                    #Используем image_frame для создания Label
                    label = tk.Label(image_frame, image=img_tk, bg="black")
                    #Сохраняем ссылку на ImageTk.PhotoImage, чтобы избежать сборки мусора
                    image_references[img_path] = img_tk

                    label.pack(side=tk.LEFT, padx=5)
                    image_labels_container.append(label)

                except Exception as e:
                    logger.error(f"Не удалось загрузить изображение {image_file}:\n{e}")
                    continue #если одно изображение не загрузилось, продолжаем с другими

            return image_labels_container #Возвращаем список загруженных меток, чтобы знать, создался ли фрейм



        def show_component_versions(event):
            about_program_text = (
                f"Версии Компонентов:\n"
                f"---Главные Компоненты---\n"
                f"Ядро программы (трей): {trey_version}\n"
                f"Защита Нагрузки: {real_time_protect_version}\n"
                f"Мастер Автозагрузки: {autorun_master_version}\n"
                f"Менеджер Процессов: {process_manager_version}\n"
                f"Файловый Менеджер: {file_manager_version}\n"
                f"Раблокировка всего: {unlock_all_version}\n"
                f"---Мини Компоненты---\n"
                f"Главное меню: {unlocker_version}\n"
                f"Пугало: {scarecrow_protection_version}\n"
                f"Очистка Кэша: {clear_cache_version}\n"
                f"Менеджер Пользователей: {users_manager_version}\n"
                #f"Менеджер Пользователей: данный компонент отсутствует из-за его неработоспособности\n"
                f"Перезапуск ПК: {restart_version}\n"
                f"Запуск от имени администратора: {run_version}\n"
                #f"Голосовое Управление: {on_board_pc_version}\n"
                f"Голосовое Управление: данный компонент отсутствует из-за его нестабильности\n"
                f"---Системные Компоненты---\n"
                f'Шифрование "Шифр Цезаря": 2.2\n'
                f"Смена Критичности: {edit_criticality_version}\n"
                f"Прочие Компоненты: {other_components_version}\n"
                f"Генератор Заголовков: {random_string_version}\n"
                f"Выход из программы: {exit_version}\n"
                f"О Программе: {about_program_version}\n"
                f"Настройки: {settings_and_update_version}"
            )
            messagebox.showinfo(random_string(), about_program_text)



        def open_gpl_licenses(event):
            webbrowser.open("https://www.gnu.org/licenses/gpl-3.0.html")



        def open_website(event):
            webbrowser.open("https://sites.google.com/view/neo-organization")



        def donate_window(event):
            def open_donationalerts(event):
                webbrowser.open_new("https://www.donationalerts.com/r/anonimneo")

            def open_trade_on_steam(event):
                webbrowser.open_new("https://steamcommunity.com/tradeoffer/new/?partner=1842324943&token=xPAad4EP")

            donate_window = tk.Tk()
            donate_window.title(random_string())
            donate_window.configure(bg="black")
            donate_window.resizable(False, False)

            #Создаем фрейм для центрирования элементов
            frame = tk.Frame(donate_window, bg="black")
            frame.pack(expand=True, padx=20, pady=20)

            label = tk.Label(frame, text="Поддержать нас можно, оплатив 2 банки сгущёнки, перейдя по ссылке:", fg="white", bg="black", font=("Arial", 12))
            label.pack(pady=(0, 10))

            link1 = tk.Label(frame, text="DonationAlerts", fg="red", bg="black", cursor="hand2", font=("Arial", 12, "underline"))
            link1.pack()
            link1.bind("<Button-1>", open_donationalerts)

            label2 = tk.Label(frame, text="или поддержать через Обмен в Steam", fg="white", bg="black", font=("Arial", 12))
            label2.pack(pady=(10, 0))

            link2 = tk.Label(frame, text="Steam", fg="red", bg="black", cursor="hand2", font=("Arial", 12, "underline"))
            link2.pack()
            link2.bind("<Button-1>", open_trade_on_steam)

            donate_window.mainloop()

        about_window = tk.Tk()
        about_window.title(random_string())
        about_window.configure(bg="black")

        #Текст
        label_text = f"Антивирус Монтировка!\nВытащит любой гвоздь из крышки гроба вашего ПК!\n(как минимум попытается, а если не смог - поставь Linux)\nCreated by NEO Organization\nPowered by Departament K\nCoded by @AnonimNEO, Всего строчек кода : {all_line}\nПрограмисты/Задумщики/Художники/Тестировщики : @AnonimNEO\nЛицензия: GPL v3.0 Copyleft 🄯 2024 - 2026\n"
        label = tk.Label(about_window, text=label_text, bg="black", fg="white", font=("ComicSans", 16))
        label.pack(pady=20)

        image_labels = load_images(about_window)

        versionlink = tk.Label(about_window, text="Версии Компонентов", bg="black", fg="green", cursor="hand2", font=("ComicSans", 16))
        versionlink.pack(pady=10)
        versionlink.bind("<Button-1>", show_component_versions)

        donationalerts_link = tk.Label(about_window, text="Поддержать нас через DonationAlerts или Steam", bg="black", fg="red", cursor="hand2", font=("ComicSans", 16))
        donationalerts_link.pack(pady=10)
        donationalerts_link.bind("<Button-1>", donate_window)

        gpl_link = tk.Label(about_window, text="Лицензия GPL v3.0", bg="red", fg="white", cursor="hand2", font=("ComicSans", 16))
        gpl_link.pack(pady=10)
        gpl_link.bind("<Button-1>", open_gpl_licenses)

        website_link = tk.Label(about_window, text="Веб-Сайт NEO Organization", bg="blue", fg="yellow", cursor="hand2", font=("ComicSans", 16))
        website_link.pack(pady=10)
        website_link.bind("<Button-1>", open_website)

        about_window.mainloop()
    except Exception as e:
        logger.critical(f"В Компоненте AboutProgram произошла неизвестная ошибка!\n{e}")