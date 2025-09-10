# Script para solicitar y mostrar información del usuario.

# Se solicita la información al usuario y se almacena en variables.
nombre = input("Por favor, introduce tu nombre: ")
apellido = input("Por favor, introduce tu apellido: ")
codigo_seccion = input("Por favor, introduce tu Código-sección: ")
sede = input("Por favor, introduce tu sede: ")

# Se imprime la información recopilada en la pantalla.
print("\n--- Información del Estudiante ---")
print(f"Nombre completo: {nombre} {apellido}")
print(f"Código-sección: {codigo_seccion}")
print(f"Sede: {sede}")