import numpy as np


def Product(a1, b1, a2, b2):
    AsBs = np.array([a1*a2, a1*b2+a2*b1])
    return(AsBs)
