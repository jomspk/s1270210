import random

string=""
countH=0
countT=0
print("Who are you?")
y=input()
print("Hello, "+y+"!")
z="you"
print("Tossing a coin...")
for i in range(3):
    x=random.randrange(2)
    if x==0:
        countH=countH+1
        string="Heads"
    else:
        countT=countT+1
        string="Tails"
    print("Round "+str(i+1)+": "+string)
print("Heads: "+str(countH)+", Tails: "+str(countT))
if countH>countT:
    print(z+" won")
else:
    print(z+" lost")