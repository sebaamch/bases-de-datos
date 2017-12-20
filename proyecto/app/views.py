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

@app.route('/test')
def rojo():
	return render_template("layout.html",usuario = "perrito",barras="perrote")


#@app.route('/forms')
#def pikashu():
#	variable1= "Seguidores"
#	return render_template("megazord.html",usuario = "perrito",barras="perrote",variable1=variable1)

@app.route('/index')
def index():
	variable1= "Seguidores"
	return render_template("megazord.html",usuario = "perrito",barras="perrote",variable1=variable1)
