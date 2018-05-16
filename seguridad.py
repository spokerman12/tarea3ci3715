
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
        self.usuarios = {}

    def registrarUsuario(self, usuario, clave1, clave2):
        #assert(not(usuario in self.usuarios.keys()))

        if not (re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',usuario)):
            print("Correo electronico invalido. No sigue el formato")
            return False

        if not(8 <= len(clave1) <= 16) :
            print("Clave invalida. Longitud debe estar entre 8 y 16 caracteres")
            return False

        if not(re.match('[^\W_]',clave1)):
            print("Clave invalida. Contiene caracteres especiales")
            return False

        m = 0
        M = 0
        d = False
        for a in list(clave1) :
            if a.isupper() :
                M+=1
            if a.islower() :
                m+=1
            if a.isdigit():
                d = True

        if M == 0 or m == 0 or m+M < 3 or d == False:
            print("Clave invalida. Debe incluir un numero y al menos 3 letras, una mayuscula y una minuscula")
            return False

        if usuario in self.usuarios.keys():
            print("Correo electronico invalido. Ya esta registrado")
            return False
        if clave1 != clave2:
            print("Clave invalida. Las claves no coinciden")
            return False
        if clave1 == "":
            print("Clave invalida. No puede ser vacia")
            return False
        self.usuarios[usuario] = clave1[::-1]
        return True

    def ingresarUsuario(self, usuario, clave) :
        print(self.usuarios)
        if usuario in self.usuarios.keys():
            if self.usuarios[usuario] == clave[::-1]:
                print("Usuario aceptado")
                return True
            else:
                print("Clave invalida")
                return False
        else:
            print("Usuario invalido")
            return False
