from app import app
from flask import render_template,request,redirect
from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/', methods=["POST", "GET"])
def formulario():
	return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
	alerta=""
	if request.method == "POST":
		email = request.form["loginmail"]
		password = request.form["loginPassword"]

		sql="""SELECT mail,password from users where users.mail = '%s'
		"""%(email)
		cur.execute(sql)
		resultados = cur.fetchone()

		if resultados == None	:
			alerta="cuenta inexistente"
			return render_template("login.html", alerta = alerta)

		elif resultados[1] != password :
			alerta="contrasena invalida"
			return render_template("login.html", alerta = alerta )
		else :
			return render_template("megazord.html",email=email)
	else:

		return render_template("login.html")

@app.route('/registrarse', methods=["POST","GET"])
def registrarse():
	alerta=""
	if request.method == "POST":
		email=request.form["mail"]
		password=request.form["password"]
		rut=request.form["rut"]
		nombre1=request.form["primernombre"]
		nombre2=request.form["segundonombre"]
		apellido1=request.form["primerapellido"]
		apellido2=request.form["segundoapellido"]
		direccion=request.form["direccion"]
		ciudad=request.form["ciudad"]
		comuna=request.form["comuna"]

		print(email)
		print(rut)
		if len(rut) >10:
			alerta="Rut demasiado largo, vuelva ingresar"
			return render_template("register.html", alerta = alerta)

		sql="""SELECT mail,password from users where users.mail ='%s';
		"""%(email)
		cur.execute(sql)
		resultadoMail= cur.fetchall()
		print(resultadoMail)

		sql="""SELECT rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna from propietario where propietario.rut ='%s';
		"""%(rut)
		cur.execute(sql)
		resultadopropietario = cur.fetchall()
		print(resultadopropietario)

		if len(resultadoMail) == 0 and len(resultadopropietario) == 0 :
			sql ="""INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');
			"""%(rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna)
			cur.execute(sql)
			conn.commit()

			sql ="""INSERT INTO users(mail,password) VALUES ('%s','%s');
			"""%(email,password)
			cur.execute(sql)
			conn.commit()

			sql="""INSERT INTO prop_user(rut,id_user) VALUES('%s','%s');
			"""%(rut,email)
			cur.execute(sql)
			conn.commit()
			

			return render_template("megazord.html",rut = rut,mail=email,alerta=alerta)

		elif len(resultadoMail) != 0:
			alerta="mail ya utilizado"
			return render_template("register.html", alerta = alerta)


		elif len(resultadopropietario) != 0:
			alerta="persona ya ingresada"
			return render_template("register.html", alerta = alerta)

		else: 
			return render_template("register.html",alerta=alerta)
		
	return render_template("register.html",alerta=alerta)


@app.route('/actualizar/<email>', methods=["POST","GET"])
def registrarse(email):
	alerta=""
	if request.method == "POST":
		rut=request.form["rut"]
		nombre1=request.form["primernombre"]
		nombre2=request.form["segundonombre"]
		apellido1=request.form["primerapellido"]
		apellido2=request.form["segundoapellido"]
		direccion=request.form["direccion"]
		ciudad=request.form["ciudad"]
		comuna=request.form["comuna"]

		print(email)
		print(rut)
		if len(rut) >10:
			alerta="Rut demasiado largo, vuelva ingresar"
			return render_template("register.html", alerta = alerta)

		sql="""SELECT mail,password from users where users.mail ='%s';
		"""%(email)
		cur.execute(sql)
		resultadoMail= cur.fetchall()
		print(resultadoMail)

		sql="""SELECT rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna from propietario where propietario.rut ='%s';
		"""%(rut)
		cur.execute(sql)
		resultadopropietario = cur.fetchall()
		print(resultadopropietario)

		sql="""SELECT rut FROM users, prop_user, propietario WHERE mail = id_user AND prop_user.rut = propietario.rut AND mail = '%s%';
		"""%(email)
		cur.execute(sql)
		rutdelaconcha = cur.fetchall()
		print(rutdelaconcha)

		if len(resultadoMail) == 0 and len(resultadopropietario) == 0 :
			sql ="""UPDATE propietario SET rut ='%s',nombre1='%s',nombre2='%s',apellido1='%s',apellido2='%s',direccion='%s',ciudad='%s',comuna='%s' WHERE rut ='%s%';
			"""%(rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna,rutdelaconcha)
			cur.execute(sql)
			conn.commit()

			sql="""UPDATE prop_user SET rut='%s' WHERE id_user = '%s';
			"""%(rut,email)
			cur.execute(sql)
			conn.commit()
			

			return render_template("megazord.html",rut = rut,email=email,alerta=alerta)

		elif len(resultadoMail) != 0:
			alerta="mail ya utilizado"
			return render_template("register.html", alerta = alerta,email=email)


		elif len(resultadopropietario) != 0:
			alerta="persona ya ingresada"
			return render_template("register.html", alerta = alerta,email=email)

		else: 
			return render_template("register.html",alerta=alerta,email=email)
		
	return render_template("register.html",alerta=alerta,email=email)


