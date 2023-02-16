# to print answer
ans = "dont_know"
def print_ans():
    global ans
    print(ans,end=" . ")
# to take input
inp = input("enter the equation to find derivative \nENTER : ")
x = inp.count("-")
if "-*" or "- * "in inp :
	print(x*"-",end = " . ")
	lpg = True
if "." in inp :
    k = inp.find(".")
    if lpg == True :
        for i in range(0,k):
            m = (inp[i])
            m.replace("-","")
            print(m)
    else :
        for i in range(0,k) :
            print(inp[i],end="")

sink = 1000
cosk = 1000
tank = 1000
cotk = 1000
seck = 1000
coseck = 1000
logk = 1000
one_by_xk = 1000	
exponentialk = 1000
x_race_to_nk = 1000

# for 1/x function
def one_by_x() :
    global inp
    global ans
    global list
    if "/" in inp:
        d = inp.find("/")
        c = []
        for i in range(d+1,len(inp)) :
            c.append(inp[i])
        str = ""
        for i in c :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"-1/{str}**2")
            print_ans()
            if ans != "-1/x**2" :
                inp = str
                check_inp()
            else :
                pass
    
# for constant functions
def constant() :
    if inp.isdigit():
        global ans
        ans = 0
        print_ans()

#for sin function
def sin():
    global inp
    global ans
    global list
    if "sin(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"cos({str})")
            print_ans()
            if ans != "cos(x)" :
                inp = str
                check_inp()
            else :
            	pass
       
# for cos function
def cos():
    global inp
    global ans
    global list
    if "cos(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"-sin({str})")
            print_ans()
            if ans != "-sin(x)":
                inp = str
                check_inp()
            else :
                pass
    

# for tan function
def tan():
    global ans
    global inp
    global list
    if "tan(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"sec**2({str})")
            print_ans()
            if ans != "sec**2(x)" :
                inp = str
                check_inp()
            else :
                pass
          
# for cot function
def cot():
   global ans
   global inp
   global list
   if "cot(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"-cosec**2({str})")
            print_ans()
            if ans != "-cosec**2(x)" :
                inp = str
                check_inp()
            else :
                pass
  
# for cosec function
def cosec():
    global ans
    global inp
    global list
    if "cosec(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"-cosec({str})*cot({str})")
            print_ans()
            if ans != "-cosec(x)*cot({str})" :
                inp = str
                check_inp()
            else :
                pass
   

# for sec function
def sec():
    global ans
    global inp
    global list
    if "sec(" in inp :
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"sec({str})*tan({str})")
            print_ans()
            if ans != "sec(x)*tan(x)" :
                inp = str
                check_inp()
            else :
                pass
 

"""# for root functions
def root_x() :
    if "**1/2" in inp:
	    global ans
	    ans = "something"
	    print_ans()

for constant ** x functions
def constant_race_to() :
    if "a**" in inp :
	    w = inp.find("**")
	    for i in range(0,w):
		    global ans
		    ans = ans + inp[i]
	    ans = inp + "." +"log" + (ans)
	    print_ans()"""

# for x**n function
def x_race_to_n():
   global ans
   global inp
   global list
   if "x**" in inp :
        d = inp.find("x**")
        c = []
        for i in range(d+4,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = (f"({int(str) - 1})x**({str})")
            print_ans()
            inp = "annu"
          
# for logarithemic functuon
def log() :
    global inp
    global ans
    global list
    if "log(" in inp:
        d = inp.find("(")
        c = []
        for i in range(d+1,len(inp)-1) :
            c.append(inp[i])
        str = ""
        for i in c :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"1/{str}")
            print_ans()
            if ans != "1/x" :
                inp = str
                check_inp()
            else :
                pass
  

# for exponential functions	
def exponential():
   global ans
   global inp
   global list
   if "e**" in inp :
        d = inp.find("e")
        c = []
        for i in range(d+4,len(inp)-1) :
            c.append(inp[i])
        str = ""	
        for i in c  :
            str = "".join(c)
        if str.isdigit() :
            ans = 0
            print_ans()
        elif not str.isdigit():
            ans = (f"e**({str})")
            print_ans()
            if ans != "e**(x)" :
                inp = str
                check_inp()
            else :
                pass
	
# for nx function
def nx() :
    global inp
    global ans
    if inp.isdigit() :
        ans = 0
        print_ans()
    elif not inp.isdigit() :
        ans = inp.replace("x","")
        if ans.isdigit() :
            print(ans)

list = [sink,cosk,tank,cotk,seck,coseck,logk,one_by_xk,exponentialk,x_race_to_nk]
def main() :
    if list[0] == min(list) :
        sin() 
    if list[1] == min(list) :
        cos() 
    if list[2] == min(list) :
        tan()
    if list[3] == min(list) :
        cot() 
    if list[4] == min(list) :
        sec() 
    if list[5] == min(list) :
        cosec() 
    if list[6] == min(list) :
        log()
    if list[7] == min(list) :
        one_by_x()
    if list[8] == min(list) :
        exponential()
    if list[9] == min(list) :
    	x_race_to_n()

def check_inp():
    global sink
    global cosk
    global tank
    global cotk
    global seck
    global coseck
    global logk
    global one_by_xk
    global exponentialk
    global x_race_to_nk
    if "sin(" in inp :
        sink = inp.find("sin(")
        list[0] = sink
    if "cos(" in inp :
        cosk = inp.find("cos(")
        list[1] = cosk
    if "tan(" in inp :
        tank = inp.find("tan(")
        list[2] = tank
    if "cot(" in inp :
        cotk = inp.find("cot(")
        list[3] = cotk
    if "sec(" in inp :
        seck = inp.find("sec(")
        list[4] = seck
    if "cosec(" in inp :
        coseck = inp.find("cosec(")
        list[5] = coseck
    if "log(" in inp :
    	logk = inp.find("log(")
    	list[6] = logk
    if "/" in inp :
    	one_by_xk = inp.find("/")
    	list[7] = one_by_xk
    if "e**" in inp :
    	exponentialk = inp.find("e**")
    	list[8] = exponentialk
    if "x**" in inp :
    	x_race_to_nk = inp.find("x**")
    	list[9] = x_race_to_nk
    sink = 1000
    cosk = 1000
    tank = 1000
    cotk = 1000
    seck = 1000
    coseck = 1000
    logk = 1000
    one_by_xk = 1000	
    exponentialk = 1000
    x_race_to_nk = 1000
    main()
check_inp()
nx()
