#every time your crush love changes beacause of random module
website = "https://www.ghanta.com"
print(website)
import random
ans = random.randint(60,100)

inp1 = input("Enter your name            : ")
gen1 = input("Enter your gender\nm] male \nf] female\nenter                      : ")
inp2 = input("Enter your crush name      : ")
gen2 = input("Enter your crush gender\nm] male\nf] female                  : ")

if gen1 == "m" and gen2 == "f" :
	print(f"congrats {inp1} ! \nshe loves you {ans}%") 
elif gen1 == "f" and gen2 == "m" :
	print(f"congrats {inp1} ! \nhe loves you {ans}% ")
