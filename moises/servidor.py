import socket
import requests
HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        msg = msg.decode('utf-8')
        response = requests.get('http://gistapis.etufor.ce.gov.br:8081/api/linhas/' + msg)
        msg = str(response.json())
        msg = msg.encode('utf-8')
        con.send(msg)


    print('Finalizando conexao do cliente', cliente)
    con.close()


    #API'S: https://gist.github.com/ronaldoarg/fb07de9a7af64ccb9b0e7b436a4e28e6