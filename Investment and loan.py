inp1 = int(input("Enter the loan or Investment amount:"))
inp2 = int(input("Enter number of years : "))
inp3 = int(input("Enter intrest or vaj on loan : "))
def calculate() :
    if inp3==0 :
        print("Constant amount ! ")
    else :
    	global inp1
    	amount_add = (inp1/100)*inp3
    	inp1 = inp1 + amount_add
    	return amount_add
i = 1
for years in range(0,inp2+1) :
    calculate()
    print(f"for {i} year --> {inp1}")
    i = i+1
	
	
	

