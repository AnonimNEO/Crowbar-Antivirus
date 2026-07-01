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
#from PIL import Image, ImageTk
#Графический Интерфейс
from tkinter import messagebox
import tkinter as tk
#Логирование Ошибок
try:
    from OF import Logger
    logger = Logger()
except:
    from loguru import logger
#Обращение к веб-браузеру
import webbrowser
#Обращение к Системным Командам и Значениям
import os

#Импорт Компонентов
from config import *
from languages import l
from RS import RS

global about_program_version
about_program_version = "0.3.6 Beta"
image_references = {}
er = l("error")

def AP(autorun_master_version=er,
       crowbar_antivirus_scripts_handler_version=er,
       clear_cache_version=er,
       crowbar_menu_version=er,
       crowbar_console_version=er,
       exit_version=er,
       edit_criticality_version=er,
       file_editor_version=er,
       file_manager_version=er,
       file_replacer_version=er,
       get_full_access_version=er,
       on_board_pc_version=er,
       other_function_version=er,
       process_manager_version=er,
       restart_version=er,
       real_time_protect_version=er,
       registry_monitor=er,
       random_string_version=er,
       run_version=er,
       settings_and_update_version=er,
       software_installation_manager=er,
       scarecrow_protection_version=er,
       trey_version=er,
       unlock_all_version=er,
       users_manager_version=er):
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
                logger.exception(f"AP - {l("read_dir_error")} {images_path}")
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
                    logger.exception(f"AP - {l("read_image_error")} {image_file}")
                    continue #если одно изображение не загрузилось, продолжаем с другими

            return image_labels_container #Возвращаем список загруженных меток, чтобы знать, создался ли фрейм



        def show_component_versions(event):
            version_component_text = (
                f"{l("version_component")}:\n"
                f"{l("pac")}: {program_authentication_clyth}\n"
                f"---{l("general_component")}---\n"
                f"{l("program_kernel")}: {trey_version}\n"
                f"{l("RLP")}: {real_time_protect_version}\n"
                f"{l("ARM")}: {autorun_master_version}\n"
                f"{l("PM")}: {process_manager_version}\n"
                f"{l("FM")}: {file_manager_version}\n"
                f"{l("UA")}: {unlock_all_version}\n"
                f"{l("FE")}: {file_editor_version}\n"
                f"{l("RLP")}: {real_time_protect_version}\n"
                f"{l("SIM")}: {software_installation_manager}\n"
                f"{l("RM")}: {real_time_protect_version}\n"
                f"---{l("mini_component")}---\n"
                f"{l("CM")}: {crowbar_menu_version}\n"
                f"{l("UM")}: {users_manager_version}\n"
                f"{l("FR")}: {file_replacer_version}\n"
                f"{l("SP")}: {scarecrow_protection_version}\n"
                f"{l("CC")}: {clear_cache_version}\n"
                f"{l("R")}: {restart_version}\n"
                f"{l("Run")}: {run_version}\n"
                f"{l("OBPC")}: {on_board_pc_version}\n"
                f"---{l("system_component")}---\n"
                f"{l("encryption")}: AES\n"
                f"{l("CASH")}: {crowbar_antivirus_scripts_handler_version}\n"
                f"{l("EC")}: {edit_criticality_version}\n"
                f"{l("GFA")}: {get_full_access_version}\n"
                f"{l("OF")}: {other_function_version}\n"
                f"{l("Console")}: {crowbar_console_version}\n"
                f"{l("RS")}: {random_string_version}\n"
                f"{l("AP")}: {about_program_version}\n"
                f"{l("SAU")}: {settings_and_update_version}"
                f"{l("E")}: {exit_version}\n"
            )
            messagebox.showinfo(RS(), version_component_text)



        def open_gpl_licenses(event):
            webbrowser.open("https://www.gnu.org/licenses/gpl-3.0.html")



        def open_website(event):
            webbrowser.open("https://anonimneo.github.io/NEO-Organization//")



        def donate_window(event):
            def open_donationalerts(event):
                webbrowser.open_new("https://www.donationalerts.com/r/anonimneo")

            def open_trade_on_steam(event):
                webbrowser.open_new("https://steamcommunity.com/tradeoffer/new/?partner=1842324943&token=xPAad4EP")

            donate_window = tk.Tk()
            donate_window.title(RS())
            donate_window.configure(bg="black")
            donate_window.resizable(False, False)

            #Создаем фрейм для центрирования элементов
            frame = tk.Frame(donate_window, bg="black")
            frame.pack(expand=True, padx=20, pady=20)

            label = tk.Label(frame, text=l("support_text"), fg="white", bg="black", font=("Arial", 12))
            label.pack(pady=(0, 10))

            link1 = tk.Label(frame, text="DonationAlerts", fg="red", bg="black", cursor="hand2", font=("Arial", 12, "underline"))
            link1.pack()
            link1.bind("<Button-1>", open_donationalerts)

            label2 = tk.Label(frame, text=l("steam_trade_text"), fg="white", bg="black", font=("Arial", 12))
            label2.pack(pady=(10, 0))

            link2 = tk.Label(frame, text="Steam", fg="red", bg="black", cursor="hand2", font=("Arial", 12, "underline"))
            link2.pack()
            link2.bind("<Button-1>", open_trade_on_steam)

            donate_window.mainloop()

        about_window = tk.Tk()
        about_window.title(RS())
        about_window.configure(bg="black")

        #Текст
        label = tk.Label(about_window, text=l("about_program_text"), bg="black", fg="white", font=("ComicSans", 16))
        label.pack(pady=20)

        image_labels = load_images(about_window)

        version_link = tk.Label(about_window, text=l("version_component"), bg="black", fg="green", cursor="hand2", font=("ComicSans", 16))
        version_link.pack(pady=10)
        version_link.bind("<Button-1>", show_component_versions)

        donationalerts_link = tk.Label(about_window, text=l("donation_alerts_text"), bg="black", fg="red", cursor="hand2", font=("ComicSans", 16))
        donationalerts_link.pack(pady=10)
        donationalerts_link.bind("<Button-1>", donate_window)

        gpl_link = tk.Label(about_window, text=f"{l("license")} GPL v3.0", bg="red", fg="white", cursor="hand2", font=("ComicSans", 16))
        gpl_link.pack(pady=10)
        gpl_link.bind("<Button-1>", open_gpl_licenses)

        website_link = tk.Label(about_window, text=l("website_neo_organization"), bg="blue", fg="yellow", cursor="hand2", font=("ComicSans", 16))
        website_link.pack(pady=10)
        website_link.bind("<Button-1>", open_website)

        about_window.mainloop()
    except Exception as e:
        logger.exception(l("ap_exception_text"))

if __name__ == "__main__":
    AP()
