# importar as bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database


#Criar janela de login

jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300") # tamanho da minha tela
jan.configure(background="white")
jan. resizable(width= False, height= True) # Isso barra o meu usuario de modificar o tamanho da tela
jan.attributes("-alpha", 0.9) # deixa transparente a minha aplicação
jan.iconbitmap(default="icons/LogoIcon.ico") # coloca icone na minha aplicação

#Carregandos as imagens
logo = PhotoImage(file="icons/logo.png")

# Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#Username
UserLabel = Label(RightFrame,text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry= ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

#Password
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry= ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def login():
    user = UserEntry.get()
    password = PassEntry.get()
    database.cursor.execute(
        """
        SELECT * FROM register
        WHERE (user =? AND Password = ?)
        """, (user, password)
    )
    print("login Sucessfull")
    VerifyLogin= database.cursor.fetchone()
    try:
        if(user in VerifyLogin and password in VerifyLogin):
            messagebox.showinfo(title="Login sucessful", message="Sua conta foi logada com sucesso")
    except:
        messagebox.showinfo(title="Verify your register", message="Verifique seus dados estão corretos ou confirme se está cadastrado")

#Button
LoginButton= ttk.Button(RightFrame, text="Login", width=30, command=login)
LoginButton.place(x=100, y=225)

def Register():
    #Revomendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadastro

    #Inserir NOME no register
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry= ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    #Inserir EMAIL no register
    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=65)

    def RegisterToDataBase():
        name = NomeEntry.get()
        email = EmailEntry.get()
        username = UserEntry.get()
        password = PassEntry.get()

        if(name == "" and email == "" and username == "" and password == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")
        else:
            database.cursor.execute(
                """
                INSERT INTO register(name, email, user, password) VALUES(?, ?, ?, ?)
                """,(name, email, username, password)
            )
            database.conn.commit()
            messagebox.showinfo(title="Register Info", message="Your Account Register Sucessfull")

    #Inserir BUTTON de BACK LOGIN e REGISTRAR
    Register = ttk.Button(RightFrame, text="Registar", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackLogin():
        #Removendo Widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)

        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)

        Register.place(x=5000)
        BackLoginButton.place(x=5000)
        #Trazendo de volta o widgets de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    BackLoginButton = ttk.Button(RightFrame, text="Back to login", width=20, command=BackLogin)
    BackLoginButton.place(x=125, y=260)





RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)



jan.mainloop()