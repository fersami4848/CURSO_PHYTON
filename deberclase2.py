#mi variable de datos
saludo= "Hola yo soy Fernanda y me gustan los animales"
print (saludo)

#lista de cosas
mascotas= "Estos son los nombres de mis mascotas"
print (mascotas)
mascota_1="Lobi"
mascota_2 = "Galleta"
lista= [mascota_1, mascota_2]
print (lista)

##diccionario permite visualizar un grupo de datos con su etiqueta
edades=" estas son las edades de mis mascotas"
print (edades)
mi_diccionario={'Lobi': '9 años', 'Galleta':'8 meses'}
print (mi_diccionario)


#tipos de numeros (numerica)
#enteros
numero_mascotas= "Este es el numero de mascotas que tengo"
print (numero_mascotas)
gatos=[1]*1
perros=[1]*1
print (gatos, perros)

#flotantes
Edad= "la edad en años de mis mascostas es"
Lobi= [10.4]*1
Galleta= [0.8]*1
print (Lobi, Galleta)

vetel= "Antes tenia un perro llamado vetel, si aun viviera su edad seria"
print (vetel)
vect_complejo= [15+4j]*1
print (vect_complejo)

diccionario={"Numero de gatos": gatos , "edad del gato": Lobi}
print (diccionario)

#cadenas 

cadena_simple= "hola galleta"
cadena_doble= ["DEJA DE DESTRUIR", "TODO"]
print (cadena_simple)
print (cadena_doble)


#########
#data frame (tabla con 2 dimensiones)
import pandas as pd 

#crear data frame
mascotas={
    'Nombre': ['Lobi', 'Galleta'],
    'Edad': [10,0.8],
    'Color': [amarillo, blanco],
}
df= pd.DataFrame (mascotas)
print (df)
