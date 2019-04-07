import numpy as np

def bwt(s):
	permes = sorted([s[i:] + s[0:i] for i in range(len(s))])
	return (''.join((w[-1] for w in permes)), permes.index(s))
	
def ibwt(s, i):
	indices = np.array(sorted(range(len(s)), key= lambda i : s[i]), dtype=np.int)
	f = ''.join([s[j] for j in indices])
	
	tmp = ''
	j = i
	for k in range(len(s)):
		tmp += f[j]
		j = indices[j]
	
	return tmp
	
	
	
if __name__ == '__main__':
	t = bwt('abaab')
	print(t)
	print(ibwt(t[0], t[1]))