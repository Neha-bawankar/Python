class Bird:
    def make_sound(self):
        return "Some generic bird sound"

class Sparrow(Bird):
    def make_sound(self):
        return "Chirp chirp"

class Parrot(Bird):
    def make_sound(self):
        return "Squawk"

class Duck(Bird):
    def make_sound(self):
        return "Quack quack"

def describe_bird(bird):
    print(f"This bird says: {bird.make_sound()}")

if __name__ == "__main__":
    # Creating instances of different bird types
    sparrow = Sparrow()
    parrot = Parrot()
    duck = Duck()

    # Demonstrating polymorphism
    describe_bird(sparrow)
    describe_bird(parrot)
    describe_bird(duck)
    describe_bird(Bird())  # Using the base class