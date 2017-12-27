#실습 2-4
def double(n) :
    return n*2

def halve(n) :
    return n//2

def mult(m,n) :
    ans = 0
    while not n==0 :
        m,n,ans = m,halve(n),double(m) + ans
        while not n%2 == 0 :
            m,n,ans = m,n-1,ans
    return ans

print (mult(5,4))
