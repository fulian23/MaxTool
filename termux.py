import os
os.system('pkg update')
os.system('pkg upgrade')
a=input('是否安装vim curl wget git unzip unrar(Y/n)')
if a.strip() == "N" or a.strip() == "n":
    pass
else:
    print('\n######installing######')
    os.system('pkg install vim curl wget git unzip unrar')
    print('###### Done ######')
a=input('是否安装oh-my-zsh(Y/n)')
if a.strip() == "N" or a.strip() == "n":
    pass
else:
    print('\n######installing######')
    os.system('pkg install zsh')
    os.system('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
    print('###### Done ######')
    a=input('是否更换主题(Y/n)')
    if a.strip() == "N" or a.strip() == "n":
        pass
    else:
        a=input('输入更换的主题')
        f=open('.zshrc','r',encoding='gbk')
        f1=open('zshrc','a+',encoding='utf-8')
        for line in f:
            if "robbyrussell" in line:
                line=line.replace("robbyrussell",a)
            f1.write(line)
        os.system("rm .zshrc")
        os.system("mv zshrc .zshrc")
a=input("是否更换键盘布局(Y/n)")
if a.strip() == "N" or a.strip() == "n":
    pass
else:
    os.system("cd $HOME&& mkdir .termux>/dev/null 2>&1; echo \"extra-keys = [['ESC',':',';','=','(',')','[','$',']'],['TAB','|','/','~','*','HOME','UP','END','PGUP'],['CTRL','ALT','_','–','ENTER','LEFT','DOWN','RIGHT','PGDN']]\">.termux/termux.properties;termux-reload-settings")
    print("完成！")
