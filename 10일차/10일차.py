def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
        file.close()
        return members
def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + "\n"
        file.write(line)
        file.close()
#실습 1
def login(members):
    username = input("Enter your name: (4letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4letters max) ")
    if username in members.keys():
        if trypassword == members[username][0]:
            print("you played ", members[username][1]," games and won ", members[username][2]," of them.")
            print("tour all-time winning percentage is","(0:.2f)".format(divide(members[username][2],members[username][1])),"%")
            if int(members[username][3]) >= 0:
                print("you have", members[username][3],"chips")
            else:
                print("you owe", members[username][3],"chips")
            return username, members[username][1], members[username][2], members[username][3], members
        else:
            login(members)
    else:
        members[username] = (trypassword,0,0,0)
        return username, 0,0,0, members
def divide(x,y): return x/y if y>0 else 0
#실습 2
def show_top5(members):
    print("----")
    sorted_members = sorted(dict.items(),key=lambda x: x[0][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    print(sorted_members[:5])
    
print(login(load_members()))
