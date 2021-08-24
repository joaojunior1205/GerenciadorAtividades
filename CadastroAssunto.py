#Dev Sebastião e João Vitor 

import sqlite3
from sqlite3.dbapi2 import Error
from ConexaoBanco import Conexao

class Cadastro_Assunto:

    def insert(self, nomeAssunto):
        
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            #SQL para inserir os dados no banco de dados.
            sql = 'INSERT INTO Assunto (nomeAssunto) VALUES (?)'

            cursor.execute(sql, [nomeAssunto])
        
            conexao.commit()
            cursor.close()
            conexao.close()

            return print('Cadastrado com sucesso!')
        except:
            return 'Erro ao inserir assunto!'
        
    def selectC_assunto(self):
    
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            #Consultar todo o banco
            sql = "SELECT * FROM Assunto"
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
            resultset =  cursor.execute("SELECT * FROM Assunto WHERE IdAssunto="+ str(vlr_id)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset   

    def atualizar(self,vlr_id,nomeAssunto):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Assunto SET nomeAssunto = ? WHERE IdAssunto = (?)'
            cursor.execute(sql,(nomeAssunto,vlr_id))

            conexao.commit()
            cursor.close()
            conexao.close()
            return True
        
        except sqlite3.OperationalError as e:
            print("Erro na atualização de assunto: {}".format(e))
            return False
        
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))

    def consultar_detalhes(self, assunto):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute("SELECT * FROM Assunto WHERE nomeAssunto LIKE '%"+str(assunto)+"%'" ).fetchall()

        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset        

    