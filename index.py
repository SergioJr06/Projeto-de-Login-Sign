#Importar as Bibliotecas:
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar a nossa janela:
janela = Tk() #sinalizar que esta variavel é uma janela
janela.title("DP Systems - Acess Panel") #titulo da janela
janela.geometry("600x300") #tamanho da janela
janela.configure(background="white") #cor de fundo da janela
janela.resizable(width=False, height=False) #dizer que ela não podera ser redimensionada (não é responsivel)
janela.attributes("-alpha", 0.9) #Transparencia da janela
janela.iconbitmap(default="icons/LogoIcon.ico") #Icone da Janela

#----------CARREGANDO IMAGENS----------#
logo = PhotoImage(file="icons/logo.png")

#----------WIDGETS-----------#
#COLUNA QUE IRÁ APARECER NO LADO ESQUERDO DA JANELA, cor : Azul escuro:
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief = "raise")
LeftFrame.pack(side=LEFT) #APARECER A COLUNA NO LADO ESQUERDO

#COLUNA DO LADO DIREITO (com pequena separação de 5 pixels de espaço):
RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief = "raise")
RightFrame.pack(side=RIGHT)

#POSICIONAMEMTO DA IMAGEM LOGO:
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#APARECER O TEXTO USUÁRIO NA TELA DIREITA:
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=10, y=100) 

#ENTRADA DE DADOS DO USUÁRIO:
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=160, y=114)

#APARECER O TEXTO DE SENHA:
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=10, y=145) 

#ENTRADA DE DADOS DA SENHA:
PassEntry = ttk.Entry(RightFrame, width=32, show="*")
PassEntry.place(x=150, y=159)

def Login():
    User = UserEntry.get().strip()  # Remove espaços em branco no início e no final
    Pass = PassEntry.get().strip()  # Remove espaços em branco no início e no final

    if not User or not Pass:
        messagebox.showinfo(title="Login Info", message="Both username and password are required.")
        return

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Pasword = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title="Login Info", message="Login Sucessfull, Welcome!")
    else:
        messagebox.showinfo(title="Login Info", message="User isn't found, try again!")

#BOTOES Login e Sign:
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y= 225)


#REMOVENDO WIDGETS DE LOGIN:
def Sign():
    LoginButton.place(x=23452361)
    SignButton.place(x=5000)
    
    #INSERINDO WIDGETS DE CADASTRO:
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=10, y=5)
    NomeEntry = Entry(RightFrame, width=39)
    NomeEntry.place(x=110, y=20)    
    
    EmailLabel = Label(RightFrame, text="Email: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=10, y=55)
    EmailEntry = Entry(RightFrame, width=41)
    EmailEntry.place(x=95, y=68)

#COMANDO PARA RECEBER OS DADOS DE REGISTER (NOME, EMAIL, USER, PASS):
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if(Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Empty Entry")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Pasword) VALUES( ?, ?, ?, ?)
            """, (Name, Email, User, Pass)) #INSERIR OS DADOS NA TABELA
            DataBaser.conn.commit() #SALVAR AS ALTERAÇÕES FEITAS
            messagebox.showinfo(title="Register Info", message="Register Sucessfull") #CAIXA DE AVISO DE SUCESSO
            
    #BOTOES DE REGISTRAR E VOLTAR
    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)
    
    def BackToLogin():
        #REMOVENDO WIDGETS DE CADASTRO
        NomeLabel.place(x=450453045)
        NomeEntry.place(x=383893494)
        EmailLabel.place(x=23942385)
        EmailEntry.place(x=34834923)
        Register.place(x=8534983944)
        Back.place(x=93493942349933)
        
        #TRAZENDO DE VOLTA OS WIDGETS
        LoginButton.place(x=100)
        SignButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)  
    Back.place(x=125, y=260)     
    
SignButton = ttk.Button(RightFrame, text="Sign", width=20, command=Sign)
SignButton.place(x=125, y= 260)

janela.mainloop()
