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
        #assert(True)

if __name__ == "__main__":
    unittest.main()