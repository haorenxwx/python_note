#59.py
n = 4

top,bot,left,right = 0,n-1,0,n-1
num = 1
result = [[0 for __ in range(n)] for __ in range(n)]
while bot>top and right>left:
    for i in range(left,right):
        result[top][i] = num
        num+=1
    for j in range(top,bot):
        result[j][right] = num
        num+=1
    for i in reversed(xrange(left+1,right+1)):
    #for i in range(right,left,-1):
        result[bot][i] = num
        num+=1
    for j in reversed(xrange(top+1,bot+1)):
    #for j in range(bot,top,-1):
        result[j][left] = num
        num+=1

    top,bot,left,right = top+1,bot-1,left+1,right-1
    print(top,bot,left,right)
if right == left and top == bot:
    result[top][left] = num
print(result)