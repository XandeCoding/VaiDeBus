import sqlite3

connection = sqlite3.connect ("CompOnibus.db")
cursor = connection.cursor ()

sqlPessoas = """
CREATE TABLE pessoas	(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						cpf TEXT UNIQUE NOT NULL,
						nome TEXT NOT NULL,
						sexo TEXT NOT NULL,
						usuario TEXT UNIQUE NOT NULL,
						senha TEXT NOT NULL)"""

sqlMotorista = """
CREATE TABLE motoristas	(numMotorista INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						cpfMotorista TEXT UNIQUE NOT NULL)"""

sqlClientes = """
CREATE TABLE clientes 	(numCliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						cpfCliente TEXT UNIQUE NOT NULL,
						codViagem INTEGER)"""

#Passageiros parametro derivado, ao adicionar viagem que usa onibus do bd,
#o atributo passageiros e incrementado
sqlOnibus = """
CREATE TABLE onibus 	(numOnibus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						placa TEXT UNIQUE NOT NULL,
						ano INTEGER NOT NULL,
						passageiros INTEGER NOT NULL,
						modelo TEXT NOT NULL,
						qtdPoltronas INTEGER NOT NULL)"""

sqlViagens = """
CREATE TABLE viagens 	(numViagem INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						onibusPlaca TEXT NOT NULL,
						motoristaViagem TEXT NOT NULL,
						diaViagem TEXT NOT NULL,
						horario TEXT NOT NULL,
						cidadeOrigem TEXT NOT NULL,
						cidadeDestino TEXT NOT NULL)"""

sqlCompanhia = """
CREATE TABLE companhia 	(numCompanhia INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						cnpj TEXT UNIQUE NOT NULL,
						usuario TEXT UNIQUE NOT NULL,
						senha TEXT NOT NULL)"""

cursor.execute (sqlPessoas)
cursor.execute (sqlMotorista)
cursor.execute (sqlClientes)
cursor.execute (sqlOnibus)
cursor.execute (sqlViagens)
cursor.execute (sqlCompanhia)

connection.commit ()
connection.close ()