# VM Backup Script

This is a Python script for performing backups of virtual machine data. It uses the `BackupManager` class to handle backup operations and manages disk space considerations.
I made sure to use only the default library of python, if one is missing after launch use this command: `pip install -r requirement.txt`

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

1. Clone this repository to your local machine:
```bash
git clone https://github.com/alexdjetic/backup_qemu.git
```

## Install

### windows: 
In order to install python3.11 on windows 10/11:

- official site of python: [python3](https://www.python.org/downloads/)

or

- install powershell(latest version) to this date : [powershell install](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)
- using winget tool: [winget install](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- then in powershell 6.x+, `winget install python3`


### Linux:

#### debian/ubuntu
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python python-pip
```

#### fedora/redhat
```bash
dnf update
dnf install python python-pip
```

#### archlinux
```bash
pacman -Syu
pacman -S python python-pip
```

#### alpine
```bash
apk update
apk upgrade
apk add python3 python-pip
```

2. verify python version
- `python --version`

3. launch the script:
```bash
cd backup_qemu #change current directory to backup
chmod +x *.py #give execution right to file
python3 main.py #launch the script
```

## be careful
- to launch on windows, you need modify the code a bit where the sudo is use because sudo is not available on windows(and launch in administtrator mode if need) or use WSL(windows subsystem linux) to launch the script, here the official link and stepp to download wsl: [install wsl](https://learn.microsoft.com/en-us/windows/wsl/install)

## what will change in few month
- I will make sure that script work on windows
- make a graphical interface for this utility, i don't know if use a tk or an other framework
- if you have suggestion or improve this projekt, pull a request

Have a great day 😏
