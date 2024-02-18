class Solution(object):
    def ispalindrome(self,x):
        if x<0:
            return False
            res=0
        while x>res:
            res=res*10+x%10
            x=x//10
        return True if (x==res) else False
    ispalindrome()