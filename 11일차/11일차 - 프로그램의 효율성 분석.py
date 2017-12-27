#11일차 - 효율성(정확성, 빠른 시간, 적은 공간, 적은 에너지)
#today - 효율성(시간)
#1. 검색
#찾고자 하는것 : key // 검색대상: xs key가 xs안에 있는지를 찾아냄
#              찾은 후 위치번호를 알려줌

#선형검색 - 한줄로 검색
#while버전
def linear_search_while(key,xs):
    i=0
    while i<len(xs) and key != xs[i]:
        i+=1
    return i
#for버전
def linear_search_for(key,xs):
    i=0
    for x in xs:#xs내의 모든 원소 x에 대해서 순서대로 검색
        if key == x:
            return i
        i+=1
    return i#다 찾아봤는데 값이 없으면 xs의 길이를 return해줌.(길이를 return == 못찾음)
            #i == len(xs)-1까지 검색 => xs의 끝까지 검색
            #i == len(xs) => xs의 끝까지 검색했는데 못찾음.

#이분검색 - 이산수학의 Bubble Sort와 같음.
#xs의 가운데를 검사 후, key와 xs의 가운데의 값이 같으면 => 위치번호 내줌
#xs의 가운데를 검사 후, key보다 크면 왼쪽 반쪽을 다시 반으로 나누어 검사
#xs의 가운데를 검사 후, key보다 작으면 오른쪽 반쪽을 다시 반으로 나누어 검사
def binary_search(key,xs):
    low = 0             #xs의 시작 위치번호
    high = len(xs)-1    #xs의 끝 위치번호
    index = -1          #못찾은 경우 == -1, 찾은경우 == key
    while low <=high and index == -1:
        mid = (high + low)//2
        if key == xs[mid]:
            index = mid
        elif key < xs[mid]:
            high = mid -1
        else:
            low = mid + 1
    return index

#실행시간 분석
import time
def search_time():
    def timer(search,key,xs):
        t1 = time.time()#시간이 매우 조밀하게 나타남.(t1 == 시작시점)(1/1조)초단위
        search(key,xs)
        t2 = time.time()#시간이 매우 조밀하게 나타남.(t2 == 끝시점)(1/1조)초단위
        return (t2-t1)*1000000#(1/1조)초는 너무 많아서 100만 곱해줌.
    xs = [x for x in range(100000)]#List Comprehension - 리스트를 쉽게 표현
                            #0부터 99999까지의 범위.
                            #{xㅣx ∈{0~99999}}와 같음.
    print("선형검색(while 버전)")
    print("first:",int(timer(linear_search_while,0,xs)),"micro sec")
    print("middle:",int(timer(linear_search_while,50000,xs)),"micro sec")
    print("last:",int(timer(linear_search_while,99999,xs)),"micro sec")
    print()
    print("선형검색(for 버전)")
    print("first:",int(timer(linear_search_for,0,xs)),"micro sec")
    print("middle:",int(timer(linear_search_for,50000,xs)),"micro sec")
    print("last:",int(timer(linear_search_for,99999,xs)),"micro sec")
    print()
    print("Python 라이브러리 메소드")
    t1 = time.time()
    xs.index(0)
    t2 = time.time()
    print("first:",int((t2-t1)*1000000),"micro sec")
    t1 = time.time()
    xs.index(50000)
    t2 = time.time()
    print("middle:",int((t2-t1)*1000000),"micro sec")
    t1 = time.time()
    xs.index(99999)
    t2 = time.time()
    print("last:",int((t2-t1)*1000000),"micro sec")
    print()
    print("이분검색")
    print("first:",int(timer(binary_search,0,xs)),"micro sec")
    print("middle:",int(timer(binary_search,66666,xs)),"micro sec")
    print("last:",int(timer(binary_search,99999,xs)),"micro sec")
    print("none:",int(timer(binary_search,-1,xs)),"micro sec")
search_time()
#2. 정렬
#xs를 정한 차순으로 나열
#원소의 크고 작음을 서로 비교

#삽입정렬
#xs의 리스트에서 빼내서 rs라는 리스트에 순서에 맞게 새로 정렬(가장 큰것을 찾음)
#while버전
def insert(x,ss):
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

def isort(xs):
    ss = []
    while xs != []:
        ss = insert(xs[0],ss)
        xs = xs[1:]
    return ss

#for버전
def insert(x,ss):
    rs = []
    for s in ss:
        if x<= s:
            rs.append(x)
            return rs + ss
        else:
            rs.append(s)
    rs.append(x)
    return rs

def isort(xs):
    ss = []
    for x in xs:
        ss = insert(x,ss)
    return ss

#선택정렬
#xs를 쭉 훑어서 제일 작은것을 발견 후  ss라는 새로운 리스트에 넣음
#for 버전은 없음
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
#위의 삽입정렬과 선택정렬은 속도가 느림.

#합병정렬 - merge sort
#리스트를 반으로 자름
#반으로 나눠진 각각의 리스트(a,b)를 각각 a끼리만 b끼리만 정렬시킴
#나눠진 두개의 리스트를 다시 합침(합병)
#a와b를 비교 작은 것을 rs로 넣음
#ex)a[0]과 b[0]중 a[0]이 작으면 a[0]을 rs에 넣음.
#   a[1]과 b[0]를 다시 비교 후 작은것을 rs에 넣음. 반복함.
def merge(xs,ys):
#정렬되어 있는 리스트 2개를 합쳐서 정렬된 리스트로 만들어 내주는 함수
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

#퀵정렬
#경우에 따라 합병정렬보다 빠른경우도 있고 아닌 경우도 있음.
#합병정렬 - 무조건 반으로 쪼갬
#퀵정렬 - 조건 하에 반으로 쪼갬
#기준값을 정해줌.(pivot)
#pivot보다 작으면 왼쪽, 크면 오른쪽
#왼쪽 오른쪽으로 나뉜 것 중에서 다시 pivot 설정해서 또 왼쪽 오른쪽으로 나눔
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

#오름차순 - 이미 정렬된 리스트
#내림차순 - 반대로 정렬된 리스트

#실습
import random
def ascending_list():
    return [x for x in range(100)]

def descending_list():
    return [x for x in range(100,0,-1)]

def random_list():
    xs = [x for x in range(100)]
    random.shuffle(xs)
    return xs

