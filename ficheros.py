#!/usr/bin/python3

def numLineasFichero(fichero):

	try:
		fichero.seek(0)
		return len(fichero.readlines())
	except AttributeError:
		print("Debes insertar un fichero")
		return -1

def numLineasFicheroRuta(ruta):
	numLineas = -1
	try:
		fichero = open(ruta, 'r')
		numLineas = len(fichero.readlines())
		fichero.close()
		
	except AttributeError:
		print("Debes insertar un fichero")
	return numLineas
