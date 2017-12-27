def find_last(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    pos = text.find(key)
    while not text.find(key,pos + 1) == -1 : 
        pos = text.find(key,pos + 1)

    outfile.write(key + "의 위치번호는 " + str(pos) + "\n")
    infile.close()
    outfile.close()
    print("done")
find_last("article.txt","컴퓨터")
