import os
from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":   
    os.system("pip install pynput")
if _platform == "darwin":
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
