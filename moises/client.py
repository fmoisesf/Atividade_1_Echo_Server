#Escrever um programa em Python para um cliente que conecta-se a um servidor (echo server) que implementa uma aplicação
#para informar o nome de uma linha de ônibus da cidade de Fortaleza a partir do número da linha.


import socket

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = ''
while True:
    while type(msg) != int:
        try:
            msg = int(input("\npesquise uma linha ou digite 1000 para sair.\n "))
            break
        except:
            print("Valor inválido")
            continue
    if msg == 1000:
        break


    msg = str(msg).encode('utf-8')
    tcp.send(msg)
    msg = tcp.recv(1024)
    msg = msg.decode('utf-8')
    print("+____________________________________________________________________+")
    print(msg)
    print("+____________________________________________________________________+")
print("fim do programa")
tcp.close()
