import sys

from sona import *
from socket import socket
import colorama
from colorama import Fore, Back, Style
from time import sleep
import os
from threading import Thread as thr
from random import choice
import pickle
import climage

class sticker:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

colorama.init(autoreset=True)

mk = "ABCDEFGHIKJMNOPQRSTXYZabcdefghikmnopqrstxyz1234567890!@#$%^&*"
mks = "ABCDEFGHIKJMNOPQRSTXYZabcdefghikmnopqrstxyz1234567890"


with open("plugins/anime_stickers.pk", 'rb') as f:
    stickers = pickle.load(f)

def gen_key():
    key = ""
    for i in range(16):
        key+=choice(mk)
    return key

def gen_name():
    key = ""
    for i in range(8):
        key+=choice(mks)
    return key

def debug(pr):
    print(f"[{Fore.YELLOW}Debug{Style.RESET_ALL}]: {pr}")


os.system("clear")
print("\n \n")
print(Fore.BLUE+"Welcome to ELRSA remote connector")
print(" ")


class connection:
    def __init__(self, username, address, key):
        self.username = username
        self.address = address
        self.key = key


connections = []

pr = 9090

tm = 0.1
c = 0
while c<1:
    print(f"\r[{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'********'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*******'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'**'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'******'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'***'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*****'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'****'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'****'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*****'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'***'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'******'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'**'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*******'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'********'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*******'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'******'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'**'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*****'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'***'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'****'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'****'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'***'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*****'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'**'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'******'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+'*'}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'*******'+Style.RESET_ALL}]", end='')
    sleep(tm)
    print(f"\r[{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+Fore.RED+'*'+Style.RESET_ALL}{Style.DIM+'********'+Style.RESET_ALL}]", end='')
    sleep(tm)
    c+=1

print("\n")

connectors = []
def start_server_session(username):
    port = pr
    sock = socket()
    sock.bind(('127.0.0.1', port))
    print(Fore.YELLOW+"Listening for connection"+Style.RESET_ALL)
    sock.listen(2)
    e, t = sock.accept()
    print(Fore.YELLOW+"Connection detected, generating key")
    ks = gen_key()
    aes_send = AESCipher(ks)
    e.send(ks.encode())
    print(ks)
    def rem(e):
        ks = e.recv(1024).decode()
        aes_get = AESCipher(ks)
        while 1:
            data = aes_get.decrypt(e.recv(1024))
            user = data.split("|")[0]
            print(f"\r[{Fore.RED+user+Style.RESET_ALL}]: {data.split('|')[1]} \n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ", end = '')
    thr(target=rem, args=(e,)).start()
    while 1:
        smsg = input(f"({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ")
        e.send(aes_send.encrypt(f"{username}|{smsg}"))

def start_client_session(username):
    addr = input(f"({Fore.BLUE+'Address'+Style.RESET_ALL})>>> ")
    port = input(f"({Fore.BLUE + 'Enter The Port [d for default 9090]' + Style.RESET_ALL})>>> ")
    if port == 'd':
        port == 9090
    else:
        port = int(port)
    sock = socket()
    # sock.bind((addr, port))
    sock.connect((addr, port))
    print("Generating key...")
    ks = gen_key()
    aes_send = AESCipher(ks)
    print(ks)
    sock.send(ks.encode())
    ks = sock.recv(1024).decode()
    aes_get = AESCipher(ks)
    passwd = input(f"({Fore.BLUE + 'Server password' + Style.RESET_ALL})>>> ")
    sock.send(aes_send.encrypt(passwd))
    answ = aes_get.decrypt(sock.recv(1024))
    if answ == "Done":
        rk = 1

    else:
        rk = 0
        print(f"[{Fore.RED}Wrong password{Style.RESET_ALL}]")
    def rem(sock, ks):
        try:
            while 1:
                data = aes_get.decrypt(sock.recv(1024))
                try:
                    _ = data.split("|")[1]
                    user = data.split("|")[0]
                    if user != username:
                        if data.split("|")[1].split(":")[0] == "sticker":
                            for stk in stickers:
                                if stk.name == data.split('|')[1].split(':')[1]:
                                    print(f"\r[{Fore.RED + user + Style.RESET_ALL}]:")
                                    print(stk.pattern)
                                    print(f"\n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ")

                        else:
                            print(
                                f"\r[{Fore.RED + user + Style.RESET_ALL}]: {data.split('|')[1]} \n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ",
                                end='')
                except IndexError:
                    if user != username:
                        print(
                            f"\r{data}\n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ",
                            end='')

        except ValueError:
            print(f"[{Fore.RED}Value Error, may be you entered wrong password{Style.RESET_ALL}]")
            sys.exit()
    if rk:
        thr(target=rem, args=(sock, ks, )).start()
    while rk:
        smsg = input(f"({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ")
        if smsg.split(".")[0] == "console":
            if smsg.split(".")[1] == "stickers":
                for j in stickers:
                    print(j.name)
        else:
            sock.send(aes_send.encrypt(f"{username}|{smsg}"))


