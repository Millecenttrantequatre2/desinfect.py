import os
import sys
import psutil
import time
import tkinter as tk
from tkinter import messagebox

def clear_console():
    if sys.platform.startswith('win'):
        os.system("cls")
    else:
        os.system("clear")

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  

def welcome_message():
    clear_console()
    welcome_text = "Bienvenue !\n\nCeci est un script de désinfection créé par 1134.\nAppuyez sur Entrée pour lancer le script...\n"
    print_slow(welcome_text)
    input()

def search_malicious_processes():
    clear_console()
    print("Recherche de logiciels malveillants en cours d'exécution")
     
    for _ in range(10):  
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)  
    
    malicious_processes_found = False
    suspicious_processes = ["malicious_process.exe", "evil_service"]

    for process in psutil.process_iter():
        if process.name() in suspicious_processes:
            print(f"\nProcessus suspect trouvé : {process.name}")
            malicious_processes_found = True

    if not malicious_processes_found:
        print("\nAucun logiciel malveillant en cours d'exécution.")

    input("\nAppuyez sur Entrée pour continuer...")

def delete_backdoors():
    suspicious_directories = [
        "/usr/bin", "/usr/sbin", "/bin", "/sbin", "/etc/init.d",
        os.path.expanduser("~/.ssh"), os.path.expanduser("~/.config"),
        os.path.expanduser("~/.local/bin"), os.path.expanduser("~/.local/share")
    ]

    suspicious_extensions = [".sh", ".py", ".exe", ".dll", ".vbs"]

    files_deleted = False

    for directory in suspicious_directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if any(file.endswith(ext) for ext in suspicious_extensions):
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            files_deleted = True
                            print(f"Fichier suspect supprimé : {file_path}")
                        except Exception as e:
                            pass

    if not files_deleted:
        print("Aucun fichier suspect trouvé.")

def delete_token_grab_files():
    suspicious_directories = []
    if sys.platform.startswith('win'):
        suspicious_directories.extend([
            os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup"),
            os.path.join(os.environ["APPDATA"], "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup"),
            os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup"),
            os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        ])
    elif sys.platform.startswith('linux'):
        suspicious_directories.append(os.path.expanduser("~/.config/autostart"))
    elif sys.platform.startswith('darwin'):
        suspicious_directories.append(os.path.expanduser("~/Library/LaunchAgents"))

    malicious_extensions = [".py", ".exe", ".bat", ".vbs", ".ps1"]

    files_deleted = False

    for directory in suspicious_directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if any(file.endswith(ext) for ext in malicious_extensions):
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            files_deleted = True
                            print("Fichier malveillant supprimé :", file_path)
                        except Exception as e:
                            pass

    if not files_deleted:
        print("Aucun fichier malveillant trouvé.")

def restart_computer():
    if messagebox.askyesno("Redémarrage nécessaire", "Voulez-vous redémarrer l'ordinateur maintenant ?"):
        if sys.platform.startswith('win'):
            restart_windows()
        elif sys.platform.startswith('linux'):
            restart_linux()
        elif sys.platform.startswith('darwin'):
            restart_mac()
    else:
        clear_console()

def restart_windows():
    os.system("shutdown /r /t 1")

def restart_linux():
    os.system("sudo reboot")

def restart_mac():
    os.system("sudo reboot")

def check_running_processes():
    suspicious_processes = ["malicious_process.exe", "evil_service"]
    for process in psutil.process_iter():
        if process.name() in suspicious_processes:
            print(f"Processus suspect trouvé : {process.name}")

def check_file_permissions():
    suspicious_files = ["/etc/shadow", "/root/.ssh/authorized_keys"]
    for file_path in suspicious_files:
        if os.path.exists(file_path):
            file_permissions = oct(os.stat(file_path).st_mode)
            if file_permissions != "0o600":
                print(f"Permissions suspectes pour le fichier {file_path} : {file_permissions}")

if __name__ == "__main__":
    welcome_message()
    clear_console()
    delete_backdoors()
    delete_token_grab_files()
    search_malicious_processes()
    restart_computer()