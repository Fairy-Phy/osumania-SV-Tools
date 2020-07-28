def aperys_constant(digit: int) -> str:
	from sympy import N, zeta
	return str(N("zeta(3)", digit))

if __name__ == "__main__":
	digit = 10000
	print(aperys_constant(digit))
