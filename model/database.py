from curses import noecho
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv
 
class Database:
    def __init__(self):
            load_dotenv()
            self.host = getenv('DB_HOST')
            self.username = getenv('DB_USERNAME')
            self.password = getenv('DB_PSWD')
            self.database = getenv('DB_NAME')
            self.connection = None #Inicialização da conexão
            self.cursor = None #Inicialização do cursor

    def conectar(self):
          """Estabelece uma conexão com o banco ce dados"""
          try:
                self.connection = mysql.connector.connect(
                      host = self.host,
                      database = self.database,
                )