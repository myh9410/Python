#실습 2-3
def double(n) :
    return n*2

def halve(n) :
    return n//2

def mult(m,n) :
    def loop(m,n,ans) : 
        if n<= 0 :
            return ans
        else :
            if n%2 == 0 :
                return loop(m,halve(n),double(m)+ans)
            else :
                return loop(m,n-1,ans)
        return ans
    return loop(m,n,0)

print (mult(5,4))
