def isPalindrome(x): 
    return x == x[::-1] 
def minPalPartion(sting, i,j):
	if i >= j:
		return 0
	if isPalindrome(sting[i:j+1]):
		return 0

	ans = float('inf')
	for k in range(i,j):
		temp = 1+minPalPartion(sting,i,k) + minPalPartion(sting,k+1,j)
		ans = min(ans,temp)
	return ans




string = "ababbbabbababa"
print("Min cuts needed for Palindrome Partitioning is ",  minPalPartion(string, 0, len(string) -1),) 