print("Welcome To the Python BMI Calculator Program")

global unit

unit=''

xs=input("Do you want to quit program?(Y/N)").upper()

Unit1=["Supported Weight Units-kg,lb"]
Unit2=["m","cm","in"]
print(Unit1)
print(Unit2)


def unity():
	unit = input("Unit used for height ===> ").lower()
	wcalc = input("Unit used for weight ===> ").lower()
	listingunits = ["kg", "lb"]
	if wcalc in listingunits:
		y = listingunits.index(wcalc)
		print(f"You selected weight unit: {listingunts[y]}")
	else:
		print(f"{wcalc} is invalid")
		exit()
	if wcalc == "kg":
		weight = float(weight)
	elif wcalc == "lb":
		weight = float(weight) * 0.45359237
def loading():
	symbols = ['-', '/', '|', '\\']
	start_time = time.time()
	i = 0
	while time.time() - start_time < 2:
		i = (i + 1) % len(symbols)
		print('\r\033[K%s Calculating...' % symbols[i], flush=True, end='')
		time.sleep(0.1)
	print('\r\033[K', end='')
	return()

listofunits = ["m" ,"ft", "cm"]


if unit in listofunits:
	 	
		x = listofunits.index(unit)
		print(f"You selected unit: {listofunits[x]}")


else:
	print(f"{unit} is invalid")
	exit()

if unit=="cm":
	height= height(float) *100
elif unit=="m":
	height=float(height)
elif unit=="ft":
	height=float(height) * 0.3048
k=height*height
bmi = weight / k
loading()
print("Your BMI is: ", bmi)

if xs == "Y":
	exit()

else:

	we=input("(Number only) Weight ===> ")
	height=input("(Number only) Height===> ")

	unity()

