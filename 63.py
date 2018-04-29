#63.py
obstacleGrid = [[0,1,0,0,1],[0,1,0,0,0],[1,0,0,0,1],[0,1,0,0,0]]
print(obstacleGrid)
m = len(obstacleGrid)
n = len(obstacleGrid[0])
for i in range(m):
    if obstacleGrid[i][0] == 1:
        for i in range(i,m):
            obstacleGrid[i][0] = 0
    	break
    else:
        obstacleGrid[i][0] = 1
for i in range(1,n):
    if obstacleGrid[0][i] == 1:
        for i in range(i,n):
            obstacleGrid[0][i] = 0
    	break
    else:
        obstacleGrid[0][i] = 1
print(obstacleGrid)