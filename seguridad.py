
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

        if not(re.match('[^\W_]',clave1)):
            print("Clave invalida. Contiene caracteres especiales")

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
        print("Usuario aceptado")
        return True