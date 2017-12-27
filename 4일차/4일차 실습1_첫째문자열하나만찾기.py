#실습문제1 첫째문자열 하나만 찾기
def find_first(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    pos = text.find(key)
    outfile.write(key + "의 위치번호는 " + str(pos) + "\n")
    infile.close()
    outfile.close()
    print("done")
find_first("article.txt","컴퓨터")
find_first("article.txt","한양대")
