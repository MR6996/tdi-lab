

def sturmian(integers):
	if len(integers) < 1:
		raise ValueError('List empty!')
		
	tmp = ['b', 'a']
	s = ''
	
	for i in integers:
		#if i < 1: 
		#	raise ValueError('Negative value!')
		
		s = tmp[1]*i + tmp[0]
		tmp[0] = tmp[1]
		tmp[1] = s
		
	return s
	
	
if __name__ == '__main__':
	print(sturmian([1,1,1]))