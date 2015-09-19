__author__ = 'Vivek'

#Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

def diagonal(self, A):
	    res = []
	    for i in range(2 * len(A) - 1) :
	        if i < len(A) :
	            z = 0
	        else :
	            z = i - len(A) + 1
	        temp = []
	        for j in range(z, i - z + 1) :
	            temp.append(A[j] [i - j])
	        res.append(temp)
	    return res
