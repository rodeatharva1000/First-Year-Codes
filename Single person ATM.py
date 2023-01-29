username = "abc"
pin = None 
balance = 0 

def createaccount():
    inp1 = input("enter your name = ")
    global username
    username = inp1
    inp2 = int(input("enter the ATM PIN for yyour account = "))
    global pin
    pin = inp2

def changepin():
    inp3 = input("enter user name = ")
    global username
    if username == inp3 :
        inp4 = int(input("enter the old pin = "))
        global pin
        if pin == inp4:
            inp5 = int(input("enter the new pin = "))
            pin = inp5
        else:
            print("old pin does not match !")
    else:
        print("username does not match !")
        
def deposite():
    inp5 = input("enter user name = ")
    global username
    if username == inp5:
        inp6 = int(input("enter deposite amount = "))
        global balance
        balance = balance + inp6
    else:
        print("check username again !")

def withdraw():
    inp7 = input("enter username = ")
    global username
    if username == inp7 :
        inp8 = int(input("enter your pin = "))
        if pin == inp8 :
            inp9 = int(input("enter the amount you want to withdraw = "))
            global balance
            if balance >= inp9 :
                print(f"you withdraw {inp9} rupees")
                balance = balance - inp9
            else:
                print("insufficient balance ! ")
        else:
            print("wrong pin !")
    else:
        print("check username")

def check_balance():
    inp9 = input("enter user name = ")
    global username
    if username == inp9 :
        inp10 = int(input("enter pin = "))
        global pin
        if pin == inp10 :
            global balance
            print(f"your current balance is {balance}")
        else:
            print("wrong pin ! ")
    else :
        print("user does not exists ! ")
    
        
def working(): 
    user_input = int(input("what do you waht to do \n1] enter 1 to create account \n2] enter 2 to change pin \n3] enter 3 to deposite \n4] enter 4 to withdraw \n5] enter 5 to check balance \n= "))         
    if user_input == 1:
        createaccount()
    elif user_input == 2:
        changepin()
    elif user_input == 3:
        deposite()
    elif user_input == 4:
        withdraw()
    elif user_input == 5:
        check_balance()
    
for i in range(0,100):
    xinp = int(input("enter 10 to process atm \nenter 0 to exit = "))
    if xinp == 10:
        working()
    elif xinp == 0:
        username = None
        pin = None
        balance = None
        break
