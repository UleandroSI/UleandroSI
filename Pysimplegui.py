__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

import PySimpleGUI as sg
import socket
import os
from datetime import date
from C_banco_IP import Banco


class Application:
    def __init__(self):
        # Layout
        sg.theme('DarkAmber')   # Add a little color to your windows
        # All the stuff inside your window. This is the PSG magic code compactor...
        layout = [ [sg.Text('Este programa varre o range de IP escolhilho apartir de 10 até 245.')],
                [sg.Text('Digite o range para o numero de IP. Ex.: 3 = 192.168.3.'), sg.InputText(size=(2,1), key='range')],
                [sg.Button('OK'), sg.Button('Cancel')]
                ]

        # Create the Window
        self.window = sg.Window('Busca IPs Livres', layout)


    def Iniciar(self):
        # Event Loop to process "events"
        while True:
            # Extrat data
            self.button, self.values = self.window.Read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            
            entrada = self.values['range']
            print(f'Entrada: {entrada}')

#self.window.close()
tela = Application()
tela.Iniciar()