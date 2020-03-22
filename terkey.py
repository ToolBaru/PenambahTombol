# -*- coding: utf-8 -*-
import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
os.system('xdg-open https://www.youtube.com/channel/UCsX7NpPEK8a0T2MCJJQ4o7w')
print(a+'\t ╔══════════════════════════════════╗')
print(a+'\t ║Creator :Sabila                   ║')
print(a+'\t ║ Youtobe:HackSael,ToturialTermux  ║')
print(a+'\t ╚══════════════════════════════════╝')
print('\n[+] Proses..')
sleep(1)
print(b+'\n[+] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[+] Success !')
print(c+'[√]SubscribeDuluChanelSaya') 
sleep(1)
print(b+'\n[+] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[+] Success..!')
print(c+'[√]SubscribeDuluChanelSaya') 
sleep(1)
print(b+'\n[+] Setting up..')
sleep(1)
os.system('termux-reload-settings')
print(a+'[+] Successfully !!')
print(b+'[√]Subscribe lagi chanel temen gue:v') 
os.system('xdg-open https://www.youtube.com/channel/UC-jqeOYc14BEQhpuiJA2qbQ')


print(a+'[√]Jangan lupa subcsribe Chanel saya dan teman saya ') 
print(a+'[√]Grup Whatsapp : https://chat.whatsapp.com/IjyIjR5aB8YHaEJWarEwqz') 

