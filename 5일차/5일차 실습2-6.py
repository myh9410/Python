#실습 2-6
def double(n) :
    return n*2

def halve(n) :
    return n//2

def mult(m,n) :
    ans = 0
    while not n == 1 :
        if not n%2 == 0 :
            m,n,ans = double(m),n/2 - 0.5,ans + m
        else :
            m,n = double(m),halve(n)
    while n == 1 :
        ans,n = ans + m,n//2
    return ans
print(mult(57,86))

