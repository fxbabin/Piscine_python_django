#! /usr/bin/python3

class HotBeverages():
    price = 0.30
    name = "hot beverage"

    def description(self):
        return ("Just some hot water in a cup.")
    
    def __str__(self):
        return ("name : {}\n"
                "price : {:.2f}\n"
                "description : {}"
                .format(self.name, self.price, self.description()))

class Coffee(HotBeverages):
    name = "coffee"
    price = 0.40
    
    def description(self):
        return ("A coffee, to stay awake.")

class Tea(HotBeverages):
    name = "tea"

class Chocolate(HotBeverages):
    name = "chocolate"
    price = 0.50
    
    def description(self):
        return ("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverages):
    name = "cappuccino"
    price = 0.45
    
    def description(self):
        return ("Un po' di Italia nella sua tazza!")


def main():
    beverage = HotBeverages()
    #print("Hot beverage :\n"
    #      "{}".format(beverage))
    print(beverage)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    chocolate = Chocolate()
    print(chocolate)
    cappuccino = Cappuccino()
    print(cappuccino)

if __name__ == '__main__':
    main()