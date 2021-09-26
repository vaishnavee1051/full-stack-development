x=4
n=10
s=0
s = 1+x+x^2+x^3+x^n
for i in range(n+1):
	s+=x**i
print("sum of series:",s)	