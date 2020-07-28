def gelfonds_constant(digit: int) -> str:
	from sympy import N, I
	return str(N("(-1) ** -I", digit))

if __name__ == "__main__":
	digit = 10000
	print(gelfonds_constant(digit))
