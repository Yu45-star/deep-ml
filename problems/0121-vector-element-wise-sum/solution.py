def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	n = len(a)
	m = len(b)
	if n != m: return -1

	res = []

	cur = 0
	for i in range(n):
		cur = a[i] + b[i]
		res.append(cur)

	return res
