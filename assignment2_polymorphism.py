"""
Assignment 2: Polymorphism Challenge! 
This demonstrates polymorphism with different classes implementing the same method differently.
"""

from abc import ABC, abstractmethod

# Abstract base class for vehicles
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    @abstractmethod
    def move(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    def stop(self):
        """Common method for all vehicles"""
        return f"{self.name} comes to a stop."

class Car(Vehicle):
    """Car class with driving movement"""
    
    def __init__(self, name, speed, fuel_type="gasoline"):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        return f"{self.name} is driving on the road at {self.speed} mph! "
    
    def honk(self):
        return f"{self.name} honks: BEEP BEEP!"

class Plane(Vehicle):
    """Plane class with flying movement"""
    
    def __init__(self, name, speed, altitude=30000):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):
        return f"{self.name} is flying through the sky at {self.speed} mph at {self.altitude} feet! ✈"
    
    def takeoff(self):
        return f"{self.name} takes off and climbs to {self.altitude} feet!"

class Boat(Vehicle):
    """Boat class with sailing movement"""
    
    def __init__(self, name, speed, boat_type="sailboat"):
        super().__init__(name, speed)
        self.boat_type = boat_type
    
    def move(self):
        return f"{self.name} is sailing across the water at {self.speed} knots!"
    
    def anchor(self):
        return f"{self.name} drops anchor and stays in place."

class Bicycle(Vehicle):
    """Bicycle class with pedaling movement"""
    
    def __init__(self, name, speed, gear_count=21):
        super().__init__(name, speed)
        self.gear_count = gear_count
    
    def move(self):
        return f"{self.name} is pedaling along the path at {self.speed} mph! "
    
    def ring_bell(self):
        return f"{self.name} rings the bell: RING RING! "

# Animal polymorphism example
class Animal(ABC):
    """Abstract base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    @abstractmethod
    def move(self):
        """Abstract method for animal movement"""
        pass
    
    @abstractmethod
    def make_sound(self):
        """Abstract method for animal sounds"""
        pass

class Dog(Animal):
    """Dog class with running movement"""
    
    def move(self):
        return f"{self.name} the {self.species} is running and wagging its tail! "
    
    def make_sound(self):
        return f"{self.name} barks: WOOF WOOF! "

class Bird(Animal):
    """Bird class with flying movement"""
    
    def move(self):
        return f"{self.name} the {self.species} is soaring through the air! "
    
    def make_sound(self):
        return f"{self.name} chirps: TWEET TWEET! "

class Fish(Animal):
    """Fish class with swimming movement"""
    
    def move(self):
        return f"{self.name} the {self.species} is swimming gracefully underwater! "
    
    def make_sound(self):
        return f"{self.name} makes bubbles: *blub blub* 🫧"

class Snake(Animal):
    """Snake class with slithering movement"""
    
    def move(self):
        return f"{self.name} the {self.species} is slithering across the ground! "
    
    def make_sound(self):
        return f"{self.name} hisses: HISSSS! "

# Demonstration functions
def demonstrate_vehicle_polymorphism():
    print("=== VEHICLE POLYMORPHISM DEMO ===\n")
    
    # Create different vehicles
    vehicles = [
        Car("Tesla Model 3", 120, "electric"),
        Plane("Boeing 747", 550, 35000),
        Boat("Ocean Explorer", 25, "yacht"),
        Bicycle("Mountain Bike", 15, 18)
    ]
    
    # Demonstrate polymorphism - same method, different behavior
    for vehicle in vehicles:
        print(f"--- {vehicle.name} ---")
        print(vehicle.move())  # Same method call, different implementations!
        print(vehicle.stop())
        
        # Demonstrate unique methods
        if isinstance(vehicle, Car):
            print(vehicle.honk())
        elif isinstance(vehicle, Plane):
            print(vehicle.takeoff())
        elif isinstance(vehicle, Boat):
            print(vehicle.anchor())
        elif isinstance(vehicle, Bicycle):
            print(vehicle.ring_bell())
        print()

def demonstrate_animal_polymorphism():
    print("=== ANIMAL POLYMORPHISM DEMO ===\n")
    
    # Create different animals
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Bird("Tweety", "Canary"),
        Fish("Nemo", "Clownfish"),
        Snake("Slither", "Python")
    ]
    
    # Demonstrate polymorphism
    for animal in animals:
        print(f"--- {animal.name} the {animal.species} ---")
        print(animal.move())      # Same method, different behavior!
        print(animal.make_sound()) # Same method, different behavior!
        print()

def demonstrate_polymorphism_in_action():
    """Show how polymorphism works with mixed collections"""
    print("=== POLYMORPHISM IN ACTION ===\n")
    
    # Mixed collection of vehicles
    transportation = [
        Car("Sports Car", 180),
        Plane("Fighter Jet", 1200),
        Bicycle("Racing Bike", 25)
    ]
    
    print("Starting a race with different vehicles:")
    for i, vehicle in enumerate(transportation, 1):
        print(f"{i}. {vehicle.move()}")
    
    print("\nAll vehicles stopping:")
    for vehicle in transportation:
        print(f"   {vehicle.stop()}")

# Main demonstration
def demonstrate_assignment2():
    print("=== ASSIGNMENT 2: POLYMORPHISM CHALLENGE ===\n")
    
    demonstrate_vehicle_polymorphism()
    demonstrate_animal_polymorphism()
    demonstrate_polymorphism_in_action()

if __name__ == "__main__":
    demonstrate_assignment2()
