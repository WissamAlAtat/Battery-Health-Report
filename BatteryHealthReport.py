import subprocess
import getpass
import os


def getDesktopPath():
    user=getpass.getuser()
    desktopPath=f"C:\\Users\\{user}\\Desktop\\battery-report.html"
    return desktopPath