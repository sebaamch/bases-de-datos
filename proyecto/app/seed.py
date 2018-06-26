from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur= conn.cursor()

sql = """ chupalo entonces
"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
