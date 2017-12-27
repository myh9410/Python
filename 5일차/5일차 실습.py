#실습[1]
#def gcd(m,n) :
#    if n == 0 :
#        return m
#    else :
#        return gcd(n,m%n)
#print(gcd(18,57))

def gcd(m,n) :
    while n != 0 :
        if m>n :
            m = m%n
        if n>m : 
            n = n%m
        if n == 0 :
            return m
    return gcd(m,n)
print(gcd(18,48))
