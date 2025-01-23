class Vehicle:
   
   # Base class for all vehicles.
   
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
   
    # Car class implementing the move method.
   
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
  
   # Plane class implementing the move method.
   
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
  
  #  Boat class implementing the move method.
    
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
   
   # Bicycle class implementing the move method.
  
    def move(self):
        print("Pedaling 🚴")

# Example usage
vehicles = [Car(), Plane(), Boat(), Bicycle()]
for vehicle in vehicles:
    vehicle.move()
