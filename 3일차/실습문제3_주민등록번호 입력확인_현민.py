def format_ok(f,m,b):
    return m=="-" and len(f)==6 and len(b)==7 and f.isdigit() and b.isdigit() and (1<=int(f[2])*10 + int(f[3])<=12) and (1<=int(f[4])*10 + int(f[5])<=31)

def last_digit_ok(f1,b1):
    return int(b1[-1]) == int(str(11 - ((int(f1[0])*2 + int(f1[1])*3 + int(f1[2])*4 + int(f1[3])*5 + int(f1[4])*6 + int(f1[5])*7 + int(b1[0])*8 + int(b1[1])*9 + int(b1[2])*2 + int(b1[3])*3 + int(b1[4])*4 + int(b1[5])*5) % 11))[-1])
def isRNN(message):
    s = input(message)
    t = s.partition("-")
    while not (format_ok(t[0],t[1],t[2]) and last_digit_ok(t[0],t[2])):
        print ("Invalid number")
        s = input(message)
        t = s.partition("-")
    return s
isRNN("주민번호를 입력하세요.")
