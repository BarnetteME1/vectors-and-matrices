from functools import reduce

class ShapeException(Exception):
    pass


def dot(vector_1, vector_2):
    new_vector = []
    if shape_exception_vxv(vector_1, vector_2) == True:
        vec_len = range(0,len(vector_1))
        for pos in vec_len:
            new_vector.append(vector_1[pos]*vector_2[pos])
    return reduce(lambda x, y: x+y, new_vector)


def magnitude(vector):
    scalar = 0
    vector_len = len(vector)
    for spot in range(0, vector_len):
        scalar += (vector[spot] **2)
    return (scalar **(1/2))


def shape(vertrices):
    length = []
    column = []
    length.append(len(vertrices))
    for list in vertrices:
        try:
            column = (len(list))
        except:
            continue
    if column != []:
        length.append(column)
    return tuple(length)


def vector_add(vector_1, vector_2):
    new_vector = []
    if shape_exception_vxv(vector_1, vector_2) == True:
        vec_len = range(0,len(vector_1))
        for pos in vec_len:
            new_vector.append(vector_1[pos] + vector_2[pos])
    return new_vector


def vector_sub(vector_1, vector_2):
    new_vector = []
    if shape_exception_vxv(vector_1, vector_2) == True:
        vec_len = range(0,len(vector_1))
        for pos in vec_len:
            new_vector.append(vector_1[pos] - vector_2[pos])
    return new_vector


def vector_sum(*vectors):
    vec_len = len(vectors[0])
    posi = 0
    new_vec = []
    for pos in range(0, vec_len):
        new_number = 0
        for vector in vectors:
            new_number += vector[pos]
        new_vec.append(new_number)
    return new_vec


def vector_multiply(vector_1, scalar):
    new_vector = []
    vec_len = range(0,len(vector_1))
    for pos in vec_len:
        new_vector.append(vector_1[pos] *scalar)
    return new_vector


def vector_mean(*vectors):
    new_vector = vector_sum(*vectors)
    len_vectors = len(vectors)
    multi_vector = vector_multiply(new_vector, (1/len_vectors))
    return multi_vector


def matrix_row(matrix, num):
    return matrix[num]


def matrix_col(matrix, num):
    col = []
    for line in matrix:
        col.append(line[num])
    return col


def matrix_scalar_multiply(matrix, scalar):
    new_matrix = []
    for row in matrix:
        new_row = 0
        for column in row:
            new_row += column * scalar
        new_matrix.append(new_row)
    return new_matrix


def matrix_vector_multiply(matrix, vector):
    len_vec = len(vector)
    new_vec = []
    for row in matrix:
        number = 0
        for pos in range(0,len_vec):
            number += (vector[pos] * row[pos])
        new_vec.append(number)
    return new_vec


def matrix_matrix_multiply(matrix_1, matrix_2):
    new_matrix = []
    len_m2_row = len(matrix_2[0])
    len_m2_col = len(matrix_2)
    len_m1_row = len(matrix_1[0])
    len_m1_col = len(matrix_1)
    new_m2 = []
    for pos2 in range(len_m2_row):
        new_m2_row = []
        new_m2_row += matrix_col(matrix_2, pos2)
        new_m2.append(new_m2_row)
    for posit in range(0, len_m1_col):
        new_row = []
        for posi in range(0,len_m2_row):
            new_num = 0
            for pos in range(0, len_m1_row):
                new_num += (matrix_1[posit][pos] * new_m2[posi][pos])
            new_row.append(new_num)
        new_matrix.append(new_row)
    return new_matrix
