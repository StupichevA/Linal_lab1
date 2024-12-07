import unittest
from class_matrix import csr_Matrix, sum_csr, mult_csr, mult_num
from determinator import det

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [0, 2, 4, 6],
            [1, 0, 3, 0],
            [0, 0, 0, 0],
            [0, 3, 0, 4]
        ]

        self.matrix2 = [
            [3, 1, 7, 4],
            [1, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 4, 5, 0]
        ]

        self.sum = [
            [3, 3, 11, 10],
            [2, 0, 3, 2],
            [0, 0, 0, 0],
            [2, 7, 5, 4]
        ]
        self.mult_2 = [
            [0, 4, 8, 12],
            [2, 0, 6, 0],
            [0, 0, 0, 0],
            [0, 6, 0, 8]
        ]
        self.mult = [
            [14, 24, 30, 4],
            [3, 1, 7, 4],
            [0, 0, 0, 0],
            [11, 16, 20, 6]
        ]
        self.csr = csr_Matrix(self.matrix)
        self.csr2 = csr_Matrix(self.matrix2)
        self.s_csr = csr_Matrix(self.sum)
        self.mn_csr = csr_Matrix(self.mult_2)
        self.m_csr = csr_Matrix(self.mult)

        self.m = [
            [1,7,3,4,5],
            [2,4,4,5,6],
            [3,7,8,6,7],
            [4,5,6,7,3],
            [5,6,9,8,9],
        ]

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_csr_matrix(self):
        self.assertEqual(self.csr.get_CSRx(), [2,4,6,1,3,3,4])
        self.assertEqual(self.csr.get_CSRi(), [1,2,3,0,2,1,3])
        self.assertEqual(self.csr.get_CSRp(), [0,3,5,5,7])

    def test_get_elem(self):
        self.assertEqual(self.csr.get_elem(0,0),self.matrix[0][0])
        self.assertEqual(self.csr.get_elem(1, 0), self.matrix[1][0])
        self.assertEqual(self.csr.get_elem(2, 2), self.matrix[2][2])

    def test_trace(self):
        self.assertEqual(self.csr.trace(), 4)

    def test_sum_csr(self):
        self.assertEqual(sum_csr(self.csr, self.csr2).CSRx, self.s_csr.CSRx)
        self.assertEqual(sum_csr(self.csr, self.csr2).CSRi, self.s_csr.CSRi)
        self.assertEqual(sum_csr(self.csr, self.csr2).CSRp, self.s_csr.CSRp)

    def test_mult_num(self):
        self.assertEqual(mult_num(self.csr, 2).CSRx, self.mn_csr.CSRx)
        self.assertEqual(mult_num(self.csr, 2).CSRi, self.mn_csr.CSRi)
        self.assertEqual(mult_num(self.csr, 2).CSRp, self.mn_csr.CSRp)

    def test_mult_csr(self):
        self.assertEqual(mult_csr(self.csr, self.csr2).CSRx, self.m_csr.CSRx)
        self.assertEqual(mult_csr(self.csr, self.csr2).CSRi, self.m_csr.CSRi)
        self.assertEqual(mult_csr(self.csr, self.csr2).CSRp, self.m_csr.CSRp)

    def determinator(self):
        self.assertEqual(det(self.matrix), 0)
        self.assertEqual(det(self.m), 315)

if __name__ == '__main__':
    unittest.main()
