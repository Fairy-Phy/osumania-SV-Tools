def golden_ratio(digit: int) -> str:
	from sympy import N, sqrt
	return str(N("(1 + sqrt(5)) / 2", digit))

if __name__ == "__main__":
	digit = 10000
	print(golden_ratio(digit))
