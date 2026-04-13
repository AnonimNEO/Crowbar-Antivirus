#Общее количество строчек кода
all_line = "8298"

#Каталог логов
log_path = "log"

#Каталог изображений
images_path = "."

#Файл базы плохих процессов
bad_process_txt = "bad_process.txt"

#Файл максимальной нагрузки на CPU
ultimate_load_cpu_txt = "ultimate_load_cpu.txt"

#Файл максимальной нагрузки на RAM
ultimate_load_ram_txt = "ultimate_load_ram.txt"

#Файл базы исключений
exception_process_txt = "exception_process.txt"

#Имя лог файла очистки temp
clear_temp_log = "Clear_Temp_log"

#Главный лог файл
T_log_txt = "Crawbar_log.txt"

#Ключ Шифрования
clyth = 13

#icon - только иконка, only-windows - только окно, window - иконка и окно
start_interface = "icon"

#Контрастная тема
black_theme = {"bg": "black", "fg": "white", "bbg": "darkblue", "bfg": "white", "abg": "blue", "afg": "white", "lbg":  "black", "lfg": "white", "stb": "#090909", "tbg": "darkblue", "tfg": "white"}

#Тёмная тема
dark_theme = {"bg": "#1e1f22", "fg": "white", "bbg": "#243048", "bfg": "white", "abg": "#548af7", "afg": "white", "lbg":  "#1e1f22", "lfg": "white", "stb": "#1e1f22", "tbg": "#243048", "tfg": "white"}

#Светлая тема
white_theme = {"bg": "white", "fg": "black", "bbg": "white", "bfg": "black", "abg": "gray", "afg": "black", "lbg":  "white", "lfg": "black", "stb": "gray", "tbg": "white", "tfg": "black"}

#Красная тема
red_theme = {"bg": "black", "fg": "white", "bbg": "darkred", "bfg": "white", "abg": "red", "afg": "black", "lbg":  "black", "lfg": "white", "stb": "red", "tbg": "darkred", "tfg": "white"}

#Серая тема
gray_theme =  {"bg": "gray", "fg": "white", "bbg": "gray", "bfg": "white", "abg": "white", "afg": "black", "lbg":  "gray", "lfg": "white", "stb": "gray", "tbg": "black", "tfg": "white"}

#Оранжевая тема
orange_theme =  {"bg": "gray", "fg": "white", "bbg": "darkorange", "bfg": "white", "abg": "orange", "afg": "black", "lbg":  "gray", "lfg": "darkorange", "stb": "gray", "tbg": "darkorange", "tfg": "black"}

#Зелёная тема
lime_theme =  {"bg": "green", "fg": "white", "bbg": "green", "bfg": "white", "abg": "lime", "afg": "black", "lbg":  "green", "lfg": "lime", "stb": "green", "tbg": "lime", "tfg": "black"}

#(НЕ РЕДАКТИРОВАТЬ)Кортеж тем
theme = {"black": black_theme, "dark": dark_theme, "white": white_theme, "red": red_theme, "gray": gray_theme, "orange": orange_theme, "lime": lime_theme}

#Тема по умолчанию
default_theme = "dark"

#Автозапуск LoadProtection
start_lp = False

#Способ перезагрузки win32com, os, subprocess, bat
restart_windows = "win32com"

#Через сколько секунд выполнить перезагрузку
time_to_restart = "1"

#Для win32com, перезапустить ли ОС? True - да | False - нет
reboot_os = True

#Для win32com, закрыть ПО принудительно? True - да | False - нет
force_software = True

#Для способа bat, имя файла .bat (обязательно .bat)
restart_windows_bat = "restart_windows.bat"

#Имя пользователя по умолчанию
default_user_name = "Admin"

#Количество секунд до обновления списка процессов
time_to_update_process_list = 5

#Количество секунд до обновления списка процессов в LoadProtection
time_to_close_window = 5

#Количество секунд до закрытия вопроса после заморозки
time_sleep_to_close_question = 30

#Количество секунд до закрытия окна вопроса о добавлении базе исключения
time_sleep_to_close_question2 = 60

#Количество секунд ожидания когда LoadProtection повторит сканирование
time_sleep_to_scan = 5

#Стандартное значения предельной нагрузки на CPU
ultimate_load_cpu = 25

#Стандартное значение предельной нагрузки на RAM
ultimate_load_ram = 20

#База запрещённых процессов по имени
bad_process = ["virus", "malware", "trojan", "yandex", "browser", "max"]

#База Исключений
exception_process = ["System Idle Process", "System.exe", "dwm.exe", "mmc.exe", "cmd.exe", "conhost.exe", "explorer.exe", "smss.exe", "Memory Compression", "Interrupts", "Registry", "csrss.exe", "wininit.exe", "services.exe", "RuntimeBroker.exe", "InputPersonalization.exe", "ApplicationFrameHost.exe", "WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe", "taskhostw.exe", "sihost.exe", "spoolsv.exe", "SearchIndexer.exe", "SearchFilterHost.exe", "SearchProtocolHost.exe", "SearchProtocolHost.exe", "dllhost.exe", "lsass.exe", "fontdrvhost.exe", "csrss.exe", "winlogon.exe", "fontdrvhost.exe", "TiWorker.exe", "regedit.exe", "MsMpEng.exe"]