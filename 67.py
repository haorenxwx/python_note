#67.py
a = "11"
b = "101"
def addBinary(a,b):
	if len(a) == 0: return b
	if len(b) == 0: return a
	if a[-1] == '1' and b[-1] == '1':
		return addBinary(addBinary(a[:-1],b[:-1]),'1')+'0'
	if a[-1] == '0' and b[-1] == '0':
		return addBinary(a[:-1],b[:-1])+'0'
	else:
		return addBinary(a[:-1],b[:-1])+'1'
print(addBinary(a,b))