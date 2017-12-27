#실습1-3
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
    func = 1
    while not n == 0 : 
        if even(m) and even(n) :
            m,n,func = m//2,n//2,func*2
        elif even(m) and odd(n) :
            m,n,func = m//2,n,func
        elif odd(m) and even(n) :
            m,n,func = m,n//2,func
        elif odd(m) and odd(n) and m <= n :
            m,n,func = m,((n-m)//2),func
        else :
            m,n,func = n,(m-n)//2,func
    return m * func

print(gcd(18,48))


