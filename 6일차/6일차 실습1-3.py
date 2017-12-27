nil = []
def cons(x,xs) :
    return [x] + xs
def head(xs) :
    return xs[0]
def tail(xs) :
    return xs[1:]
def null(xs) :
    return xs == nil
def concat(xs,ys) :
    return xs + ys
def snoc(xs,x) :
    return xs + [x]
def concat(xs,ys) :
    return xs + ys

def insert(x,ss) :
    rs = nil
    while not null(ss) :
        if x <= head(ss) :
            return concat(rs,cons(x,ss))
        else :
            rs = snoc(rs,head(ss))
            ss = tail(ss)
    return snoc(rs,x)

print(insert(6,cons(2,(cons(4,cons(5,cons(7,cons(8,nil))))))))
