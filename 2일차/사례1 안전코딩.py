days = input("며칠?")
while not days.isdigit() :
    print ("숫자만 입력해주세요.")
    days = input("며칠?")
days = int(days)
if days > 0 :
    hours = days * 60 * 24
    print("일을 분으로 따지면",hours , "분이다.")
else :
    print("양수만 입력해주세요.")
    
