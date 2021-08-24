#Dev João Alvez

from PyQt5 import uic
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from CadastroAluno import Cadastro_Aluno

class Consulta_Aluno:
    
    def telaConsultaAluno():
        Consulta = uic.loadUi("Tela/Consulta_Aluno.ui")

         # Remover linha   
        def removerlinha():
            while(Consulta.tabela.rowCount() > 0):
                Consulta.tabela.removeRow(0)

        
        def lista_dados():
               
            a = Cadastro_Aluno()
            sqlaluno = a.select()
            Consulta.tabela.setRowCount(len(sqlaluno))
            Consulta.tabela.setColumnCount(7)
            Consulta.header = Consulta.tabela.horizontalHeader()
            Consulta.tabela.setColumnWidth(0,90)
            Consulta.tabela.setColumnWidth(1,250)
            Consulta.tabela.setColumnWidth(2,250)
            Consulta.tabela.setColumnWidth(3,250)
            Consulta.tabela.setColumnWidth(4,125) 
            Consulta.tabela.setColumnWidth(5,250)
            Consulta.tabela.setColumnWidth(6,450) 
            for i in range(0,len(sqlaluno)):
                for j in range(0, 7):
                 Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(sqlaluno[i][j])))
            
           
        def Mostra_Dados():
            # Pega o id na tabela 
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            #Verifica o id
            a = Cadastro_Aluno()
            reg = a.pegaid(vlr_id)
            Consulta.txt_aluno.setText(str(reg[0][1]))
            Consulta.txt_pai.setText(str(reg[0][2]))
            Consulta.txt_mae.setText(str(reg[0][3]))
            Consulta.txt_fone.setText(str(reg[0][4]))
            Consulta.txt_email.setText(str(reg[0][5]))
            Consulta.txt_end.setText(str(reg[0][6]))
            Consulta.lab_infor.setText('')

        def alterar():
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            aluno = Consulta.txt_aluno.text()
            pai_aluno = Consulta.txt_pai.text()
            mae_aluno = Consulta.txt_mae.text() 
            fone = Consulta.txt_fone.text()
            email_aluno = Consulta.txt_email.text()
            end = Consulta.txt_end.text()
                       
            # Atualizar os registros no banco
            a = Cadastro_Aluno()
            if  a.atualizar(vlr_id,aluno,pai_aluno,mae_aluno,fone,email_aluno,end) == True:
                #Mostrar mensagem para usuário
                lista_dados()
                Consulta.lab_infor.setText('Atualização executado com sucesso!')
            
                #Limpar os campos texto
                limpar()

        def consultar():
            

            if Consulta.txt_buscar == "":
                print('Informe o que deseja consultar !')
                Consulta.txt_buscar.setFocus()
            else:
                removerlinha()
                
                a = Cadastro_Aluno()
                aluna = Consulta.txt_buscar.text()
             
                alunos = a.consultar_detalhes(aluna)
                Consulta.tabela .setRowCount(len(alunos))
                Consulta.tabela.setColumnCount(7)
                Consulta.tabela.header = Consulta.tabela.horizontalHeader()
                
                     
                for i in range(0,len(alunos)):
                    for j in range(0, 7):
                        Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(alunos[i][j]))) 
                Consulta.txt_buscar.setText("")
              
                
       
        def limpar():
            Consulta.txt_aluno.setText('')
            Consulta.txt_pai.setText('')
            Consulta.txt_mae.setText('')
            Consulta.txt_fone.setText('')
            Consulta.txt_email.setText('')
            Consulta.txt_end.setText('')
           
        
        removerlinha()
        lista_dados() 
        Consulta.tabela.clicked.connect(Mostra_Dados) 
        Consulta.Bt_editar.clicked.connect(alterar)  
        Consulta.bt_buscar.clicked.connect(consultar)
        Consulta.exec()