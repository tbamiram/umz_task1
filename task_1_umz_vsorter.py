Moteghaier = input("Enter your chiz : ")

if Moteghaier.isdigit():
    print("number or int")
elif len(Moteghaier) > 1 and Moteghaier[0] == "[" and Moteghaier[-1] == "]":
    print("list.")
else:
    print("string.")