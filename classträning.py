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

    def i_did_turn(self):
        if self.rattutslag == 0:
            print("You are now facing forward")
        elif self.rattutslag > 0:
            print(f"You are now turning right by {self.rattutslag}")
        else:
            print(f"You are now turning left by {-self.rattutslag}")


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
    speed = 0

    def status(self, action):
        if self.turned_on:
            print(f"Motor is turned on and I am {action}; speed is {self.speed}")
        else:
            print(f"Motor is off")

    def is_engine_on(self):
        return self.turned_on

    def engine_on(self):
        if self.turned_on:
            print(f"Engine is already on...")
            print(f"You can begin to drive...")
        else:
            self.turned_on = True
            print("Engine is turning on")
            loading()
            time.sleep(1)
            self.status("started")
            time.sleep(1)
            print(f"You can begin to drive")

    def engine_off(self):
        if self.turned_on:
            self.turned_on = False
            self.speed = 0
            self.status("stopped")
            time.sleep(1)
            print(f"Engine is now off")
        else:
            print(f"The engine is already off...")

    def gasa(self):
        if (self.turned_on):
            self.speed += 10
        self.status("accelerating")

    def bromsa(self):
        if (self.turned_on):
            self.speed -= 10
            self.status("breaking")
        elif self.speed == 0:
            self.status("stopped")


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

    def status(self):
        print("")

    def turn_right(self, degree):
        self.ratt.rattutslag = degree
        time.sleep(1.5)
        self.ratt.i_did_turn()
        self.turn_forward()

    def turn_left(self, degree):
        self.ratt.rattutslag = -degree
        time.sleep(1.5)
        self.ratt.i_did_turn()
        self.turn_forward()

    def turn_forward(self):
        self.ratt.rattutslag = 0
        time.sleep(1.5)
        self.ratt.i_did_turn()

    def drive_take_over(self):
        self.turn_left(10)
        self.motor.gasa()
        self.turn_right(10)
        self.motor.bromsa()
        print("I did take over")

    def drive_car(self):
        self.motor.gasa()
        self.turn_right(90)
        self.drive_take_over()
        self.turn_left(90)
        print("")
        self.motor.bromsa()

    def drive_to_city(self, city):
        if city == "Los Angeles":
            self.motor.gasa()
            self.turn_left(45)
            self.turn_forward()
            print("Driving for 2,5h")
            self.turn_right(45)
            print("You have now arrived in Los Angeles")
            self.motor.bromsa()

        elif city == "New York":
            self.motor.gasa()
            self.turn_right(45)
            print("Driving for 12h")
            self.turn_left(45)
            print("You have now arrived in New York")
            self.motor.bromsa()

        elif city == "Chicago":
            self.motor.gasa()
            self.turn_forward()
            print("Driving for 20 min")
            self.turn_left(90)
            print("You have now arrived in Chicago")
            self.motor.bromsa()






    def destination(self):
        cities = ["Los Angeles", "New York", "Chicago"]
        print(f"Destinations: {cities}")
        city = input("Destination: ")
        if city in cities:
            self.drive_to_city(city)





    def finished_driving(self):
        self.motor.engine_off()
        print("Thank you for driving!")

    def aktivitet(self):
        turn_on_engine = input("Would you like to turn the engine on?: ")
        if turn_on_engine:
            if self.motor.is_engine_on():
                print("Motor is already turned on")
            else:
                self.motor.engine_on()
                time.sleep(1.5)

            print("")
            self.drive_car()
            self.destination()

# Här skapar du dina bilar
bilar_lista = []
bilar = {}
bmw = Bil("BMW", "blue",
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
# Här kör du din bil


print(f"Available cars: {bilar_lista}")
choose_car = input("Which car would you like to drive?: ")
car = bilar[choose_car]
print("")

print(f"The {choose_car} has now been chosen")
print("Entering"), (loading())

car.aktivitet()

time.sleep(1)
car.finished_driving()
