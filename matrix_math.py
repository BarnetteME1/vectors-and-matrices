class ShapeException(Exception):
    pass


def dot(vector_1, vector_2):
    new_vector = []
    if shape_exception_vxv(vector_1, vector_2) == True:
        vec_len = range(0,len(vector_1))
        for pos in vec_len:
            new_vector.append(vector_1[pos]*vector_2[pos])
    return reduce(lambda x, y: x+y, new_vector)


def magnitude():
    pass


def shape():
    pass


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


def vector_sum():
    pass


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
