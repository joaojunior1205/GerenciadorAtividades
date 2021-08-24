#Dev Sebastião e João Vitor 

from PyQt5 import uic
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from CadastroAssunto import Cadastro_Assunto

class Consulta_Assunto:
    
    def telaConsultaAssunto():
        Consulta = uic.loadUi("Tela/Consulta_Assunto.ui")
        
         # Remover linha   
        def removerlinha():
            while(Consulta.tabela.rowCount() > 0):
                Consulta.tabela.removeRow(0)
        
        def lista_dados():
            
            # Mostrar os dados.   
            a = Cadastro_Assunto()
            sqlassunto = a.selectC_assunto()
            Consulta.tabela.setRowCount(len(sqlassunto))
            Consulta.tabela.setColumnCount(2)
            Consulta.header = Consulta.tabela.horizontalHeader()
            Consulta.tabela.setColumnWidth(0,90)
            Consulta.tabela.setColumnWidth(1,350)
            for i in range(0,len(sqlassunto)):
                for j in range(0, 2):
                 Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(sqlassunto[i][j])))

        def Mostra_Dados():
                # Pega o id na tabela 
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            #Verifica o id
            a = Cadastro_Assunto()
            reg = a.pegaid(vlr_id)
            Consulta.lineEdit_8.setText(str(reg[0][1]))
            
        def alterar():
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            nomeAssunto = Consulta.lineEdit_8.text()
                       
            # Atualizar os registros no banco
            a = Cadastro_Assunto()
            if  a.atualizar(vlr_id,nomeAssunto) == True:
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
                
                a = Cadastro_Assunto()
                aluna = Consulta.txt_buscar.text()
             
                alunos = a.consultar_detalhes(aluna)
                Consulta.tabela .setRowCount(len(alunos))
                Consulta.tabela.setColumnCount(2)
                Consulta.tabela.header = Consulta.tabela.horizontalHeader()
                
                     
                for i in range(0,len(alunos)):
                    for j in range(0, 2):
                        Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(alunos[i][j]))) 
            Consulta.txt_buscar.setText("")
                      
            
        def limpar():
            Consulta.lineEdit_8.setText('')

        Consulta.tabela.clicked.connect(Mostra_Dados) 
        Consulta.Bt_Consultar_Atividade_2.clicked.connect(alterar) 
        Consulta.bt_buscar.clicked.connect(consultar)
        removerlinha() 
        lista_dados()
        Consulta.exec()