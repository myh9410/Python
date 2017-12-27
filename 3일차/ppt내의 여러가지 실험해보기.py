#실습문제 1 : 정수 입력확인
def remove_sign(r) :
    if r.startswith("+") or r.startswith("-") :
        r = r[1:]
        return r

def get_int_signed(message) :
    s = input(message)
    while not remove_sign(s).isdigit():
        s = input(message)
    print(int(remove_sign(s)))
get_int_signed("수입력")
