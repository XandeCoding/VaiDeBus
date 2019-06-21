from database import *
from flask_login import LoginManager, login_required, UserMixin, login_user


class User (UserMixin):
	def __init__ (self, username, password, id, active=True):
		self.username = username
		self.password = password
		self.id = id
		self.active = active

	def get_id (self):
		return self.id

	def is_active (self):
		return self.active

	def is_authenticated (self):
		return True

	def get_auth_token (self):
		return make_secure_token (self.username, key="secret_key")

#Funcoes nao relacionadas a classe mas a gerencia do login e do registro da companhia e clientes

#Retorna o unico registro de Companhia
#futuramente talvez implementar acesso para varias companhias de onibus

def retornaCompRegistro ():
	username, password = dbSelectCompLogin ()
	aux = User (username, password, 1)
	return aux

def checaLoginComp (usuario, senha):
	userComp = retornaCompRegistro ()
	if (userComp.username == usuario and userComp.password == senha):
		return True
	else:
		return False


def configure (app):
	loginManagerCompOnibus = LoginManager ()
	loginManagerCompOnibus.login_view = "login"
	loginManagerCompOnibus.init_app (app)

	
	@loginManagerCompOnibus.user_loader
	def load_user (userid):
		return 1