#Llamamos las funciones declaradas en otro archivo

from FuncionesExternas import *

#Invocamos las funciones

funcion1()

#Invovamos la otra funcion

Q=input('introduzca un dato: ')
W=input('Introduzca otro dato: ')
print('La sumatoria de los dos datos es: ')
print(funcion2(Q,W))
