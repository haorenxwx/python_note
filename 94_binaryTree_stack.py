#94_binaryTree_stack.py

class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		list = []
		self.iteration_inorder(root,list)
		return list

	def iteration_inorder(self, root, list):
		stack = []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				list.append(root.val)
				root = root.right
		return list

	
	#常规递归解法
	def recursive_inorder(self,root):
		if root:
			self.inorder(root.left,list)
			list.append(root.val)
			self.inorder(root.right,list)
		return list


