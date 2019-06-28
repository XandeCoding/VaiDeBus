import sqlite3

def crudSqlite (function):
	#print (function)
	def decorator (*args):
		connection = sqlite3.connect ("CompOnibus.db")
		cursor = connection.cursor ()
		command = function (*args)
		cursor.execute (command)
		connection.commit ()
		connection.close ()
	return (decorator)









"""
Implementacao das funcoes de insercoes referentes a cada tabela da bd
"""
@crudSqlite
def dbInsertPessoa (cpf, nome, sexo, usuario, senha):
	return """
	INSERT INTO pessoas (cpf, nome, sexo, usuario, senha)
	VALUES ("{}", "{}", "{}", "{}", "{}")
	""".format (cpf,nome, sexo, usuario, senha)

@crudSqlite
def dbInsertMotorista (cpf, nome, sexo, usuario, senha):
	dbInsertPessoa (cpf, nome, sexo, usuario, senha)
	return """
	INSERT INTO motoristas (cpfMotorista)
	VALUES ("{}")
	""".format (cpf)

@crudSqlite
def dbInsertCliente (cpf, nome, sexo, usuario, senha):
	dbInsertPessoa (cpf, nome, sexo, usuario, senha)
	return """
	INSERT INTO clientes (cpfCliente)
	VALUES ("{}")
	""".format (cpf)

@crudSqlite
def dbInsertOnibus (placa, ano, passageiros, modelo, qtdPoltronas):
	return """
	INSERT INTO onibus (placa, ano, passageiros, modelo, qtdPoltronas)
	VALUES ("{}", "{}", "{}", "{}", "{}")
	""".format (placa, ano, passageiros, modelo, qtdPoltronas)

@crudSqlite
def dbInsertCompanhia (cnpj, usuario, senha):
	return """
	INSERT INTO companhia (cnpj, usuario, senha)
	VALUES ("{}", "{}", "{}")
	""".format (cnpj, usuario, senha)

@crudSqlite
def dbInsertViagem (onibusPlaca, motoristaViagem, diaViagem,
					horario, cidadeOrigem, cidadeDestino):
	return """
	INSERT INTO viagens (onibusPlaca, motoristaViagem, diaViagem,
						horario, cidadeOrigem, cidadeDestino)
	VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
	""".format (onibusPlaca, motoristaViagem, diaViagem, horario,
		cidadeOrigem, cidadeDestino)











#Implementacao das funcoes de selecao referentes a cada tabela e casos especificos da bd 
def dbSelectPessoa (data, field):
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT id, nome, usuario
	FROM pessoas
	WHERE {} = {}""".format (field, data)

	cursor.execute (command)
	data = cur.fetchall ()
	connection.close ()
	return data


def dbSelectAllNomeMotoristas ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT nome 
	FROM pessoas JOIN motoristas on cpf = cpfMotorista"""

	cursor.execute (command)
	data = cursor.fetchall ()
	connection.close ()
	return data

def dbSelectAllOnibus ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT placa, ano, passageiros, modelo, qtdPoltronas, numOnibus
	FROM onibus"""

	cursor.execute (command)
	data = cursor.fetchall ()
	connection.close ()
	return data

def dbSelectAllMotoristas ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT nome, cpf
	FROM pessoas JOIN motoristas on cpf = cpfMotorista"""

	cursor.execute (command)
	data = cursor.fetchall ()
	connection.close ()
	return data

def dbSelectMotorista (numMotorista):
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT id, cpf, nome, sexo, usuario, senha 
	FROM motoristas, pessoas
	WHERE "{}" = "{}"
	""".format(numMotorista, id)
	
def dbSelectAllClientes ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT nome, cpf
	FROM pessoas"""

	cursor.execute (command)
	data = cursor.fetchall ()
	connection.close ()
	return data

def dbSelectAllViagens ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT cidadeOrigem, cidadeDestino, diaViagem, horario, onibusPlaca, motoristaViagem, numViagem
	FROM viagens"""

	cursor.execute (command)
	data = cursor.fetchall ()
	connection.close ()
	return data

def dbSelectViagem (numViagem):
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT cidadeOrigem, cidadeDestino, motoristaViagem, onibusPlaca, diaViagem, horario, numViagem
	FROM viagens
	WHERE numViagem = "{}" """.format (numViagem)

	cursor.execute (command)
	data = cursor.fetchone ()
	connection.close ()
	return data

