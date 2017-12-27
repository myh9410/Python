#실습문제2 : 정수+실수 입력확인
def isfloat(s) :
    t = s.partition(".")
    return t[0].isdigit() and t[2].isdigit() or t[0].isdigit and t[2] == "" or t[0] == "" and t[2].isdigit()

def remove_sign(s) :
    if s.startswith("+") or s.startswith("-") :
        return s[1:]
    else :
        return s

def get_fixed_signed(message) :
    s = input(message)
    s1 = remove_sign(s)
    while not (s1.isdigit and isfloat(s1)):
        s = input(message)
        s1 = remove_sign(s)
    print(float(s))
    return float(s)
get_fixed_signed("수입력")
