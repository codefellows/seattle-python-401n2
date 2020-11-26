class Animal:
    def __str__(self):
        return "I am animal"


class Duck(Animal):
    def __init__(self, name, category="normal"):
        print("I am alive")
        self.name = name
        self.category = category

    def __str__(self):
        return f"quack from {self.name}"

    def __repr__(self):
        return "repr quack"

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category


if __name__ == "__main__":
    daisy = Duck("daisy")
    daisy_clone = Duck("daisy", category="other")

    print("ducks are equal", daisy == daisy_clone)
