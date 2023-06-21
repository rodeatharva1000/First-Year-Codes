# opp**2 + adj**2 = hypo**2


hypo = ""
opp = ""
adj = ""

inp_side_pri = float(input("enter side length 1 : "))
inp = int(input("side type 1)hypotenous\n2)opposite\n3)adjecent : "))
if inp== 1 :
    hypo = inp_side_pri
elif inp == 2 :
    opp = inp_side_pri
elif inp == 3 :
    adj = inp_side_pri

inp_side_sec = float(input("enter side length 2 : "))
inp = int(input("side type 1)hypotenous\n2)opposite\n3)adjecent : "))
if inp== 1 :
    hypo = inp_side_sec
elif inp == 2 :
    opp = inp_side_sec
elif inp == 3 :
    adj = inp_side_sec
    
def hypo_fun() :
    global hypo
    hypo = (adj**2 + opp**2)**(1/2)
def opp_fun() :
    global opp
    opp = (hypo**2 - adj**2)**(1/2)
def adj_fun() :
    global adj
    adj = (hypo**2 - opp**2)**(1/2)
    


if hypo == "" :
    hypo_fun()
elif opp == "" :
    opp_fun()
elif adj == "" :
    adj_fun()
    
    
print(f"sin : {opp}/{hypo}")
print(f"cos : {adj}/{hypo}")
print(f"tan : {opp}/{adj}")
print(f"cot : {adj}/{opp}")
print(f"sec : {hypo}/{adj}")
print(f"cosec : {hypo}/{opp}")

#@ rodeatharva
#Github : github.com/rodeatharva1000
