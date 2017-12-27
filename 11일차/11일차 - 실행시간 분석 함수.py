#실행시간 분석
import time
def search_time():
    def time(search,key,xs):
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
    print("first:",int(timer(linear_search_for,0,xs)),"micro sec")
    print("middle:",int(timer(linear_search_for,50000,xs)),"micro sec")
    print("last:",int(timer(linear_search_for,99999,xs)),"micro sec")
    print()
    print("Python 라이브러리 메소드")
    t1 = time.time()
    xs.index(0)
    t2 = time.time()
    print("first:",int(t2-t1)*1000000),"micro sec")
    t1 = time.time()
    xs.index(50000)
    t2 = time.time()
    print("middle:",int(t2-t1)*1000000),"micro sec")
    t1 = time.time()
    xs.index(99999)
    t2 = time.time()
    print("last:",int(t2-t1)*1000000),"micro sec")
    print()
    print("이분검색")
    print("first:",int(timer(binary_search,0,xs)),"micro sec")
    print("middle:",int(timer(binary_search,66666,xs)),"micro sec")
    print("last:",int(timer(binary_search,99999,xs)),"micro sec")
    print("none:",int(timer(binary_search,-1,xs)),"micro sec")
