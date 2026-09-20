import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	z = X @ weights + bias

	z = np.clip(z, a_min=-500, a_max=500)

	p = 1 / (1 + np.exp(-z))

	return (p >= 0.5).astype(int)

