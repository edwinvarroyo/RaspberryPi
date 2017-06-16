# -*- coding: utf-8 -*-
import MySQLdb
import random

# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","root","n0m3l0s3","latatuadora_core")

# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
cont = 0
styles = ["OldSchol", "New school", "Puntillismo", "Geometrico", "Trash Polka", "Black work", "Acuarela", "Japones", "Tribal", "Caligrafia", "Ilustracion", "Surreal", "Biomecanico"]
texts = ["styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext","styletext"]
for x in styles:
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO style (name, calculatorText, quotation) VALUES ('"+x+"','"+ texts[cont] +"', true)"
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "styles")
cont = 0
bodyparts = ["Oreja", "Muñeca", "Cuello", "Manos", "Rodilla", "Dedos", "Pies", "Pierna", "Espalda", "Pantorrilla", "Hombros", "Brazos"]
for x in bodyparts:
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO bodypart (name) VALUES ('"+x+"')"
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "bodyparts")
cont = 0
for x in xrange(0, 20):
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO  flashelement (flashId, element) VALUES (%d, %d)"%(random.randrange(1, 10),random.randrange(1, 15))
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "Flash-Element")
cont = 0
for x in xrange(0, 20):
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO  flashstyle (flashId, style) VALUES (%d, %d)"%(random.randrange(1, 10),random.randrange(1, 13))
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "Flash-Style")
cont = 0
sizes = ["small", "medium", "large", "extra large"]
for x in sizes:
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO  size (description) VALUES ('"+x+"')"
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "Flash-Size")
cont = 0
for x in xrange(0, 10):
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO  flash (realImageUrl, sellImageUrl, amount, sizeId, significant, artistId, copyrigth, sell) VALUES ('../images/realImg.jpg', '../images/sellImg.jpg', %d, %d, 'mock signicant', %d, true, false)"%(random.randrange(200, 1000, 50),random.randrange(1, 4),random.randrange(1, 10))
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "Flash")
######################Tattoos#################################

tattoos = 0
for x in xrange(0, 20):
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO tattoo (element, partbody, dimensionsX, dimensionsY, image, name, publicate, style, artistId, votes) VALUES (%d, %d, %d, %d, '../images/mocktattoo.jpg','Tattoo', true, %d, %d, %d)"%(random.randrange(1, 10),random.randrange(1, 10),random.randrange(1, 10),random.randrange(1, 10),random.randrange(1, 10),random.randrange(1, 10), random.randrange(1, 20))
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   tattoos=tattoos+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(tattoos, "Tattoos")


#####################Elements#############################

elements = ["Flor", "Dragon", "Bot", "Aire", "Agua", "Arbol", "Vida", "Lobo", "Leon", "Rosa de los Vientos", "Infinito", "Craneo", "Luna", "Sol", "Estrella"]
cont = 0
for x in elements:
	# Preparamos el query SQL para insertar un registro en la BD
	sql = "INSERT INTO element (name) VALUES ('"+x+"')"
	try:
	   # Ejecutamos el comando
	   cursor.execute(sql)
	   # Efectuamos los cambios en la base de datos
	   bd.commit()
	   cont=cont+1
	except:
	   # Si se genero algún error revertamos la operación
	   bd.rollback()
print(cont, "Elements")
# Nos desconectamos de la base de datos
bd.close()