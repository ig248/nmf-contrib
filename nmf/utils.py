import numpy as np
import scipy.sparse as sp


def check_non_negative(X, whom, accept_nan=False):
    """
    Check if there is any negative value in an array.

    Parameters
    ----------
    X : array-like or sparse matrix
        Input data.

    whom : string
        Who passed X to this function.

    accept_nan : boolean
        If True, NaN values are accepted in X.
    """
    # avoid X.min() on sparse matrix since it also sorts the indices
    if sp.issparse(X):
        if X.format in ['lil', 'dok']:
            X = X.tocsr()
        if X.data.size == 0:
            X = np.arange(1)
        else:
            X = X.data

    if accept_nan:
        X_min = np.nanmin(X)
    else:
        X_min = np.min(X)
        if np.isnan(X_min):
            raise ValueError("NaN values in data passed to %s" % whom)

    if X_min < 0:
        raise ValueError("Negative values in data passed to %s" % whom)
