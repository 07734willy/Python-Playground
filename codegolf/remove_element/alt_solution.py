class Solution:
 def removeElement(s,n,v):
  a=[e for e in n if e != v];n[:len(a)]=a;return len(a)
