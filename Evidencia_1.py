import os
import datetime
import re
import random

archivo="espacio.csv"
espacio={}

print("\nOpciones:")
print("\t[A] Registrar una sala")
print("\t[R] Registrarse")
print("\t[C] Consultar reservaciónes")
print("\t[F] Modificar registro")
print("\t[V] Ver todos los registros")
print("\t[S] Salir")

while True:

    opcion = input("\n Dime, ¿qué deseas hacer?: ")
    if (not opcion.upper() in "ARCFVS"):
        print("Opcion no valida, intenta de nuevo.")
        continue

    if (opcion.upper()=="S"):
        print("Fin del programa.")
        break

    if (opcion.upper()=="A"):
        print("Salas disponibles: \n\t - Sala 1 \n\t - Sala 2 \n\t - Sala 3\n\t - Sala 4\n\t - Sala 5  ")
        sala=input("Escoge una sala: ")
        if espacio.get(sala)==None:
            nombre=input("Nombre del evento: ")
            turno = input("¿En que turno será?: ")
            integrantes=float(input("¿De cuántas personas será su evento? "))
            Fecha = input("Dime la fecha del evento (dd/mm/aaaa):")
            fecha_procesada = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
            print(f"El folio de tu evento es: {random.randrange(9999999)}")
            espacio.update({sala:[sala,nombre,turno,integrantes,Fecha]})
            print("Evento reservado exitosamente.")
        else:
            print("Sala ocupada. No se puede repetir.")

    if (opcion.upper()=="R"):

        cliente=input("Dime tu nombre: ")
        print(f"Está es tu clave de acceso: {random.randrange(9999999)}")


    if (opcion.upper()=="C"):

        sala=input("Numero de evento a buscar: ")

        recuperado=espacio.get(sala)
        if recuperado==None:
            print("Evento no encontrado.")
        else:
            print(f"{recuperado[0]},{recuperado[1]},{recuperado[2]},{recuperado[3]}")

    if (opcion.upper()=="F"):

        sala=input("Numero de sala a modificar: ")

        recuperado=espacio.get(sala)
        if recuperado==None:
            print("Asistente no encontrado. No se puede modificar")
        else:
            print(f"espacio actuales: {recuperado[0]},{recuperado[1]},{recuperado[2]},{recuperado[1]},{recuperado[2]}")
            Nombre=input("Nuevo Nombre del sala: ")
            espacio.update({sala:[sala,Nombre,turno,Fecha]})
            print("Nombre modificado.")

    if (opcion.upper()=="V"):
        print("Los registros son: ")
        datos=[sala,nombre,turno,fecha_procesada]
        print(datos)



