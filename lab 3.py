#This program converts pints of milk to quarts, gallons, and pints.
#Created by: Chris Caponi
pints= int(input("How many pints of milk are on the truck?  "))

gal=pints//8
quart=(pints%8)//2
pint=pints%2

print(pints,"Pints=")
print("\t",gal,"gallon(s),")
print("\t",quart,"quart(s),and")
print("\t",pint,"pint(s).")

percGal=((gal*8)/pints)*100
percQuar=((quart*2)/pints)*100
percPint=(pint/pints)*100

print("Of the",pints,"pints:")
print(format(percGal,"15.3f"),"%"," of the pints became gallons",sep="")
print(format(percQuar,"15.3f"),"%"," became quarts, and",sep="")
print(format(percPint,"15.3f"),"%"," stayed as pints.",sep="")

print(input("press enter to exit."))

      








