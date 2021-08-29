import os
from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":   
    os.system("pip install pynput")
elif _platform == "darwin":
    os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    os.system("python3 get-pip.py")
elif _platform == "win32" or _platform == "win64":
    os.system("[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};")
    os.system("(new-object System.Net.WebClient).DownloadFile('http://www.mysite.com', 'C:\Temp\file')")
    os.system("cd C:\Temp\file"
    os.system("python get-pip.py")
