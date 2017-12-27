#실습1-2
def even(n) :
    if n%2 == 0 :
        return True
    else :
        return False
def odd(n) :
    if n%2 == 1 :
        return True
    else :
        return False

def gcd(m,n) :
    def loop(m,n,func) : 
        if m == 0 or n == 0 : 
            if m == 0 :
                return n*func
            else :
                return m*func
        else :
            if even(m) and even(n) :
                return loop(m//2,n//2,func*2)
            elif even(m) and odd(n) :
                return loop((m//2),n,func)
            elif odd(m) and even(n) :
                return loop(m,(n//2),func)
            elif odd(m) and odd(n) and m <= n :
                return loop(m,((n - m)//2),func)
            else :
                return loop(n,((m - n)//2),func)
    return loop(m,n,1)
print(gcd(18,48))
