#! /usr/bin/python3

import random
from beverages import HotBeverages, Coffee, Cappuccino, Tea, Chocolate

class CoffeeMachine():
    
    def __init__(self):
        self.obsolescence = 0

    class EmptyCup(HotBeverages):
        name = "empty cup"
        price = 0.90

        def description(self):
            return ("An empty cup?! Gimme my money back!")
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.obsolescence = 0

    def serve(self, hotBeverage):
        self.obsolescence += 1
        if self.obsolescence >= 10:
            raise self.BrokenMachineException()
        choice = random.uniform(0, 1)
        if round(choice) == 0:
            return (hotBeverage())
        else:
            return (self.EmptyCup)


def main():
    coffeemachine = CoffeeMachine()
    for _ in range (10):
        try:
            print(coffeemachine.serve(Chocolate).name, coffeemachine.obsolescence)
            print(coffeemachine.serve(Tea).name, coffeemachine.obsolescence)
            print(coffeemachine.serve(Cappuccino).name, coffeemachine.obsolescence)
            print(coffeemachine.serve(Coffee).name, coffeemachine.obsolescence)
        except Exception as e:
            print(e)
            coffeemachine.repair()

if __name__ == '__main__':
    main()