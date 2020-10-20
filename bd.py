import sqlite3


banco = sqlite3.connect("cadastros.db")

cursor = banco.cursor()

# Cria o Banco de dados
try:
    cursor.execute("CREATE TABLE cadastros (nome text, sobrenome text, email text, senha text)")
    banco.commit()
except sqlite3.OperationalError:
    print("Banco de Dados JA CRIADO")
