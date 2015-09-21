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
    if shape_exception_vxv(vector_1, vector_2) == True:
        vec_len = range(0,len(vector_1))
        for pos in vec_len:
            new_vector.append(vector_1[pos] - vector_2[pos])
    return new_vector


def vector_mean():
    pass


def matrix_row(matrix):
    pass


def matrix_col():
    pass


def matrix_vector_multiply(matrix, scalar):
    new_matrix = []
    for row in matrix:
        new_row = 0
        for column in row:
            new_row += column * scalar
        new_matrix.append(new_row)
    return new_matrix


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
