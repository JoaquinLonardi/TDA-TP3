import unittest
from algoritmo import algoritmo_backtracking, leer_archivo


class TP3Test(unittest.TestCase):
    def test_5(self):
        B_conjuntos_prensa = leer_archivo('5.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(2, minimo)

    def test_7(self):
        B_conjuntos_prensa = leer_archivo('7.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 2)

    def test_10_pocos(self):
        B_conjuntos_prensa = leer_archivo('10_pocos.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 3)

    # def test_10_todos(self):
    #     B_conjuntos_prensa = leer_archivo('10_todos.txt')
    #     minimo = algoritmo_backtracking(B_conjuntos_prensa)
    #     self.assertEqual(minimo, 10)

    def test_10_varios(self):
        B_conjuntos_prensa = leer_archivo('10_varios.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 6)

    def test_15(self):
        B_conjuntos_prensa = leer_archivo('15.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 4)


    def test_20(self):
        B_conjuntos_prensa = leer_archivo('20.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 5)


    def test_50(self):
        B_conjuntos_prensa = leer_archivo('50.txt')
        minimo = algoritmo_backtracking(B_conjuntos_prensa)
        self.assertEqual(minimo, 6)

    # def test_75(self):
    #     B_conjuntos_prensa = leer_archivo('75.txt')
    #     minimo = algoritmo_backtracking(B_conjuntos_prensa)
    #     self.assertEqual(minimo, 8)
    #
    # def test_100(self):
    #     B_conjuntos_prensa = leer_archivo('100.txt')
    #     minimo = algoritmo_backtracking(B_conjuntos_prensa)
    #     self.assertEqual(minimo, 9)
    # def test_200(self):
    #     B_conjuntos_prensa = leer_archivo('200.txt')
    #     minimo = algoritmo_backtracking(B_conjuntos_prensa)
    #     self.assertEqual(minimo, 9)



if __name__ == '__main__':
    unittest.main()
