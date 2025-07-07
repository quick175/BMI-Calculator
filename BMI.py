print("Welcome To the Python BMI Calculator Program")

global unit

unit=str

xs=input("Do you want to quit program?(Y/N)").upper()

Unit1=["Supported Weight Units-kg,lb"]
Unit2=["m,cm,ft,in"]
print(Unit1)
print(Unit2)


def unity():
    unit = input("Unit used for height ===> ").lower()
    listofunits = ["m", "in", "ft", "cm"]
    if unit in listofunits:
        x = listofunits.index(unit)
        print(f"You selected unit: {listofunits[x]} (index {x})")
    else:
        print(f"{unit} is invalid")
        exit()

	
	
	
	
	
	
	
	
"""stop=len(Unit2)
	for i in range(stop):
		if Unit2[i] == unit:
			print(unit,"is valid")
		else:
			print(unit,"is invalid")
			exit()"""




if xs == "Y":
	exit()

else:
	
	we=input("(Number only) Weight ===> ")
	#w_calc()
	height=input("(Number only) Height===> ")
	
	unity()

