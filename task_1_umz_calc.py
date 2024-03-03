a= float (input("enter number 1 :"))
x=input("enter your operation:")
b=float (input("enter number 2 :"))
if x in ("sum" ,"difference","multiple", "divide" ):
    if x== "sum":
        resault=a+b
    elif x== "difference":
        resault=a-b
    elif x== "multiple":
        resault=a*b
    elif x== "divide":
        resault=a/b  
    else : 
        print("invalid operation")  
print("Resault:", resault)      