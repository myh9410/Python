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

def remove_one(x,xs) :
    def loop(xs,rs) :
        if not null(xs) :
            if x == head(xs) :
                return concat(rs,tail(xs))
            else :
                return loop(tail(xs),snoc(rs,head(xs)))

def smaller(x,y) :
    if x < y :
        return x
    else :
        return y

def smallest(xs) :
    if length(xs) >= 2 :
        x = smallest(tail(xs))
        return smaller(head(xs),x)
    else :
        return head(xs)

def ssort(xs) :
    if not null(xs) :
        x = smallest(xs)
        return cons(x,ssort(remove_one(x,xs)))
    else :
        return nil
