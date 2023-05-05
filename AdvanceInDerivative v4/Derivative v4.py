
# PYTHON PROJECT

# DERIVATIVE ADVANCE PROGRAM IN PYTHON (version : 4.0.0)

"""1] putting currect number and type of of bracket in the proper sequence is the heart of this program 
   2] program may behave unexpectadely if not proper brackets are given 
   3] input should be in the form of currect input method
   4] the examples are given for this refrence purpose"""



"""i also uploaded this program at github
   check my python reposetary at github"""


# my github link : https://github.com/rodeatharva1000


from colorama import Fore, Back, Style


# THE ANSWER STRING
the_ans_string = ""


# Addition prperty of string
def ans_property(add) :
    global the_ans_string
    the_ans_string = the_ans_string + add + " "
    

# changing the variables same as before
def change_insider(to) :
   global the_ans_string
   the_ans_string = the_ans_string.replace("[x]",f"[{to}]")
   


# DEFINING THE MAIN CLASS
class Derivative :
    
    # CLASS VARIABLES
    inp = None
    ans = None
 
    # CLASS CONSTRUCTOR FOR Derivative CLASS
    def __init__(self,catagory_inp) :
            self.inp = catagory_inp
            if self.inp == "-" :
                self.ans = Fore.BLUE+"] - ["+Style.RESET_ALL
                self.print_ans()
            else :
                self.check_inp()
                

     
    # PRINTING ANSWER
    def print_ans(self) :
        ans_property(self.ans)
        
        
    # SEPERATE CONSTANTS
    def seperate_constant(self) :
        find_one = self.inp.find(".")
        find_two = self.inp.find("[")
        if find_one < find_two :
            if "." in self.inp :
                list_one = []
                list_two = []
                str_one = ""
                str_two = ""
                for item in range(0,find_one) :
                    list_one.append(self.inp[item])
                for item in list_one :
                    str_one = "".join(list_one)
                    
                for item in range((find_one)+1,len(self.inp)) :
                    list_two.append(self.inp[item])
                for item in list_one :
                    str_two = "".join(list_two)
                
                ans_property(str_one)
                self.inp = str_two
            else :
                pass

