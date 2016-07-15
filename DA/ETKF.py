# -*- coding: utf-8 -*-

"""
Ensemble Transform Kalman Filter

Notations
----------
N : int
    length of state vector
p : int
    length of observation vector
K : int
    Number of ensembles

H : scipy.sparse.linalg.LinearOperator, (N) -> (p)
    Observation operator. **Assume Linear**.

"""

import numpy as np
from .linalg import symmetric_square_root
from . import ensemble


def analysis(H, R):
    R_inv = np.linalg.inv(R)

    def update(xs, yO):
        xb, Xb = ensemble.deviations(xs)
        _, k = Xb.shape
        yb = H(xb)
        Yb = H(Xb)
        YR = np.dot(Yb.T, R_inv)
        Pa = np.linalg.inv(np.dot(YR, Yb) + (k-1)*np.identity(k))
        wa = np.dot(Pa, np.dot(YR, yO - yb))
        Wa = symmetric_square_root((k-1)*Pa)
        return ensemble.reconstruct(xb + np.dot(Xb, wa), np.dot(Xb, Wa))
    return update
