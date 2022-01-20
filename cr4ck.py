#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Do Not Copy This Script :)
##### LOGO #####
logo2 = """
\033[1;93m███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗     
\033[1;93m████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║    
\033[1;92m██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║    
\033[1;92m██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║      
\033[1;91m██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝      
\033[1;91m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░      
\033[1;95m-------------------- \033[1;94mNew Version 1.0------------------➤  
\033[1;91m.                   TERMUX MY4NM4R TEAM　 
\033[1;97m.　                  Brand: B4BY DR4GON
\033[1;95m.                  　 Creation: M4RMU
\033[1;96m.                   тεcнησℓσgү вү мαямυ
\033[1;92m.                                        B4BY
\033[1;92m.                                             DR4G0N
\033[1;95m------------------------- \033[1;93mM4RMU -----------------------➤
"""

try:
    import os
    import sys
    import time
    import urllib
    import platform
    import requests
    import base64
except ImportError:
    os.system('pip2 install requests') #Module Not found Eror :(

#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()

logo2_base = 'G1swOzk3bQkkJCQkJCQkJCAgJCQkJCQkJCQgICQkICAgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgJCQgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgICQkICQkCgkkJCQkJCQkJCAgJCQgICAgICQkICAgICQkJAoJJCQgICAkJCAgICQkICAgICAkJCAgICQkICQkCgkkJCAgICAkJCAgJCQgICAgICQkICAkJCAgICQkCgkkJCAgICAgJCQgJCQkJCQkJCQgICQkICAgICAkJAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQogfHwgG1swOzk3bRtbMDs0MW0gUHJvZ3JhbW1pbmcgaXMgdGhpbmtpbmcgbm90IHR5cGluZyA6KSAbWzBtIHx8Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tChtbMDs5N20g4p6kIEF1dGhvciAgOiBZZXN3YW50IE1pc2hyYQobWzA7OTdtIOKepCBWZXJzaW9uIDogMy4wChtbMDs5N20g4p6kIGZiLXBhZ2UgOiBodHRwczovL2ZiLmNvbS9UZWNobmljYWwuTWlzaHJhCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t'
logo2 = base64.b64decode(logo_base) # logo with base64 encodeing :)

def home(): #main menu
    baba(" Updating Çommand")
    os.system("clear")
    arm = platform.architecture()[0] #Checking arm
    print logo2 #raw
    print 47*("-")
    print('Your Device Is \033[0;92m'+arm).center(45)  #Show Raw
    print 47*("\033[0;97m-")
    baba("\tUpdateing => ")
    os.system("clear")
    print logo2
    device = platform.architecture()[0]
    if device == '64bit':
        from libmainrdx import x_x_x_home_x_x_x
        x_x_x_home_x_x_x()
    elif device == '32bit':
        os.system("clear")
        os.system("exit")
        os.system("cd $HOME") #Home 
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        print("$ Your Device Has Been No Support :( ")
    else:
        os.system("clear")
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        os.system("exit")

if __name__ == '__main__':
    os.system("git pull")
    home()
