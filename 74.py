#74.py


matrix = [[1],[3]]

target = 2

if not matrix:
    print False
if not matrix[0]:
    print False
m = len(matrix)
n = len(matrix[0])
tops, tope = 0, m-1
mid = (tops+tope)/2
        
if target < matrix[0][0] or target > matrix[-1][-1]:
    print False
while tops<=tope:
    mid = (tops+tope)/2
    print("mid",mid)
    print('matrix[mid][0]',matrix[mid][0],'matrix[mid][-1]',matrix[mid][-1])

    if matrix[mid][0]<= target<= matrix[mid][-1]:
        break
    if target < matrix[mid][0]:
        tope = mid-1
        #mid -=1#in case tops = tope-1
    elif target >matrix[mid][-1]:
        tops = mid+1
        #mid+=1


#get 'mid'
lefts, lefte = 0, n-1
while lefts<=lefte:
    mid2 = (lefts+lefte)/2
    print("mid2",mid2,"mid",mid)
    if matrix[mid][mid2] == target:
        print True
    if target < matrix[mid][mid2]:
        lefte = mid2-1
    else:
        lefts = mid2+1
print False