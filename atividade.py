#Dev Andressa Carolina e Maxuell Lima 

from PyQt5 import uic, QtWidgets
from CadastroAtividade import Cadastro_Atividade
from CadastroAluno import Cadastro_Aluno 

class Atividade:
    
    def telaAtividade():
        Atividade = uic.loadUi("Tela/Atividade.ui")

        Atividade.nomeAtividade.setPlaceholderText(' Nome da atividade')
        Atividade.periodo.setPlaceholderText(' Período da atividade')
        Atividade.descricao.setPlaceholderText(' Desrição da atividade')

        Ativ = Cadastro_Atividade()
        sql = Ativ.consultaComboBox()
              
        for registro in sql:
            Atividade.Box_Assunto.addItem(str(registro[0]))
        
        def cadastrar():
            c = Cadastro_Atividade()
            # Pega o assunto que o usuário escolheu no combobox e coloca na variavel
            assunto = Atividade.Box_Assunto.currentText()
            # Pesquisa no banco de dados o assunto que o usuário escolheu
            sql = c.consultaAssunto(assunto)
            # Coloca o id do assunto na variavel
            c.idassunto = str(sql[0][0])
          

            # Consulta tabela aluno 
            al = Cadastro_Aluno()
            # Coloca todas as informações da tabela aluno na variavel
            aluno = al.select()
          
            
            
            try:
                c.descricao = Atividade.descricao.text()
                c.nomeAtividade = Atividade.nomeAtividade.text()
                c.periodo = Atividade.periodo.text()

                if (Atividade.descricao.text()!="" and Atividade.nomeAtividade.text()!="" and Atividade.periodo.text()!=""):

                    c.insert(c.idassunto, c.descricao,c.nomeAtividade,c.periodo)
                    limpar()
                else:
                    print("Erro! Preencha todos os campos obrigatórios!")
            except:
                return print('Erro no cadastro de atividade')

        def limpar():
            Atividade.descricao.setText('')
            Atividade.nomeAtividade.setText('')
            Atividade.periodo.setText('')
        
        Atividade.Bt_Cadastro.clicked.connect(cadastrar)
        Atividade.exec()