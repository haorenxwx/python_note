#66.py

digits = [9,9]
digits.insert(0,0)
print(digits)

temp =1
for i in reversed(range(len(digits))):
	digits[i] += temp
	temp = digits[i]/10
	digits[i] = digits[i]%10
if digits[0] == 0:
	print digits[1:]
else:
	print digits