# coding: utf-8
__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

import os
from datetime import date
data_atual = date.today()
data_atual = str(data_atual.strftime("%d/%m/%Y"))
data_arquivo = data_atual.replace("/", "-")

# Definir função para testar ping
def check_ping(hostname):
    # Executa o ping do primeiro hostname
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Computador Ativo"
    else:
        pingstatus = "Sem resposta"

    return pingstatus

caminho = os.path.join("IP_Server", "caminho", "da", "Pasta", "da", "Rede")

# Abre o arquivo para salvar os IPs disponiveis
with open("C:/SysTI" + "/IPDisponivel_" + data_arquivo + ".txt", "w") as ips_disponiveis:
    #ips_disponiveis = open("D:\LEANDRO\Comandos\Python\IPDisponivel.txt", "a")
    
    with open("C:/SysTI/IPlivres.txt", "r") as ips_livres:
        for linha in ips_livres:
            
            # Recupera do arquivo ips_livres cada linha contendo o IP para testar
            hostname = linha
            # Envia para a função check_ping o IP para ser testado
            resultado = check_ping(hostname)
            if resultado == 'Sem resposta':
                print("IP Livre: {}" .format(linha))
                ips_disponiveis.write("{}\n" .format(linha))
