from itertools import*
class Solution:
 def countAndSay(f,n,s="1"):return s if n<2else f.countAndSay(n-1,"".join(str(len(list(v)))+d for d,v in groupby(s)))
