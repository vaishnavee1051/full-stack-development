a=9
factorial=1
if(a<0):
   print("factorial not exist")
elif(a==0):
   print("The factorial of 0 is 1")
else:
   for i in range(1,10):
       factorial = factorial*i
   print("The factorial of",a,"is",factorial)