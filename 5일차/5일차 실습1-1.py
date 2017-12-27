#실습1-1
def gcd(m,n) :
    while n != 0 :
        m,n = n,m%n
    return m
print(gcd(18,48))