def remote_server(username, host, port):
    password = input(f"({Fore.BLUE + 'Server password' + Style.RESET_ALL})>>> ")
    sock = socket()
    sock.bind((host, port))
    print(Fore.YELLOW + "Listening for connection" + Style.RESET_ALL)
    ks = gen_key()
    aes_send = AESCipher(ks)
    def rem(e, t):
        global connections
        ks = e.recv(1024).decode()
        u = 1
        aes_get = AESCipher(ks)
        pas = aes_get.decrypt(e.recv(1024))
        if pas != password:
            e.send(aes_send.encrypt("Fault"))
            e.close()
            u = 0
            print(
                f"\r[{Fore.RED}Connection with wrong password detected{Style.RESET_ALL}]: {t}\n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ",
                end='')
            for j in connections:
                j.send(aes_send.encrypt(f"SERVER|Wrong password attempt detected: {t}"))
        else:
            e.send(aes_send.encrypt("Done"))
            connections.append(e)
            print(
                f"\r[{Fore.YELLOW}New user connected{Style.RESET_ALL}]: {t}\n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ",
                end='')
            for j in connections:
                j.send(aes_send.encrypt(f"SERVER|New user connected: {t}"))
        while u:
            data = aes_get.decrypt(e.recv(1024))
            user = data.split("|")[0]
            for j in connections:
                try:
                    j.send(aes_send.encrypt(f"{user}|{data.split('|')[1]}"))
                    print(
                        f"\r[{Fore.RED + user + Style.RESET_ALL}]: {data.split('|')[1]} \n({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ",
                        end='')
                except IndexError:
                    j.send(aes_send.encrypt(f"{data}"))


    while 1:
        sock.listen(2)
        e, t = sock.accept()
        e.send(ks.encode())
        thr(target=rem, args=(e, t, )).start()

    print(Fore.YELLOW + "Connection detected, generating key")


    print(ks)
    connections.append(e)


    while 1:
        smsg = input(f"({Fore.BLUE + 'msg' + Style.RESET_ALL})>>> ")
        for j in connections:
            j.send(aes_send.encrypt(f"{user}|{smsg}"))


user = input(f"({Fore.BLUE+'Username'+Style.RESET_ALL})>>> ")
server_or_client = input(f"({Fore.BLUE+'Server[s]/Client[c]'+Style.RESET_ALL})>>> ")

if server_or_client == 'c':
    start_client_session(user)
elif server_or_client == 's':
    host = input(f"({Fore.BLUE + 'Enter The Host [d for default]' + Style.RESET_ALL})>>> ")
    port = input(f"({Fore.BLUE + 'Enter The Port [d for default 9090]' + Style.RESET_ALL})>>> ")
    if host == 'd':
        host = '127.0.0.1'
    if port == 'd':
        port = 9090
    else:
        port = int(port)
    remote_server(user, host, port)
else:
    remote_server(user)