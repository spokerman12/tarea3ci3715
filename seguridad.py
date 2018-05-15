
#!/usr/bin/python3
"""
Titulo: 

Descripcion: Implementacion de la clase Seguridad

Autores:Leonardo Lopez     14-10576 
        Daniel Francis     12-10863
         

Equipo: Null Pointer Exception

Fecha:/05/2018.
"""


class Seguridad():

    def __init__(self):
        self.usuarios = {}

    def registrarUsuario(self, usuario, clave1, clave2):
        #assert(not(usuario in self.usuarios.keys()))
        #assert(clave1 == clave2)
        if usuario in self.usuarios.keys() or clave1 != clave2 :
            return False
        self.usuarios[usuario] = clave1
        return True

    def ingresarUsuario(self, usuario, clave) :
        print("Usuario aceptado")
        return True