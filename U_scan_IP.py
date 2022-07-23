__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

# Declarando as variaveis de inicio e fim para não inicializar com algum valor antigo.
from msilib.schema import ComboBox
import socket
import os
import requests
from tkinter import *
from datetime import date
from C_banco_IP import Banco


#os.remove("C:/SysTI/IPlivres.txt")
IPsLivres = []
# Recolhe data atual para nomear arquivo de saida.txt
data_atual = date.today()
data_atual = str(data_atual.strftime("%d/%m/%Y"))
data_arquivo = data_atual.replace("/", "-")


class Application():

    def __init__(self, master=None):
        self.fonte_padrao = ("Arial", "10")

        self.msg_ip_disponivel = ''' IP Disponível.'''
        
        self.primeiroConteiner = Frame(master)
        self.primeiroConteiner["pady"] = 10
        self.primeiroConteiner.pack()

        self.segundoConteiner = Frame(master)
        self.segundoConteiner["padx"] = 20
        self.segundoConteiner.pack()

        self.terceiroConteiner = Frame(master)
        self.terceiroConteiner["padx"] = 20
        self.terceiroConteiner.pack()

        self.quartoConteiner = Frame(master)
        self.quartoConteiner["pady"] = 20
        self.quartoConteiner.pack()

        master.title("Busca IPs Livres")
        self.texto_orientacao1 = Label(self.primeiroConteiner, text="Este programa varre o range de IP escolhilho apartir de 10 até 245.")
        self.texto_orientacao1["font"] = ("Arial", "10", "bold")
        self.texto_orientacao1.pack()

        self.texto_orientacao2 = Label(self.segundoConteiner, text="Digite o range para o numero de IP. Ex.: 3 = 192.168.3.")
        self.texto_orientacao2.pack(side= LEFT)
        self.range = Entry(self.segundoConteiner)
        self.range["width"] = 30
        self.range["font"] = self.fonte_padrao
        self.range.pack(side=LEFT)
        self.range.focus()

        self.botao1 = Button(self.segundoConteiner)
        self.botao1["text"] = "ENVIAR"
        self.botao1["font"] = ("Calibri", "8")
        self.botao1["width"] = "12"
        self.botao1["command"] = self.verificaEntrada
        self.botao1.pack()

        self.mensagem = Label(self.terceiroConteiner, text="", font="self.fonte_padrao")
        self.mensagem.pack()

        self.mensagem2 = Label(self.quartoConteiner, font="self.fonte_padrao", text="Msg 2")
        self.mensagem2.pack()

        self.labelframe = LabelFrame(master, text="IPs para uso:")
        #self.labelframe.pack(fill="both", expand="yes")
        self.labelframe.pack()


        self.textbox = Text(self.labelframe)
        self.textbox.pack()
        self.textbox.config(bg='#A67449')
        self.textbox.config(state='disabled')


    def verificaEntrada(self):
        # Recebe o range para scanear
        self.entrada = self.range.get()
        if not self.entrada:
            self.mensagem["text"] = "Digite um número inteiro."
        else:
            try:
                self.entrada = int(self.entrada)
                # caso usuario digite um range inexistente ele verifica.
                if self.entrada < 0 or self.entrada > 3:
                    self.mensagem["text"] = "Range deve estar entre 0 e 3."
                else:
                    self.mensagem["text"] = "Procurando IPs."
                    self.funcao_principal(self.entrada)
            except ValueError:
                self.mensagem["text"] = "É aceito apenas numeros inteiros."


    # Função que vefifica se IP está registrado no DNS com nslookup.
    def check_nslookup(self, range):
        global IPsLivres
        self.range = range
        # i é o parametro que conta quantos equipamentos terá por range.
        i = 10
        while i < 15:
            self.comeco = "192.168." # IP ja definido com o começo do endereço.
            # junta o range + o i do ultimo quadrante.
            ip = self.comeco + str(self.range) + "." + str(i)

            try:
                # socket.gethostbyaddr(ip) usa a funcao para encontrar o nome do equipamento registrado no dominio com o IP informado.
                self.endereco = socket.gethostbyaddr(ip)
                self.mensagem2["text"] = "IP {} - Registrado como {}".format(self.endereco[2], self.endereco[0])
                self.textbox.insert("end", self.endereco[0])
                print("IP {} - Registrado como {}".format(self.endereco[2], self.endereco[0]))
            # caso não encontre o nome do equipamento trata o erro, e imprime qual o IP que falhou.
            except socket.herror:
                self.mensagem2["text"] = "Endereço: {} não encontrado.".format(ip)
                print("Endereço: {} não encontrado.".format(ip))
                IPsLivres.append(ip)
                
            i += 1 # incrementa para avançar o ultimo numero.


    # Função para pingar os IPs.
    def check_ping(self, hostname):
        response = os.system("ping -n 1 " + hostname)
        # verifica se respondeu...
        if response == 0:
            pingstatus = "Network Error"
        else:
            pingstatus = "Network Active"

        return pingstatus

    # Função para salvar arquivo IPlivres no disco.
    def salva_arquivo(self):
        global IPsLivres
        f = open("C:/SysTI/IPlivres.txt", "x")
        for linhas_do_arquivo in IPsLivres:
            with open("C:/SysTI" + "/IPDisponivel_" + data_arquivo + ".txt", "a") as arquivo:
                arquivo.write("{}\n".format(linhas_do_arquivo))

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into ipsLivres (ip, data) values ('" + linhas_do_arquivo + "', '" + data_atual + "' )")

            banco.conexao.commit()
            for row in c.execute('SELECT * FROM ipsLivres'):
                print(row)
                self.textbox.insert("1.0", row)
            c.close()

            return "Usuário cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do usuário"
        

    # Funcão de fluxo do programa
    def funcao_principal(self, entrada):
        global IPsLivres
        self.textbox.insert(INSERT, "Saindo agora função princ.")
        self.entrada = entrada
        retorno_check_nslookup = self.check_nslookup(self.entrada)

        # Imprimir IPs disponíveis
        for ping in IPsLivres:
            self.pingstatus = self.check_ping(ping)
            if self.pingstatus == "Network Active":
                print(self.pingstatus, ping)
                IPsLivres.remove(ping)
            elif self.pingstatus == "Network Error":
                print("IP Disponível.",ping)
            else:
                print("Erro no ping.")

        retorno_salva_arquivo = self.salva_arquivo()


root = Tk()
Application(root)
root.title("Buscar IP Livre")
root.geometry('600x500')
root.mainloop()
