import os, sys
from time import sleep as timeout
from hs.tool import *

def main():
    banner()
    print("\n")
    print("   [01] 终端美化")
    print("   [02] 实用工具")
    print("   [03] 系统安装")
    print("   [04] 基础工具")
    print("   [05] msf木马生成")
    print("   [10] 退出\n")
    a = input("tools > ")
    
    if a.strip() == "1" or a.strip() == "01":
        print("\n")
        print("       [01] oh-my-zsh")
        print("       [00] 返回\n")
        b = input("tools > ")
        
        if b.strip() == "01" or b.strip() == "1": ohmyzsh()
        
        elif b.strip() == "00" or b.strip() == "0": restart()
        else:
            print("\nERROR: 输入错误")
            timeou(2)
            restart()
#工具
    elif a.strip() =="2" or a.strip() =="02":
            print("\n")
            print("        [01] sqlmap")
            print("        [02] nmap")
            print("        [03] Metasploit")
            print("        [00] 返回\n")
            c = input("tools > ")
            if c.strip() == "01" or c.strip() == "1": sqlmap()
            elif c.strip() == "02" or c.strip() == "2": nmap()
            elif c.strip() == "03" or c.strip() == "3": metasploit()
            elif c.strip() == "00" or c.strip() == "0": restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#系统
    elif a.strip() =="3" or a.strip() =="03":
            print("\n")
            print("        [01] Arch")
            print("        [02] Ubuntu")
            print("        [03] Kali Nethunter")
            print("        [04] Fedora")
            print("        [00] 返回")
            d = input("tools > ")
            if d.strip() == "01" or d.strip() == "1": arch()
            elif d.strip() == "02" or d.strip() == "2": ubuntu()
            elif d.strip() == "03" or d.strip() == "3": nethunter()
            elif d.strip() == "04" or d.strip() == "4": fedora()
            elif d.strip() == "00" or d.strip() == "0":restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#基础
    elif a.strip() =="4" or a.strip() =="04":
            print("\n")
            print("        [01] vim curl wget git unzip unrar一键安装")
            print("        [02] sudo")
            print("        [03] gcc")
            print("        [04] 更换清华源")
            print("        [05] 恢复官方源")
            print("        [00] 返回\n")
            e = input("tools > ")
            if e.strip() == "01" or e.strip() == "1": jichu()
            elif e.strip() == "02" or e.strip() == "2": sudo()
            elif e.strip() == "03" or e.strip() == "3": qhy()
            elif e.strip() == "04" or e.strip() == "4": qhy()
            elif e.strip() == "05" or e.strip() == "5": gfy()
            elif e.strip() == "00" or e.strip() == "0": restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#木马
    elif a.strip() =="5" or a.strip() =="05":
            print("\n")
            print("        请选择目标系统: ")
            print("        [01] Android")
            print("        [02] Windows x32")
            print("        [03] Windows x64")
            print("        [00] 返回")
            f = input("tools > ")
            if f.strip() == "01" or f.strip() == "1": android()
            elif f.strip() == "02" or f.strip() == "2":windows()
            elif f.strip() == "03" or f.strip() == "3":windows64()
            elif f.strip() == "00" or f.strip() == "0":restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
    elif a.strip() == "10":
        sys.exit()
    elif a.strip() == "update": update()
    else:
        print("\nERROR: 输入错误")
        timeout(2)
        restart()

if __name__ == "__main__":
    main()
