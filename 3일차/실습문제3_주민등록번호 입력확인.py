#주민등록번호 입력검증 함수
def isRNN(message) :
    s = input(message)
    t = s.partition("-")
    f = s[0:5]
    b = s[7:13]
    m = s[6]
    def format_ok(f,m,b) :
        return m == "-" and f.isdigit() and len(f) == 6 and b.isdigit() and len(b) == 7 and (1<=f[2]*10 + f[3] <= 12) and (1<=f[4]*10 + f[5]<=31)
    def last_digit_ok(t) :
        return int(s[-1]) == 11 - ((2*int[t[0]] + 3*int(t[1]) + 4*int(t[2]) + 5*int(t[3]) + 6*int(t[4]) + 7*int(t[5]) + 8*int(t[7]) + 9*int(t[8]) + 2*int(t[9]) + 3*int(t[10]) + 4*int(t[11]) + 5*int(t[12]))%11)
    while not (format_ok(f,m,b) and last_digit_ok(t)) : 
        print("Invalid number")
        s = input(message)
        t = s.partition("-")
    return s
isRNN("주민번호를 입력하세요.")

    
