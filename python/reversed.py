a=456789
reversed_a=0

while(a!=0):
    digit=a%10
    reversed_a = reversed_a*10+digit
    a//=10

print("Reversed Number: " + str(reversed_a))