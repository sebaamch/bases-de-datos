from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

sql = """ DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
"""

cur.execute(sql)

sql ="""
CREATE TABLE users (mail varchar(50) PRIMARY KEY,password varchar(50));
"""
cur.execute(sql)


sql ="""
CREATE TABLE  prop_user
				(rut varchar(10),id_user varchar(50));
"""
cur.execute(sql)


sql ="""
CREATE TABLE  servicios
				(rut_empresa varchar(10) PRIMARY KEY,rut_user varchar(10),nombre_empresa varchar(50),giro varchar(50));
"""
cur.execute(sql)


sql="""
CREATE TABLE propietario
				(rut varchar(10) PRIMARY KEY, nombre1 varchar (41), nombre2 varchar(41), apellido1 varchar(41), apellido2 varchar(41) , direccion varchar(120),ciudad varchar(41),comuna varchar(41));
"""
cur.execute(sql)

sql ="""
CREATE TABLE chequera
				(id_chequera int);
"""
cur.execute(sql)

sql ="""
CREATE TABLE pertenecen
				(rut_serv varchar(10),id_chequera int);
"""
cur.execute(sql)

sql ="""
CREATE TABLE cheques_chequeras
				(id_cheques int,id_chequera int);
"""
cur.execute(sql)

sql ="""
CREATE TABLE cheques
				(id serial PRIMARY KEY,monto int,codigo_banco int, ano int,mes int, dia int, factura_pagada int, receptor int);
"""
cur.execute(sql)

sql ="""
CREATE TABLE bancos
				(id int PRIMARY KEY,nombre varchar(50));
"""
cur.execute(sql)

sql ="""
CREATE TABLE receptor
				(rut_recep varchar(10),nombre varchar(50));
"""
cur.execute(sql)

sql ="""
CREATE TABLE factura
				(id int PRIMARY KEY,monto int);
"""
cur.execute(sql)
conn.commit()
cur.close()
conn.close()




