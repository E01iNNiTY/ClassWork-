PRICE_LIST = {
    ("Toyota", "Camry"): 25000,
    ("Honda", "Civic Type R"): 37000,
    ("BMW", "M3 Competition"): 70000
}

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.wheels = 4
        self.price = PRICE_LIST.get((brand, model), 0)

    def print_car(self):
        print(f"I am a {self.brand} {self.model}")
        print(f"I have {self.wheels} wheels")
        print(f"My price is ${self.price:,}")

def main():
    camry = Car("Toyota", "Camry")
    honda = Car("Honda", "Civic Type R")
    bmw = Car("BMW", "M3 Competition")

    camry.print_car()
    honda.print_car()
    bmw.print_car()

if __name__ == "__main__":
    main()