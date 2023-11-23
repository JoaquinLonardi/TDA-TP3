import unittest
from algoritmo import leer_archivo
from programacion_lineal import hitting_set

class TP3Test(unittest.TestCase):
    def test_5(self):
        B_conjuntos_prensa = leer_archivo("../archivos_prueba/5.txt")
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(2, minimo)

    def test_7(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/7.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 2)

    def test_10_pocos(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/10_pocos.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 3)

    def test_10_todos(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/10_todos.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 10)

    def test_10_varios(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/10_varios.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 6)

    def test_15(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/15.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 4)


    def test_20(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/20.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 5)


    def test_50(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/50.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 6)

    def test_75(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/75.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 8)

    def test_100(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/100.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 9)
    def test_200(self):
        B_conjuntos_prensa = leer_archivo('../archivos_prueba/200.txt')
        minimo = hitting_set(B_conjuntos_prensa)
        self.assertEqual(minimo, 9)



if __name__ == '__main__':
    unittest.main()
