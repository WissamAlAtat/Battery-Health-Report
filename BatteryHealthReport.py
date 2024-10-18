import subprocess
import getpass
import os


def getDesktopPath():
    user=getpass.getuser()
    desktopPath=f"C:\\Users\\{user}\\Desktop\\battery-report.html"
    return desktopPath

def run_powershell_as_admin(command):
    powershell_command = f'powershell.exe -Command "Start-Process PowerShell -ArgumentList \'{command}\' -Verb RunAs"'
    subprocess.run(powershell_command, shell=True)


output_path = getDesktopPath()
command = f'powercfg /batteryreport /output "{output_path}"'
run_powershell_as_admin(command)