import sys

def _residualSet(code, s_prec):
	s_i = set()
	for w_1 in code:
		for w_2 in s_prec: 
			if w_1 != w_2 and w_2.startswith(w_1):
				s_i.add(w_2.replace(w_1,'', 1))
	
	return s_i
	
	
def _residualSetI(code, s_prec):
	return _residualSet(code, s_prec).union(_residualSet(s_prec, code))

	
def spAlgorithm(code):
	s = [_residualSet(code, code)]
	
	while len(s[-1]) != 0:
		if len(s[-1].intersection(code)) != 0:
			return (False, s)
		
		for s_i in s[:-1]:
			if(s[-1] == s_i):
				return (False, s)
		
		s.append(_residualSetI(code, s[-1]))	
		
	return (True, s)
	
	

if __name__ == '__main__':
	if len(sys.argv) > 1:
		code = None
		with open(sys.argv[1],'r') as f:
			code = set([line[:-1] for line in f.readlines()])
		
		print('\nCode:\n', code)
		isUD, sets = spAlgorithm(code)	
		print('\nCalculated sets:\n', str(sets).replace('},', '},\n'))

		if isUD:
			print('\nThe code is UD!')
		else:
			print('\nThe code is not UD!')
	else: 
		print('Usage: %s file'%sys.argv[0])
		