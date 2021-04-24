__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

import socket

# Declarando as variaveis de inicio e fim para não inicializar com algum valor antigo.
inicio = fim = 0
while True:
        # inicio é o parametro que contem o range de inicio
        inicio = int(input("Digite o range de inicio: "))
        # fim é o parametro que contem o range final
        fim = int(input("Digite o range final: "))
        # caso usuario digite o primeiro range maior, o if verifica e volta para digitar novamente.
        if inicio > fim:
                print("Inicio deve ser maior que final!")
        else:
                break

while inicio <= fim:
        # i é o parametro que conta quantos equipamentos terá por range.
        i = 10
        while i < 250:
                comeco = "192.168." # IP ja definido com o começo do endereço.
                # junta o comeco com o inicio do range + o i do ultimo quadrante.
                ip = comeco + str(inicio) + "." + str(i)

                try:
                            # socket.gethostbyaddr(ip) usa a funcao para encontrar o nome do equipamento registrado no dominio com o IP informado.
                            endereco = socket.gethostbyaddr(ip)
                            print("IP {} - Registrado como {}".format(endereco[2],endereco[0]))
                            # caso não encontre o nome do equipamento trata o erro, e imprime qual o IP que falhou.
                except socket.herror:
                    print("Endereço: {} não encontrado.".format(ip))
                    # Cria ou abre arquivo .txt para salvar IPS livres
                    with open("C:/SysTI/IPlivres.txt", "a") as arquivo:
                        arquivo.write("{}\n".format(ip))
                i += 1 # incrementa para avançar o ultimo quadrante.
                        
        inicio += 1 # incrementa para passar o range.