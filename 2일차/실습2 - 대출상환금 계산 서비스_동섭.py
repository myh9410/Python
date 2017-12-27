p=input("대출원금이 얼마인가요?")
while not(p.isdigit() and int(p)>=1000000):
    p=input("대출원금이 얼마인가요?")
p=int(p)

y=input("상환기간은 몇년인가요?")
while not (y.isdigit() and int(y)>=1):
    y=input("상환기간은 몇년인가요?")
y=int(y)

r=input("이자율은 몇% 인가요?")
t=r.partition(".")
while not ((t[0].isdigit() and t[2].isdigit() or t[0].isdigit() and t[2]=="" or t[0]=="" and t[2].isdigit())
    r=input("이자율은 몇%인가요")
    t=r.partition(".")
r=float(r)/100

c=(1+r)**y
d=int(c*p*r/(c-1))
