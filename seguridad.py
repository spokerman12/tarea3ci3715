
#!/usr/bin/python3
"""
Titulo: 

Descripcion: Implementacion de la clase Seguridad

Autores:Leonardo Lopez     14-10576 
        Daniel Francis     12-10863
         

Equipo: Null Pointer Exception

Fecha:/05/2018.
"""
import re

class Seguridad():

    def __init__(self):
        # Crea un diccionario vacio.
        self.usuarios = {}
        
    """
    Recibe 3 strings una de usuario y 2 de clave.
    Realiza las comprobaciones pertinentes y registra al usuario.
    Retorna True si se registro correctamente al usuario.
    Retorna False en caso contrario.
    """
    def registrarUsuario(self, usuario, clave1, clave2):
        # Comprobamos si el email sigue el estandar .
        if not (re.fullmatch('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',usuario)):
            print("Correo electronico invalido. No sigue el formato")
            return False
        
        # Comprobamos que la clave tenga la longitud deseada.
        if not(8 <= len(clave1) <= 16) :
            print("Clave invalida. Longitud debe estar entre 8 y 16 caracteres")
            return False

        # Comprobamos que la clave solo contenga caracteres alfanumericos (no especiales).
        if not(re.fullmatch('[^\W_]*',clave1)):
            print("Clave invalida. Contiene caracteres especiales")
            return False

        # Comprobamos que la clave tenga la cantidad necesaria de mayusculas, minusculas y digitos.
        m = 0 # contador de minusculas .
        M = 0 # contador de mayusculas.
        d = False # Se le asigna true si se encuentra un digito.
        # iteramos por cada caracter de la clave.
        for a in list(clave1) :
            if a.isupper() :
                M+=1
            if a.islower() :
                m+=1
            if a.isdigit():
                d = True

        # Comprobamos que la clave cumpla con las restricciones.
        if M == 0 or m == 0 or m+M < 3 or d == False:
            print("Clave invalida. Debe incluir un numero y al menos 3 letras, una mayuscula y una minuscula")
            return False

        # Comprobamos que el email aparezca en el diccionario.
        if usuario in self.usuarios.keys():
            print("Correo electronico invalido. Ya esta registrado")
            return False
        
        # Comprobamos que las claves suministradas sean iguales.
        if clave1 != clave2:
            print("Clave invalida. Las claves no coinciden")
            return False
        
        # En caso 
        # Se guarda en el diccionario un par con el correo y la clave invertida
        self.usuarios[usuario] = clave1[::-1]
        return True

    """
    Recibe 2 strings una de usuario y una de clave.
    Retorna True si el usuario existe en el 
    diccionario y la clave es correcta.
    Retorna False en caso contrario.
    Imprime por la salida estandar un mensaje segun el caso.
    """
    def ingresarUsuario(self, usuario, clave) :
        # Comprobamos que el usuario aparezca en el diccionario.
        if usuario in self.usuarios.keys():
            # Comprobamos que la clave coincida con la guardada en el diccionario.
            if self.usuarios[usuario] == clave[::-1]:
                print("Usuario aceptado")
                return True
            else:
                print("Clave invalida")
                return False
        else:
            print("Usuario invalido")
            return False
