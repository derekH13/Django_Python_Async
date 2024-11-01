import unittest

from math_operations import addition_operation, subtration_operation


class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        # USANDO UMA FUNÇÃO QUE AINDA NÃO EXISTE
        math_addition_result = addition_operation(num_1=5, num_2=10)
        # o resultado tem que ser igual á 15
        self.assertEqual(math_addition_result, 15)

    def test_subtration_operation(self):
        # USANDO UMA FUNÇÃO QUE AINDA NÃO EXISTE
        math_subtcration_result = subtration_operation(num_1=10, num_2=10)
        # VERIFICANDO SE O RESULTADO FOI COMO ESPERADO
        self.assertEqual(math_subtcration_result, 0)


if __name__ == '__main__':
    unittest.main()
