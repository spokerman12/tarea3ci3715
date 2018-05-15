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
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")

    def test_ingresarUsuarioExists(self) :
        S = Seguridad()
        S.ingresarUsuario("prueba@example.gg","Clave123")

    def test_ClavesIguales(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","Clave123","Clave123"))

    def test_ClavesDiferentes(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave123","Clave1232"))

    def test_CamposVacios(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("","",""))

    def test_UsuarioYaExiste(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave1232","Clave1232"))

    def test_DosUsuariosMismaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertTrue(S.registrarUsuario("prueba2@example.gg","Clave123","Clave123"))

    def test_VolteaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertEqual(S.usuarios["prueba@example.gg"],"321evalC")

    def test_UsuarioNoSigueFormato(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("pruebaexample.gg","Clave123","Clave123"))

    def test_ClaveConCaracteres(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","Clave123!@#","Clave123!@#"))

    def test_ClaveMuyLarga(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave123Clave123Clave123Clave123Clave123","Clave123Clave123Clave123Clave123Clave123"))

    def test_ClaveMuyCorta(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave","Clave"))

    def test_ClaveLen7(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","123Cla7","123Cla7"))

    def test_ClaveLen8(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","123Cla78","123Cla78"))

    def test_ClaveLen9(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","123Cla789","123Cla789"))

    def test_ClaveLen15(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","0123Cla78912345","0123Cla78912345"))

    def test_ClaveLen16(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","0123Cla789123Cla","0123Cla789123Cla"))

    def test_ClaveLen17(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","0123Cla789123Cla7","0123Cla789123Cla7"))

if __name__ == "__main__":
    unittest.main()