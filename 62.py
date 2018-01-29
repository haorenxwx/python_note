#62.py
m = 4
n = 6


matric = [[1 for i in range(n)] for i in range(m)]
print(matric)

for i in range(1,m):
	for j in range(1,n):
		matric[i][j] = matric[i-1][j]+matric[i][j-1]
print(matric[-1][-1])

