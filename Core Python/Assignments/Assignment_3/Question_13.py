### Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit--0 to 50
# For next 100 units Rs. 0.75/unit -- 50-150
# For next 100 units Rs. 1.20/unit -- 150-250
# For unit above 250 Rs. 1.50/unit -- above 250
# An additional surcharge of 20% is added to the bill

# Take electricity unit from user
unit=int(input("Enter the Electricity units ::"))
bill=0

#perform the operation
#line of code can be shortend with the use of loop. 
if(unit>250):
    over_unit= unit-250
    bill+=over_unit*1.5
    unit=unit-over_unit
if(unit>=150):
    over_unit= unit-150
    bill+=over_unit*1.2 
    unit=unit-over_unit
if(unit>=50):
    over_unit= unit-50
    bill+=over_unit*0.75 
    unit=unit-over_unit
if(unit>=0):
    over_unit= unit-0
    bill+=over_unit*0.5
    unit=unit-over_unit
bill= 1.2*bill

#display result
print(f"The bill amount for given unit is :: {bill}")