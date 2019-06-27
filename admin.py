from database import *
from flask import Flask, request, render_template, redirect, url_for, flash


def configure (app):
	
	@app.route ("/admin/controlPanel/")
	def controlPanel ():
		return (render_template ("baseAdmin.html"))
	#Falta adicionar os styles css, por falta de tempo vou testar
	#somente a funcionalidade dos mesmos na adicao, e depois
	#que o banco de dados estiver populado vou implementar as outras
	#funcoes do banco de dados






	#Onibus
	@app.route ("/admin/controlPanel/addOnibus", methods=["GET", "POST",])
	def addOnibus ():
		if request.method == "GET":
			return render_template ("addOnibus.html")
		if request.method == "POST":
			# processar dados
			placa = request.form.get ("placa")
			ano = request.form.get ("ano")
			modelo = request.form.get ("modelo")
			qtdPoltronas = request.form.get ("qtdPoltronas")
			#validar - implementar caso invalido 
			if not placa and not ano and not modelo and not qtdPoltronas:
			 	flash ("Registro invalido, tente novamente!")
			# insercao no banco de dados - Implementar checagem para verificar se ja existe registro identico
			# cpf valido e senha segura
			else:
				dbInsertOnibus (placa, ano, 0, modelo, qtdPoltronas)
			# implementar caso valido
				flash ("Registro concluido!")
		return render_template('mensagemAdmin.html')

	@app.route ("/admin/controlPanel/selectOnibus", methods=["GET", "POST",])
	def selectOnibus ():
		if request.method == "GET":
			return render_template ("selectOnibus.html", dataOnibus = dbSelectAllOnibus ())

	@app.route ("/admin/controlPanel/updateOnibus", methods=["GET", "POST",])
	def updateOnibus ():
		numOnibus = request.form.get ("atualizar")
		print ("Numero do Onibus " +numOnibus)
		#if request.method == "GET":
		return render_template ("updateOnibus.html", 
				dataOnibus = dbSelectOnibus (numOnibus))
		if request.method == "POST":
			# processar dados
			placa = request.form.get ("placa")
			ano = request.form.get ("ano")
			modelo = request.form.get ("modelo")
			qtdPoltronas = request.form.get ("qtdPoltonas")
			#validar - implementar caso invalido 
			#if not placa and not ano and not modelo and not qtdPoltronas:
			# 	flash ("Atualizacao invalida, tente novamente!")
			# insercao no banco de dados - Implementar checagem para verificar se ja existe registro identico
			# cpf valido e senha segura
			#else:
			dbUpdateOnibus (numOnibus, placa, ano, modelo, qtdPoltronas)
			# implementar caso valido
			flash ("Atualizacao concluida!")
			return render_template('mensagemAdmin.html')

	@app.route ("/admin/controlPanel/deleteOnibus", methods=["POST",])
	def deleteOnibus ():
		numOnibus = request.form.get ("deletar")
		dbDeleteOnibus (numOnibus)

		return redirect (url_for ("selectOnibus"))



		




	#Motoristas
	@app.route ("/admin/controlPanel/addMotorista", methods=["GET", "POST",])
	def addMotorista ():
		if request.method == "GET":
			return render_template ("addMotorista.html")

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
				dbInsertMotorista (cpf, nome, sexo, usuario, senha)
				# implementar caso valido
				flash ("Registro concluido!")
		return render_template ("mensagemAdmin.html")
	@app.route ("/admin/controlPanel/selectMotorista", methods=["GET", "POST",])
	def selectMotorista ():
		if request.method == "GET":
			return render_template ("selectMotorista.html", dataMotoristas = dbSelectAllMotoristas ())

	#Viagens
	@app.route ("/admin/controlPanel/addViagem", methods=["GET", "POST",])
	def addViagem ():
		if request.method == "GET":
			return render_template ("addViagem.html", dataMotoristas = dbSelectAllNomeMotoristas (), dataOnibus = dbSelectAllOnibus ())
		if request.method == "POST":
			# processar dados
			onibusPlaca = request.form.get ("onibusPlaca")
			motoristaViagem = request.form.get ("motoristaViagem")
			diaViagem = request.form.get ("diaViagem")
			horario = request.form.get ("horario")
			cidadeOrigem = request.form.get ("cidadeOrigem")
			cidadeDestino = request.form.get ("cidadeDestino")			
			#validar - implementar caso invalido
			if not onibusPlaca and not motoristaViagem and not diaViagem and not horario and not cidadeOrigem and not cidadeDestino:
			 	flash ("Registro invalido, tente novamente!")
			 	#Implementar checagem de integridade com as outras tabelas
			else:
				dbInsertViagem (onibusPlaca, motoristaViagem, diaViagem,
					horario, cidadeOrigem, cidadeDestino)
				# implementar caso valido
				flash ("Registro concluido!")
		return render_template ("mensagemAdmin.html")

	@app.route ("/admin/controlPanel/selectViagem", methods=["GET", "POST",])
	def selectViagem ():
		if request.method  == "GET":
			return render_template ("selectViagem.html", dataViagens = dbSelectAllViagens ())



	@app.route ("/admin/controlPanel/updateViagem", methods=["GET", "POST",])
	def updateViagem ():
		if request.method == "GET":
			numViagem = request.form.get ("atualizar")
			return render_template ("updateViagem.html", 
					dataViagem = dbSelectViagem (numViagem), 
					dataMotoristas = dbSelectAllNomeMotoristas (),
					dataOnibus = dbSelectAllOnibus ())
		if request.method == "POST":
			onibusPlaca = request.form.get ("onibusPlaca")
			motoristaViagem = request.form.get ("motoristaViagem")
			diaViagem = request.form.get ("diaViagem")
			horario = request.form.get ("horario")
			cidadeOrigem = request.form.get ("cidadeOrigem")
			cidadeDestino = request.form.get ("cidadeDestino")	
			if not onibusPlaca and not motoristaViagem and not diaViagem and not horario and not cidadeOrigem and not cidadeDestino:
			 	flash ("Atualizacao invalida, tente novamente!")
			 	#Implementar checagem de integridade com as outras tabelas
			else:
				dbInsertViagem (numViagem, onibusPlaca, motoristaViagem, diaViagem,
					horario, cidadeOrigem, cidadeDestino)
				# implementar caso valido
				flash ("Atualizacao concluida!")
		return render_template ("mensagemAdmin.html")	

	@app.route ("/admin/controlPanel/deleteViagem", methods=["POST",])
	def deleteViagem ():
		numViagem = request.form.get ("deletar")
		dbDeleteViagem (numViagem)

		return redirect (url_for ("selectViagem"))
