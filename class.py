class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def display_info(self):
        return f"Superhero: {self.name}, Power: {self.power}, Weakness: {self.weakness}"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} mph using {self.power}!"

# Example usage
hero1 = Superhero("Shadow", "Invisibility", "Bright Light")
hero2 = FlyingSuperhero("Skyhawk", "Wind Manipulation", "Storms", 500)

print(hero1.display_info())
print(hero1.use_power())
print(hero2.display_info())
print(hero2.use_power())