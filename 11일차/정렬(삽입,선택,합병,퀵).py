################################################################################
#삽입정렬
def insert_while(x,ss):
    rs = []
    while ss != []:
        if x <= ss[0]:
            rs.append(x)
            return rs + ss
        else:
            rs.append(ss[0])
            ss = ss[1:]
    rs.append(x)
    return rs

def isort_while(xs):
    ss = []
    while xs != []:
        ss = insert_while(xs[0],ss)
        xs = xs[1:]
    return ss

#for버전
def insert_for(x,ss):
    rs = []
    for s in ss:
        if x<= s:
            rs.append(x)
            return rs + ss
        else:
            rs.append(s)
    rs.append(x)
    return rs

def isort_for(xs):
    ss = []
    for x in xs:
        ss = insert_for(x,ss)
    return ss
################################################################################
#선택정렬
def smaller(x,y):
    if x < y :
        return x
    else:
        return y

def smallest(xs) :
    (x,xs) = (xs[0],xs[1:])
    while xs != [] :
        x = smaller(xs[0],x)
        xs = xs[1:]
    return x

def ssort(xs) :
    ss = []
    while xs != []:
        x = smallest(xs)
        xs.remove(x)
        ss.append(x)
    return ss
################################################################################
#합병정렬
def merge(xs,ys):
    rs = []
    while xs != [] and ys != []:
          #xs와 ys가 빌 때 까지 계속 반복시킴
        if xs[0] <= ys[0]:
            rs.append(xs[0])#xs[0]이 작으니까 rs에 붙여줌
            xs = xs[1:]#xs[0]을 붙여준 후 xs의 범위를 다시 설정
        else:#xs[0] > ys[0]
            rs.append(ys[0])
            ys = ys[1:]
    return rs + xs + ys

def msort(xs):
#리스트를 합병정렬하는 함수
    if xs != [] and xs[1:] != []:
        mid = len(xs) // 2
        return merge(msort(xs[:mid]),msort(xs[mid:]))
                     #나누어진 두개의 리스트를 합병시킴
    else:
        return xs
################################################################################
#퀵정렬
def partition(pivot,xs):
    left = []
    right = []
    for x in xs:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left,right

def qsort(xs):#quicksort
    if xs != []:
        pivot = xs[0]#여기서는 맨 앞을 기준으로 설정함.
        left, right = partition(pivot,xs[1:])
        return qsort(left) + [pivot] + qsort(right)
    else:
        return []
################################################################################
#실습
import random
import time
def ascending_list():
    return [x for x in range(100)]
print(ascending_list())
def descending_list():
    return [x for x in range(100,0,-1)]

def random_list():
    xs = [x for x in range(100)]
    random.shuffle(xs)
    return xs

def search_time():
    def timer(search,xs):
        t1 = time.clock()
        search(xs)
        t2 = time.clock()
        return (t2-t1)*1000000
    xs = [x for x in range(100)]
    xs1 = ascending_list()
    ys1 = descending_list()
    zs1 = random_list()
    print()
    print("삽입정렬(while버전)")
    print("ascending:",int(timer(isort_while,xs1)),"micro sec")
    print("descending:",int(timer(isort_while,ys1)),"micro sec")
    print("random:",int(timer(isort_while,zs1)),"micro sec")
    print()
    xs2 = ascending_list()
    ys2 = descending_list()
    zs2 = random_list()
    print("선택정렬")
    print("ascending:",int(timer(ssort,xs2)),"micro sec")
    print("descending:",int(timer(ssort,ys2)),"micro sec")
    print("random:",int(timer(ssort,zs2)),"micro sec")
    print()
    xs3 = ascending_list()
    ys3 = descending_list()
    zs3 = random_list()
    print("합병정렬")
    print("ascending:",int(timer(msort,xs3)),"micro sec")
    print("descending:",int(timer(msort,ys3)),"micro sec")
    print("random:",int(timer(msort,zs3)),"micro sec")
    print()
    xs4 = ascending_list()
    ys4 = descending_list()
    zs4 = random_list()
    print("퀵정렬")
    print("ascending:",int(timer(qsort,xs4)),"micro sec")
    print("descending:",int(timer(qsort,ys4)),"micro sec")
    print("random:",int(timer(qsort,zs4)),"micro sec")
    print()
    print("Python 라이브러리 메소드")
    t1 = time.clock()
    xs5 = ascending_list()
    ys5 = descending_list()
    zs5 = random_list()
    t2 = time.clock()
    print("ascending:",int(timer(list.sort,xs5)),"micro sec")
    print("descending:",int(timer(list.sort,ys5)),"micro sec")
    print("random:",int(timer(list.sort,zs5)),"micro sec")
    print()
search_time()
