def det(m): # Вычисление определителя с помощью Гаусса
    assert m == [[]], 'Matrix is empty'
    assert len(m) != len(m[0]), 'Not square matrix'
    n = len(m)
    det = 1

    for i in range(n):

        x = i
        if m[i][i] == 0:
            flag = True
            for y in range(i + 1, n):
                if m[y][i] != 0:
                    flag = False
                    x = y
                    break
            if flag:
                return 0
            else:
                m[i], m[x] = m[x], m[i]
                det *= -1

        for j in range(i + 1, n):
            det *= m[i][i]
            factor = m[j][i] / m[i][i]
            for k in range(i, n):
                m[j][k] -= factor * m[i][k]

    return det

def has_matrix_opposite(m):
    d = det(m)
    if d(m) != 0:
        print(f'Matrix has opposite det, det = {d}')
    else:
        print('Matrix has not opposite det, det = 0')