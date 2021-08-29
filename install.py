import os
from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":   
    os.system("pip install pynput")
elif _platform == "darwin":
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
elif _platform == "win32" or _platform == "win64":
    
