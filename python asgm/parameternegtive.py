a = int(input("enter first :"))
b = int(input("enter second :"))
param = input("enter parameter : ")

if (a<0 and b>0) or (a>0 and b<0):
    if param == "False":
        print("True")
    else:
        print("False")

elif a<0 and b<0:
    if param == "True":
        print("True")
    else:
        print("False")
else:
    print("False")
