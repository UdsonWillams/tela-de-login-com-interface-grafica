import PySimpleGUI as sg
import bd


def janela_login():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Email')],
        [sg.InputText(key="loginEmail")],
        [sg.Text('Senha')],
        [sg.Input(password_char="*", key="loginSenha")],
        [sg.Button("Logar")],
        [sg.Button("Inscrever-se")]
    ]
    return sg.Window("login", layout=layout, finalize=True)


def janela_se_inscrever():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Digite seu Email')],
        [sg.InputText(key="email")],
        [sg.Text('Digite sua Senha')],
        [sg.Input(key="senha")],
        [sg.Text('Digite seu nome')],
        [sg.InputText(key="nome")],
        [sg.Text('Digite sua sobrenome')],
        [sg.Input(key="sobrenome")],
        [sg.Button("Inscreva-se")]
    ]
    return sg.Window("Inscrição", layout=layout, finalize=True)


# sg.DEFAULT_BASE64_LOADING_GIF
def janela_logado():
    sg.theme("Reddit")
    layout = [
        [sg.Image('like.gif', size=(448, 498))],
        [sg.Text("Logado com sucesso")]
    ]
    return sg.Window("Logado", layout=layout, finalize=True)


janela1, janela2, janela3 = janela_login(), None, None
emailEntrar, senhaEntrar = None, None
while True:
    janela, evento, valores = sg.read_all_windows()
    # fecha a janela caso voce feche no X
    if janela == janela1 and evento == sg.WIN_CLOSED:
        break
    if janela == janela1 and evento == "Logar":
        loginEmail = valores["loginEmail"]
        loginSenha = valores["loginSenha"]
        bd.cursor.execute("SELECT email FROM cadastros WHERE email = '" + loginEmail + "'")

        for dado in bd.cursor.fetchall():
            if dado[0] == loginEmail:
                emailEntrar = True
            else:
                emailEntrar = False

        bd.cursor.execute("SELECT senha FROM cadastros WHERE email = '" + loginEmail + "'")
        for dado in bd.cursor.fetchall():
            if dado[0] == loginSenha:
                senhaEntrar = True
            else:
                senhaEntrar = False

        if emailEntrar and senhaEntrar:
            janela1.hide
            janela3 = janela_logado()
        else:
            sg.popup("senha ou email invalidos")

    # abre a janela 2 caso voce precise se inscrever
    if janela == janela1 and evento == "Inscrever-se":
        janela2 = janela_se_inscrever()
        janela1.hide

    if janela == janela2:
        email = valores["email"]
        senha = valores["senha"]
        nome = valores["nome"]
        sobrenome = valores["sobrenome"]
        emBranco = False
        if valores["email"] != "" and valores["senha"] != "" and valores["nome"] != "" and valores["sobrenome"] != "":
            bd.cursor.execute(
                "INSERT INTO cadastros VALUES('" + nome + "', '" + sobrenome + "', '" + email + "', '" + senha + "')")
            bd.banco.commit()
            emBranco = True
        if evento == "Inscreva-se":
            if emBranco:
                sg.popup("Inscrição feita com sucesso.")
                janela2.hide()
                janela1.un_hide()
            else:
                sg.popup("Inscrição mal sucedida")
                janela2.hide()
                janela1.un_hide()