def dbSelectOnibus (numOnibus):
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT placa, ano, modelo, qtdPoltronas
	FROM onibus
	WHERE numOnibus = "{}" """.format (numOnibus)

	cursor.execute (command)
	data = cursor.fetchone ()
	connection.close ()
	return data

def dbSelectCompLogin ():
	connection = sqlite3.connect ("CompOnibus.db")
	cursor = connection.cursor ()
	command = """
	SELECT usuario, senha
	FROM companhia
	WHERE numCompanhia = 1"""

	cursor.execute (command)
	data = cursor.fetchone ()
	connection.close ()
	return data









"""
Implementacao das funcoes de alteracoes referentes a cada tabela da bd
"""
#Argumentos, campo para alteracao, chave de alteracao, campo de pesquisa no bd
#chave de pesquisa

@crudSqlite
def dbUpdate (table, setCampo, alteracao, whereCampo, chave):
	return """
	UPDATE "{}" SET "{}" = "{}" WHERE "{}" = "{}"
	""".format (table, setCampo, alteracao, whereCampo, chave)

@crudSqlite 
def dbUpdateOnibus (numOnibus, placa, ano, modelo, qtdPoltronas):
	return """
	UPDATE onibus
	SET placa = "{}",
		ano = "{}",
		modelo = "{}",
		qtdPoltronas = "{}"
	WHERE numOnibus = "{}"
	""".format (placa, ano, modelo, qtdPoltronas, numOnibus)

@crudSqlite
def dbUpdatePessoa (id, nome, sexo, usuario, senha):
	return """
	UPDATE pessoas
	SET cpf = "{}",
		nome = "{}",
		sexo = "{}",
		usuario = "{}",
		senha = "{}",
	WHERE id = "{}"
	""".format (cpf, nome, sexo, id)

@crudSqlite
def dbUpdateMotorista (numMotorista, cpfMotorista, nome, sexo, usuario, senha):
	return """
	SELECT numMotorista, cpfMotorista, id, nome, sexo, usuario, senha
	FROM motoristas, pessoas
	SET cpfMotorista = "{}"
		cpf = "{}",
		nome = "{}",
		sexo = "{}",
		usuario = "{}",
		senha = "{}",
	WHERE "{}" = "{}"
	""".format(cpfMotorista, cpfMotorista, nome,
			 sexo, usuario, senha, numMotorista, id)

	
@crudSqlite 
def dbUpdateViagem (numViagem, onibusPlaca, motoristaViagem, diaViagem,
					horario, cidadeOrigem, cidadeDestino):
	return """
	UPDATE viagens
	SET onibusPlaca = "{}",
		motoristaViagem = "{}",
		diaViagem = "{}",
		horario = "{}",
		cidadeOrigem = "{}",
		cidadeDestino = "{}",
	WHERE numViagem = "{}"
	""".format (onibusPlaca, motoristaViagem, diaViagem,
				horario, cidadeOrigem, cidadeDestino, numViagem)





"""
Implementacao das funcoes de remocao referentes a cada tabela da bd
"""
@crudSqlite
def dbDeletePessoa (cpf):
	return """
	DELETE FROM pessoas where cpf = "{}"
	""".format (cpf)

@crudSqlite
def dbDeleteMotorista (cpfMotorista):
	dbDeletePessoa (cpfMotorista)
	return """
	DELETE FROM motoristas where cpfMotorista = "{}"
	""".format (cpf)

@crudSqlite
def dbDeleteCliente (cpfCliente):
	dbDeletePessoa (cpfCliente)
	return """
	DELETE FROM clientes where cpfCliente = "{}"
	""".format (cpf)

@crudSqlite
def dbDeleteOnibus (numOnibus):
	return """
	DELETE FROM onibus where numOnibus = "{}"
	""".format (numOnibus)

@crudSqlite
def dbDeleteViagem (numViagem):
	return """
	DELETE FROM viagens where numViagem = "{}"
	""".format (numViagem)

