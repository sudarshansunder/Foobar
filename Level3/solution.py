def loc(h, tar, cur_h):
	cur_h /= 2
	right = h - 1
	left = h - 1 - cur_h
	cur_h -= 1
	if right == tar or left == tar:
		return h
	else:
		if tar <= left:
			return loc(left,tar,cur_h);
		else:
			return loc(right,tar,cur_h);

def answer(h, q):
	num = 2**h - 1
	p = []
	for val in q:
		if val < num and val >=1:
			p.append(loc(num,val,num-1))
		else:
			p.append(-1);
	return p