#작성자 : 문용호
#학번 : 2014037938

#이메일 주소의 포맷 : <사용자이름>@<호스트이름>
###################################################################################
def get_email(message) :
    s = input(message)
    a = s.partition("@")
    while not (email_true(s) and local_true(a[0])and host_true(a[2]) and 1<=len(a[2])<=255) :
        print ("다시 입력해주세요.email이 잘못되었습니다.")
        s = input(message)
        a = s.partition("@")
#email을 "@"를 기준으로 나눈 후 아래의 조건을 정의해준  함수 local_true(ㅣ) 와 host_true(h)가 "@"의 앞과 끝에 오도록 설정.
#전체 문장의 길이가 1과 255 사이가 되도록 설정.
#조건에 맞지 않을 경우 재입력 하도록 설정.
###################################################################################
    local = a[0]
    host = a[2]
    if local.startswith("(") :
        l1 = local.partition(")")
        local = l1[2]
    if local.endswith(")") :
        l2 = local.partition("(")
        local = l2[0]
    if host.startswith("(") :
        l3 = local.partition(")")
        local = l3[2]
    if host.endswith(")") :
        l4 = local.partition("(")
        local = l4[0]
#partition을 통해서 "@"를 기준으로 3등분 되도록 설정
#주석 제거
###################################################################################
    total = local + "@" + host
    print("이메일 : " + total)
    return total
###################################################################################
def email_true(e) : 
    x0 = 0
    Answer0 = 0
    while not x0 == len(e) - 1 :
        if e[x0] == "@" :
            Answer0 = Answer0 + 1
        x0 = x0 + 1
    return Answer0 == 1 and not (e.startswith("@") or e.endswith("@"))
#email에서 "@"가 1개가 아닌경우 걸러주고, @로 시작하거나 @로 끝나는 경우 걸러줌.
###################################################################################
#사용자이름 허용기준
def local_true(l) :
    x1 = 0
    Answer1 = 0
    while not x1 == len(l)-1 : 
        if l[x1] =="." and l[x1+1] =="." :
           Answer1 = Answer1 + 1 
        x1 = x1+1
    return Answer1 == 0 and not(l.startswith(".") or l.endswith(".")) and not ("[" in l or "]" in l or "<" in l or ">" in l)
#"."과"."이 연속되면 허용되지 않도록 설정
#"."으로 시작하는지?끝나는지? 검사해주고, 특수문자 중 허용되지 않는것은 받지 않도록 설정
#################################################################################
#IP주소는 '['와']'로 둘러싸는 형태도 허용
#################################################################################
#호스트이름 허용기준
def host_true(h) :
    x2 = 0
    Answer2 = 0
    while not x2 == len(h) -1 :
        if h[x2] == "." and h[x2+1] == "." :
            Answer2 = Answer2 + 1
        x2 = x2 + 1
    d = 0              #(호스트에서 "."의 갯수)
    x2by1 = 0
    while not x2by1 == len(h)-1 :
        if h[x2by1] == "." :
            d = d + 1
        x2by1 = x2by1 + 1
#"."과"."이 연속되면 허용되지 않도록 설정
#################################################################################
#호스트이름 허용기준
    x2by2 = 0
    Answer2by1 = 0
    y = h.partition(".")
    if d == 0 and not (1<=len(h)<=63) :
        Answer2by1 = Answer2by1 + 1
    while not x2by2 == d :
        if y[2].find(".") == -1 and not (1<=len(y[2])<=63) :
            Answer2by1 = Answer2by1 + 1
        if not (1<=len(y[0])<=63) :
            Answer2by1 = Answer2by1 + 1
        y = y[2]
        y = y.partition(".")
        x2by2 = x2by2 + 1
#"."을 기준으로 앞부분과 뒷부분 길이를 측정
#"."을 가운데 끼워 단어를 나열.
#1자이상 최대 63자까지 허용.
##################################################################################
#호스트이름 허용기준
    x2by3 = 0
    Answer2by2 = 0
    while not x2by3 == len(h) :
        if not (h[x2by3] == "." or h[x2by3] == "-" or h[x2by3].isdigit() or h[x2by3].isalpha()) : 
            Answer2by2 = Answer2by2 + 1
        x2by3 = x2by3 + 1
    return Answer2 == 0 and Answer2by1 == 0 and Answer2by2 == 0 and not(h.startswith('.') or h.endswith('.'))
#영문 알파벳,숫자,하이픈,점으로구성된 문자열은 허용
##################################################################################
print("email을 입력하세요.")
get_email("email : ")

#"."과"."이 연속되면 허용되지 않도록 설정

#귀띔 : startswith,endswith,find,rfind,isalpha,isdigit,partition,strip
