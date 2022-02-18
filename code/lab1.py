list_for_equivalent_closure = set()


def make_set(matrix, size):

    set_view = []

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                set_view.append((i + 1, j + 1))
    return sorted(set_view)


def matrix_set_view(matrix_set, flag=None):
    if not flag:
        print('Исходное отношение: {', end='')
        print(*matrix_set, sep=', ', end='}\n')
    else:
        print('{', end='')
        print(*matrix_set, sep=', ', end='; ')


def make_reflexive(matrix, size):

    m_reflexive = []

    for i in range(size):
        if matrix[i][i] == 0:
            m_reflexive.append((i + 1, i + 1))
            list_for_equivalent_closure.add((i + 1, i + 1))

    print(*sorted(m_reflexive), sep=', ', end='}\n\n')


def make_symmetric(matrix, size):

    m_symmetric = []

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                m_symmetric.append((j + 1, i + 1))
                list_for_equivalent_closure.add((j + 1, i + 1))

    print(*sorted(m_symmetric), sep=', ', end='}\n\n')


def make_transitive(copy, size):

    m_transitive = []
    for _ in range(size):
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if copy[k][i] == copy[i][j] == 1 and copy[k][j] == 0:
                        m_transitive.append((k + 1, j + 1))
                        copy[k][j] = 1
                        list_for_equivalent_closure.add((k + 1, j + 1))

    print(*sorted(m_transitive), sep=', ', end='}\n\n')


def is_transitive(matrix, size):

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[k][i] == matrix[i][j] == 1 and matrix[k][j] == 0:
                    return False
    return True


def is_symmetric_or_antisymmetric(matrix, size):

    flag_symmetric = True
    flag_antisymmetric = True

    for i in range(size):
        for j in range(size):
            if not matrix[i][j] == matrix[j][i]:
                flag_symmetric = False
            elif matrix[i][j] == matrix[j][i] and not i == j:
                flag_antisymmetric = False
            elif not flag_symmetric and not flag_antisymmetric:
                return False, False

    return flag_symmetric, flag_antisymmetric


def is_reflexive_or_anti_reflexive(matrix, size):

    flag_reflexive = True
    flag_anti_reflexive = True

    for i in range(size):
        if matrix[i][i] == 0:
            flag_reflexive = False
        elif matrix[i][i] == 1:
            flag_anti_reflexive = False
        if not flag_reflexive and not flag_anti_reflexive:
            return False, False

    return flag_reflexive, flag_anti_reflexive


def get_data():
    n = int(input())
    m = [[int(elem) for elem in input().split()] for _ in range(n)]
    m_set = [(i + 1, j + 1) for i in range(n) for j in range(n) if m[i][j] == 1]
    return m, sorted(m_set), n


matrix, matrix_set, size = get_data()

print('Свойства бинарного отношения:')

reflexive, anti_reflexive = is_reflexive_or_anti_reflexive(matrix, size)
if reflexive:
    print('Отношение является рефлексивным')
elif not reflexive:
    print('Отношение не является рефлексивным')
if anti_reflexive:
    print('Отношение является антирефлексивным')
else:
    print('Отношение не является антирефлексивным')


symmetric, antisymmetric = is_symmetric_or_antisymmetric(matrix, size)
if symmetric:
    print('Отношение является симметричным')
elif not symmetric:
    print('Отношение не является симметричным')
if antisymmetric:
    print('Отношение является антисимметричным')
else:
    print('Отношение не является антисимметричным')


transitive = is_transitive(matrix, size)
if transitive:
    print('Отношение является транзитивным')
else:
    print('Отношение не является транзитивным')

print('\n')
print('Тип бинарного отношения:')

quasi_order = True if transitive and reflexive else False
if quasi_order:
    print('Отношение является отношением квазипорядка')
    if quasi_order and symmetric:
        print('Отношение является отношением эквивалентности')
    if quasi_order and antisymmetric:
        print('Отношение является отношением частичного порядка')
else:
    print('Отношение не является ни отношением квазипорядка, ни эквивалентности, ни частичного порядка')
print('\n')

matrix_set_view(matrix_set)
if not reflexive:
    print('Замыкание отношения относительно рефлексивности: ', end='')
    matrix_set_view(matrix_set, 1)
    make_reflexive(matrix, size)

if not symmetric:
    print('Замыкание отношения относительно симметричности: ', end='')
    matrix_set_view(matrix_set, 1)
    make_symmetric(matrix, size)

if not transitive:
    copy = matrix
    print('Замыкание отношения относительно транзитивности: ', end='')
    matrix_set_view(matrix_set, 1)
    make_transitive(copy, size)


print('Замыкание отношения относительно эквивалентности: ')
matrix_set_view(matrix_set, 1)
print(*sorted(list_for_equivalent_closure), sep=', ', end='}\n\n')

'''
Примеры входных данных:

4
0 1 1 0
1 1 1 0
0 1 1 0
0 0 0 1

4
0 1 0 0
0 0 0 0
0 0 0 1
0 1 0 0

3 
0 1 0
0 0 1
1 0 0
'''