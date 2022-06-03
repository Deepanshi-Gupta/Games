import random
    
def Chance(name,listnum):
    choice=int(input("Enter the numbers you want to Say (1/2/3) : "))
    if choice<=3:
        for i in range(choice):
            num=int(input("Enter the number : "))
            if len(listnum)==0:
                print("You lose")
                return 1
            else:
                if num>21 or num not in listnum:
                    print("Wrong nuumber\nPlease play again ")
                    return 0
                else:
                    listnum.remove(num)
        return -1            
    else:
        print("Wrong input ")
        return 0

def play(ch,listnum,l):
    while True:
        result = Chance(ch,listnum)
        if result==0:
            #ch=next_chance(ch,l)
            print("now it's ",ch," turn")
        elif result==1:
            break
        else:
            ch=next_chance(ch,l)
            print("now it's ",ch," turn")
        
def next_chance(name,l):
    for i in l:
        if name!=i:
            return i

listnum=[i for i in range(1,21)]

print("The Game has 2 rules :- ")
print(""" 1) you can only choose upto 3 numbers at a time \n 2) if you say 21 then you lose\n """)
name1=input("Enter the name of Player A : ")
name2=input("Enter the name of Player B : ")
l=[name1,name2]
ch=random.choice(l)
print("First chance is of ",ch)

play(ch,listnum,l)
    

