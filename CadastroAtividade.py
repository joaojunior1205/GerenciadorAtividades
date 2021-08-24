#Dev Andressa Carolina e Maxuell Lima 

import sqlite3
from sqlite3.dbapi2 import Error
from ConexaoBanco import Conexao

class Cadastro_Atividade:

    def insert(self,idassunto, descricao, nomeAtividade, periodo):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()
            sql = 'INSERT INTO Atividade (Id_Assunto,descricao,nomeAtividade,periodo) VALUES (?,?,?,?)'
            cursor.execute(sql,[idassunto,descricao,nomeAtividade,periodo])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Atividade: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    def consultaComboBox(self):

        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            sql = "SELECT * FROM Assunto"

            result = cursor.execute(sql).fetchall()

            cursor.execute(sql)
            cursor.close()

            return result
        except:
            return print("Ops! Ocorreu um erro na consulta dos regitros!")

    
    
    def consultaComboBox(self):

        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            sql = "SELECT Assunto.nomeAssunto FROM Assunto"
            
            result = cursor.execute(sql).fetchall ()

            cursor.execute(sql)
            conexao.close()

            return result
    
        except:
            return print("Ops! Ocorreu um erro na consulta dos regitros!")

    def consultaAssunto(self,assunto):

        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT e.IdAssunto, e.nomeAssunto 
                FROM Assunto as e 
                WHERE nomeAssunto = ?"""

        
        try:
            resultset =  cursor.execute(sql,(assunto,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset        
    
    def selectC_atividade(self):
        
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            #Consultar todo o banco
            sql = "SELECT Atividade.IdAtividade,Assunto.nomeAssunto,Atividade.nomeAtividade,Atividade.descricao,Atividade.periodo FROM Atividade INNER JOIN Assunto WHERE Id_Assunto = IdAssunto"
            resultado = cursor.execute(sql).fetchall()

            cursor.execute(sql)
            conexao.close()

            return resultado
        except:
            return print("Ops! Ocorreu um erro na consulta dos regitros!")
        
    def pegaid(self,vlr_id):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute("SELECT * FROM Atividade WHERE IdAtividade="+ str(vlr_id)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset   

    def atualizar(self,vlr_id,nomeAtividade, nomeDescricao, nomePeriodo):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Atividade SET descricao = ?, nomeAtividade = ?, periodo = ? WHERE IdAtividade = (?)'
            cursor.execute(sql,(nomeDescricao, nomeAtividade, nomePeriodo,vlr_id))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        
        except sqlite3.OperationalError as e:
            print("Erro na atualização de Atividades: {}".format(e))
            return False
        
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))

    def consultar_detalhes(self, atividade):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute("SELECT * FROM Atividade WHERE nomeAtividade LIKE '%"+str(atividade)+"%'" ).fetchall()

        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset        


