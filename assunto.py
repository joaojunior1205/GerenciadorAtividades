#Dev Sebastião e João Vitor 

from PyQt5 import uic
from CadastroAssunto import Cadastro_Assunto

class Assunto:
    
    def telaAssunto():
        Assunto = uic.loadUi("Tela/Assunto.ui")

        Assunto.Lb_Assunto.setPlaceholderText(' Nome do assunto')

        def cadastrar():
            c = Cadastro_Assunto()
            try:
                c.nomeAssunto = Assunto.Lb_Assunto.text()

                if (Assunto.Lb_Assunto.text() != ""):
                    c.insert(c.nomeAssunto)
                    limpar()
                    return 'Cadastrado com sucesso!'
                    
                else:
                    print('Erro! Preencha todos os campos obrigatórios')

            except:
                print('Erro no cadastro do assunto! ')  

        def limpar():
            Assunto.Lb_Assunto.setText('')

        Assunto.Bt_Cadastro.clicked.connect(cadastrar)
        Assunto.exec()