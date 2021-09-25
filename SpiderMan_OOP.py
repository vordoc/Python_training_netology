class Character:
    def __init__(self, name, power, energy=50, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print('Moving on 2 squares')

class Spider:
    def __init__(self, power=20, energy=30, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

    def move(self):
        self.webshoot()
        print('Moving on 1 squares')

class SpiderMan(Character, Spider):
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        self.backpack = []

    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot()     # !!! super вызывает метод webshoot от родителя, т.е. класса Spider
        else:
            print('No web!')

    def move(self):
        self.webshoot()
        print('Moving on 3 squares')

peter_parker = SpiderMan('Peter Parker', 80)
print(peter_parker.name)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.webshoot()
print('\n')

# print(SpiderMan.mro()) просмотр линеаризации наследования класса SpiderMan

peter_parker.turn_spider_sense()
print(peter_parker.energy)
print(peter_parker.power)
print('\n')
spider = Spider()

spider.move()
peter_parker.move()
print('')
print(peter_parker.backpack)
print('')

peter_parker.backpack.append('web')
peter_parker.webshoot()