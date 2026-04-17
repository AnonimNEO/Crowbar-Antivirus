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

scarecrow_protection_version = "0.3.8 Beta"

def SP(run_in_recovery, current_disc_r, current_theme):
    try:
        if run_in_recovery:
            current_disc = current_disc_r
        else:
            current_disc = "C:\\"

        vbox_dir = r"Program Files\Oracle\VirtualBox Guest Additions"
        vbox_r = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Oracle VirtualBox Guest Additions"
        vbox_hl = r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node"
        un_tool_dir = r"Program Files\Uninstall Tool"
        ph2_dir = r"Program Files\Process Hacker 2"

        #Иерархия значений:
        #-название программы
        #--path: список каталогов для создания
        #--files: список файлов для создания
        #--registry_keys: список ключей реестра и их значений (словарь: ключ - путь, значение - данные)
        PROGRAM_INFO = {
            "VMware": {
                "path": [
                    rf"{current_disc}\Program Files\VMware\VMware Tools",
                    rf"{current_disc}\Program Files\VMware\VMware Workstation",
                    rf"{current_disc}\ProgramData\VMware",
                ],
                "files": [
                    rf"{current_disc}\Program Files\VMware\VMware Tools\vmtoolsd.exe",
                    rf"{current_disc}\Program Files\VMware\VMware Workstation\vmware.exe",
                ],
                "registry_keys": {
                    r"SOFTWARE\VMware, Inc.\VMware Tools": {"InstallPath": r"C:\Program Files\VMware\VMware Tools"},
                    r"SOFTWARE\VMware, Inc.\VMware Workstation": {"InstallPath": r"C:\Program Files\VMware\VMware Workstation"},
                    r"SYSTEM\CurrentControlSet\Services\VMTools": {"ImagePath": r"C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"},
                },
            },
            "VirtualBox": {
                "path": [
                    rf"{current_disc}\{vbox_dir}",
                    rf"{current_disc}\{vbox_dir}\cert",
                    rf"{current_disc}\{vbox_dir}\Tools",
                ],
                "files": [
                    rf"{current_disc}\{vbox_dir}\VBoxDrvInst.exe",
                    rf"{current_disc}\{vbox_dir}\VBoxGuestInstallHelper.exe",
                    rf"{current_disc}\{vbox_dir}\VBoxVideo.inf",
                    rf"{current_disc}\{vbox_dir}\VBoxVideo.cat",
                    rf"{current_disc}\Users\Adminus\AppData\Local\Temp\nso9A09.tmp\nsExec.dll",
                    rf"{current_disc}\{vbox_dir}\cert\VBoxCertUtil.exe",
                    rf"{current_disc}\{vbox_dir}\cert\vbox-sha1-root.cer",
                    rf"{current_disc}\{vbox_dir}\cert\vbox-sha1-timestamp-root.cer",
                    rf"{current_disc}\{vbox_dir}\cert\vbox-sha256-root.cer",
                    rf"{current_disc}\{vbox_dir}\cert\vbox-sha256-timestamp-root.cer",
                    rf"{current_disc}\{vbox_dir}\VBoxVideo.sys",
                    rf"{current_disc}\{vbox_dir}\VBoxDisp.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxMouse.sys",
                    rf"{current_disc}\{vbox_dir}\VBoxMouse.inf",
                    rf"{current_disc}\{vbox_dir}\vboxmouse.cat",
                    rf"{current_disc}\{vbox_dir}\VBoxGuest.sys",
                    rf"{current_disc}\{vbox_dir}\VBoxGuest.inf",
                    rf"{current_disc}\{vbox_dir}\vboxguest.cat",
                    rf"{current_disc}\{vbox_dir}\VBoxTray.exe",
                    rf"{current_disc}\{vbox_dir}\VBoxControl.exe",
                    rf"{current_disc}\{vbox_dir}\Tools\VBoxAudioTest.exe",
                    rf"{current_disc}\Windows\System32\VBoxService.exe",
                    rf"{current_disc}\{vbox_dir}\vboxwddm.cat",
                    rf"{current_disc}\{vbox_dir}\VBoxWddm.sys",
                    rf"{current_disc}\{vbox_dir}\VBoxWddm.inf",
                    rf"{current_disc}\{vbox_dir}\VBoxDispD3D.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxDX.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxNine.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxSVGA.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxGL.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxDispD3D-x86.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxDX-x86.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxNine-x86.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxSVGA-x86.dll",
                    rf"{current_disc}\{vbox_dir}\VBoxGL-x86.dll",
                    rf"{current_disc}\Windows\System32\drivers\VBoxSF.sys",
                    rf"{current_disc}\Windows\System32\VBoxMRXNP.dll",
                    rf"{current_disc}\Windows\SysWOW64\VBoxMRXNP.dll",
                    rf"{current_disc}\Windows\System32\VBoxHook.dll",
                    rf"{current_disc}\{vbox_dir}\install_drivers.log",
                    rf"{current_disc}\Windows\System32\drivers\SETBEF5.tmp",
                    rf"{current_disc}\Windows\System32\drivers\SETBEF5.tmp",
                    rf"{current_disc}\Windows\System32\drivers\VBoxGuest.sys",
                    rf"{current_disc}\Windows\Temp\OLDBF06.tmp",
                    rf"{current_disc}\Windows\System32\SETBF06.tmp",
                    rf"{current_disc}\Windows\System32\SETBF06.tmp",
                    rf"{current_disc}\Windows\System32\VBoxTray.exe",
                    rf"{current_disc}\Windows\Temp\OLDBF16.tmp",
                    rf"{current_disc}\Windows\System32\SETBF16.tmp",
                    rf"{current_disc}\Windows\System32\SETBF16.tmp",
                    rf"{current_disc}\Windows\System32\VBoxControl.exe",
                    rf"{current_disc}\Windows\System32\drivers\SETE104.tmp",
                    rf"{current_disc}\Windows\System32\drivers\SETE104.tmp",
                    rf"{current_disc}\Windows\System32\drivers\VBoxMouse.sys",
                    rf"{current_disc}\{vbox_dir}\Oracle VirtualBox Guest Additions.url",
                    rf"{current_disc}\{vbox_dir}\uninst.exe",
                    rf"{current_disc}\{vbox_dir}\install_ui.log",
                ],
                "registry_keys": {
                    r"SYSTEM\CurrentControlSet\Services\VBoxSVC": {"ImagePath": r"C:\Program Files\Oracle\VirtualBox\VBoxSVC.exe"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\Setup": {"SetupapiLogStatus": r"setupapi.dev.log"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services": {"VBoxService": r"Description"},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\VBoxSF": {"NetworkProvider": r"DeviceName"},
                    r"HKEY_LOCAL_MACHINE\SOFTWARE\Oracle": {"VirtualBox Guest Additions": r"C:\Program Files\Oracle\VirtualBox Guest Additions"},
                    {vbox_r}: {"InstallDir": r"C:\Program Files\Oracle\VirtualBox Guest Additions"},
                    {vbox_r}: {"DisplayName": r""},
                    {vbox_r}: {"UninstallString": r""},
                    {vbox_r}: {"DisplayVersion": r""},
                    {vbox_r}: {"URLInfoAbout": r""},
                    {vbox_r}: {"Publisher": r""},
                    r"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Tcpip\Parameters": {"TcpWindowSize": r""},
                    {vbox_hl}: {"Oracle": r""},
                    rf"{vbox_hl}\Oracle": {"Sun Ray": r""},
                    rf"{vbox_hl}\Oracle\Sun Ray": {"ClientInfoAgent": r""},
                    rf"{vbox_hl}\Oracle\Sun Ray\ClientInfoAgent": {"ReconnectActions": r""},
                    rf"{vbox_hl}\Oracle\Sun Ray\ClientInfoAgent": {"DisconnectActions": r""},
                },
            },
            "UninstallTool": {
                "path": [
                    rf"{current_disc}\{un_tool_dir}",
                    rf"{current_disc}\{un_tool_dir}\languages",
                ],
                "files": [
                    rf"{current_disc}\{un_tool_dir}\fix-dll.rar",
                    rf"{current_disc}\{un_tool_dir}\PinToTaskbar.exe",
                    rf"{current_disc}\{un_tool_dir}\PinToTaskbarHelper.dll",
                    rf"{current_disc}\{un_tool_dir}\unins000.dat",
                    rf"{current_disc}\{un_tool_dir}\unins000.exe",
                    rf"{current_disc}\{un_tool_dir}\unins000.msg",
                    rf"{current_disc}\{un_tool_dir}\UninstallTool.cpl",
                    rf"{current_disc}\{un_tool_dir}\UninstallTool.exe",
                    rf"{current_disc}\{un_tool_dir}\UninstallTool.url",
                    rf"{current_disc}\{un_tool_dir}\UninstallToolHelper.exe",
                    rf"{current_disc}\{un_tool_dir}\UTShellExt.dll",
                    rf"{current_disc}\{un_tool_dir}\UTShellExt_x86.dll",
                    rf"{current_disc}\{un_tool_dir}\languages\Arabic.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Belarusian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Bulgarian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Chinese_Simplified.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Chinese_Traditional.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Croatian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Czech.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Danish.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Dutch.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\English.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Estonian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\French.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Georgian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\German.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Greek.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Hebrew.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Hindi.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Hungarian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Indonesian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Italian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Japanese.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Korean.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Latvian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Lithuanian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Norwegian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Persian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Polish.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Portuguese.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Portuguese_Brazilian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Romanian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Russian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Serbian_Cyrillic.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Serbian_Latin.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Slovak.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Slovenian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Spanish.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Swedish.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Turkish.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Ukrainian.xml",
                    rf"{current_disc}\{un_tool_dir}\languages\Vietnamese.xml",
                ],
                "registry_keys": {
                    r"HKEY_LOCAL_MACHINE\SOFTWARE": {"UninstallTool": rf"{current_disc}:\{un_tool_dir}\UninstallTool.exe"},
                },
            },
            "ProcessHaker2": {
                "path": [
                    rf"{current_disc}\{ph2_dir}",
                    rf"{current_disc}\{ph2_dir}\plugins",
                ],
                "files": [
                    rf"{current_disc}\{ph2_dir}\CHANGELOG.txt",
                    rf"{current_disc}\{ph2_dir}\COPYRIGHT.txt",
                    rf"{current_disc}\{ph2_dir}\kprocesshacker.sys",
                    rf"{current_disc}\{ph2_dir}\LICENSE.txt",
                    rf"{current_disc}\{ph2_dir}\peview.exe",
                    rf"{current_disc}\{ph2_dir}\ProcessHacker.exe",
                    rf"{current_disc}\{ph2_dir}\ProcessHacker.sig",
                    rf"{current_disc}\{ph2_dir}\README.txt",
                    rf"{current_disc}\{ph2_dir}\unins000.dat",
                    rf"{current_disc}\{ph2_dir}\unins000.exe",
                    rf"{current_disc}\{ph2_dir}\uninstall.ico",
                    rf"{current_disc}\{ph2_dir}\plugins\DotNetTools.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\ExtendedNotifications.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\ExtendedServices.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\ExtendedTools.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\HardwareDevices.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\NetworkTools.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\OnlineChecks.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\SbieSupport.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\ToolStatus.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\Updater.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\UserNotes.dll",
                    rf"{current_disc}\{ph2_dir}\plugins\WindowExplorer.dll",
                    rf"{current_disc}\{ph2_dir}\x86\ProcessHacker.exe",
                    rf"{current_disc}\{ph2_dir}\x86\plugins\DotNetTools.dll",
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
