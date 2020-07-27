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
				#S +=x[i-1]
				#print(x[i-1])
				
			else:
				array[i][j] = max(array[i][j - 1], array[i-1][j])
	print("fnal array", array)
	#print("String", S)

	#for printing
	i = lenx
	j = leny
	S = ''
	while i >0 and j > 0:
		if x[i-1] == y[j-1]:
			S+=x[i-1]
			i-=1
			j-=1
		else:
			if array[i][j-1] > array[i-1][j]:
				j-=1
			else:
				i-=1


	return S

import numpy as np

Y = "ABCDAF"
X = "ACBCF"
array = [[-1]*(len(Y)+1) for i in range(len(X)+1) ]
print(array,np.array(array).shape)
print "Length of LCS is ", lcs_topDown(X , Y, len(X), len(Y)) 
