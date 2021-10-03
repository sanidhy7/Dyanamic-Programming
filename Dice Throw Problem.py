# Python program
# The main function that returns number of ways to get sum 'x'
# with 'n' dice and 'm' with m faces.


def findWays(f, d, s):
	mem = [[0 for i in range(s+1)] for j in range(d+1)]
	mem[0][0] = 1
	for i in range(1, d+1):


		for j in range(1, s+1):
			mem[i][j] = mem[i][j - 1] + mem[i - 1][j - 1]
			if j - f - 1 >= 0:
				mem[i][j] -= mem[i - 1][j - f - 1]
	return mem[d][s]

print(findWays(4, 2, 1))
print(findWays(2, 2, 3))
print(findWays(6, 3, 8))
print(findWays(4, 2, 5))
print(findWays(4, 3, 5))


