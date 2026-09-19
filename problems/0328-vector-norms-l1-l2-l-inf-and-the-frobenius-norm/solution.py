import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == 'l1':
        norm = np.abs(arr).sum()

    elif norm_type == 'l2':
        norm =  np.sqrt((arr ** 2).sum())

    elif norm_type == 'linf':
        norm = np.abs(arr).max()

    elif norm_type == 'frobenius':
        if len(arr.shape) != 2:
            raise ValueError()
        else:
            norm = np.sqrt((arr ** 2).sum())
    else:
        raise ValueError()

    return float(norm)
    
