class Solution:
 def twoSum(s,n,t):r=[x for x in n if t-x in set(n)and t-x!=x]or[t//2,t//2];return [i for i,x in enumerate(n)if x in r]
