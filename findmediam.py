
s = "PAYPALISHIRING"
numRows = 3

if numRows == 1 or numRows >= len(s):
    print(s)

L = [''] * numRows
print(L)
index, step = 0, 1

for x in s:
    L[index] += x
    if index == 0:
        step = 1
    elif index == numRows -1:
        step = -1
    index += step

print(''.join(L))
'''

L = [""]* numRows
if numRows == 1 or numRows>=len(s):
    print s
index = 0
step = 1
for x in s:
    L[index] += x
    if index == 0 or index == numRows-1:
        step = -step
    index += step
print ''.join(L)
'''