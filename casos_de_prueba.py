#!/usr/bin/python3
"""
Titulo: casos_de_prueba.py

Descripcion:

Autores:Leonardo Lopez     14-10576 
        Daniel Francis     12-10863

Equipo: Null Pointer Exception

Fecha: 09/05/2018.
"""

import unittest
from seguridad import *

class FuncionTestCase(unittest.TestCase):

    def test_SeguridadExists(self) -> 'void':
        prueba = Seguridad()

    def test_registrarUsuarioExists(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","clave","clave")

    def test_ingresarUsuarioExists(self) :
        S = Seguridad()
        S.ingresarUsuario("prueba@example.gg","clave")

    

if __name__ == "__main__":
    unittest.main()