x=list()
y=0
w=0
while(w < 2):
    y=input("dammi un numero")
    x.append(y)
    w+=1

y=0
for num in x:
    y=y+int(num)

print(y/len(x))

