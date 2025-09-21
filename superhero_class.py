"""
Assignment 1: Design Your Own Class - Superhero Edition! 🦸‍♂️
This demonstrates classes, constructors, inheritance, and encapsulation.
"""

class Superhero:
    """Base Superhero class with common attributes and methods"""
    
    def __init__(self, name, real_name, power_level=50):
        self.name = name
        self.real_name = real_name
        self._power_level = power_level  # Protected attribute (encapsulation)
        self._energy = 100
        self.is_active = True
    
    def introduce(self):
        """Method to introduce the superhero"""
        return f"I am {self.name}! My real identity is {self.real_name}."
    
    def use_power(self):
        """Generic power usage method"""
        if self._energy >= 20:
            self._energy -= 20
            return f"{self.name} uses their power! Energy remaining: {self._energy}"
        else:
            return f"{self.name} is too tired to use their power!"
    
    def rest(self):
        """Method to restore energy"""
        self._energy = min(100, self._energy + 30)
        return f"{self.name} rests and recovers energy. Current energy: {self._energy}"
    
    def get_power_level(self):
        """Getter method for encapsulated power level"""
        return self._power_level
    
    def set_power_level(self, new_level):
        """Setter method with validation"""
        if 0 <= new_level <= 100:
            self._power_level = new_level
        else:
            print("Power level must be between 0 and 100!")

class FlyingHero(Superhero):
    """Inherited class for flying superheroes"""
    
    def __init__(self, name, real_name, power_level=50, flight_speed=100):
        super().__init__(name, real_name, power_level)
        self.flight_speed = flight_speed
        self.is_flying = False
    
    def fly(self):
        """Specific method for flying heroes"""
        if self._energy >= 15:
            self._energy -= 15
            self.is_flying = True
            return f"{self.name} soars through the sky at {self.flight_speed} mph! ✈️"
        else:
            return f"{self.name} is too tired to fly!"
    
    def land(self):
        """Method to land"""
        self.is_flying = False
        return f"{self.name} lands gracefully on the ground."
    
    def use_power(self):
        """Override parent method with flying-specific power"""
        if self._energy >= 20:
            self._energy -= 20
            return f"{self.name} unleashes aerial attacks from above! Energy: {self._energy}"
        else:
            return f"{self.name} is too tired to use aerial powers!"

class TechHero(Superhero):
    """Inherited class for technology-based superheroes"""
    
    def __init__(self, name, real_name, power_level=50, gadget_count=5):
        super().__init__(name, real_name, power_level)
        self.gadget_count = gadget_count
        self.gadgets = []
    
    def add_gadget(self, gadget_name):
        """Method to add new gadgets"""
        if len(self.gadgets) < self.gadget_count:
            self.gadgets.append(gadget_name)
            return f"{self.name} adds {gadget_name} to their arsenal!"
        else:
            return f"{self.name}'s gadget belt is full!"
    
    def use_power(self):
        """Override parent method with tech-specific power"""
        if self._energy >= 20 and self.gadgets:
            self._energy -= 20
            gadget = self.gadgets[0]  # Use first gadget
            return f"{self.name} deploys {gadget}! Energy: {self._energy} 🔧"
        elif not self.gadgets:
            return f"{self.name} has no gadgets to use!"
        else:
            return f"{self.name} is too tired to use gadgets!"

# Demonstration of Assignment 1
def demonstrate_assignment1():
    print("=== ASSIGNMENT 1: SUPERHERO CLASS SYSTEM ===\n")
    
    # Create different types of superheroes
    superman = FlyingHero("Superman", "Clark Kent", 95, 500)
    batman = TechHero("Batman", "Bruce Wayne", 80, 10)
    wonder_woman = Superhero("Wonder Woman", "Diana Prince", 90)
    
    # Add gadgets to Batman
    batman.add_gadget("Batarang")
    batman.add_gadget("Grappling Hook")
    batman.add_gadget("Smoke Bomb")
    
    heroes = [superman, batman, wonder_woman]
    
    # Demonstrate each hero
    for hero in heroes:
        print(f"--- {hero.name} ---")
        print(hero.introduce())
        print(f"Power Level: {hero.get_power_level()}")
        print(hero.use_power())
        
        # Demonstrate specific abilities
        if isinstance(hero, FlyingHero):
            print(hero.fly())
            print(hero.land())
        elif isinstance(hero, TechHero):
            print(f"Gadgets: {', '.join(hero.gadgets)}")
        
        print(hero.rest())
        print()

if __name__ == "__main__":
    demonstrate_assignment1()
