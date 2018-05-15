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

    def test_ClavesIguales(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","clave","clave"))

    def test_ClavesDiferentes(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","clave","clave2"))

    def test_CamposVacios(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("","",""))

    def test_UsuarioYaExiste(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","clave","clave")
        self.assertFalse(S.registrarUsuario("prueba@example.gg","clave2","clave2"))

    def test_DosUsuariosMismaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","clave","clave")
        self.assertTrue(S.registrarUsuario("prueba2@example.gg","clave","clave"))

    def test_VolteaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","clave","clave")
        self.assertEqual(S.usuarios["prueba@example.gg"],"evalc")

    def test_UsuarioNoSigueFormato(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("pruebaexample.gg","clave","clave"))


    def test_ClaveConCaracteres(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","clave!@#","clave!@#"))

if __name__ == "__main__":
    unittest.main()