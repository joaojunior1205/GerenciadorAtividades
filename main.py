#Andressa Carolina 
#Sebastião
#Joao Alves Junior 
#João Vitor 
#Maxuell Lima 

from desempenho import Desempenho
from PyQt5 import QtGui, uic, QtWidgets
from aluno import Alunos
from assunto import Assunto
from atividade import Atividade
from consulta_aluno import Consulta_Aluno
from consulta_assunto import Consulta_Assunto
from consulta_atividade import Consulta_Atividade
from desempenho import Desempenho
from CadastroDesempenho import combobox

app = QtWidgets.QApplication([])
Home = uic.loadUi("Tela/Home.ui")
Aluno = uic.loadUi("Tela/Aluno.ui")


def btCadastroAluno():
    aluno = Alunos
    aluno.telaAluno()

def btCadastroAssunto():
    assunto = Assunto
    assunto.telaAssunto()  

def btCadastroAtividade():
    atividade = Atividade
    atividade.telaAtividade()

def btConsultaAluno():
    consultaAluno = Consulta_Aluno
    consultaAluno.telaConsultaAluno()

def btConsultaAssunto():
    consultaAssunto = Consulta_Assunto
    consultaAssunto.telaConsultaAssunto()

def btConsultaAtividade():
    consultaAtividade = Consulta_Atividade
    consultaAtividade.telaConsultaAtividade()

def btCadastroDesempenho():
    desempenho = Desempenho
    desempenho.telaDesempenho()

def tabelaHome():                    
    a = combobox()
    sqldesempenho = a.situacao()
    Home.tabela.setRowCount(len(sqldesempenho))
    Home.tabela.setColumnCount(5)
    Home.header = Home.tabela.horizontalHeader()
    Home.tabela.setColumnWidth(0,80)
    Home.tabela.setColumnWidth(1,280)
    Home.tabela.setColumnWidth(2,280)
    Home.tabela.setColumnWidth(3,100)
    Home.tabela.setColumnWidth(4,345)
    for i in range(0,len(sqldesempenho)):
        for j in range(0, 5):
            Home.tabela.setItem(i,j,QtWidgets.QTableWidgetItem(str(sqldesempenho[i][j])))

tabelaHome()
Home.show()
Home.Bt_CadastroAluno.clicked.connect(btCadastroAluno)
Home.Bt_CadastroAssunto.clicked.connect(btCadastroAssunto)
Home.Bt_CadastroAtividade.clicked.connect(btCadastroAtividade)
Home.Bt_Consultar_Aluno.clicked.connect(btConsultaAluno)
Home.Bt_Consultar_Assunto.clicked.connect(btConsultaAssunto)
Home.Bt_Consultar_Atividade.clicked.connect(btConsultaAtividade)
Home.Bt_CadastroDesempenho.clicked.connect(btCadastroDesempenho)

app.exec()