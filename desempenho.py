#Dev Andressa Carolina, João Junior e Sebastião 

from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from CadastroDesempenho import combobox

class Desempenho:

    def telaDesempenho():
        
        Desempenho = uic.loadUi("Tela/Desempenho.ui")
        
        Ativ = combobox()
        sql = Ativ.comboboxAtividade()
              
        for registro in sql:
            Desempenho.comboBox.addItem(str(registro[0]))

        Aluno = combobox()
        sql = Aluno.comboboxAluno()
              
        for registro in sql:
            Desempenho.comboBox_2.addItem(str(registro[0]))
            
        def cadastroid():
            
            c = combobox()
            atividade = Desempenho.comboBox.currentText()
            sql = c.consultaAtividade(atividade)
            c.idatividade = str(sql[0][0])

            matricula = Desempenho.comboBox_2.currentText()
            sql = c.consultaAluno(matricula)
            c.idmatricula = str(sql[0][0])     
            c.conclusao = Desempenho.comboBox_3.currentText()
            c.desempenho = Desempenho.Lb_Assunto.text()

            if (Desempenho.Lb_Assunto.text()!=""):
                if c.insert(c.idatividade, c.idmatricula,c.conclusao,c.desempenho) == True:
                    limpar()
                else:
                    print("Erro no cadastro de Desempenho")
                   
            else:
                 print("Erro! Preencha todos os campos obrigatórios!")
                
                
        def limpar():
            Desempenho.Lb_Assunto.setText('')
        

        
        Desempenho.Bt_Cadastro.clicked.connect(cadastroid) 
        Desempenho.exec()
        
