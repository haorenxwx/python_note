#70.py

n = 20
if n ==0 or n ==1 or n ==2:
	print(n)
step = [1,1]
for i in range(2,n+1):

	step.append(step[i-1]+step[i-2])
print(step[-1])


    
