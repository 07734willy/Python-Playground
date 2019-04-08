from itertools import* # imports everything, including `groupby`
class Solution:
 def countAndSay(f,n,s="1"): # start with a default `s` equal to "1"
 return s if n<2        # break out of the recursion when n == 1
 else f.countAndSay(    # call the function recursively
 n-1,"".join(           # join into a single string
 str(len(list(v)))      # string containing # of consecutive digits
 +d                     # append the digit itself
 for d,v in groupby(s)))# group the digits into similar chunks
