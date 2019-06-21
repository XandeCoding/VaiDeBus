from usuario import *
from database import *
from flask import Flask, request, redirect, url_for, render_template

def configure (app):
	@app.route ("/", methods = ["POST", "GET",])
	@app.route ("/index", methods = ["POST", "GET",])
	def index ():		
		if request.method == "GET":
			return render_template ("index.html")
		elif request.method == "POST":
			username = request.form["username"]
			password = request.form["password"]
			# checa primeiro se o login e para entra para area da companhia
			if (checaLoginComp (username, password)):
				compUser = retornaCompRegistro ()
				login_user (compUser)
				return redirect ("/admin/controlPanel/")
				#return ("oi pessoal")
				pass
			else:
				return abort (401)
	@app.route ("/listarViagens")
	def listarViagens ():
		return render_template ("listarViagens.html", dataViagens = dbSelectAllViagens ())
	