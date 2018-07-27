#!/usr/bin/python3

from random import *

def generarAleatorio(minimo,maximo):
	
	try:
		if(minimo>maximo):
			aux = maximo
			maximo = minimo
			minimo = aux

		return randint(minimo, maximo)
	except TypeError:
		print("Inserta numeros")
		return 0
