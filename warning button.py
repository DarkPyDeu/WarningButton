from pynput.keyboard import Listener
from Modules.Message import ms_error
import pyAesCrypt as Cry
import os

password = "NVSIOUghoslnvgsgu3408u74tgolhnH:PGOLshsy9w8e4uth;:OSUGSUHnksjnvsoiu:SIHGISKGnb;SOHJib;iobhNSBihbn;dzoz;iouz;uh"
bufferSize = 512 * 1024
dir = "Security" # Можно и кастомную директорию

def encrypt():
    try:
        Cry.encryptFile(str(file), str(file) + ".CC", password, bufferSize)
        os.remove(file)
    except:
        pass

def decrypt():
    try:
        Cry.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
        os.remove(file)
    except:
        pass

def decrypt_dir():
    global file
    try:
        filesindir = os.listdir(dir)
        for filesindirs in filesindir:
            path = os.path.join(filesindirs)
            file = dir + "/" + path
            decrypt()
    except:
        ms_error("Warning button", "Директория не найдена \"Security\"")

def encrypt_dir():
    global file
    try:
        filesindir = os.listdir(dir)
        for filesindirs in filesindir:
            path = os.path.join(filesindirs)
            file = dir + "/" + path
            encrypt()
    except:
        ms_error("Warning button", "Директория не найдена \"Security\"")

def send(key):
    press = str(key)
    if press.find("f10") > 0:
        encrypt_dir()
    elif press.find("f9") > 0:
        decrypt_dir()

if __name__ == '__main__':
    with Listener(on_press = send) as listener:
        listener.join()