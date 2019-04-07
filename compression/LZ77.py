

class LZ77Compressor:
	
	matching_key = lambda self,x : x[1]
	
	def __init__(self, w_size = 7):
		self.w_size  = w_size
		
	def compress(self, s):
		encoded = []
		
		i = 0
		
		while i < len(s):
			matching_sfx = [(0,0,s[i])]
			
			for j in range(max(0, i-self.w_size), i):
				if s[i] == s[j]:
					l = i+1
					k = j+1
					
					while l < len(s) and s[l] == s[k]:
						l += 1
						k += 1
						
					matching_sfx += [(i-j, k-j, s[l])]
				
				
			encoded += [ max(matching_sfx, key=self.matching_key)]
			i += encoded[-1][1] + 1
			
		return encoded
		
	def decompress(self, l):
		out = ''
		
		for t in l:
			if t[1] == 0:
				out += t[2]
			elif t[0] > t[1]:
				out +=  out[-t[0]:-t[0]+t[1]] + t[2]
			else:
				out += out[-t[0]:]
				out += out[-t[0]:-t[0]-t[0]+t[1]] + t[2]

		return out;
		
	
if __name__ == '__main__':
	c = LZ77Compressor()
	
	#s = 'babbababbaabbaabaabaaa'
	#s = 'acbbacba'
	s = 'abaababa'
	print(s)
	l = c.compress(s)
	print(c.decompress(l))
	print(l)