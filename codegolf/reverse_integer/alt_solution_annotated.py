l=2**31 # This sets a constant, used for limit checks
class Solution:
 def reverse(s,x): # class and function, as usual
     r=(-1)**(x<0)* # This bit evalutes to -1 if x < 0, otherwise 1
     int(str(abs(x))[::-1]); # Converts to a reversed string, no sign
     return r if -l<r<l-1else 0 # Checks if r is in range, and yields r if so, otherwise 0
