class csr_Matrix:
    def __init__(self, m):
        self.rows = len(m)
        self.cols = len(m[0])
        self.CSRx = []
        self.CSRi = []
        self.CSRp = [0]
        for i in range(self.rows):
            number_of_not_0_elem = 0
            for j in range(self.cols):
                if m[i][j] != 0:
                    self.CSRx.append(m[i][j])
                    self.CSRi.append(j)
                    number_of_not_0_elem += 1
            self.CSRp.append(number_of_not_0_elem + self.CSRp[-1])

    def get_CSRx(self):
        return self.CSRx

    def get_CSRp(self):
        return self.CSRp

    def get_CSRi(self):
        return self.CSRi

    def print_matrix(self):
        print(self.CSRx)
        print(self.CSRi)
        print(self.CSRp)

    def print_csc_matrix(self):
        print(self.CSCx)
        print(self.CSRi)
        print(self.CSRp)

    def get_elem(self, row, col):
        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
            print("row or col out of bounds")
        else:
            for i in range(self.CSRp[row], self.CSRp[row + 1]):
                if self.CSRi[i] == col:
                    return self.CSRx[i]
            return 0

    def trace(self):
        if self.rows != self.cols:
            print("Matrix trace failed, matrix is not a square matrix")
        else:
            trace = 0
            for i in range(self.rows):
                trace += self.get_elem(i, i)
            return trace

    def csr_to_csc(self):
        nnz = len(self.CSRx)

        self.CSCx = [0 for _ in range(nnz)]
        self.CSCi = [0 for _ in range(nnz)]
        self.CSCp = [0 for _ in range(self.cols + 1)]

        for k in range(nnz):
            self.CSCp[self.CSRi[k] + 1] += 1

        for i in range(1, self.cols + 1):
            self.CSCp[i] += self.CSCp[i - 1]

        for row in range(self.rows):
            for j in range(self.CSRp[row], self.CSRp[row + 1]):
                col = self.CSRi[j]
                dest = self.CSCp[col]

                self.CSCi[dest] = row
                self.CSCx[dest] = self.CSRx[j]
                self.CSCp[col] += 1
        self.CSCp = [0] + self.CSCp
        self.CSCp.pop(-1)



def sum_csr(m1: csr_Matrix, m2: csr_Matrix):
    assert (m1.rows == m2.rows or m1.cols == m2.cols), 'matrix are different sizes'
    m = csr_Matrix([[]])
    m.rows = m1.rows
    m.cols = m1.cols
    m.CSRp.pop()

    for i in range(m1.rows):
        left1 = m1.CSRp[i]
        left2 = m2.CSRp[i]
        count = 0
        while left1 < m1.CSRp[i+1] and left2 < m2.CSRp[i+1]:
            if m1.CSRi[left1] < m2.CSRi[left2]:
                m.CSRx.append(m1.CSRx[left1])
                m.CSRi.append(m1.CSRi[left1])
                left1 += 1
            elif m1.CSRi[left1] > m2.CSRi[left2]:
                m.CSRx.append(m2.CSRx[left2])
                m.CSRi.append(m2.CSRi[left2])
                left2 += 1
            else:
                m.CSRx.append(m1.CSRx[left1] + m2.CSRx[left2])
                m.CSRi.append(m1.CSRi[left1])
                left1 += 1
                left2 += 1
                count += 1
        while left1 < m1.CSRp[i+1]:
            m.CSRx.append(m1.CSRx[left1])
            m.CSRi.append(m1.CSRi[left1])
            left1 += 1
        while left2 < m2.CSRp[i+1]:
            m.CSRx.append(m2.CSRx[left2])
            m.CSRi.append(m2.CSRi[left2])
            left2 += 1
        m.CSRp.append(m1.CSRp[i+1] - m1.CSRp[i] + m2.CSRp[i+1] - m2.CSRp[i] - count + m.CSRp[-1])
    return m


def mult_num(m: csr_Matrix, n: int):
    for i in range(len(m.CSRx)):
        m.CSRx[i] *= n
    return m



def mult_csr(m1: csr_Matrix, m2: csr_Matrix):
    assert (m1.cols == m2.rows), 'Matrix can not be multiplied. Please choose matrixs sizes N*M M*K'
    m = csr_Matrix([[]])
    m.rows = m1.rows
    m.cols = m2.cols
    m2.csr_to_csc()
    m.CSRp.pop()

    for i in range(m1.rows):
        for j in range(m2.cols):
            x = [-1]*m1.cols
            s = 0
            for v1 in range(m1.CSRp[i], m1.CSRp[i+1]):
                x[m1.CSRi[v1]] = v1
            for v2 in range(m2.CSCp[j], m2.CSCp[j+1]):
                if x[m2.CSCi[v2]] != -1:
                    s += m1.CSRx[x[m2.CSCi[v2]]] * m2.CSCx[v2]
            if s != 0:
                m.CSRx.append(s)
                m.CSRi.append(j)
        m.CSRp.append(len(m.CSRx))
    return m




def inp():
    matrix = []
    print("Input N and M")
    n, m = map(int, input().split())
    print('Input elements of m with space separated:')
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return csr_Matrix(matrix)


