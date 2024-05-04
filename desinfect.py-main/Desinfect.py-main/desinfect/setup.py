import os 
import sys
import platform

print("Installations des modules pythons requis pour la desinfection:")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install --upgrade pip install psutil")
    os.system("pip install --upgrade pip install pip install tkinter")

if sys.platform.startswith("linux"):
    "LINUX"
    os.system("pip install --upgrade pip install psutil")
    os.system("pip install --upgrade pip install pip install tkinter")
