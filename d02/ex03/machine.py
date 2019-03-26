#! /usr/bin/python3

from beverages import HotBeverages, Chocolate

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

    def serve(self, Chocolate):
        #random
        # inst or emptycup
        self.obsolescence += 1
        if self.obsolescence > 10:
            raise self.BrokenMachineException()
        if (self.obsolescence % 2) == 0:
            return (Chocolate())
        else:
            return (self.EmptyCup)


def main():
    coffeemachine = CoffeeMachine()
    i = 0
    while i < 20:
        try:
            coffeemachine.serve(Chocolate)
            print(coffeemachine.obsolescence)
        except Exception as e:
            print(e)
        i += 1


if __name__ == '__main__':
    main()