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
from tkinter import ttk, messagebox, Menu
import tkinter as tk
#Логирование Ошибок
from loguru import logger
#Работа с реестром
import winreg
#Работа с файлами
import shutil
import os

from RS import random_string
from OF import apply_global_theme
from config import theme, default_theme

scarecrow_protection_version = "0.3.7 Beta"

def SP(run_in_recovery, current_disc_r, current_theme):
    try:
        if run_in_recovery:
            current_disc = current_disc_r
        else:
            current_disc = "C:\\"

        #Иерархия значений:
        #-название программы
        #--path: список каталогов для создания
        #--files: список файлов для создания
        #--registry_keys: список ключей реестра и их значений (словарь: ключ - путь, значение - данные)
        PROGRAM_INFO = {
            "VMware": {
                "path": [
                    rf"{current_disc}\\Program Files\VMware\VMware Tools",
                    rf"{current_disc}\\Program Files\VMware\VMware Workstation",
                    rf"{current_disc}\\ProgramData\VMware",
                ],
                "files": [
                    rf"{current_disc}\\Program Files\VMware\VMware Tools\vmtoolsd.exe",
                    rf"{current_disc}\\Program Files\VMware\VMware Workstation\vmware.exe",
                ],
                "registry_keys": {
                    r"SOFTWARE\VMware, Inc.\VMware Tools": {"InstallPath": r"C:\Program Files\VMware\VMware Tools"},
                    r"SOFTWARE\VMware, Inc.\VMware Workstation": {"InstallPath": r"C:\Program Files\VMware\VMware Workstation"},
                    r"SYSTEM\CurrentControlSet\Services\VMTools": {"ImagePath": r"C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"},
                },
            },
            "VirtualBox": {
                "path": [
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\Tools",
                ],
                "files": [
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDrvInst.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxGuestInstallHelper.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxVideo.inf",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxVideo.cat",
                    rf"{current_disc}\\Users\Adminus\AppData\Local\Temp\nso9A09.tmp\nsExec.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert\VBoxCertUtil.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert\vbox-sha1-root.cer",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert\vbox-sha1-timestamp-root.cer",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert\vbox-sha256-root.cer",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\cert\vbox-sha256-timestamp-root.cer",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxVideo.sys",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDisp.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxMouse.sys",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxMouse.inf",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\vboxmouse.cat",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxGuest.sys",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxGuest.inf",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\vboxguest.cat",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxTray.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxControl.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\Tools\VBoxAudioTest.exe",
                    rf"{current_disc}\\Windows\System32\VBoxService.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\vboxwddm.cat",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxWddm.sys",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxWddm.inf",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDispD3D.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDX.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxNine.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxSVGA.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxGL.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDispD3D-x86.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxDX-x86.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxNine-x86.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxSVGA-x86.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\VBoxGL-x86.dll",
                    rf"{current_disc}\\Windows\System32\drivers\VBoxSF.sys",
                    rf"{current_disc}\\Windows\System32\VBoxMRXNP.dll",
                    rf"{current_disc}\\Windows\SysWOW64\VBoxMRXNP.dll",
                    rf"{current_disc}\\Windows\System32\VBoxHook.dll",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\install_drivers.log",
                    rf"{current_disc}\\Windows\System32\drivers\SETBEF5.tmp",
                    rf"{current_disc}\\Windows\System32\drivers\SETBEF5.tmp",
                    rf"{current_disc}\\Windows\System32\drivers\VBoxGuest.sys",
                    rf"{current_disc}\\Windows\Temp\OLDBF06.tmp",
                    rf"{current_disc}\\Windows\System32\SETBF06.tmp",
                    rf"{current_disc}\\Windows\System32\SETBF06.tmp",
                    rf"{current_disc}\\Windows\System32\VBoxTray.exe",
                    rf"{current_disc}\\Windows\Temp\OLDBF16.tmp",
                    rf"{current_disc}\\Windows\System32\SETBF16.tmp",
                    rf"{current_disc}\\Windows\System32\SETBF16.tmp",
                    rf"{current_disc}\\Windows\System32\VBoxControl.exe",
                    rf"{current_disc}\\Windows\System32\drivers\SETE104.tmp",
                    rf"{current_disc}\\Windows\System32\drivers\SETE104.tmp",
                    rf"{current_disc}\\Windows\System32\drivers\VBoxMouse.sys",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\Oracle VirtualBox Guest Additions.url",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\uninst.exe",
                    rf"{current_disc}\\Program Files\Oracle\VirtualBox Guest Additions\install_ui.log",
                ],
                "registry_keys": {
                    r"SYSTEM\CurrentControlSet\Services\VBoxSVC": {"ImagePath": r"C:\Program Files\Oracle\VirtualBox\VBoxSVC.exe"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\Setup": {"SetupapiLogStatus": r"setupapi.dev.log"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services": {"VBoxService": r"Description"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\VBoxSF": {"NetworkProvider": r"DeviceName"},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Oracle": {"VirtualBox Guest Additions": r"C:\Program Files\Oracle\VirtualBox Guest Additions"},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"InstallDir": r"C:\Program Files\Oracle\VirtualBox Guest Additions"},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"DisplayName": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"UninstallString": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"DisplayVersion": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"URLInfoAbout": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions": {"Publisher": r""},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Tcpip\Parameters": {"TcpWindowSize": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node": {"Oracle": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Oracle": {"Sun Ray": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Oracle\Sun Ray": {"ClientInfoAgent": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Oracle\Sun Ray\ClientInfoAgent": {"ReconnectActions": r""},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Oracle\Sun Ray\ClientInfoAgent": {"DisconnectActions": r""},
                },
            },
            "UninstallTool": {
                "path": [
                    rf"{current_disc}\\Program Files\Uninstall Tool",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages",
                ],
                "files": [
                    rf"{current_disc}\\Program Files\Uninstall Tool\fix-dll.rar",
                    rf"C{current_disc}\\Program Files\Uninstall Tool\PinToTaskbar.exe",
                    rf"{current_disc}\\Program Files\Uninstall Tool\PinToTaskbarHelper.dll",
                    rf"{current_disc}\\Program Files\Uninstall Tool\unins000.dat",
                    rf"{current_disc}\\Program Files\Uninstall Tool\unins000.exe",
                    rf"{current_disc}\\Program Files\Uninstall Tool\unins000.msg",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UninstallTool.cpl",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UninstallTool.exe",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UninstallTool.url",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UninstallToolHelper.exe",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UTShellExt.dll",
                    rf"{current_disc}\\Program Files\Uninstall Tool\UTShellExt_x86.dll",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Arabic.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Belarusian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Bulgarian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Chinese_Simplified.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Chinese_Traditional.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Croatian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Czech.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Danish.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Dutch.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\English.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Estonian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\French.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Georgian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\German.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Greek.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Hebrew.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Hindi.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Hungarian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Indonesian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Italian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Japanese.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Korean.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Latvian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Lithuanian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Norwegian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Persian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Polish.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Portuguese.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Portuguese_Brazilian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Romanian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Russian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Serbian_Cyrillic.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Serbian_Latin.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Slovak.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Slovenian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Spanish.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Swedish.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Turkish.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Ukrainian.xml",
                    rf"{current_disc}\\Program Files\Uninstall Tool\languages\Vietnamese.xml",
                ],
                "registry_keys": {
                    r"HKEY_LOCAL_MACHINE\SOFTWARE": {"UninstallTool": r"C:\Program Files\Uninstall Tool\UninstallTool.exe"},
                },
            },
            "ProcessHaker2": {
                "path": [
                    rf"{current_disc}\\Program Files\Process Hacker 2",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins",
                ],
                "files": [
                    rf"{current_disc}\\Program Files\Process Hacker 2\CHANGELOG.txt",
                    rf"{current_disc}\\Program Files\Process Hacker 2\COPYRIGHT.txt",
                    rf"{current_disc}\\Program Files\Process Hacker 2\kprocesshacker.sys",
                    rf"{current_disc}\\Program Files\Process Hacker 2\LICENSE.txt",
                    rf"{current_disc}\\Program Files\Process Hacker 2\peview.exe",
                    rf"{current_disc}\\Program Files\Process Hacker 2\ProcessHacker.exe",
                    rf"{current_disc}\\Program Files\Process Hacker 2\ProcessHacker.sig",
                    rf"{current_disc}\\Program Files\Process Hacker 2\README.txt",
                    rf"{current_disc}\\Program Files\Process Hacker 2\unins000.dat",
                    rf"{current_disc}\\Program Files\Process Hacker 2\unins000.exe",
                    rf"{current_disc}\\Program Files\Process Hacker 2\uninstall.ico",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\DotNetTools.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\ExtendedNotifications.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\ExtendedServices.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\ExtendedTools.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\HardwareDevices.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\NetworkTools.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\OnlineChecks.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\SbieSupport.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\ToolStatus.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\Updater.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\UserNotes.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\plugins\WindowExplorer.dll",
                    rf"{current_disc}\\Program Files\Process Hacker 2\x86\ProcessHacker.exe",
                    rf"{current_disc}\\Program Files\Process Hacker 2\x86\plugins\DotNetTools.dll",
                ],
                "registry_keys": {
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Process Hacker2": {"version": r"2"},
                },
            },
        }


        class SPI:
            def __init__(self, master):
                self.master = master
                master.title(random_string())
                master.geometry("300x215")
                master.resizable(True, True)

                #Фрейм для кнопок
                self.button_frame = ttk.Frame(master)
                self.button_frame.pack(side=tk.BOTTOM, pady=10)

                #Кнопки
                self.run_button = tk.Button(self.button_frame, text="Симуляция", command=self.run_simulation)
                self.run_button.pack(side=tk.LEFT, padx=10)

                self.delete_button = tk.Button(self.button_frame, text="Удаление", command=self.delete_simulation)
                self.delete_button.pack(side=tk.LEFT, padx=10)

                #Фрейм для чекбоксов со скроллбаром
                self.checkbox_frame = ttk.Frame(master)
                self.checkbox_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10)

                self.canvas = tk.Canvas(self.checkbox_frame, bd=0, highlightthickness=0)
                self.scrollbar = ttk.Scrollbar(self.checkbox_frame, orient="vertical", command=self.canvas.yview)
                self.scrollable_frame = ttk.Frame(self.canvas)

                self.scrollable_frame.bind(
                    "<Configure>",
                    lambda e: self.canvas.configure(
                        scrollregion=self.canvas.bbox("all")
                    )
                )

                self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
                self.canvas.configure(yscrollcommand=self.scrollbar.set)

                self.canvas.pack(side="left", fill="both", expand=True)
                self.scrollbar.pack(side="right", fill="y")

                self.checkbox_vars = {}
                self.checkboxes = {}

                #Создаем чекбоксы в два столбца
                self.create_checkboxes()



            def create_checkboxes(self):
                programs = list(PROGRAM_INFO.keys())
                num_programs = len(programs)
                half_programs = (num_programs + 1) // 2 #Рассчитываем середину, округляя вверх

                for i in range(num_programs):
                    program = programs[i]
                    var = tk.BooleanVar(value=False)
                    checkbox = ttk.Checkbutton(self.scrollable_frame, text=program, variable=var)

                    #Размещение чекбоксов в два стола
                    if i < half_programs:
                        checkbox.grid(row=i, column=0, sticky="w", padx=1, pady=2)
                    else:
                        checkbox.grid(row=i - half_programs, column=1, sticky="w", padx=10, pady=2)

                    self.checkbox_vars[program] = var
                    self.checkboxes[program] = checkbox



            def create_path(self, path):
                try:
                    os.makedirs(path, exist_ok=True)
                    logger.info(f"SP - Создан каталог: {path}")
                except OSError as e:
                    logger.error(f"SP - Ошибка при создании директории {path}:\n{e}")



            def create_file(self, path):
                try:
                    with open(path, "w"):
                        pass #Создаём пустой файл
                    logger.info(f"SP - Создан файл: {path}")
                except OSError as e:
                    logger.error(f"SP - Ошибка при создании файла {path}:\n{e}")



            def create_registry_key(self, key_path, value_name, value_data): #value_type=winreg.REG_SZ):
               try:
                    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
                    logger.info(f"SP - Создан ключ реестра: {key_path}\\{value_name} = {value_data}")
               except OSError as e:
                    logger.error(f"SP - Ошибка при создании ключа реестра {key_path}\\{value_name} = {value_data}:\n{e}")



            def delete_path(self, path):
                try:
                    if os.path.exists(path):
                        shutil.rmtree(path)
                        logger.info(f"SP - Удалена директория: {path}")
                except OSError as e:
                    logger.error(f"SP - Ошибка при удалении директории {path}:\n{e}")



            def delete_file(self, path):
                try:
                    if os.path.exists(path):
                        os.remove(path)
                        logger.info(f"SP - Удален файл: {path}")
                except OSError as e:
                    logger.error(f"SP - Ошибка при удалении файла {path}:\n{e}")



            def delete_registry_key(self, key_path, value_name):
                try:
                    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                        winreg.DeleteValue(key, value_name)
                    logger.info(f"SP - Удален ключ реестра: {key_path}\\{value_name}")
                except FileNotFoundError:
                    logger.info(f"SP - Ключ реестра не найден: {key_path}\\{value_name}")
                except OSError as e:
                    logger.error(f"SP - Ошибка при удалении ключа реестра {key_path}\\{value_name}:\n{e}")



            def run_simulation(self):
                for program, info in PROGRAM_INFO.items():
                    if self.checkbox_vars[program].get():
                        logger.info(f"SP - Запуск симуляции для {program}")
                        if "path" in info:
                            for path in info["path"]:
                                self.create_path(path)
                        if "files" in info:
                            for file_path in info["files"]:
                                self.create_file(file_path)
                        if "registry_keys" in info:
                            for key_path, key_values in info["registry_keys"].items():
                                for value_name, value_data in key_values.items():
                                    self.create_registry_key(key_path, value_name, value_data)
                        logger.info(f"SP - Симуляция для {program} завершена")
                messagebox.showinfo(random_string(), "Симуляция завершена.")



            def delete_simulation(self):
                if messagebox.askyesno(random_string(), "Вы уверены, что хотите удалить все фантомные элементы?\nЭто может повлиять на работу установленных программ, если они установлены."):
                    for program, info in PROGRAM_INFO.items():
                        if self.checkbox_vars[program].get():
                            logger.info(f"SP - Удаление симуляции для {program}")
                            if "path" in info:
                                for path in info["path"]:
                                    self.delete_path(path)
                            if "files" in info:
                                for file_path in info["files"]:
                                    self.delete_file(file_path)
                            if "registry_keys" in info:
                                for key_path, key_values in info["registry_keys"].items():
                                    for value_name, _ in key_values.items():
                                        self.delete_registry_key(key_path, value_name)
                            logger.info(f"SP - Удаление симуляции для {program} завершено")
                    messagebox.showinfo(random_string(), "Удаление завершено.")

        def restart_sp(user_theme):
            global current_theme
            current_theme = theme[user_theme]
            #SP_GUI.destroy()
            #SP(run_in_recovery, current_disc_r, current_theme)
            apply_global_theme(SP_GUI, current_theme)

        SP_GUI = tk.Tk()
        apply_global_theme(SP_GUI, current_theme)
        #GUI_SP = SP(SP_GUI)
        SPI(SP_GUI)

        #Меню
        menubar = Menu(SP_GUI)
        theme_menu = Menu(menubar, tearoff=0)
        theme_menu.add_checkbutton(label="Тёмная", command=lambda: restart_sp("dark"))
        theme_menu.add_checkbutton(label="Светлая", command=lambda: restart_sp("white"))
        theme_menu.add_checkbutton(label="Красная", command=lambda: restart_sp("red"))
        theme_menu.add_checkbutton(label="Контрастная", command=lambda: restart_sp("black"))
        theme_menu.add_checkbutton(label="Серая", command=lambda: restart_sp("gray"))
        theme_menu.add_checkbutton(label="Оранжевая", command=lambda: restart_sp("orange"))

        #Пункт "Темы"
        menubar.add_cascade(label="Темы", menu=theme_menu)

        SP_GUI.attributes("-topmost", True)

        if run_in_recovery:
            higher = tk.BooleanVar(value=False)
        else:
            higher = tk.BooleanVar(value=True)

        def toggle_topmost(GUI):
            new_state = not higher.get()
            higher.set(new_state)
            GUI.attributes("-topmost", new_state)

        def update_topmost_label(menubar, GUI):
            status = "вкл" if higher.get() else "выкл"
            #Индекс command в menubar
            menubar.entryconfig(5, label=f"Поверх всех окон: {status}")
            GUI.after(200, lambda: update_topmost_label(menubar, GUI))

        menubar.add_command(label="Поверх всех окон: вкл", command=lambda: toggle_topmost(SP_GUI))
        update_topmost_label(menubar, SP_GUI)

        SP_GUI.config(menu=menubar)

        SP_GUI.mainloop()
    except Exception as e:
        logger.critical(f"В Компоненте ScarecrowProtection произошла неизвестная ошибка!\n{e}")

if __name__ == "__main__":
    current_theme = theme[default_theme]
    SP(False, "C:\\", current_theme)
