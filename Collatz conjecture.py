no = int(input("enter the no = "))
for i in range(1,100000000000000):
    if no%2==0:
    	no = no/2
    	print(no)
    	if no==1:
    		break
	
    else:
    	no = (no*3)+1
    	print(no)
    	if no==1:
    		break
