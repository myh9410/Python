def find_all_sentence(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    ck = 0         #전체 글에서 key가 몇개있는지 확인하는 변수.
    cs = 0         #key가 있는 문장의 갯수가 몇개인지 확인하는 변수.
    pos = 0        
    key_per_sentence = 0 #한 문장에 key가 몇개인지 확인하는 변수.
    while not (pos == len(text)) : #text전체에서 작업을 수행.
        key_per_sentence = 0
        if (text[pos] == "." or text[pos] == "?") : 
            if not (text[:pos].find(key) == -1) :
                cs = cs + 1
                outfile.write(text[:pos] + "\n" + "\n")
                a = text[:pos]
                while not (a.find(key) == -1) :
                    a = a[a.find(key)+1:]
                    key_per_sentence = key_per_sentence + 1
                    ck = ck + 1
                outfile.write(key +"가" + str(key_per_sentence) + "번 등장.\n" + "\n")
            text = text[pos + 1 : ]
            pos = -1
        pos = pos + 1
    outfile.write(key + "이(가)" + str(cs) + "개 문장에서" + str(ck) + "번 등장\n")
    infile.close()
    outfile.close()
    print("done!")
find_all_sentence("article.txt","컴퓨터")
