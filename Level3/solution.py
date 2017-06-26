class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def create_tree(root, h, cur_h):
	if cur_h >= h:
		return
	root.left = Node(0)
	root.right = Node(0)
	create_tree(root.left, h, cur_h+1)
	create_tree(root.right, h, cur_h+1)

def postorder(root):
	if root is None:
		return
	postorder(root.left)
	postorder(root.right)
	root.val = postorder.count
	postorder.count += 1

def parent(root, val):
	lh = -1
	rh = -1
	if root is None:
		return -1
	if root.left is not None and root.left.val == val:
		return root.val
	if root.right is not None and root.right.val == val:
		return root.val
	lh = parent(root.left, val)
	rh = parent(root.right, val)
	return lh if lh != -1 else rh

def answer(h, q):
	root = Node(0)
	create_tree(root, h-1, 0)
	postorder.count = 1
	postorder(root)
	p = []
	for val in q:
		p.append(parent(root, val))
	return p

print answer(30, [1,2,3])