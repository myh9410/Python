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
    if not null(ss) :
        if x <= head(ss) : 
            return cons(x,ss)
        else :
            return cons(head(ss),insert(x,tail(ss)))
    else :
        return cons(x,nil)
    
def isort(xs) :
    ss = nil
    while not null(xs) :
        ss = insert(head(xs),ss)
        xs = tail(xs)
    return ss
print(isort([5,2,3,1]))
