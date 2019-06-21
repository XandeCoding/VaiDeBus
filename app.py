import os
import index
import usuario
import cadastrar
import admin

from flask import Flask

def create_app ():
	# Inicializa Aplicacao	
	app = Flask (__name__)
	port = int (os.environ.get ("PORT", 5000))
	app.run (host='0.0.0.0', port=port)
	app.secret_key = "Vai De Bus  - PS 2019"	
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	# configurar extensoes
	index.configure (app)
	usuario.configure (app)
	cadastrar.configure (app)
	admin.configure (app)
	#configurar as variaveis

	return app 