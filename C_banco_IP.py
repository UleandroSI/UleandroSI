import sqlite3

class Banco():
    
    def __init__(self):
        self.conexao = sqlite3.connect('u_scan_IP.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists ipsLivres (
                    idips integer primary key autoincrement ,
                    ip text,
                    data text)""")
        self.conexao.commit()
        c.close()
        