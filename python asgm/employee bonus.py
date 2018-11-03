ename = input("enter employee name :")
esal = float(input("enter salary :"))
desg = input("enter designation :")

if desg == 'manager':
    bonus = esal*20/100
    esal += bonus
    print("final salary :", esal)

elif desg == 'analyst':
    bonus = esal*10/100
    esal += bonus
    print("final salary :", esal)

elif desg == 'clerk':
     bonus = esal*5/100
     esal += bonus
     print("final salary :", esal)
else:
    print("incorrect slab entered")
    
print("thanks")
