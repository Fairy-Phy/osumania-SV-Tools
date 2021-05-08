"""
ネイピア数
"""

def napiers_constant(digit: int) -> str:
	from sympy import N, exp
	return str(N("exp(1)", digit))

if __name__ == "__main__":
	digit = 10000
	print(napiers_constant(digit))
