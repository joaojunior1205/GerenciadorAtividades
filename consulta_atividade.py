#Dev Andressa Carolina e Maxuell Lima 

from PyQt5 import uic
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from CadastroAtividade import Cadastro_Atividade

class Consulta_Atividade:
    
    def telaConsultaAtividade():
        Consulta = uic.loadUi("Tela/Consulta_Atividade.ui")

        # Remover linha   
        def removerlinha():
            while(Consulta.tabela.rowCount() > 0):
                Consulta.tabela.removeRow(0)


        def lista_dados():
                            
            # Mostrar os dados.   
            a = Cadastro_Atividade()
            sqlatividade = a.selectC_atividade()
            Consulta.tabela.setRowCount(len(sqlatividade))
            Consulta.tabela.setColumnCount(5)
            Consulta.header = Consulta.tabela.horizontalHeader()
            Consulta.tabela.setColumnWidth(0,80)
            Consulta.tabela.setColumnWidth(1,100)
            Consulta.tabela.setColumnWidth(2,110)
            Consulta.tabela.setColumnWidth(3,110)
            Consulta.tabela.setColumnWidth(4,110)
            for i in range(0,len(sqlatividade)):
                for j in range(0, 5):
                    Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(sqlatividade[i][j])))

        def Mostra_Dados():
                # Pega o id na tabela 
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            #Verifica o id
            a = Cadastro_Atividade()
            reg = a.pegaid(vlr_id)
            print(a)
            Consulta.txt_atividade.setText(str(reg[0][3]))
            Consulta.txt_descricao.setText(str(reg[0][2]))
            Consulta.txt_periodo.setText(str(reg[0][4]))
            
        def alterar():
            vlr_id = Consulta.tabela.item(Consulta.tabela.currentRow(),0).text()
            nomeAtividade = Consulta.txt_atividade.text()
            nomeDescricao = Consulta.txt_descricao.text()
            nomePeriodo = Consulta.txt_periodo.text()
                       
            # Atualizar os registros no banco
            a = Cadastro_Atividade()
            if  a.atualizar(vlr_id,nomeAtividade,nomeDescricao,nomePeriodo) == True:
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
                
                a = Cadastro_Atividade()
                atividade = Consulta.txt_buscar.text()
             
                alunos = a.consultar_detalhes(atividade)
                Consulta.tabela .setRowCount(len(alunos))
                Consulta.tabela.setColumnCount(5)
                Consulta.tabela.header = Consulta.tabela.horizontalHeader()
                
                     
                for i in range(0,len(alunos)):
                    for j in range(0, 5):
                        Consulta.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(alunos[i][j]))) 
                Consulta.txt_buscar.setText("")
              

         
        def limpar():
            Consulta.txt_atividade.setText('')
            Consulta.txt_descricao.setText('')
            Consulta.txt_periodo.setText('')

        Consulta.tabela.clicked.connect(Mostra_Dados) 
        Consulta.Bt_Consultar_Atividade_2.clicked.connect(alterar) 
        Consulta.bt_buscar.clicked.connect(consultar)
        removerlinha() 
        lista_dados()
        Consulta.exec()
    
        

    
