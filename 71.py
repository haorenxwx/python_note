#71.py

a = "/a/./b/../../c/"
b = a.split('/')
stack = []
for p in b:
	if p == '..':
		if stack: stack.pop()
	elif p!= '' and p!='.':
		stack.append(p)
	print(stack)
print '/'+'/'.join(stack)