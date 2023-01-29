import random
print("game have 9 chances")
my_pt = 0
co_pt = 0
for i in  range(1,10):
    comp =  random.randint(1,3)
    temp = None
    if comp ==  1:
    	temp = "S"
    elif comp == 2:
    	temp = "W"
    else :
    	temp = "G"
    inp = input("S]snake\nW]water\nG]gun\nEnter your choice :  ")
    print(f"comp choice : " ,temp)
    print(f"your   choice : " , inp     )
    if inp == "S" or inp == "s":
        if comp == 1:
            print("tie")
        elif comp == 2: 
            print("you")
            my_pt += 1
        else:
            print("comp")
            co_pt += 1
    elif inp == "W" or inp == "w":
        if comp == 1: #s
            print("comp")
            co_pt += 1
        elif comp == 2:  #w
            print("tie")
        else:
            print("you")
            my_pt += 1
    
    elif inp == "G" or inp == "g":
        if comp == 1: #s
            print("you")
            my_pt += 1
        elif comp == 2:  #w
            print("comp")
            co_pt += 1
        else:
            print("tie")
    
    else:
        print("give proper input")
        i = i-1
        continue
if co_pt == my_pt :
	print("match is tie !")
elif co_pt > my_pt :
	print(f"you loose with {co_pt - my_pt} points")
else :
	print(f"you win with {mu_pt} points")
