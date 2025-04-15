class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = True  # Default state is ON

    def __str__(self):  # User-friendly string representation
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

    def __repr__(self):  # Debugging and logging representation
        return f"Smartphone({self.brand}, {self.model}, {self.price})"

    def __eq__(self, other):  # Compare two objects for equality
        if isinstance(other, Smartphone):
            return self.brand == other.brand and self.model == other.model
        return False

    def __lt__(self, other):  # Compare two objects based on price
        if isinstance(other, Smartphone):
            return self.price < other.price
        return False

    def turn_on(self):  # Turn the smartphone ON
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):  # Turn the smartphone OFF
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

#objects
smartphone1 = Smartphone("Samsung", "Galaxy S21", 799)
smartphone2 = Smartphone("Apple", "iPhone 13", 999)
smartphone3 = Smartphone("Google", "Pixel 6", 599)
smartphone4 = Smartphone("OnePlus", "9 Pro", 969)


#usage
print(smartphone1)
smartphone1.turn_off()
smartphone1.turn_off()
smartphone1.turn_on()
smartphone1.turn_on()

#inheritance
class iphone(Smartphone):
    def __init__(self, brand, model, price, ios_version):
        super().__init__(brand, model, price)
        self.ios_version = ios_version

    def __str__(self):  # User-friendly string representation
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, iOS Version: {self.ios_version}"
    def __repr__(self):  # Debugging and logging representation
        return f"iphone({self.brand}, {self.model}, {self.price}, {self.ios_version})"
    def __eq__(self, other):  # Compare two objects for equality
        if isinstance(other, iphone):
            return self.brand == other.brand and self.model == other.model and self.ios_version == other.ios_version
        return False
    def __lt__(self, other):  # Compare two objects based on price
        if isinstance(other, iphone):
            return self.price < other.price
        return False
#objects
iphone1 = iphone("Apple", "iPhone 13", 999, "15.0")
iphone2 = iphone("Apple", "iPhone 12", 799, "14.0")
iphone3 = iphone("Apple", "iPhone 11", 699, "13.0")
iphone4 = iphone("Apple", "iPhone SE", 399, "12.0")

print(iphone1)
iphone1.turn_off()
iphone1.turn_off()

#activity 2
class vehicle:
    #constructor
    def __init__(self, name, model):
        self.name = name
        self.model = model

    #actions
    def move(self):
        print(f"{self.name} is moving")
    def stop(self):
        print(f"{self.name} has stopped")

#objects
vehicle1 = vehicle("Car", "Toyota")
vehicle2 = vehicle("Bike", "Honda")

#usage
vehicle1.move()
vehicle1.stop()
vehicle2.move()
vehicle2.stop()

#car
class car(vehicle):
    def move(self):
        print(f"{self.name} is driving")
    def stop(self):
        print(f"{self.name} has parked")
class plane(vehicle):
    def move(self):
        print(f"{self.name} is flying")
    def stop(self):
        print(f"{self.name} has landed")
#boat
class boat(vehicle):
    def move(self):
        print(f"{self.name} is sailing")
    def stop(self):
        print(f"{self.name} has docked")

#bike
class bike(vehicle):
    def move(self):
        print(f"{self.name} is pedaling")
    def stop(self):
        print(f"{self.name} has stopped pedaling")
#objects
car1 = car("Car", "Toyota")
car2 = car("Car", "Honda")
plane1 = plane("Plane", "Boeing")
plane2 = plane("Plane", "Airbus")
boat1 = boat("Boat", "Yamaha")
boat2 = boat("Boat", "Bayliner")
bike1 = bike("Bike", "Mountain")
bike2 = bike("Bike", "Road")
#usage
car1.move()
car1.stop()
car2.move()
car2.stop()
plane1.move()
plane1.stop()
plane2.move()
plane2.stop()
boat1.move()
boat1.stop()
boat2.move()
boat2.stop()
bike1.move()
bike1.stop()
bike2.move()
bike2.stop()