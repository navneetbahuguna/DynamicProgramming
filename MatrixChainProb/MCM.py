import sys
def MatrixChainOrder(arr,i,j):
	minn = sys.maxsize
	if i >= j:
		return 0
	for k in range(i,j):
		temp = MatrixChainOrder(arr,i,k) + MatrixChainOrder(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]


	if temp < minn:
		minn = temp
	return minn



arr = [1, 2, 3 ,4]
size = len(arr) 
print("Minimum number of multiplications is",  MatrixChainOrder(arr, 1,size-1)) 