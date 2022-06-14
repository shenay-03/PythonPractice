class Solution:
        
    def climbStairs(self, n: int) -> int:
        d = dict()
        def f(mem: dict, n: int):
            if (n in mem):
                return mem[n]
            elif (n < 0):
                return 0
            elif(n == 0):
                return 1
            else:
                v = sum((f(mem,n-1) ,f(mem,n-2)))
                mem[n] = v
                return v
        
        return f(d, n)
        
        