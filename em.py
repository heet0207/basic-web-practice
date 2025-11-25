grade = input("Enter the grade_level (A,B,C,D,E or F): ").upper()
city = int(input("Enter the city (1,2 or 3): "))
PT = 200
TA = 900

if grade == 'A':
    basic_pay = 60000
    other_allowances = 8000
elif grade == 'B':
    basic_pay = 50000
    other_allowances = 7000
elif grade == 'C':
    basic_pay = 40000
    other_allowances = 6000
elif grade == 'D':
    basic_pay = 30000
    other_allowances = 5000
elif grade == 'E':
    basic_pay = 20000
    other_allowances = 4000
elif grade == 'F':
    basic_pay = 10000
    other_allowances = 3000
else:
    print("Invalid grade level")
    exit()
    
    
if city == 1 :
    HRA = basic_pay*0.3
elif city == 2 :
    HRA = basic_pay*0.2
elif city == 3 :
    HRA = basic_pay*0.1
else :
    print("Invalid City Name")
    exit()
    
DRA = 0.5*basic_pay
EPF = 0.11*basic_pay
GP = basic_pay + HRA + DRA + other_allowances +TA - PT -EPF
print(GP)
annual_pay = GP*12
if annual_pay > 250000:
    if annual_pay <= 500000:
        tax = 0.05 * (annual_pay - 250000)
    elif annual_pay <= 750000:
        tax = 12500 + 0.1 * (annual_pay - 500000)
    elif annual_pay <= 1000000:
        tax = 37500 + 0.15 * (annual_pay - 750000)
    elif annual_pay <= 1250000:
        tax = 75000 + 0.2 * (annual_pay - 1000000)
    elif annual_pay <= 1500000:
        tax = 125000 + 0.25 * (annual_pay - 1250000)
    else:
        tax = 187500 + 0.3 * (annual_pay - 1500000)

print("Gross Pay of an Employee is:", GP)
print("Annual income of an Employee is:", annual_pay)
print("Income Tax to be paid by an Employee is:", tax)