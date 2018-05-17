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
    
    # Comprueba que existe la clase seguridad.
    # Tipo: Arbitrario.
    def test_SeguridadExists(self) -> 'void':
        prueba = Seguridad()

    # Comprueba que existe el metodo registrarUsuario.
    # Tipo: Arbitrario.
    def test_registrarUsuarioExists(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")

    # Comprueba que existe el metodo ingresarUsuario.
    # Tipo: Arbitrario.
    def test_ingresarUsuarioExists(self) :
        S = Seguridad()
        S.ingresarUsuario("prueba@example.gg","Clave123")

    # Registrando un usuario proporcionando 2 claves iguales.
    # Tipo: Frontera.
    def test_ClavesIguales(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","Clave123","Clave123"))

    # Registrando un usuario proporcionando 2 claves distintas.
    # Tipo: Frontera.
    def test_ClavesDiferentes(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave123","Clave1232"))

    # Caso de prueba con todos los campos vacios.
    # Tipo: Frontera.
    def test_CamposVacios(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("","",""))

    # Registrando un usuario con un email que ya esta registrado.
    # Tipo: Frontera.
    def test_UsuarioYaExiste(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave1232","Clave1232"))

    # Registrando un usuario con un email que ya esta registrado.
    # Tipo: Malicia.
    def test_DosUsuariosMismaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertTrue(S.registrarUsuario("prueba2@example.gg","Clave123","Clave123"))

    # Comprobando que la clave se voltea correctamente..
    # Tipo: Malicia.
    def test_VolteaClave(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","Clave123","Clave123")
        self.assertEqual(S.usuarios["prueba@example.gg"],"321evalC")

    # Registrando un usuario con un email que no sigue el estandar.
    # Tipo: Esquina.
    def test_UsuarioNoSigueFormato(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("pruebaexample.gg","Clave123","Clave123"))

    # Registrando un usuario con una clave con caracteres especiales.
    # Tipo: Esquina.
    def test_ClaveConCaracteres(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave123!@#","Clave123!@#"))

    # Registrando un usuario con una clave demasiado larga.
    # Tipo: Malicia.
    def test_ClaveMuyLarga(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave123Clave123Clave123Clave123Clave123","Clave123Clave123Clave123Clave123Clave123"))

    # Registrando un usuario con una clave demasiado corta.
    # Tipo: Malicia.
    def test_ClaveMuyCorta(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","Clave","Clave"))

    # Registrando un usuario con una clave de longitud 7.
    # Tipo: Esquina.
    def test_ClaveLen7(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","123Cla7","123Cla7"))

    # Registrando un usuario con una clave de longitud 8.
    # Tipo: Frontera.
    def test_ClaveLen8(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","123Cla78","123Cla78"))

    # Registrando un usuario con una clave de longitud 9.
    # Tipo: Esquina.
    def test_ClaveLen9(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","123Cla789","123Cla789"))

    # Registrando un usuario con una clave de longitud 15.
    # Tipo: Esquina.
    def test_ClaveLen15(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","0123Cla78912345","0123Cla78912345"))

    # Registrando un usuario con una clave de longitud 16.
    # Tipo: Frontera.
    def test_ClaveLen16(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","0123Cla789123Cla","0123Cla789123Cla"))

    # Registrando un usuario con una clave de longitud 17.
    # Tipo: Esquina.
    def test_ClaveLen17(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","0123Cla789123Cla7","0123Cla789123Cla7"))

    # Registrando un usuario con una clave de solo minusculas.
    # Tipo: Esquina.
    def test_ClaveMinusculas(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","asdfghjk1","asdfghjk1"))

    # Registrando un usuario con una clave de solo mayusculas.
    # Tipo: Esquina.
    def test_ClaveMayusculas(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","ASDFGHJK1","ASDFGHJK1"))

    # Registrando un usuario con una clave con una sola minuscula.
    # Tipo: Frontera.
    def test_Clave1May1min(self) :
        S = Seguridad()
        self.assertTrue(S.registrarUsuario("prueba@example.gg","ASDFGHJKl1","ASDFGHJKl1"))

    # Registrando un usuario con una clave sin digitos.
    # Tipo: Frontera.
    def test_ClaveNoNum(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","ASDFGHJKl","ASDFGHJKl"))

    # Registrando un usuario con una sola letra.
    # Tipo: Esquina.
    def test_ClaveSoloNum1Letra(self) :
        S = Seguridad()
        self.assertFalse(S.registrarUsuario("prueba@example.gg","1234567A","1234567A"))

    # Ingresando un usuario de manera correcta.
    # Tipo: Malicia.
    def test_ingresarUsuarioCorrecto(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","1234567Aaa","1234567Aaa")
        self.assertTrue(S.ingresarUsuario("prueba@example.gg","1234567Aaa"))

    # Ingresando un usuario que no esta registrado
    # Tipo: Esquina.
    def test_ingresarUsuarioInexistente(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","1234567Aaa","1234567Aaa")
        self.assertFalse(S.ingresarUsuario("manolo@example.gg","1234567Aaa"))

    # Ingresando un usuario con una clave incorrecta.
    # Tipo: Esquina.
    def test_ingresarUsuarioClaveIncorrecta(self) :
        S = Seguridad()
        S.registrarUsuario("prueba@example.gg","1234567Aaa","1234567Aaa")
        self.assertFalse(S.ingresarUsuario("prueba@example.gg","0234567Aaa"))

if __name__ == "__main__":
    unittest.main()