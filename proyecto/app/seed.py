from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur= conn.cursor()

sql = """
INSERT INTO users (mail,password) VALUES ('kmilo182@gmail.com','eltionachoesbuentipo');
INSERT INTO users (mail,password) VALUES ('naxo121@gmail.com','sejugarlolperosoyunascoenelhots');
INSERT INTO users (mail,password) VALUES ('onlymalfurion@blizzard.com','solosejugardesoporte');
INSERT INTO users (mail,password) VALUES ('soypobre@gmail.com','gunmadada');
INSERT INTO users (mail,password) VALUES ('harinasama@gmail.com','berserktraumas');
INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('192801818','camilo','andres','porte','moraga','la huerta 1214','santiago','san bernardo');
INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('194235820','jorge','osvaldo','valenzuela','vergara','parque el golf 1133','santiago','maipu');
INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('196242805','irina','sergueyevna','martinez','anufriew','marta ossa ruiz 916','santiago','maipu');
INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('194196997','ignacio','andres','lopez','figueroa','pio baroja 5548','santiago','maipu');
INSERT INTO propietario (rut,nombre1,nombre2,apellido1,apellido2,direccion,ciudad,comuna) VALUES ('205679782','malfurion','ramon','stormrage','ramirez','darnasus 1000','santiago','pudahuel');
INSERT INTO prop_user (rut,id_user) VALUES ('192801818','kmilo182@gmail.com');
INSERT INTO prop_user (rut,id_user) VALUES ('194235820','soypobre@gmail.com');
INSERT INTO prop_user (rut,id_user) VALUES ('196242805','harinasama@gmail.com');
INSERT INTO prop_user (rut,id_user) VALUES ('194196997','naxo121@gmail.com');
INSERT INTO prop_user (rut,id_user) VALUES ('205679782','onlymalfurion@blizzard.com');
INSERT INTO servicios (rut_empresa,rut_user,nombre_empresa,giro) VALUES ('111','192801818','pamacri','expendio de bebida');
INSERT INTO servicios (rut_empresa,rut_user,nombre_empresa,giro) VALUES ('112','116652056','mimami','pancitos con queso');
INSERT INTO servicios (rut_empresa,rut_user,nombre_empresa,giro) VALUES ('113','194196997','miempresa','eloboost');
INSERT INTO chequera(id_chequera) VALUES (18569);
INSERT INTO chequera(id_chequera) VALUES (20685);
INSERT INTO chequera(id_chequera) VALUES (68573);
INSERT INTO pertenecen(rut_serv,id_chequera) VALUES ('111',18569);
INSERT INTO pertenecen(rut_serv,id_chequera) VALUES ('112',20685);
INSERT INTO pertenecen(rut_serv,id_chequera) VALUES ('113',68573);
INSERT INTO cheques(id,monto,codigo_banco,ano,mes,dia,factura_pagada,receptor) VALUES(56149,10,1,2017,10,10810,65,111999911);
INSERT INTO cheques(id,monto,codigo_banco,ano,mes,dia,factura_pagada,receptor) VALUES(1000,10,29,2016,2,324,87,194235820);
INSERT INTO cheques(id,monto,codigo_banco,ano,mes,dia,factura_pagada,receptor) VALUES(1,10,15,2017,11,123958,98,200729544);
INSERT INTO cheques_chequeras(id_cheques,id_chequera) VALUES (56149,18569);
INSERT INTO cheques_chequeras(id_cheques,id_chequera) VALUES (1000,18569);
INSERT INTO cheques_chequeras(id_cheques,id_chequera) VALUES (1,68573);
INSERT INTO bancos(id,nombre) VALUES (1,'banco de la plaza');
INSERT INTO bancos(id,nombre) VALUES (2,'banco del rancagua');
INSERT INTO bancos(id,nombre) VALUES (3,'banco gelificado');
INSERT INTO receptor(rut_recep,nombre) VALUES ('111999911','don carrasco');
INSERT INTO receptor(rut_recep,nombre) VALUES ('194235820','don pobre');
INSERT INTO receptor(rut_recep,nombre) VALUES ('196242805','dona harina');
INSERT INTO factura(id,monto) VALUES (10810,10);
INSERT INTO factura(id,monto) VALUES (123958,100);
INSERT INTO factura(id,monto) VALUES (324,1);
"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()