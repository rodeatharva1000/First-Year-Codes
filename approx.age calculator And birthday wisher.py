day1 = None
month1 = None
year1 = None
day2 = None
month2 = None
year2 = None 
list1 = [day1,month1,year1]
list2 = [day2,month2,year2]
inp1 = input("enter the DOB in format = DD/MM/YYYY = ")
list1[0] = int(inp1[0:2])
list1[1] = int(inp1[3:5])
list1[2] = int(inp1[6:10])
inp2 = input("enter todays date in format = DD/MM/YYYY = ")
list2[0] = int(inp2[0:2])
list2[1] = int(inp2[3:5])
list2[2] = int(inp2[6:10])
dayx = list2[0]-list1[0]
monthx = list2[1]-list1[1] 
yearx = list2[2]-list1[2]
if list2[0]<list1[0]:
    dayx = dayx+30
    monthx = monthx-1
    print(monthx)
    if list2[1]<list2[1]:
        monthx = monthx+12
        yearx = yearx-1
    else:
        pass
else:
    pass
if list2[1]<list1[1]:
    dayx = dayx
    monthx = monthx+12
    yearx = yearx-1
else:
    pass
listx = [dayx,monthx,yearx]
print(f"you are now {yearx} years and {monthx} months and {dayx} days")
if listx[0] == 0:
    if listx[1] == 0:
        name = inp("HEY !!! i have surprice for you . please enter your name = ")
        print(f"HEY ITS YOUR {yearx} BIRTHDAY HAPPY BIRTHDAY {name} !!! \nwish you many many happy ruterns of the day")
