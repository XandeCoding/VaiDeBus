import sqlite3
from pprint import *
from database import * 

#dbInsertMotorista ("15926348-7", "Rogerio", "Masculino", "Roge", "123")

"""
dbInsertCliente ("147852369-8", "Mengao", "Masculino", "Meng", "234")
dbInsertOnibus ("B54-745", 1999, "cheio", "Ford", 57)

#dbUpdatePessoa ("nome", "Rubao", "cpf", "147852369-8")
#dbUpdatePessoa ("cpf", "1594-9", "cpf", "15926348-7")

#dbDeletePessoa ("1594-9")


#print (dbSelectCompLogin ())

def retornaCompRegistro ():
	username, password = dbSelectCompLogin ()
	print (username, password)
	#aux = User (username, password)
	return (aux)

retornaCompRegistro ()
"""
#dbInsertMotorista ("49879-1", "Roberta", "Feminino", "Robe", "133")
#dbInsertCompanhia ("147/0000", "admin", "admin")
#data = dbSelectAllOnibus ()
#pprint (data[1][0])
data = dbSelectAllNomeMotoristas ()
print (data[1][0])
