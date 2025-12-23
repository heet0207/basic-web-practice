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




#534
class pizza:
    def __init__(self,size,toppings,cheese):
        self.size=size
        self.toppings=toppings
        self.cheese=cheese
    def price(self):
        self.cost=0
        if self.size=='small':
            self.cost+=50
        elif self.size=='medium':
            self.cost+=100
        elif self.size=='large':
            self.cost+=200
        else:
            print('Enter valid size')
        topping_price_20=['corn','tomato','onion','capsicum']
        topping_price_50=['mushroom','olives','broccoli']
        for topping in self.toppings:
            if topping in topping_price_20:
                self.cost+=20
            else:
                self.cost+=50
        self.cost+=50*(len(self.cheese))
        return self.cost
class Order:
    def __init__(self,name,customerid):
        self.name=name
        self.customerid=customerid
    def order(self,n):
        self.pizzas=[]
        for i in range(n):
            toppings=[]
            cheese=[]
            print('Customize Pizza',i+1)
            size=(input('Enter the size of pizza :'))
            t=int(input('Enter No. of topping :'))
            for i in range(t):
                toppings.append(input('Enter topping :'))
            c=int(input('Enter no of cheese :'))
            for i in range(c):
                cheese.append(input('Enter cheese names :'))
            self.pizzas.append(pizza(size,toppings,cheese))
    def bill(self):
        self.total=0
        count=1
        for p in self.pizzas:
            print('Pizza',count)
            print(p.size,p.toppings,p.cheese)
            self.total+=p.price()
            count+=1
        print('Total bill amount:',self.total)
order1=Order('As',1)
p=int(input('Enter number of0 Pizza '))
order1.order(p)
order1.bill()


class Student:
    def __init__(self):
        # constructor
        self.students = []

    # accept student details
    def accept(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print("\nEnter details of student", i + 1)
            name = input("Enter Name: ")
            roll = int(input("Enter Roll Number: "))
            marks1 = int(input("Enter Marks of Subject 1: "))
            marks2 = int(input("Enter Marks of Subject 2: "))

            self.students.append({
                "name": name,
                "roll": roll,
                "marks1": marks1,
                "marks2": marks2
            })

    # display all students
    def display(self):
        if not self.students:
            print("No student records found.")
            return

        print("\nList of Students")
        for s in self.students:
            print("Name :", s["name"])
            print("RollNo :", s["roll"])
            print("Marks1 :", s["marks1"])
            print("Marks2 :", s["marks2"])
            print()

    # search student by roll number
    def search(self):
        roll = int(input("Enter roll number to search: "))
        for s in self.students:
            if s["roll"] == roll:
                print("\nStudent Found")
                print("Name :", s["name"])
                print("RollNo :", s["roll"])
                print("Marks1 :", s["marks1"])
                print("Marks2 :", s["marks2"])
                return
        print("Student not found.")

    # delete student by roll number
    def delete(self):
        roll = int(input("Enter roll number to delete: "))
        for s in self.students:
            if s["roll"] == roll:
                self.students.remove(s)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    # update roll number
    def update(self):
        old_roll = int(input("Enter old roll number: "))
        new_roll = int(input("Enter new roll number: "))

        for s in self.students:
            if s["roll"] == old_roll:
                s["roll"] = new_roll
                print("Roll number updated successfully.")
                return
        print("Student not found.")


# Main Program
obj = Student()

while True:
    print("\n--- Student Management System ---")
    print("1. Accept")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.accept()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.search()
    elif choice == 4:
        obj.delete()
    elif choice == 5:
        obj.update()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
