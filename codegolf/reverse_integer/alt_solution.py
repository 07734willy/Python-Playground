l=2**31
class Solution:
 def reverse(s,x):r=(-1)**(x<0)*int(str(abs(x))[::-1]);return r if -l<r<l-1else 0
