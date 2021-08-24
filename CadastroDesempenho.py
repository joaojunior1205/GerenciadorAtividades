#Dev Andressa Carolina, João Junior e Sebastião 
from sqlite3.dbapi2 import Error
from PyQt5 import uic,QtWidgets
from ConexaoBanco import Conexao
import sqlite3

class combobox:
    
    def comboboxAtividade(self):
        
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            try:    
                sql = "SELECT Atividade.nomeAtividade FROM Atividade"
                
                result = cursor.execute(sql).fetchall ()

                cursor.execute(sql)
                conexao.close()

                return result
        
            except:
                return print("Ops! Ocorreu um erro na consulta dos regitros!")
            
    def comboboxAluno(self):
        
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            try:    
                sql = "SELECT Aluno.nome FROM Aluno"
                
                result = cursor.execute(sql).fetchall ()

                cursor.execute(sql)
                conexao.close()

                return result
        
            except:
                return print("Ops! Ocorreu um erro na consulta dos regitros!")
            
    def consultaAtividade(self,atividade):
    
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT e.IdAtividade, e.nomeAtividade
                FROM Atividade as e 
                WHERE nomeAtividade = ?"""

        
        try:
            resultset =  cursor.execute(sql,(atividade,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset      
      
    def consultaAluno(self,aluno):
        
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT e.matricula, e.nome
                FROM Aluno as e 
                WHERE nome = ?"""

        
        try:
            resultset =  cursor.execute(sql,(aluno,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset 
    
           
    def insert(self,idatividade, idmatricula, conclusao, desempenho):
        
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()
            sql = 'INSERT INTO Situacao (Id_Atividade,Id_matricula,conclusao,desempenho) VALUES (?,?,?,?)'
            cursor.execute(sql,[idatividade, idmatricula, conclusao, desempenho])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Desempenho: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False
        
    def situacao(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            #Consultar todo o banco
            sql = "SELECT Situacao.IdSituacao,Atividade.nomeAtividade,Aluno.nome,Situacao.conclusao,Situacao.desempenho FROM Situacao INNER JOIN Atividade,Aluno ON Id_Atividade = IdAtividade AND Id_matricula = matricula"
            resultado = cursor.execute(sql).fetchall()

            cursor.execute(sql)
            conexao.close()

            return resultado
        except:
            return print("Ops! Ocorreu um erro na consulta dos regitros!")