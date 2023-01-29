print("@simultanious equations")
print("spaces are allowed")
print("IN FORMAT : n1x+m1y=k1")
print("show error if y1=y2 or xx1=xx2")
inp1 = input("Enter 1st equation  : ")
inp1 = inp1.replace(" ","")
p = inp1.find("x")
a = []
for i in range(0,p):
	a.append(inp1[i])

q = inp1.find("y")
b = []
for j in range(p+1,q):
	b.append(inp1[j])

r = inp1.find("=")
c = []
for k in range(q+2,len(inp1)):
	c.append(inp1[k])

print("IN FORMAT : n2x+m2y=k2")
inp2 = input("Enter 2st equation  : ")
inp2 = inp2.replace(" ","")
p = inp2.find("x")
d = []
for i in range(0,p):
	d.append(inp2[i])

q = inp2.find("y")
e = []
for j in range(p+1,q):
	e.append(inp2[j])

r = inp2.find("=")
f = []
for k in range(q+2,len(inp2)):
	f.append(inp2[k])

n1 = "".join(a)
print("n1 = ",n1)
m1 = "".join(b)
print("m1 = ",m1)
k1 = "".join(c)
print("k1 = ",k1)
n2 = "".join(d)
print("n2 = ",n2)
m2 = "".join(e)
print("m2 = ",m2)
k2 = "".join(f)
print("k2 = ",k2)

x1 = int(n2)*int(n1)
y1 = int(n2)*int(m1)
z1 = int(n2)*int(k1)

x2 = int(n1)*int(n2)
y2 = int(n1)*int(m2)
z2 = int(n1)*int(k2)
y = (z1-z2)/(y1-y2)

xx1 = int(m2)*int(n1)
yy1 = int(m2)*int(m1)
zz1 = int(m2)*int(k1)

xx2 = int(m1)*int(n2)
yy2 = int(m1)*int(m2)
zz2 = int(m1)*int(k2)
x = (zz1-zz2)/(xx1-xx2) 
print(f"x is : ",x)

print(f"y is : ",y)
