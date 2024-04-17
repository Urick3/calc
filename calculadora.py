import unittest
import math

class Calculadora:
    def __init__(self):
        pass

    def soma(self,x,y):
        return x+y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y
    
    def divisao(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y
    
    def raiz_quadrada(self, x):
        if x <= 0:
            raise ValueError("Não é possível calcular a raiz de zero.")
        return math.sqrt(x)


class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()
    
    def teste_soma(self):
        self.assertEqual(self.calc.soma(1,3), 4)
        self.assertEqual(self.calc.soma(300,400), 700)

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(5,4),1)
        self.assertNotEqual(self.calc.subtracao(5,2),4)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(2,3), 6)
        self.assertEqual(self.calc.multiplicacao(1,1), 1)
        self.assertEqual(self.calc.multiplicacao(0,0), 0)

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(6, 3), 2)
        self.assertEqual(self.calc.divisao(6, 3), 2)
     
    def test_raiz_quadrada(self):
        self.assertEqual(self.calc.raiz_quadrada(16),4)
        self.assertEqual(self.calc.raiz_quadrada(-2),3)
        

if __name__ == '__main__':
    unittest.main()