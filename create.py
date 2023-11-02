import os
import time

iconame=f'{int (time.time() *1000)}.ico'
with open('coleak.ico',"br") as f:
    cont=f.read()
with open(f'{iconame}',"bw") as f:
    cont+=iconame.encode()
    f.write(cont)
a='''
███████╗██╗   ██╗██╗██╗     ██╗  ██╗██╗██████╗ ██╗███╗   ██╗ ██████╗ 
██╔════╝██║   ██║██║██║     ██║  ██║██║██╔══██╗██║████╗  ██║██╔════╝ 
█████╗  ██║   ██║██║██║     ███████║██║██║  ██║██║██╔██╗ ██║██║  ███╗
██╔══╝  ╚██╗ ██╔╝██║██║     ██╔══██║██║██║  ██║██║██║╚██╗██║██║   ██║
███████╗ ╚████╔╝ ██║███████╗██║  ██║██║██████╔╝██║██║ ╚████║╚██████╔╝
╚══════╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
'''                                                                                                  '      '''
print(a)
os.system(f'pyinstaller -F -w b.py -n HipsMain.exe -i {iconame}')
print()
print()
print('exe file is in dist/HipsMain.exe')
os.remove(iconame)
os.remove('HipsMain.exe.spec')
os.remove('content.txt')
os.remove('b.py')