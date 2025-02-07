
class CarSelector: # this is creating a python class ith the name CarSelecotr
    def __init__(self): #This is initiating the class with the agruemtns self
        self.cars = { # this is a my list called cars encapsulated by self 
            "Honda Fit": { # this is the dic key
                "MPG": "30 city / 36 highway", 
                "Price": "$16,190",
                "Drivetrain": "Front-Wheel Drive",
                "Brakes": "Disc Brakes (Front), Drum Brakes (Rear)"
            },
            "Toyota Corolla": { #dic key
                "MPG": "31 city / 40 highway",
                "Price": "$20,425",
                "Drivetrain": "Front-Wheel Drive",
                "Brakes": "Disc Brakes (Front & Rear)"
            },
            "Ford Mustang": { # dic key
                "MPG": "21 city / 30 highway",
                "Price": "$27,155",
                "Drivetrain": "Rear-Wheel Drive",
                "Brakes": "Disc Brakes (Front & Rear)"
            },
                "Subaru BRZ": { #dic key
                "MPG": "20 city / 27 highway",
                "Price": "$40,240",
                "Drivetrain": "All-Wheel Drive",
                "Brakes": "Regenerative Braking + Disc Brakes"
            }
        }
    
    def show_cars(self): #makes a function shower_cars with a agruemnt self
        print("Available Cars:") # print to screen the words 
        for index, car in enumerate(self.cars.keys(), start=1): #this for lopps loops car 1 by one giving it a enumeration self.cars.keys runs the keys 
            print(f"{index}. {car}") # print the numberd car list 
    
    def select_car(self, car_name): #A function to select a car agruemnt self and car_name 
        car_info = self.cars.get(car_name) 
        if car_info:
            print(f"\nCar Selected: {car_name}")
            for key, value in car_info.items():
                print(f"{key}: {value}")
        else:
            print("Car not found. Please select a valid car.")

if __name__ == "__main__":
    selector = CarSelector()
    selector.show_cars()
    car_name = input("\nEnter the name of the car you want to select: ").lower
    selector.select_car(car_name)


tasks = ["Task ", "Task ", "Task "]

for index, tasks in enumerate(tasks, start=1):
    print(f"{index}, {tasks}")
