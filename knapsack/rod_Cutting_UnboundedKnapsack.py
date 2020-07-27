
def cutRod(arr,val,size):
	if size == 0:
		return 0
	if val[size - 1] <= size:
		return max(arr[size-1]+cutRod(arr,val,size-val[size-1]),
			cutRod(arr,val,size))
	else:
		return cutRod(arr[size-1],val,size)







arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
val = [i for i in range(1,size+1)]
print(val)
print("Maximum Obtainable Value is", cutRod(arr,val, size)) 