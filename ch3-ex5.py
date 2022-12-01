a=input("Enter your name : ")
b=len(a)
i=0

temp=""
while i<b:
    if a[i] not in temp:
        temp=temp+a[i]
        print(a[i],"is reapt",a.count(a[i]),"times")
    i=i+1