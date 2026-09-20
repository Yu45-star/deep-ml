import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	# Your code here
	n = X.shape[1] # X.shape: (n, d), Y.shape :(n,)
	w = np.zeros(n)
	b = 0.0

	losses = []

	for i in range(iterations):
		z = X @ w + b

		p = 1 / (1 + np.exp(-z)) # (n,)

		# loss
		loss = - np.sum(y * np.log(p + 1e-10) + (1 - y) * np.log(1 - p + 1e-10))

		losses.append(round(loss, 4))

		dw = X.T @ (p - y)
		db = np.sum(p - y)

		# gradient descent
		w -= learning_rate * dw
		b -= learning_rate * db

	coefficients = np.concatenate(([b], w))
	coefficients = np.round(coefficients, 4).tolist()

	return coefficients, losses
