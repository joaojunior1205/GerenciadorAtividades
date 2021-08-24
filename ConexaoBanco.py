import sqlite3

class Conexao():
    
    def conectar(self):
        conexao = None #Inserindo um objeto nulo
        db_path = 'GestaoAluno.db' #Nome do banco de dados

        try:
            conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar ao banco de dados {db_path}.")

        return conexao

    #Criando tabela de alunos
    def createTableAluno(self, conexao, cursor):
        sql = '''CREATE TABLE IF NOT EXISTS Aluno(
            matricula INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            nomeMae TEXT, 
            nomePai TEXT, 
            telefone TEXT NOT NULL, 
            email TEXT NOT NULL, 
            endereco TEXT NOT NULL
            );'''
        cursor.execute(sql)
        conexao.commit()

    #Criando tabela de assunto
    def createTableAssunto(self, conexao, cursor):
        sql = '''CREATE TABLE IF NOT EXISTS Assunto(
            IdAssunto INTEGER PRIMARY KEY AUTOINCREMENT, 
            nomeAssunto VARCHAR NOT NULL
            );'''
        cursor.execute(sql)
        conexao.commit()

    #Criando tabela de atividades
    def createTableAtividade(self, conexao, cursor):
        sql = '''CREATE TABLE IF NOT EXISTS Atividade(
            IdAtividade INTEGER PRIMARY KEY AUTOINCREMENT, 
            Id_Assunto INTEGER NOT NULL, 
            descricao TEXT NOT NULL, 
            nomeAtividade TEXT NOT NULL, 
            periodo TEXT NOT NULL,
            FOREIGN KEY(Id_Assunto) REFERENCES IdAssunto(Assunto)
            );'''
        cursor.execute(sql)
        conexao.commit()

    #Criando tabela de atividade
    def createTableSituacao(self, conexao, cursor):
        sql = '''CREATE TABLE IF NOT EXISTS Situacao(
            IdSituacao INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_matricula INTEGER NOT NULL,
            Id_Atividade INTEGER NOT NULL,
            conclusao TEXT NOT NULL,
            desempenho TEXT NOT NULL,
            FOREIGN KEY(Id_matricula) REFERENCES matricula(Aluno),
            FOREIGN KEY(Id_Atividade) REFERENCES IdAtividade(Atividade)
            );'''
        cursor.execute(sql)
        conexao.commit()


    #Conexçao
    def  createTables(self):
        #Criando a conexão
        conexao = self.conectar()
        #Criando o cursor 
        cursor = conexao.cursor()

        #Passando a conexão e cursor para as funções de criar tabelas.
        self.createTableAluno(conexao, cursor)
        self.createTableAssunto(conexao, cursor)
        self.createTableAtividade(conexao, cursor)
        self.createTableSituacao(conexao, cursor)
    

        