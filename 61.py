#61.py

def rotation(head,k):
	if not head:
		return head
	if k == 0:
		return head
	dummy = ListNode(0)
	dummy.next = head
	p = dummy
	count = 0
	while p.next :
		p = p.next
		count+=1
	p.next = dummy.next
	step = count-k%count
	for i in range(step):
		p = p.next
	head = p.next
	p.next = None

def createLink(n):
	if n<0:
		return False
	if n==1:
		return Node(1)
	else:
		root=Node(1)
		temp = root
		for i in range(2,n+1):
			temp.next = Node(i)
			temp = temp.next
		temp.next = root
		return root

a = createLink(4)
while a.next:
	print(a.value)
	a = a.next

