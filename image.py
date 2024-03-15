import numpy as np

def add_padding(M):
    """
    Ajoute un padding à la matrice afin que ses dimensions soient divisibles par 4
    """
    lines = M.shape[0] % 4
    cols = M.shape[1] % 4
    if lines or cols:
        res = np.zeros((
            M.shape[0]+lines,
            M.shape[1]+cols,
            3,
        ), dtype=np.uint8)
        res[:res.shape[0]-lines, :res.shape[1]-cols] = M
        return res, (lines, cols)
    return M, (lines, cols)

def remove_padding(M, pad):
    """
    Retire le padding de la matrice
    """
    return M[:M.shape[0]-pad[0], :M.shape[1]-pad[1]]
