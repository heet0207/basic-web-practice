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
        elif self.size=='Large':
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
            size=(input('Enter the size of pizza'))
            t=int(input('Enter No. of topping'))
            for i in range(t):
                toppings.append(input('Enter topping:'))
            c=int(input('Enter no of cheese:'))
            for i in range(c):
                cheese.append(input('Enter cheese names'))
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
order1.order(2)
order1.bill()