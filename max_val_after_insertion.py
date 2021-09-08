class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != "-":
            for i in range(len(n)):
                if int(n[i]) < x:
                    ret_str = n[:i] +str(x) + n[i:]
                    return ret_str
                return n + str(x)
        else:
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    ret_str = n[:i] +str(x) + n[i:]
                    return ret_str
                return n + str(x)
                    
            
                    
