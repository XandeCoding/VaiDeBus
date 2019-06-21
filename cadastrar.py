from database import *

from flask import Flask, request, redirect, url_for, render_template, flash

def configure (app):
	@app.route ("/cadastrar", methods=["POST","GET",])
	def cadastrar ():
		if request.method == "GET":
			return render_template ("cadastrar.html")
		if request.method == "POST":
			# processar dados
			nome = request.form.get ("nome")
			cpf = request.form.get ("cpf")
			usuario = request.form.get ("usuario")
			senha = request.form.get ("senha")
			sexo = request.form.get ("sexo")			
			#validar - implementar caso invalido
			if not nome and not cpf and not usuario and not senha and not sexo:
			 	flash ("Registro invalido, tente novamente!")
			# insercao no banco de dados - Implementar checagem para verificar se ja existe registro identico
			# cpf valido e senha segura
			else:
				dbInsertCliente (cpf, nome, sexo, usuario, senha)
				# implementar caso valido
				flash ("Registro concluido!")
		return render_template("baseMensagem.html")
		


