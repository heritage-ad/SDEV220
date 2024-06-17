#Author: Heritage Adigun
#Date: 06.17.2024
#File Name: Automobile Description
#Short Desc: This app accept user input for car, year, make, model, doors, and type of roof and store the data in class attributes.

#super class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#second class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#get year, make, model, doors, and roof from user and validate if neccesary
def get_car_details():
    vehicle_type = "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    while True:
        roof = input("Enter the type of roof (solid or sun roof): ")
        if roof in ["solid", "sun roof"]:
            break
        else:
            print("Invalid input. Please enter 'solid' or 'sun roof'.")


#Create an object of vehicle type
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    return car

#print details
def display_car_details(car):
    print("\nVehicle details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

#Run the main function
if __name__ == "__main__":
    car = get_car_details()
    display_car_details(car)
