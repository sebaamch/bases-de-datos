from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

sql = """ DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
"""
cur.execute(sql)
sql ="""
CREATE TABLE test
           (id serial PRIMARY KEY, num integer, data varchar);
"""
cur.execute(sql)
sql="""
CREATE TABLE mesas
           (numero integer PRIMARY KEY, reservada boolean, lugar boolean);
"""
cur.execute(sql)
sql="""
CREATE TABLE empleados
           (nombre varchar(255),apellido varchar(255), rut varchar(10) PRIMARY KEY, sexo boolean,tipo varchar(255),sueldo integer, num_mesas integer, FOREIGN KEY (num_mesas) REFERENCES mesas (numero));
"""
cur.execute(sql)
sql="""
CREATE TABLE productos
           (id_producto varchar(255) PRIMARY KEY,
            cantidad integer,
            valor integer
            );
"""

cur.execute(sql)
sql="""
CREATE TABLE proveedores
           (nombre varchar (255),
           rut_empresa varchar(10) PRIMARY KEY,
           idproducto varchar(255),
           cant_mercaderia integer,
           CONSTRAINT FK_proveedores_idproducto FOREIGN KEY (idproducto) REFERENCES productos (id_producto)
           );
"""
cur.execute(sql)
sql="""
CREATE TABLE menus
           (id_menu varchar(255),
           precio_menu integer,
           descuento integer,
           PRIMARY KEY (id_menu,precio_menu)
           );
"""
cur.execute(sql)
sql="""
CREATE TABLE pedidos
	(fecha_id varchar(40),
	 rut_empleado varchar(10),
	 num_mesa integer,
	 num_menu integer,
	 PRIMARY KEY( fecha_id,rut_empleado,num_mesa,num_menu),
	 FOREIGN KEY (rut_empleado) REFERENCES empleados(rut),
	 FOREIGN KEY (num_mesa) REFERENCES mesas (numero),
	 FOREIGN (num_menu) REFERENCES menus(id_menu));
"""
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
