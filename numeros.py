#!/usr/bin/python3

def esPar(numero):
	try:
		return (numero % 2 == 0)
	except TypeError:	
		return False

def esImpar(numero):
	try:
		return (numero % 2 == 1)
	except TypeError:	
		return False

def pedirNumeroEntero():

	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Introduce un numero entero: "))
			correcto=True
		except ValueError:
			print('Error, introduce un numero entero')
	
	return num
