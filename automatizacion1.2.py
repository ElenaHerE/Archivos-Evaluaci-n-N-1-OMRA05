# Script para verificar el rango de una VLAN.

try:
    # Se solicita al usuario que introduzca un número de VLAN.
    vlan_numero = int(input("Introduce el número de la VLAN: "))

    # Se verifica si el número está en el rango normal.
    if 1 <= vlan_numero <= 1005:
        print(f"La VLAN {vlan_numero} corresponde al rango normal.")
    # Se verifica si el número está en el rango extendido.
    elif 1006 <= vlan_numero <= 4094:
        print(f"La VLAN {vlan_numero} corresponde al rango extendido.")
    # Si no está en ninguno de los rangos válidos.
    else:
        print(f"La VLAN {vlan_numero} está fuera de los rangos válidos (1-4094).")

# Se maneja el error si el usuario no introduce un número.
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")
