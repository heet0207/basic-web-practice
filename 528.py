class rectangle:
    def __init__(self,len,width):
        self.len=len
        self.width=width
    def area(self):
        area=self.len*self.width
        print("Area=",area)
r=rectangle(5,4)
r.area()


class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("Name:",self.name)
        print("mark :",self.mark)
    def set_mark(self,mark):
        self.mark=mark
    def get_mark(self):
        return self.mark
st=student("Alice",20)
st.display()
st.set_mark(25)
print('Name :',st.name,'&',"Updated mark:",st.get_mark())


class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
        print("Area of circle:",area)
    def perimeters(self):
        perimeter=2*3.14*self.radius
        print("Perimeter of circle:",perimeter)
c=circle(3)
c.area()
c.perimeters()



class Store:
    def __init__(self):
        self.items = {}

    def add_item(self, code, price):
        self.items[code] = price

    def display_items(self):
        print("\nItem Code\tPrice")
        for code, price in self.items.items():
            print(f"{code}\t\t{price}")

    def generate_bill(self):
        quantities = {}
        print("\nEnter quantity of each item:")
        for code in self.items:
            qty = int(input(f"Enter quantity of {code} : "))
            quantities[code] = qty

        print("\n***********************Bill************************")
        print("ITEM\tPRICE\tQUANTITY\tSUBTOTAL")
        total = 0
        for code, price in self.items.items():
            subtotal = price * quantities[code]
            total += subtotal
            print(f"{code}\t{price}\t{quantities[code]}\t\t{subtotal}")

        print("***************************************************")
        print("Total= ", total)



store = Store()
n = int(input("Enter no of items: "))

for i in range(n):
    code = input("Enter code of item: ")
    price = int(input("Enter cost of item: "))
    store.add_item(code, price)

store.display_items()
store.generate_bill()
