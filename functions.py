import numpy as np

from input_getter import  input_getter

def is_basis():
    dim, vec = input_getter()
    matrix = np.array(vec)
    rank = np.linalg.matrix_rank(matrix)

    if  rank == dim == len(vec):
        print(f"Your set of vectors is a basis in {dim}D dimension!\n")
    else:
        print(f"Your set of vectors is not basis in {dim}D dimension!\n")


def is_span():
    dim, vec = input_getter()
    matrix = np.array(vec)
    rank = np.linalg.matrix_rank(matrix)

    if rank == dim:
        print(f"Your set of vectors is a spanning set in {dim}D dimension!\n")
    else:
        print(f"Your set of vectors is not spanning set in {dim}D dimension!\n")
