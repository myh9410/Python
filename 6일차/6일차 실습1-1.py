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
    
def insert(x,ss) :
    if not null(ss) :
        if x <= head(ss) : 
            return cons(x,ss)
        else :
            return cons(head(ss),insert(x,tail(ss)))
    else :
        return cons(x,nil)

print(insert(1,cons(2,cons(4,cons(5,cons(7,cons(8,nil)))))))
