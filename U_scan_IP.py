__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

# Declarando as variaveis de inicio e fim para não inicializar com algum valor antigo.
import socket
import os
import requests
from tkinter import *
os.remove("C:/SysTI/IPlivres.txt")
IPsLivres = []

# Função para pingar os IPs.
def check_ping(hostname):
    response = os.system("ping -n 1 " + hostname)
    # verifica se respondeu...
    if response == 0:
        pingstatus = "Network Error"
    else:
        pingstatus = "Network Active"

    return pingstatus

# Função para salvar arquivo IPlivres no disco.
def salva_arquivo(IPsLivres):
    f = open("C:/SysTI/IPlivres.txt", "x")
    for linhas_do_arquivo in IPsLivres:
        with open("C:/SysTI/IPlivres.txt", "a") as arquivo:
            arquivo.write("{}\n".format(linhas_do_arquivo))

# Função para receber valor de escaneamento.
def botao_comecar():
    while True:
        # Recebe o range para scanear
        range = int(input("Digite o range: "))
        # caso usuario digite um range inexistente ele verifica.
        if range < 0 or range > 3:
            print("Range deve estar entre 0 e 3.")
        else:
            break

def check_nslookup(IPsLivres):
    # i é o parametro que conta quantos equipamentos terá por range.
    i = 210
    while i < 245:
        comeco = "192.168." # IP ja definido com o começo do endereço.
        # junta o range + o i do ultimo quadrante.
        ip = comeco + str(range) + "." + str(i)

        try:
            # socket.gethostbyaddr(ip) usa a funcao para encontrar o nome do equipamento registrado no dominio com o IP informado.
            endereco = socket.gethostbyaddr(ip)
            print("IP {} - Registrado como {}".format(endereco[2],endereco[0]))
        # caso não encontre o nome do equipamento trata o erro, e imprime qual o IP que falhou.
        except socket.herror:
            print("Endereço: {} não encontrado.".format(ip))
            IPsLivres.append(ip)
            
        i += 1 # incrementa para avançar o ultimo numero.



def principal():
    # Imprimir IPs disponíveis
    print("")
    print("IPs disponiveis para uso: ")
    print("")
    for ping in IPsLivres:
        pingstatus = check_ping(ping)
        if pingstatus == "Network Active":
            print(pingstatus, ping)
            IPsLivres.remove(ping)
        elif pingstatus == "Network Error":
            print("IP Disponível.",ping)
        else:
            print("Erro no ping.")

    salva_arquivo(IPsLivres)

janela1 = Tk()
janela1.title("Busca IPs Livres")
texto_orientacao1 = Label(janela1, text="Este programa varre o range de IP escolhilho apartir de 10 até 245.").grid(column=1, row=0)
texto_orientacao2 = Label(janela1, text="Digite o range para o numero de IP. Ex.: 3 = 192.168.3.").grid(column=1, row=1)
botao1 = Button(janela1, text="ENVIAR").grid(column=2, row=2)


janela.mainloop()