from app import app
from flask import render_template,request,redirect
from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

@app.route('/', methods=["POST", "GET"])
def formulario():
	if request.method=="POST":
		nombre = request.form["nombre"]
		"""sql = "insert into usuarios(nombre) values('%s')"%(nombre)
	
		cur.execute(sql)
		conn.commit()"""

	return render_template("login.html")#,usuario = "perrito" ,barras="perrote"

@app.route('/login', methods=["POST"])
def login():
	alerta=""
	if request.method == "POST":
		email = request.form["loginmail"]
		password = request.form["loginPassword"]

		sql="""SELECT mail from users where users.mail = '%s'
		"""%(email)
		cur.execute(sql)
		resultados = cur.fetchone()

		if resultados == None	:
			alerta="cuenta inexistente"
	#		"""sql = "INSERT INTO users (mail,password) VALUES (mail,'eltionachoesbuentipo');"
	#		"""
		return render_template("login.html", alerta = alerta)

	return render_template("megazord.html",usuario = "perrito",barras="perrote",variable1=variable1)

@app.route('/registrarse')
def registrarse():
	"""sql = "escribir la consulta aqui"
	"""
	cur.execute(sql)
	resultados = cur.fetchall()
	

	return render_template("register.html",usuario = "perrito",barras="perrote")

#@app.route('/test')
#def rojo():
#	return render_template("megazord.html",usuario = "perrito",barras="perrote")


#@app.route('/forms')
#def pikashu():
#	variable1= "Seguidores"
#	return render_template("megazord.html",usuario = "perrito",barras="perrote",variable1=variable1)

@app.route('/index')
def index():
	variable1= "Seguidores"
	return render_template("megazord.html",usuario = "perrito",barras="perrote",variable1=variable1)
