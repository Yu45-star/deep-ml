import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
	# Your code here
	mean = X.mean(axis = -1, keepdims=True)
	var = X.var(axis = -1, keepdims=True)

	X = (X - mean) / np.sqrt(var + epsilon)

	return gamma * X + beta