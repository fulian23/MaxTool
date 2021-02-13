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
    
    if a== "1" or a == "01":
        print("\n")
        print("       [01] oh-my-zsh")
        print("       [00] 返回\n")
        b = input("tools > ")
        
        if b == "01" or b == "1": ohmyzsh()
        
        elif b == "00" or b == "0": restart()
        else:
            print("\nERROR: 输入错误")
            timeou(2)
            restart()
#工具
    elif a =="2" or a =="02":
            print("\n")
            print("        [01] sqlmap")
            print("        [02] nmap")
            print("        [03] Metasploit")
            print("        [00] 返回\n")
            c = input("tools > ")
            if c == "01" or c == "1": sqlmap()
            elif c == "02" or c == "2": nmap()
            elif c == "03" or c == "3": metasploit()
            elif c == "00" or c == "0": restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#系统
    elif a =="3" or a =="03":
            print("\n")
            print("        [01] Arch")
            print("        [02] Ubuntu")
            print("        [03] Kali Nethunter")
            print("        [04] Fedora")
            print("        [00] 返回")
            d = input("tools > ")
            if d == "01" or d == "1": arch()
            elif d == "02" or d == "2": ubuntu()
            elif d == "03" or d == "3": nethunter()
            elif d == "04" or d == "4": fedora()
            elif d == "00" or d == "0":restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#基础
    elif a =="4" or a =="04":
            print("\n")
            print("        [01] vim curl wget git unzip unrar一键安装")
            print("        [02] sudo")
            print("        [03] gcc")
            print("        [04] 更换清华源")
            print("        [05] 恢复官方源")
            print("        [00] 返回\n")
            e = input("tools > ")
            if e == "01" or e == "1": jichu()
            elif e == "02" or e == "2": sudo()
            elif e == "03" or e == "3": qhy()
            elif e == "04" or e == "4": qhy()
            elif e == "05" or e == "5": gfy()
            elif e == "00" or e == "0": restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
#木马
    elif a =="5" or a =="05":
            print("\n")
            print("        请选择目标系统: ")
            print("        [01] Android")
            print("        [02] Windows x32")
            print("        [03] Windows x64")
            print("        [00] 返回")
            f = input("tools > ")
            if f == "01" or f == "1": android()
            elif f == "02" or f == "2":windows()
            elif f == "03" or f == "3":windows64()
            elif f == "00" or f == "0":restart()
            else:
                print("\nERROR: 输入错误")
                timeout(2)
                restart()
    elif a == "10":
        sys.exit()
    elif a == "update": update()
    else:
        print("\nERROR: 输入错误")
        timeout(2)
        main()

if __name__ == "__main__":
    main()
