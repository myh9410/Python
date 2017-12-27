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

def length(xs) :
    if not null(xs) :
        return length(tail(xs)) + 1
    else :
        return 0

def smaller(x,y) :
    if x < y :
        return x
    else :
        return y
    
def smallest(xs) :
    (x,xs) = (head(xs),tail(xs))
    while not null(xs) :
        x = smaller(head(xs),x)
        xs = tail(xs)
    return x

print(smallest(cons(3,cons(2,cons(5,cons(4,nil))))))
