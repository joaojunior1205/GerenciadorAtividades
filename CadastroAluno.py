#Dev Jão Junior 

import sqlite3
from sqlite3.dbapi2 import Error
from ConexaoBanco import Conexao

class Cadastro_Aluno:


    # SQL para cadastro de aluno
    def insert(self, nome, nomeMae, nomePai, telefone, email, endereco): 
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            #SQL para inserir os dados no banco de dados.
            sql = 'INSERT INTO Aluno (nome, nomePai, nomeMae, telefone, email, endereco) VALUES (?, ?, ?, ? ,? ,?)'

            cursor.execute(sql, (nome, nomePai, nomeMae, telefone, email, endereco))
        
            conexao.commit()
            cursor.close()
            conexao.close()

            return print("Cadastrado com sucesso!")
        except:
            return print("Erro ao inserir aluno!")


    #SQL para consulta de alunos
    def select(self):

        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM Aluno').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

    def pegaid(self,vlr_id):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute("SELECT * FROM Aluno WHERE matricula="+ str(vlr_id)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset   

    def atualizar(self,vlr_id,aluno,pai_aluno,mae_aluno,fone,email_aluno,end ):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE Aluno SET nome = ?, nomePai = ?, nomeMae = ?, telefone = ?, email = ?, endereco = ? WHERE matricula = (?)'
            cursor.execute(sql,(aluno,pai_aluno,mae_aluno,fone,email_aluno,end,vlr_id))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        
        except sqlite3.OperationalError as e:
            print("Erro na atualização de alunos: {}".format(e))
            return False
        
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))

    def consultar_detalhes(self, aluna):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute("SELECT * FROM Aluno WHERE nome LIKE '%"+str(aluna)+"%'" ).fetchall()

        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset
