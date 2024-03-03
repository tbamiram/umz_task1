mode = input("1:fahrenheit to celsius \n 2:celsius to fahrenheit \n enter your mode:")
temp1 = float (input("pls enter your temp:"))
if mode in ("1","2"):
    if mode=="1" :
        resault=(temp1-32)/1.8
    elif mode=="2" :
        resault=(1.8*temp1)+32 
print("Resault:", resault)      