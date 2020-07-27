
def findLongestRepeatingSubSeq(strr,m,n):
	if m == 0 or n == 0:
		return 0
	if strr[m-1] == strr[n-1] and m != n:
		return 1+findLongestRepeatingSubSeq(strr,m-1,n-1)
	else:
		return max(findLongestRepeatingSubSeq(strr,m,n-1),findLongestRepeatingSubSeq(strr,m-1,n))







str = "abcdefabcdeee"
m = len(str)
print("The length of the largest subsequence that repeats itself is : ",findLongestRepeatingSubSeq(str,m,m)) 