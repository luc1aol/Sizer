import re

def dniValido(accion):
    while True:
            dni = input(f"Ingrese el DNI del cliente para {accion} (0 para finalizar): ")

            if dni == '0':
                return int(dni)
            
            if re.match(r'^\d{8}$', str(dni)):
                return int(dni)
            else:
                print("Error: El DNI debe tener 8 dígitos numéricos. Inténtelo de nuevo.")
            