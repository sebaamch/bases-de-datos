from app import app
from flask import render_template,request,redirect
from configuraciones import *
import psycopg2

#conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,passwd))
#cur = conn.cursor()

@app.route('/', methods=["POST", "GET"])
def formulario():
	return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
	alerta=""
	if request.method == "POST":
		email = request.form["loginrut"]
		password = request.form["loginPassword"]

		sql="""SELECT rut,password from empleados where empleados.rut = '%s'
		"""%(rut)
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
		password=request.form["password"]
		rut=request.form["rut"]
		nombre=request.form["nombre"]
		apellido=request.form["apellido"]
		sexo=request.form["sexo"]

		print(email)
		print(rut)
		if len(rut) >10 and len(rut) < 9:
			alerta="Rut invalido vuelva ingresar"
			return render_template("register.html", alerta = alerta)

		sql="""SELECT * from empleados where empleados.rut ='%s';
		"""%(rut)
		cur.execute(sql)
		resultadoempleado = cur.fetchall()
		print(resultadoempleado)

		if len(resultadoempleado) == 0 :
			sql ="""INSERT INTO empleados (rut,nombre,apellido,sexo) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');
			"""%(rut,nombre,apellido,sexo)
			cur.execute(sql)
			conn.commit()
			return render_template("megazord.html",rut = rut,alerta = alerta)

		elif len(resultadoempleado) != 0:
			alerta="Rut ya utilizado"
			return render_template("register.html", alerta = alerta)
		else:
			return render_template("register.html",alerta=alerta)
	else:
		return render_template("register.html",alerta=alerta)

@app.route('/test', methods=["POST","GET"])
def test():
	return render_template("tables.html")
