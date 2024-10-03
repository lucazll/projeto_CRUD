from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email ,senha)

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com Sucesso!')

        cursor = conn.cursor()

        sql = 'INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)'
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()

    else:
        print('Falha ao conectar ao banco de dados!')

def listar_usuario():
    if conn.is_connected():
        print('Banco de dados conectado com Sucesso!')

        cursor = conn.cursor()

        cursor.execute('select id, nome, email from usuario;')

        usuarios = cursor.fetchall()
        cursor.close() 
        conn.close()
        return usuarios
       

    else:
        print('Falha ao conectar com o banco de ddados!')

def remover_usuario(email):
    if conn.is_connected():
        print('Banco de dados conectado com Sucesso!')
        
        cursor = conn.cursor()
        sql_select = 'select id, nome, email from usuario where email=%s;'
        cursor.execute(sql_select,(email,))
        usuario = cursor.fetchone()
        if usuario:
            print('usuario encontrado!')
            sql_delete = 'DELETE FROM usuario WHERE email=%s;'
            cursor.execute(sql_delete, (email,))
            print(f'usuario {usuario[1]} deletado com sucesso!')
            conn.commit()
            cursor.close()
            conn.close()

        else:
            print('Usuario não encontrado!')