card_number1= int (input("pls enter your card number:"))
password = int(input("pls enter your pass:"))
while True:
    j= input("1:variz pool \n 2:bardasht pool \n 3:mojoodi \n q for quit\n  what do you want to do?:")
    if j in ("1","2","3","q"):
        if j== "1":
            card_number2= int (input("pls enter card number:"))
            x=int (input("Enter the amount:"))
            print(x," $ transferred from ",card_number1,"to",card_number2)
        if j== "2":
            m=int(input("Enter the amount:"))
            print(m," $ was withdrawn")
        if j=="3":
            print("thereis felan qadr $ in your bank account")
        if j=="q":
            break