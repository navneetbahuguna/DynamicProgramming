
import time
val = [3, 34, 4, 12, 5, 2] 
#wt = [10, 20, 30] 
summ = 9
n = len(val)





# by Dynamic programing

def knapsack(val,W,n):
	array = [[-1 for j in range(W+1)]for i in range(n+1)]
	#print("array",array)

	if W == 0 or n == 0:
		return 0

	if array[n][W] != -1:
		return array[n][W]
	if val[n-1] <= W:
		array[n][W] =  max(val[n-1]+knapsack(val,W - val[n-1],n-1), knapsack(val,W,n-1))
		return array[n][W]
	else:
		array[n][W] =  knapsack(val,W,n-1)
		return array[n][W]

start = time.time()

print(knapsack(val,summ,n))
end = time.time()

print("time taken", end - start)