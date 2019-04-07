class Solution:
 def removeElement(s,n,v):
  a=[e for e in n if e != v]; # create a new list, consisting only of
                              # elements not equal to `v`
  n[:len(a)]=a;   # Assign a to the slice 0..len(a) in `n`, in-place
  return len(a)   # return the length of the slice