@app.route('/numeroempresas/<mail>')
def numerodeempresas(email):

	sql="""SELECT COUNT(*) FROM users, prop_user, propietario, servicios WHERE mail = id_user AND prop_user.rut = propietario.rut AND propietario.rut = rut_user AND mail = '%s%';
	"""%(mail)
	cur.execute(sql)
	numeroempresas = cur.fetchall()
	print(numeroempresas)
	return render_template(numeroempresas = numeroempresas,email=email)

@app.route('/numerochequeras/<mail>')
def numerochequeras(email):

	sql="""SELECT COUNT(*) FROM users, prop_user, propietario, servicios, pertenecen, chequera WHERE mail = id_user AND prop_user.rut = propietario.rut AND propietario.rut = rut_user AND rut_empresa = rut_serv AND pertenecen.id_chequera = chequera.id_chequera AND mail = '%s%';"""%(mail)
	cur.execute(sql)
	numerochequeras = cur.fetchall()
	print(numerochequeras)
	return render_template(numerochequeras = numerochequeras,email=email)

@app.route('/numerocheques/<mail>')
def numerodecheques(email):

	sql="""SELECT COUNT(*) FROM users, prop_user, propietario, servicios, pertenecen, chequera, cheques_chequeras, cheques WHERE mail = id_user AND prop_user.rut = propietario.rut AND propietario.rut = rut_user AND rut_empresa = rut_serv AND pertenecen.id_chequera = chequera.id_chequera AND chequera.id_chequera = cheques_chequeras.id_chequera AND id_cheques = id AND mail = '%s%';
	"""%(mail)
	cur.execute(sql)
	numerocheques = cur.fetchall()
	print(numerocheques)
	return render_template(numerocheques = numeroempresas,email=email)

@app.route('/empresas/<mail>')
def empresas(email):
	sql="""SELECT nombre_empresa FROM servicios, propietario, prop_user, users WHERE mail = id_user AND prop_user.rut = propietario.rut AND propietario.rut = rut_user AND mail = '%s%';
	"""
	cur.execute(sql)
	empresas = cur.fetchall()
	return render_template("empresas.html",empresas=empresas)

@app.datos('/datos/<mail>')
def datos(email):
	sql="""SELECT * FROM users, prop_user, propietario WHERE mail = id_user AND prop_user.rut = propietario.rut AND mail = '%s%';
	"""%(mail)
	cur.execute(sql)
	datos = cur.fetchall()
	return render_template("datos.html",datos=datos)

@app.route('/chequeras/<empresas>')
def chequeras(empresas):
	sql="""SELECT chequera.id_chequera FROM chequera, pertenecen, servicios WHERE chequera.id_chequera = pertenecen.id_chequera AND rut_serv = rut_empresa AND rut_empresa = '%s%';
	"""
	cur.execute(sql)
	chequeras = cur.fetchall()
	return render_template("chequeras.html",chequeras=chequeras)

@app.route('/cheques/<chequeras>')
def chequeras(chequeras):
	sql="""SELECT id FROM cheques, cheques_chequeras, chequera WHERE id = id_cheques AND chequera.id_chequera = cheques_chequeras.id_chequera AND chequera_id_chequera = '%s%';
	"""%chequeras
	cur.execute(sql)
	cheques = cur.fetchall()
	return render_template("cheques.html",cheques=cheques)

@app.route('/facturas/<cheques>')
def facturas(cheques):
	sql="""SELECT monto FROM cheques, factura WHERE factura_pagada = factura.id AND cheques.id = '%s%';"""%cheques
	cur.execute(sql)
	facturas = cur.fetchall()
	return render_template("facturas.html",facturas=facturas)

@app.route('/test')
def index():
	return render_template("tables.html")


@app.route('/dempresas/<empresaactual>')
def dempresas(empresaactual):
	return render_template("empresa.html",empresaactual=empresaactual)
