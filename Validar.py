import re

def dniValido(accion):
    while True:
        dni = int(input(f"Ingrese el DNI del cliente para {accion} (0 para finalizar): "))

        if dni == 0:
            return dni
        
        if re.match(r'^\d{8}$', str(dni)):
            return dni
        else:
            print("Error: El DNI debe tener 8 dígitos numéricos. Inténtelo de nuevo.")