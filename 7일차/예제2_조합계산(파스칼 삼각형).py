#조합계산 base
def comb(n,r) :
    if not (r==0 or r==n):
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1
print(comb(30,3))

#
