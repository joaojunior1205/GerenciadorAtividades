#Dev Jão Junior 

from PyQt5 import uic
from CadastroAluno import Cadastro_Aluno

class Alunos:
    
    def telaAluno(): 
        Aluno = uic.loadUi("Tela/Aluno.ui")

        Aluno.nomeAluno.setPlaceholderText(' Nome do aluno')
        Aluno.nomePai.setPlaceholderText(' Nome do Pai')
        Aluno.nomeMae.setPlaceholderText(' Nome da Mãe')
        Aluno.telefoneAluno.setPlaceholderText(' (00)9 2345-1234')
        Aluno.emailAluno.setPlaceholderText(' E-mail')
        Aluno.enderecoAluno.setPlaceholderText(' Endereço')

        def cadastrar():
            c = Cadastro_Aluno()
            try:
                c.nome = Aluno.nomeAluno.text()
                c.nomePai = Aluno.nomePai.text()
                c.nomeMae = Aluno.nomeMae.text()
                c.telefone = Aluno.telefoneAluno.text()
                c.email = Aluno.emailAluno.text()
                c.endereco = Aluno.enderecoAluno.text()

                if (Aluno.nomeAluno.text() != "" and Aluno.telefoneAluno.text() != "" and Aluno.emailAluno.text() != "" and Aluno.enderecoAluno.text() != ""):
                    c.insert(c.nome, c.nomeMae, c.nomePai, c.telefone, c.email, c.endereco)
                    limpar()
                    return 'Cadastrado com sucesso!'
                else:
                    print('Preencha todos os campos obrigatórios!')
        
            except:
                return 'Erro ao gravar contato!'

        def limpar():
            Aluno.nomeAluno.setText('')
            Aluno.nomePai.setText('')
            Aluno.nomeMae.setText('')
            Aluno.telefoneAluno.setText('')
            Aluno.emailAluno.setText('')
            Aluno.enderecoAluno.setText('')

        Aluno.Bt_Cadastrar.clicked.connect(cadastrar)
        Aluno.Bt_Limpar.clicked.connect(limpar)

        Aluno.exec()

    
    
        