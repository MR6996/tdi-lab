import math as m
def gamma(n):
    """
    Return a binary string that rappresent n in gamma encoding.
    
    Parameters:
        n (int): integer to rappresent (must be greater than 0)

    Returns:
        str : gamma rappresentation of n    
    """
    N = m.floor(m.log(n,2))
    return '0'*N + bin(n)[2:]

def fromGamma(g):
    """
    Return a list of integers in g rappresented in gamma encoding
    
    Parameters:
        g (str): gamma rappresentation of some integers

    Returns:
        list : list of integer rappresented
    """
    l = []
    
    i = 0
    count = 0
    while i < len(g):
        if g[i] == '0': 
            count+= 1
            i += 1
        else: 
            r_bound = i+count+1
            l += [int(g[i:r_bound], 2)]
            i = r_bound
            count = 0
            
    return l


def delta(n):
    """
    Return a binary string that rappresent n in delta encoding.
    
    Parameters:
        n (int): integer to rappresent (must be greater than 0)

    Returns:
        str : delta rappresentation of n    
    """
    N = m.floor(m.log(n,2))
    return gamma(N+1) + bin(n)[3:]

def fromDelta(d):
    """
    Return a list of integers in g rappresented in delta encoding
    
    Parameters:
        d (str): delta rappresentation of some integers

    Returns:
        list : list of integer rappresented
    """
    l = []
    
    i = 0
    count = 0
    while i < len(d):
        if d[i] == '0': 
            count+= 1
            i += 1
        else: 
            N = int(d[i:i+count+1], 2)
            l_bound = i + count + 1
            r_bound = i + count + N
            l += [int('1' + d[l_bound:r_bound], 2)]
            i = r_bound
            count = 0
    
    return l



# ## Fibonacci encoding
# 
# For determine the index $n$ of Fibonacci sequence of a given $F$ is used the formula: $$n(F) = \Bigg\lfloor\log_{\phi}\Bigg(F\sqrt{5} + \frac{1}{2}\Bigg)\Bigg\rfloor$$ where $\phi = \frac{1 + \sqrt{5}}{2}$ 
# 
# For calculate the i-th fibonacci number is used the following relation: 
# $$\begin{pmatrix} F_{n+1} & F_{n} \\ F_{n} & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$$

phi = (1 + 5 ** .5)/2

def fibonacci_index(F):
    """
    """
    return m.floor(m.log(F * (5**.5) + .5)/m.log(phi))

def fibonacci_number(i):
    """
    Return the i-th Fibonacci numeber
    """
    if i == 0: return 0
    
    M = [1, 1, 1, 0]
    tmp = [1, 0, 0, 1]
    
    for j in bin(i-1)[:1:-1]:
        if j == '1':
            tmp = [M[0]*tmp[0] + M[1]*tmp[2], M[0]*tmp[1] + M[1]*tmp[3],                    M[2]*tmp[0] + M[3]*tmp[2], M[2]*tmp[1] + M[3]*tmp[3]]
        
        M = [M[0]*M[0] + M[1]*M[2], M[0]*M[1] + M[1]*M[3],              M[2]*M[0] + M[3]*M[2], M[2]*M[1] + M[3]*M[3]]
        
    return tmp[0]
    
def fibonacci(n):
    """
    Return a binary string that rappresent n in fibonacci code.
    
    Parameters:
        n (int): integer to rappresent (must be greater that 0)

    Returns:
        str : fibonacci rappresentation of n    
    """
    tmp = '1'
    r = n
    idx = fibonacci_index(n)
    F_idx = fibonacci_number(idx)
    F_idx_1 = fibonacci_number(idx+1)
    
    if F_idx_1 <= n:
        r -= F_idx_1
        last_idx = idx + 1
    else:
        r -= F_idx
        last_idx = idx
        
    while r > 0:
        idx = fibonacci_index(r)
        F_idx = fibonacci_number(idx)
        F_idx_1 = fibonacci_number(idx+1)
        
        if F_idx_1 <= r:
            r -= F_idx_1
            tmp = '1' + '0'*(last_idx - idx) + tmp
            last_idx = idx + 1
        else:
            r -= F_idx
            tmp = '1' + '0'*(last_idx - idx - 1) + tmp
            last_idx = idx
            
    return '0'*(last_idx - 2) + tmp + '1'


def levenshtein(n):
    """
    Return a binary string that rappresent n in Levenshtein code.
    
    Parameters:
        n (int): integer to rappresent

    Returns:
        str : Levenshtein rappresentation of n    
    """
    if n == 0: return '0'
    c = 1
    tmp = bin(n)[3:]
    m = len(tmp)
    
    while m != 0:
        m_bin = bin(m)[3:]
        tmp = m_bin +  tmp
        m = len(m_bin)
        c += 1

    return '1'*c + '0' + tmp

def fromLevenshtein(ls):
    """
    Return a list of integers in ls rappresented in Levenshtein encoding
    
    Parameters:
        ls (str): Levenshtein rappresentation of some integers

    Returns:
        list : list of integer rappresented
    """
    l = []
    
    i = 0
    count = 0
    N = 1
    while i < len(ls):
        if ls[i] == '1': 
            count+= 1
            i += 1
        elif count == 0:
            l += [0]
            i += 1
        else:
            i += 1
            for j in range(count-1):
                r_bound = i + N
                N = int('1' + ls[i:r_bound], 2)
                i = r_bound
                
            l += [N]
            count = 0
            N = 1
            
    return l

def rice(n, **args):
    """
    Return a binary string that rappresent n in Rice encoding.
    
    Parameters:
        n (int): integer to rappresent
        k (int): parameter of Rice encoding, default=0

    Returns:
        str : Rice rappresentation of n  
    """
    if 'k' in args: k = args['k']
    else: k = 0
        
    q = int(n/2**k)
    r = n % 2**k
    
    return '1'*(q+1) + bin(r)[2:]

	
	
	

if __name__ == '__main__':

	# #### Test of Gamma encoding
	print('11 ->', gamma(11))

	test = gamma(11) + gamma(12) + gamma(153)
	print(test, '<-', fromGamma(test))


	# #### Test of Delta encoding
	print('11 ->', delta(11))

	test = delta(11) + delta(31) + delta(156)
	print(test, '<-', fromDelta(test))
	
	# #### Test of Fibonacci encoding
	print('12 ->', fibonacci(73))
		
	# #### Test of Levenshtein encoding
	print('11 ->', levenshtein(11))

	test = levenshtein(12) + levenshtein(152) + levenshtein(0) + levenshtein(42) 
	print(test, '<-', fromLevenshtein(test))
		
	# #### Test of Rice encoding
	print('42->', rice(42, k=1))
	print('42->', rice(42, k=5))
	print('42->', rice(42, k=6))

