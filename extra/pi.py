def pi(digit: int) -> str:
	from sympy import N, atan
	return str(N("((12 * atan(1/49)) + (32 * atan(1/57)) - (5 * atan(1/239)) + (12 * atan(1/110443))) * 4", digit))

if __name__ == "__main__":
	digit = 10000
	print(pi(digit))
