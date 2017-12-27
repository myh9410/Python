#실습 2-2
def mult(m,n) :
    ans = 0
    while not n == 0 :
        ans,n = ans + m,n-1
    return ans
print(mult(5,4))
    
