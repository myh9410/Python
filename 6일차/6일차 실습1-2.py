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
    def loop(ss,rs) :#x는 값안바뀌니 loop안에 넣을필요 X
        if not null(ss) :
            if x<=head(ss) :
                return concat(rs,cons(x,ss))
            else :
                return loop(tail(ss),snoc(rs,head(ss)))
        else :
            return snoc(rs,x)
    return loop(ss,nil)

print(insert(6,cons(2,(cons(4,cons(5,cons(7,cons(8,nil))))))))
