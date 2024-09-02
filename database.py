#Criação do banco de dados (SQLite)

import sqlite3

conn =sqlite3.connect('Users.db')

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS register(
        id_users INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        user TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    """
)

print("Conectado ao Banco de dados")