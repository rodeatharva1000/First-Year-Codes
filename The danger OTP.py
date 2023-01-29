list = []
import random
def key_1():
    ans1 = random.randint(1,9)
    global list
    list.append(str(ans1))

def key_2():
    tp = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z")
    ans2 = random.randint(0,24)
    global list
    x = tp[ans2]
    list.append(x)
    
for i in range(1,9):
    ans = random.randint(1,2)
    if ans == 1:
        key_1()
    elif ans == 2:
        key_2()

for j in range(0,len(list)):
    print(list[j],end = "")
print("\n")

list2 = []
inp = input("enter the OTP = ")
for i in range(0,len(inp)):
    list2.append(inp[i])

if list == list2 :
    print("correct OTP")
else:
    print("wrong OTP !")



