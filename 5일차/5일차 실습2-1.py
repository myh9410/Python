#실습 2-1
def mult(m,n) :
    def loop(n,ans) : 
        if n > 0 :
            return loop(n-1,ans + m)
        else :
            return ans
    return loop(n,0)

print(mult(5,4))
