
#Longest Common Subsequence

"""LCS Problem Statement: Given two sequences, find the length of longest 
subsequence present in both of them. A subsequence is a sequence that appears
 in the same relative order, but not necessarily contiguous. For example, 
 'abc',
  'abg', 'bdf', 'aeg', 'acefg', .. etc are subsequences of 'abcdefg'."""
'''
def lcs(x,y,lenx,leny):
	if lenx == 0 or leny == 0:
		return 0
	if x[lenx - 1] == y[leny - 1]:
		return 1+lcs(x,y,lenx-1, leny - 1)
	else:
		return max(lcs(x,y,lenx, leny - 1), lcs(x,y,lenx-1, leny))






X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X , Y, len(X), len(Y)) 


'''
'''

def lcs_mem(x,y,lenx,leny):
	array = [[-1]*(leny+1) for i in range(lenx+1) ]
	#print(array.shape)
	if lenx == 0 or leny == 0:
		return 0

	if array[lenx][leny] != -1:
		return array[lenx][leny]

	if x[lenx - 1] == y[leny - 1]:
		array[lenx][leny] = 1+lcs_mem(x,y,lenx-1, leny - 1)
		return array[lenx][leny]
	else:
		array[lenx][leny] = max(lcs_mem(x,y,lenx, leny - 1), lcs_mem(x,y,lenx-1, leny))
		return array[lenx][leny]


X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs_mem(X , Y, len(X), len(Y)) 



'''
#top down approach
def lcs_topDown(x,y,lenx,leny):
	array = [[-1]*(leny+1) for i in range(lenx+1) ]
	S = ''
	#print(array.shape)
	for i in range(lenx+1):
		for j in range(leny+1):
			if i == 0 or j == 0:
				array[i][j] = 0
				

			if x[i - 1] == y[j - 1]:
				array[i][j] = 1 + array[i-1][j-1]
				S +=x[i-1]
				print(x[i-1])
				
			else:
				array[i][j] = max(array[i][j - 1], array[i-1][j])
	print("fnal array", array)
	print("String", S)
	return array[lenx][leny]




import numpy as np

Y = "ABCDAF"
X = "ACBCF"
array = [[-1]*(len(Y)+1) for i in range(len(X)+1) ]
print(array,np.array(array).shape)
print "Length of LCS is ", lcs_topDown(X , Y, len(X), len(Y)) 
