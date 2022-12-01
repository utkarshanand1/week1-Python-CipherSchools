

print("**********************************")
print("********* This is simple calculator ******")
print("+ for addition")
print("- for subraction")
print("* for multiplication")
print("/ for division")
print("** for power of firstno. to secondno.")
print("// floor division")
print("%" "for remainder")
print("**********************************")
num1=int(input("Enter your first no. : "))
num2=int(input("Enter your second  no. : "))
operator_1=input('Enter what u what to do : ') 
if operator_1=='+':
    print("Sum :",num1+num2)
elif operator_1=='-':
    print("subtract :",num1-num2)
elif operator_1=='*':
    print("multiply:",num1*num2)
elif operator_1=='/':
    print("divide",num1/num2)
elif operator_1=='**':
    print("power",num1**num2)
elif operator_1=='//':
    print("Floar division",num1//num2)
elif operator_1=='%':
    print("remainder",num1%num2)
else:
    print("Fill correctly")

