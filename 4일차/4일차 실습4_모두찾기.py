def find_all(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    c = 0
    pos = text.find(key)
    while not text.find(key,pos) == -1 :
        c = c + 1
        pos = text.find(key,pos+1)
    outfile.write(key + "가 나타난 총 횟수는 " + str(c) + "번이다.\n")
    infile.close()
    outfile.close()
    print("done")
find_all("article.txt","컴퓨터")
