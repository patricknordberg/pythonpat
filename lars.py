import time


def loading():
    load_time = "."
    while True:
        if load_time == "....":
            load_time = "."
            break
        else:
            print(".", end="")
            load_time += "."
            time.sleep(1)
        print("")




print(f"Initializing specs"), (loading())




class Ratt:
    rattutslag = 0

class Interior:
    def __init__(self, seat: str, color: str, material: str):
        self.seat = seat
        print(f"The number of seats is {seat}")

        self.color = color
        print(f"The color of the seats are {color}")

        self.material = material
        print(f"The material of the seats is {material}")

class Performance:
    def __init__(self, horsepower: int, engine_type: str, top_speed: int, acceleration: float):
        self.horsepower = horsepower
        print(f"The horsepower is {horsepower}")

        self.engine_type = engine_type
        print(f"The type of engine is {engine_type}")

        self.top_speed = top_speed
        print(f"The top speed is {top_speed} km/h")

        self.acceleration = acceleration
        print(f"The time from 0-100 is {acceleration} seconds")

class Motor:
    turned_on = False

    def engine_on(self):
        if self.turned_on:
            print(f"Engine is already on...")
            print(f"You can begin to drive...")
        else:
            self.turned_on = True
            print("Engine is turning on.", loading())
            time.sleep(1)
            print(f"Engine is now on")
            time.sleep(1)
            print(f"You can begin to drive")

    def engine_off(self):
        if self.turned_on:
            self.turned_on = False
            print("Engine is turning off."), (loading())

            time.sleep(1)
            print(f"Engine is now off")
        else:
            print(f"The engine is already off...")

class Bil:
    ratt = Ratt()
    motor = Motor()


    def __init__(self, brand: str, color: str, performance: Performance, interior: Interior):
        self.brand = brand
        print(f"The brand is {brand}")
        self.color = color
        self.performance = performance
        self.interior = interior
        self.turned_on: bool = False


    def turn_right(self):
        self.ratt.rattutslag = 1
        print(f"You are now turning right")

    def turn_left(self):
        self.ratt.rattutslag = -1
        print(f"You are now turning left")

    def turn_forward(self):
        self.ratt.rattutslag = 0
        print(f"You are now facing forward")

    def turn_park(self):
        self.ratt.rattutslag = 2
        print(f"You are now parked")

    def drive_car(self):
        self.turn_forward()
        time.sleep(1.5)
        self.turn_right()
        time.sleep(1.5)
        self.turn_left()
        time.sleep(1.5)
        self.turn_park()
        time.sleep(1.5)
        print("")
        self.motor.engine_off()

    def aktivitet(self):
        turn_on_engine = input("Would you like to turn the engine on?: ")
        if turn_on_engine == "Yes":
            self.motor.turned_on = True
        print("")
        self.motor.engine_on()
        time.sleep(1.5)
        print("")
        self.drive_car()


#Här skapar du dina bilar
bilar_lista = []
bilar = {}
bmw = Bil("BMW","blue",
          Performance(374, "M440i", 285, 4.3),
          Interior("4-seater", "black", "alcantara"))
bilar_lista.append(bmw.brand)
bilar[bmw.brand] = bmw
bil1 = bilar["BMW"]

print("")
print("...")
time.sleep(1.5)
print("")

volvo = Bil("Volvo", "white",
            Performance(256, "T5", 250, 7.5),
            Interior("5-seater", "black", "leather"))
bilar_lista.append(volvo.brand)
bilar[volvo.brand] = volvo
bil2 = bilar["Volvo"]

print("")
print("...")
time.sleep(1.5)
print("")
#Här kör du din bil


def chosen_car(car: Bil):
    car.aktivitet()


print(f"Available cars: {bilar.keys()}")
choose_car = input("Which car would you like to drive?: ")

print("")
for car in bilar:
    if car == choose_car:
        print(f"The {choose_car} has now been chosen")
        print("Entering"), (loading())
        chosen_car(bilar[car])



time.sleep(1)
print("Thank you for driving!")

