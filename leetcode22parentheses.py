#leetcode22parentheses.py

'''def ParenGe(l,r,item, res):
	if r < 1:
		return
	if r == 0 and l == 0:
		res.append(item)
		print("for every item append:\n") 
		print(res)
	if l > 0:
		print("for every left modify:\n")
		print(item)
		ParenGe(l-1, r, item+'(', res)
	if r > 0:
		print("for every right modify\n")
		print(item)
		ParenGe(l, r-1, item+')', res)
res = []
ParenGe(3,3,'',res)
print(res)
'''

#create Q as a generater

def generate(p,left,right):
	if right >= left >= 0:
		if not right:
			return p
		for q in generate(p+'(',left-1,right): 
			yield q
			print('for every left q yield\n'+p+'(')
			print(left,right)
			
		for q1 in generate(p+')',left,right-1): 
			yield q1
			print('for every right q1 yield\n'+p+')')
			print(left,right)
print(list(generate('',3,3)))

'''        
def generate(p, left, right):
    if right >= left >= 0:
        if not right:
            yield p
        for q in generate(p + '(', left-1, right): yield q
        for q in generate(p + ')', left, right-1): yield q
print(list(generate('', 3, 3)))
'''

