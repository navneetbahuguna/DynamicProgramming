
import time
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val)


#by using recurrsion
def knapsack(val,wt,W,n):
	if W == 0 or n == 0:
		return 0
	if wt[n-1] <= W:
		return max(val[n-1]+knapsack(val,wt,W - wt[n-1],n-1), knapsack(val,wt,W,n-1))
	else:
		return knapsack(val,wt,W,n-1)
start = time.time()

print(knapsack(val,wt,W,n))
end = time.time()

print("time taken", end - start)

'''


# by Dynamic programing

def knapsack(val,wt,W,n):
	array = [[-1 for j in range(W+1)]for i in range(n+1)]
	#print("array",array)

	if W == 0 or n == 0:
		return 0

	if array[n][W] != -1:
		return array[n][W]
	if wt[n-1] <= W:
		array[n][W] =  max(val[n-1]+knapsack(val,wt,W - wt[n-1],n-1), knapsack(val,wt,W,n-1))
		return array[n][W]
	else:
		array[n][W] =  knapsack(val,wt,W,n-1)
		return array[n][W]

start = time.time()

print(knapsack(val,wt,W,n))
end = time.time()

print("time taken", end - start)
'''