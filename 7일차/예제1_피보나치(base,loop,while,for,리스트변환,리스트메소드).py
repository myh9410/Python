#base
def fib(n):
    if n > 1 :
        return (fib(n-1) + fib(n-2))
    else:
        return n	#1일땐 1나오고 0일땐 0나오게됨.
print(fib(10))

#loop
def fibtail(n):
    def loop(k,old,new):
        if k < n : 
            return loop(k+1,new,old+new)
        else:    #k == n
            return new
    return loop(1,0,1)
print(fibtail(10))

#while문
def fib_while(n):
    k,old,new = 1,0,1
    while k<n:
        k,old,new = k+1,new,old+new
    return new

print(fib_while(10))

#for문 이용
def fibfor(n):
    old,new = 0,1
    for k in range(2,n+1):
        old,new = new,old + new
    return new
print(fibfor(10))

#위의 for문을 더 간단하게.
def fibfor(n):
    old,new = 0,1
    for _ in range(n-1):
        old,new = new,old + new
    return new
print(fibfor(10))

#list로 변환하여 함수 작성
def fibseq(n):
    fibs = [0,1]
    for k in range(2,n+1):
        fibs = fibs+ [fibs[k-1] + fibs[k-2]]
    return fibs
print(fibseq(10))

#리스트메소드(append)를 이용하여 함수 작성
def fibseq(n):
    fibs = [0,1]
    for k in range(2,n+1):
        fib = fibs[k-1] + fibs[k-2]
        fibs.append(fib)
    return fibs
print(fibseq(10))

#리스트메소드(pop)을 이용하여 함수작성
def fib(n):
    return fibseq(n).pop()
print(fib(10))

