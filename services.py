from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email ,senha)

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com Sucesso!')

        cursor = conn.cursor()

        sql = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()

    else:
        print('Falha ao conectar ao banco de dados!')