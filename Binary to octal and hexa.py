print("Format (octal) : (10011001.1101)~(16)")
print("Format (hexa) : (10011001.1101)~(8)")

inp = input("Enter : ")
inp = inp.split("~")

def hexa() :
    base = 8
    str = inp[0]
    str = str.replace("(","")
    str = str.replace(")","")
    
    str = str.split(".")
    pri_str = str[0]
    sec_str = str[1]
    print("[" ,end = "")
    pri_length = len(str[0])
    sec_length = len(str[1])
    
    for item in range(0,pri_length) :
        print(f"{pri_str[item]}*(8)^({pri_length-1})",end = "+")
        pri_length = pri_length - 1
       
    
    for item in range(0,sec_length) :
        items = -(item+1)
        
    ans = (f"{sec_str[item]}*(8)^({items})+")      
    ans = ans[0:len(ans)-1] 
    print(ans,"]")
    
      
    
def octal() :
    base = 16
    str = inp[0]
    str = str.replace("(","")
    str = str.replace(")","")
    
    str = str.split(".")
    pri_str = str[0]
    sec_str = str[1]
    print("[" ,end = "")
    pri_length = len(str[0])
    sec_length = len(str[1])
    
    for item in range(0,pri_length) :
        print(f"{pri_str[item]}*(16)^({pri_length-1})",end = "+")
        pri_length = pri_length - 1
       
    
    for item in range(0,sec_length) :
        items = -(item+1)
        
    ans = (f"{sec_str[item]}*(8)^({items})+")      
    ans = ans[0:len(ans)-1] 
    print(ans,"]")     
        
     
    
hexa_val = False
octal_val = False

if inp[1] == "(8)" :
    hexa()
elif inp[1] == "(16)" :
    octal()
    
    

    

    
