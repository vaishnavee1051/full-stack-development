p1=500
p2=200
distance=5
total=0
cost=0
if(distance<3):
    cost=10
if(distance<6):
    cost=20
else:
    cost=30
total=(distance*cost)+(p1+p2)
print(total)