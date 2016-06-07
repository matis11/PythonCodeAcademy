# Code Academy 3: Wszystko jest obiektem
# 			  put.NET junior
# ______________________________________
# 				   2016
# ______________________________________

class Robot:
    __secretMission = "KILL_ALL_HUMANS"
	
    name = ""
    hp = 100
    ep = 100
    targets = []

	# Konstruktor, uruchamiany przy tworzeniu obiektu klasy Robot
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print("Hello, I'm " + self.name)

    def addEnemy(self, enemy):
        self.targets.append(enemy)

    def attack(self, enemy):
        if enemy in self.targets:
            print("Attacking " + enemy)
        else:
            print("Sorry, cannot do")

class Atlas(Robot):
	# Nadpisanie konstruktora klasy Robot
    def sayHello(self):
        print("Hi there!")


# Tworzenie obiektu player1
player1 = Atlas(name = "Atlas")
player1.sayHello()

# __secretMission jest polem ukrytym, nie mozna uzyskac dostepu
#print(Atlas.__secretMision)
