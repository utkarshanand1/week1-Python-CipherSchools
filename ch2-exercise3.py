name,char=input().split(",")
print(len(name))
print(name.count(char.lower())+name.count(char.upper()))