# example : 33.sin(90x)
        
    
    # REMOVING MINUS 
    def seperate_minus(self) :
        if ")-" in self.inp :
            pass
        else :
            if "-" in self.inp :
                if "[" in self.inp :
                    find_pri = self.inp.find("-")
                    find_sec = self.inp.find("[")
                    if find_pri < find_sec :
                        list = []
                        for item in range(0,len(self.inp)) :
                            if item == 0 :
                                pass
                            else :           
                                list.append(self.inp[item])
                        str = "".join(list)
                        self.inp = str          
                        self.ans = "(-)"
                        self.print_ans() 
                else :
                    self.ans = "(-)"
                    self.print_ans()
                    self.inp = self.inp.replace("-","")
            



    
    
    # LOOPING THE FUNCTION 
    def myfind(self) :
        global the_ans_string
        primary_list = [0]
        secondary_list = []
        for item in range(0,len(self.inp)) :
            if self.inp[item] == "[" :
                primary_list.append(item)
        
        find = self.inp.find("]")
        secondary_list.append(find)
        
        open_bracket = max(primary_list)
        
        secondary_inp = ""
        
        for item in range((open_bracket)+1,find) :
            secondary_inp = secondary_inp + self.inp[item]
        
        if ")+" in secondary_inp :
            ans_property(Fore.GREEN+"("+Style.RESET_ALL)
            self.inp = self.inp.replace(secondary_inp,"x") 
            self.check_inp()
            change_insider(secondary_inp)  
            self.inp = ""
            ans_property(Fore.GREEN+")"+Style.RESET_ALL)
            secondary_inp = secondary_inp.replace("(","[")
            secondary_inp = secondary_inp.replace(")","]") 
            obj = Catagory(secondary_inp)
        elif ")-" in secondary_inp :
            ans_property(Fore.GREEN+"("+Style.RESET_ALL)
            self.inp = self.inp.replace(secondary_inp,"x") 
            self.check_inp() 
            change_insider(secondary_inp)       
            self.inp = "" 
            ans_property(Fore.GREEN+")"+Style.RESET_ALL)
            secondary_inp = secondary_inp.replace("(","[")
            secondary_inp = secondary_inp.replace(")","]")
            obj = Catagory(secondary_inp)
        elif ")*" in secondary_inp :
            ans_property(Fore.GREEN+"("+Style.RESET_ALL)
            self.inp = self.inp.replace(secondary_inp,"x") 
            self.check_inp() 
            change_insider(secondary_inp)
            self.inp = ""
            ans_property(Fore.GREEN+")"+Style.RESET_ALL)
            secondary_inp = secondary_inp.replace("(","[")
            secondary_inp = secondary_inp.replace(")","]")
            obj = Catagory(secondary_inp)
        elif ")/" in secondary_inp :
            ans_property(Fore.GREEN+"("+Style.RESET_ALL)
            self.inp = self.inp.replace(secondary_inp,"x") 
            self.check_inp() 
            change_insider(secondary_inp)
            self.inp = ""
            ans_property(Fore.GREEN+")"+Style.RESET_ALL)
            secondary_inp = secondary_inp.replace("(","[")
            secondary_inp = secondary_inp.replace(")","]")
            obj = Catagory(secondary_inp)
        else :
            pass
    
    
    # CHECKING INPUT (CONSIDERING BOTH CLASSES)
    def check_inp(self) : 
    
        self.myfind()
        
        self.seperate_minus()
        
        self.seperate_constant()
        
        if self.inp == "+" :
            self.ans = Fore.BLUE+"] + ["+Style.RESET_ALL
            self.print_ans()
                  
        elif self.inp == "/" :
            self.ans = "/"
            self.print_ans()
        
        elif self.inp.startswith("sin[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sin()
        
        elif self.inp.startswith("cos[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cos()
        
        elif self.inp.startswith("tan[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.tan()
        
        elif self.inp.startswith("cot[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cot()
        
        elif self.inp.startswith("sec[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sec()
        
        elif self.inp.startswith("cosec[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cosec()
            
        elif self.inp.startswith("sin^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sin_inv()
                
        elif self.inp.startswith("cos^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cos_inv()
                
        elif self.inp.startswith("tan^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.tan_inv()
                
        elif self.inp.startswith("cot^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cot_inv()
                
        elif self.inp.startswith("sec^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sec_inv()       
        
        elif self.inp.startswith("cosec^[-1]") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cosec_inv()
               
        elif self.inp.startswith("log[") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.log()
        
        elif self.inp.startswith("e^") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.exponential()
        
        elif "/" and "]^" in self.inp : 
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.twwo_in()
        
        elif "/" in self.inp :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.one_by_x()
        
        elif "]^" in self.inp :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :                
                self.choose() 
        
        elif not self.inp.isdigit() :
            self.nx()
        
        elif self.inp.isdigit() :
            self.constant()

    
    # DISIGIONS
    def twwo_in(self) :
        if self.inp.startswith("[") :
            self.choose()
        elif not self.inp.startswith("[") :
            self.one_by_x()
    
    
    # SIN(TRIGO) FUNCTION
    def sin(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"cos[{str}]")
            self.print_ans()
            if self.ans != "cos[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : sin(90x) , sin(cos(90x))

    
    # COS(TRIGO) FUNCTION
    def cos(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-sin[{str}]")
            self.print_ans()
            if self.ans != "-sin[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : cos(tan(90x))
    
    
    # TAN(TRIGO) FUNCTION
    def tan(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"sec^(2)[{str}]")
            self.print_ans()
            if self.ans != "sec^(2)[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : tan(sin(90x))

    
    # COT(TRIGO) FUNCTION
    def cot(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-cosec^(2)[{str}]")
            self.print_ans()
            if self.ans != "-cosec^(2)[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass

 # example : cot(sec(90x)) 

    
    # SEC(TRIGO) FUNCTION
    def sec(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"sec[{str}]*tan[{str}]")
            self.print_ans()
            if self.ans != "sec[x]*tan[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : sec(tan(cosec(90x))) 

    
    # COSEC(TRIGO) FUNCTION
    def cosec(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-cosec[{str}]*cot[{str}]")
            self.print_ans()
            if self.ans != "-cosec[x]*cot[{str}]" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : cosec(tan(90x))   


    # SININV(TRIGO) FUNCTION
    def sin_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"1/[1-({str})^2]^(1/2)")
            self.print_ans()
            if self.ans != "1/[1-(x)^2]^(1/2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                

 # example : sin^(-1)(tan(3x))
                
    
    # COSINV(TRIGO) FUNCTION
    def cos_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-1/[1-({str})^2]^(1/2)")
            self.print_ans()
            if self.ans != "-1/[1-(x)^2]^(1/2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                
                

 # example : cos^(-3)(tan(4x))
                
                
     # TANINV(TRIGO) FUNCTION 
    def tan_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"1/1+({str})^(2)")
            self.print_ans()
            if self.ans != "1/1+(x)^(2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                          

 # example : tan^(-1)(cot(99x))
 
 
                
    # COTINV(TRIGO) FUNCTION
    def cot_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-1/1+({str})^(2)")
            self.print_ans()
            if self.ans != "-1/1+(x)^(2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                

 # example : cot^(-1)(sec(7x))
                
             
    # SECINV(TRIGO) FUNCTION
    def sec_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"1/({str})[({str})^(2)-1]^(1/2)")
            self.print_ans()
            if self.ans != "1/(x)[(x)^(2)-1]^(1/2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                
                

 # example : sec^(-1)(log(3x))
                
                
    # COSECINV(TRIGO) FUNCTION
    def cosec_inv(self) :
        find = self.inp.find("^[-1][")
        list = []
        for i in range(find+6,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-1/({str})[({str})^(2)-1]^(1/2)")
            self.print_ans()
            if self.ans != "-1/(x)[(x)^(2)-1]^(1/2)" :
                self.inp = str
                self.check_inp()
            else :
                pass
                
                

 # example : cosec^(-1)(sin(cos(9x)))
    
    
    
    # LOG FUNCTION
    def log(self) :
        find = self.inp.find("[")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""
        for i in list :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"1/{str}")
            self.print_ans()
            if self.ans != "1/x" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : log(sin(90x))

    
    # N(X) FUNCTION
    def nx(self) :
        str = self.inp.replace("x","(1)")
        self.ans = str
        self.print_ans()
         
        
    # ABOUT CONSTANT
    def constant(self) :
        self.ans = "0"
        self.print_ans()


# example : 33 , 43   

    # DISIGION
    def choose(self) :
        list = []
        str = ""
        find_one = self.inp.find("[")
        find_two = self.inp.find("]")
        for item in range((find_one)+1,find_two) :
            list.append(self.inp[item])
            
        str = "".join(list)

        if "x" not in str :
            self.cons_race_to_x()
        else :
            self.x_race_to_n()
            

    
    # CONSTANT RACE TO X
    def cons_race_to_x(self) :
        str_one = ""
        str_two = ""
        list_one = []
        list_two = []
        find_one = self.inp.find("[")
        find_two = self.inp.find("]^")
        find_pri = self.inp.find("^[")
        for item in range((find_one)+1,find_two) :
            list_one.append(self.inp[item])
       
        for item in range((find_pri)+2,len(self.inp)-1) :
            list_two.append(self.inp[item])
        
        str_one = "".join(list_one)
        str_two = "".join(list_two)
        
        
        if "x" not in str_two :
            self.ans = 0
            self.print_ans()
        elif not str_two.isdigit() :
            self.ans = (f"({str_one})^({str_two}).log({str_one})")
            self.print_ans()
            if self.ans != "({str_one})^(x).log({str_one})" :
                self.inp = str_two
                self.check_inp()
            else :
                pass
                
                
 # example : (32)^(log(x))
        
        
    
    
    # EXPONENTIAL FUNCTION
    def exponential(self):
        find = self.inp.find("e")
        list = []
        for i in range(find+3,len(self.inp)-1) :
            list.append(self.inp[i])
        str = ""	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"e^[{str}]")
            self.print_ans()
            if self.ans != "e^[x]" :
                self.inp = str
                self.check_inp()
            else :
                pass

 # example : e^(cos(90x))   
    
    
    # 1/X FUNCTION
    def one_by_x(self) :
        find = self.inp.find("/")
        find_second = self.inp.find("[")
        
        list = []
        list_second = []
        list_third = []
        str = ""
        str_second = ""
        str_third = ""
        
        for i in range(0,find) :
            list.append(self.inp[i])
        for i in list :
            str = "".join(list)
        
        
        for i in range(find_second+1,len(self.inp)-1) :
            list_second.append(self.inp[i])        
        for i in list_second : 
            str_second = "".join(list_second)

        
        for i in range(find+1,find_second) :
            list_third.append(self.inp[i])        
        for i in list_third : 
            str_third = "".join(list_third)

        
        if str_second.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str_second.isdigit():
            self.ans = (f"-{str}/{str_third}[{str_second}]^2")
            self.print_ans()
            if self.ans != "-1/[x]^2" : 
                self.inp = str_second
                self.check_inp() 
            else :
                pass  


# example : 1/(x) , 22/44(cos(90x))
    
    
    
    # VARIABLE RACE TO CONSTANT (Root functions also includes here)
    def x_race_to_n(self): 
        find = self.inp.find("]^")
        find_second = self.inp.find("^[")
        list = []
        list_second = []
        str = ""
        str_second = ""
        
        
        for i in range(1,find) :
            list.append(self.inp[i])	
        for i in list :
            str = "".join(list)

        for i in range(find_second+2,len(self.inp)-1) :
            list_second.append(self.inp[i])	
        for i in list_second :
            str_second = "".join(list_second)
        
        if str.isdigit() :
            self.ans = "0" 
            self.print_ans()

        elif not str.isdigit() : 
            self.ans = (f"{str_second}.{str}^{int(str_second)-1}")
            self.print_ans()
            if "[x]^" not in self.inp :
                self.inp = str
                self.check_inp()
            else :
                pass         

# example : (sin(cos(90x)))^(67)



# FINDING AND APPLYING CATYAGORY FOR 2 (U AND V) FUNCTIONS


class Catagory :

    # CATAGORY CLASS VARIABLES
    
    main_inp = None
    
    main_ans = None 
    
   
     # PRINTING MAIN ANSWER
    def print_main_ans(self) :
        ans_property(self.main_ans)
    
    
    # FOR SPECIAL ANSWER OF DIVIDION
    def print_main_division_ans(self) :
        ans_property(f"[({self.main_ans})^2]")
    
    
    
    # CLASS CONSTRUCTOR FOR Catagory CLASS
    def __init__(self,inputs) : 
        self.main_inp = inputs
        self.main_inp = self.main_inp.replace(" ","")
        self.main_inp = self.main_inp.lower()
        self.check_main_inp()
    
    
    
    # CHECKING MAIN INPUT
    def check_main_inp(self) :
        if "]+" in self.main_inp :
            self.plus()
        elif "]*" in self.main_inp :
            self.product()  
        elif "]/" in self.main_inp :      
            self.division()   
        elif "]-" in self.main_inp : 
            self.minus()
        else : 
            obj = Derivative(self.main_inp)

    
    # FUNCTION OF PLUS
    def plus(self) :
        self.main_inp = self.main_inp.replace("]+","]]+")
        plus_list = self.main_inp.split("]+")
        plus_list.append("+")
        plus_list[1] , plus_list[2] = plus_list[2] , plus_list[1]
        
        
        ans_property(Fore.BLUE+"["+Style.RESET_ALL)
        for object in range(0,len(plus_list)) :
            obj = Derivative(plus_list[object])
        ans_property(Fore.BLUE+"]"+Style.RESET_ALL)

    
    # FUNCTION OF MINUS
    def minus(self) : 
        str = ""
        list = []
        for item in self.main_inp :
            list.append(item)
        for items in list :
            str = "".join(list) 
            self.main_inp = str
        self.main_inp = self.main_inp.replace("]-","]]-")
        minus_list = self.main_inp.split("]-") 
        minus_list.append("-")
        minus_list[1] , minus_list[2] = minus_list[2] , minus_list[1]

        ans_property(Fore.BLUE+"["+Style.RESET_ALL)
        for object in range(0,len(minus_list)) :
            obj = Derivative(minus_list[object])
        ans_property(Fore.BLUE+"]"+Style.RESET_ALL)
        
    
    
    
    # FUNCTION OF PRODUCT    
    def product(self) : 
        self.main_inp = self.main_inp.replace("]*","]]*")
        product_list = self.main_inp.split("]*")
        product_list.append("+")
        product_list.append(product_list[0])
        product_list.append(product_list[1])
        
        ans_property(Fore.BLUE+"{"+Style.RESET_ALL)
        ans_property(Fore.BLUE+"["+Style.RESET_ALL)
        for object in range(0,len(product_list)) :   
            if object % 2 == 0 :
                obj = Derivative(product_list[object])
            else :
                self.main_ans = product_list[object]
                self.print_main_ans() 
        ans_property(Fore.BLUE+"]"+Style.RESET_ALL)
        ans_property(Fore.BLUE+"}"+Style.RESET_ALL)
        
       

    
    # FUNCTION OF DIVISION
    def division(self) :
        self.main_inp = self.main_inp.replace("]/","]]/")
        division_list = self.main_inp.split("]/")
        division_list[0] , division_list[1] = division_list[1] , division_list[0]
        division_list.append("-")
        division_list.append(division_list[1])
        division_list.append(division_list[0])
        division_list.append("/")
        division_list.append(division_list[0])

        
        
        
        # FOR CREATING OBJECT ACCORDING TO LIST
        for object in range(0,len(division_list)) : 
            if object == 1 :
                obj = Derivative(division_list[object])
            elif object == 2 :
                obj = Derivative(division_list[object])
            elif object == 4 :
                obj = Derivative(division_list[object])
            elif object == 5 :
                ans_property(Fore.BLUE+"]"+Style.RESET_ALL) 
                ans_property(Fore.RED+"}"+Style.RESET_ALL) 
                obj = Derivative(division_list[object])
            elif object == 0 :
                ans_property(Fore.RED+"{"+Style.RESET_ALL)
                ans_property(Fore.BLUE+"["+Style.RESET_ALL) 
                self.main_ans = division_list[object]
                self.print_main_ans()
            elif object == 3 :
                self.main_ans = division_list[object] 
                self.print_main_ans() 
            elif object == 6 :
                self.main_ans = division_list[object] 
                self.print_main_division_ans()

print(Fore.BLUE+"version : 4*",Style.RESET_ALL)
print(Fore.RED+"# Fundamental Calculus(I1912)",Style.RESET_ALL)
print(Fore.GREEN+"               [ ADVANCE IN DERIVATIVES ]"+Style.RESET_ALL)
print(Fore.YELLOW+"\n 1 } Enter The Function To Find Derivative ( limitaion till u and v )\n 2 } For Outer Function Use [ ] \n 3 } For Inner Function Use ( ) \n 4 } Use . To Multiply Constant \n 5 } Use ^ to show powers \n 6 } Input According To The Input Methods Is Mendetary\n 7 } Read Instructions Before Using\n 8 } Try Provided Examples To Learn More About Input Methods \n"+Style.RESET_ALL)

print(Fore.GREEN+" Ex : -"+Style.RESET_ALL)

print(" 1 ] sin(2x) \n 2 ] 58.sin(log(3x)) \n 3 ] log(sec(32x))+tan(5x) \n 4 ] tan[sec(6x)-33.sin(x)] \n 5 ] sec[23.tan(3x)-tan(3x)]-log[4x]")





# RUNNING LOOP TILL INFINITY
while True :
    print(Fore.BLUE+"__________________________________________________________"+Style.RESET_ALL)
    print("\n")
    inputs = input(Fore.RED+" Enter : f(x) : "+Style.RESET_ALL)
    print(Fore.GREEN+f" (d/dx) of {inputs} is "+Style.RESET_ALL)
    if "[" not in inputs :
        inputs = inputs.replace("(","[")
        inputs = inputs.replace(")","]")
    # creating object of Catagory class
    obj = Catagory(inputs)
    print("\n")
    print(" "+the_ans_string)
    the_ans_string = ""


# EXAMPLES ON CATAGORIES :

# catagory (+) : sin(90x)+cos(90x)

# catagory (-) : sin(90x)-sin(tan(90x))

# catagory (*) : sin(90x)*sec(95x)

# catagory (/) : cosec(90x)/sec(90x)


# program catagory - maths\calculus\derivatives

# work catagory - u+v / u-v / u.v | u/v

# code editor - visual studio (VS) code 

# language - python

# VERSION THREE
# release : 05/05/2023
# last update : lets see
# three level two function dervatives

# Developed and maintained by :- @ Rode Atharva Mahesh 

# OS : on windows os

# for any queery  :  rodeatharva2@gmail.com
