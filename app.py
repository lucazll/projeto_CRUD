from tkinter import *
import services

def main():
    def on_enviar():
        nome = nome_entr.get()
        email = email_entr.get()
        senha = senha_entr.get()
        services.enviar_dados(nome, email, senha)

        # para limpar os campos
        nome_entr.delete(0, END)
        email_entr.delete(0, END)
        senha_entr.delete(0, END)


        
    # Criando uma janela
    janela = Tk()
    janela.geometry('600x500')
    janela.title('Sistema de gerenciamento de Usuarios')

    # Criando a label com o título
    titulo = Label(janela, text='CRUD_01 LUCAS', font=('Agency FB', 30))

    # Distanciamento do titulo para a janela
    titulo.pack(pady= 45)

    # componentes de entradas

    # nome
    nome = Label(janela, text= 'Nome: ')
    nome.place(x=40, y=120)

    global nomeentr
    nome_entr = Entry(janela, width= 30)
    nome_entr.place(x=80, y=120)

    # email
    email = Label(janela, text= 'Email: ')
    email.place(x=40, y=170)

    global email_entr
    email_entr = Entry(janela, width= 30)
    email_entr.place(x=80, y=170)

    # senha
    senha = Label(janela, text='Senha: ')
    senha.place(x=40, y=220)

    # comando show esconde a senha
    global senha_entr
    senha_entr = Entry(janela, show='*', width= 30)
    senha_entr.place(x=80, y=220)

   
    # Fazer um butão: 'Button'
    cadastrar = Button(janela, text='Cadastrar', width=15, command=on_enviar)
    cadastrar.place(x=450, y=300)


    listar = Button(janela, text='Listar Usuarios', width= 15)
    listar.place(x=450, y=350)


    # Criando o Frame
    janela.mainloop()


# Rodando a função principal
if __name__ == '__main__':
    main()