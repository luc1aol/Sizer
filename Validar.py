# Importamos el módulo re para trabajar con expresiones regulares
# Definimos la función dniValido que valida si el DNI ingresado es correcto
# Entramos en un bucle infinito para pedir el DNI repetidamente hasta que sea válido
# Solicitamos al usuario que ingrese un DNI, personalizando el mensaje con la acción
# Si el usuario ingresa '0', se convierte a entero y se devuelve para finalizar la función
# Usamos una expresión regular para verificar que el DNI tenga exactamente 8 dígitos
# Si el DNI es válido (8 dígitos numéricos), lo convertimos a entero y lo retornamos
# Si el DNI no tiene 8 dígitos, mostramos un mensaje de error
import re

def dniValido(accion):
    '''
    - Valida el dni ingresado.
    - Parámetros: 
        accion
    -Retorno:
        DNI validado.
    '''
    while True:
            dni = input(f"Ingrese el DNI del cliente para {accion} (0 para finalizar): ")

            if dni == '0':
                return int(dni)
            
            if re.match(r'^\d{8}$', dni):
                return dni
            else:
                print("Error: El DNI debe tener 8 dígitos numéricos. Inténtelo de nuevo.")

def telValido(accion):
    '''
    - Valida el número de telefono ingresado.
    - Parámetros: 
        accion
    -Retorno:
        Número de telefono validado.
    '''
    while True:
        tel = input(f"Ingrese el telefono con código de país del cliente para {accion}: ")
        if re.match("^\+\d",tel):   
             return tel
        else:
             print("Error, el número de telefono es incorrecto (Ej +5466578867). Inténtelo nuevamente.")    
