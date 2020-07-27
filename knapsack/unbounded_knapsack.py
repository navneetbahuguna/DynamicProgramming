
def unbounded_knapsack(val,wt,W,n):
	if n == 0 or W == 0:
		return 0
	if wt[n-1] <= W:
		return max(val[n-1] + unbounded_knapsack(val,wt,W - wt[n-1],n),unbounded_knapsack(val,wt,W,n-1))
	else:
		return unbounded_knapsack(val,wt,W,n-1)







W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 

print(unbounded_knapsack(val,wt,W,n))