hour = int(input("enter the hour :"))
talk = input("is the parrot talking.. enter True/False :")

if (hour<6 or hour>20) and talk == "True":
    print("True")
else:
    print("False")