#실습 2-5
def double(n) :
    return n*2

def halve(n) :
    return n//2

def mult(m,n) :
    def loop(m,n) :
        if n == 1 :
            return m
        else :
            if n%2 == 0 :
                return loop(double(m),halve(n))
            else :
                return m + loop(double(m),n/2 - 0.5)

    if n == 0 :
        return 0
    else :
        return loop(m,n)

print(mult(57,86))
