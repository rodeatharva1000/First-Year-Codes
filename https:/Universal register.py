seta = set()
w = int(input("count of students in class =  "))
for j in range(1,w+1):
	seta.add(j)
setb = set()

for i in range (1,w+1):
	inp = int(input("enter the roll no = "))
	if inp==0:
	    break
	else:
	  	setb.add(inp)
z = seta.symmetric_difference(setb)
z.discard(0)
list = [z]
list.sort()
print("absent no are = ")
print(list)
