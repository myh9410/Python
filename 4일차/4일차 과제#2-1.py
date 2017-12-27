def one_sentence_per_line(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0
    c = 0
    while not (c==len(text)) :
        if (text[c] == "." or text[c] == "?") :
            t = text[ :c+1].strip("\n")
            outfile.write(t + "\n" + "\n")
            count = count + 1
            text = text[c+1: ]
            c = -1
        c = c + 1
    outfile.write("문장이 총" + str(count) + "개\n")
    infile.close()
    outfile.close()
    print("done")
one_sentence_per_line("article.txt")
