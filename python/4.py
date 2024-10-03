from datetime import datetime

# Base class Vehicle
class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    def rent_vehicle(self):
        self.is_available = False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, rental_days):
        return self.rental_price * rental_days

    def __str__(self):
        return f"{self.brand} {self.model} (ID: {self.vehicle_id}) - {'Available' if self.is_available else 'Rented'}"


# Car class, inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, doors):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.doors = doors

    def __str__(self):
        return f"Car: {super().__str__()}, Doors: {self.doors}"


# Bike class, inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, bike_type):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.bike_type = bike_type

    def __str__(self):
        return f"Bike: {super().__str__()}, Type: {self.bike_type}"


# Truck class, inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.capacity = capacity

    def __str__(self):
        return f"Truck: {super().__str__()}, Capacity: {self.capacity} tons"


# Customer class
class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented_vehicles = []
        self.rental_history = []

    def rent_vehicle(self, vehicle):
        if vehicle.is_available:
            vehicle.rent_vehicle()
            rental_record = {"vehicle": vehicle, "rented_at": datetime.now()}
            self.rented_vehicles.append(rental_record)
            print(f"{self.name} rented {vehicle}.")
        else:
            print(f"{vehicle} is not available.")

    def return_vehicle(self, vehicle):
        for record in self.rented_vehicles:
            if record['vehicle'] == vehicle:
                rental_duration = (datetime.now() - record['rented_at']).days + 1  # at least 1 day
                rental_cost = vehicle.calculate_rental_cost(rental_duration)
                self.rental_history.append({**record, "returned_at": datetime.now(), "cost": rental_cost})
                vehicle.return_vehicle()
                self.rented_vehicles.remove(record)
                print(f"{self.name} returned {vehicle}. Rental cost: ${rental_cost:.2f}")
                return rental_cost
        print(f"{self.name} did not rent {vehicle}.")

    def view_rental_history(self):
        return self.rental_history

    def __str__(self):
        return f"Customer: {self.name}, License: {self.license_number}"


# RentalService class to manage vehicles and rental process
class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added vehicle: {vehicle}")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Registered customer: {customer}")

    def view_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_available]
        if available_vehicles:
            for vehicle in available_vehicles:
                print(vehicle)
        else:
            print("No vehicles available.")

    def view_rented_vehicles(self):
        rented_vehicles = [vehicle for vehicle in self.vehicles if not vehicle.is_available]
        if rented_vehicles:
            for vehicle in rented_vehicles:
                print(vehicle)
        else:
            print("No rented vehicles.")

# Example usage
rental_service = RentalService()

# Add vehicles to the fleet
car1 = Car("C001", "Toyota", "Camry", 50, 4)
bike1 = Bike("B001", "Yamaha", "YZF-R3", 20, "Sports")
truck1 = Truck("T001", "Ford", "F-150", 100, 5)

rental_service.add_vehicle(car1)
rental_service.add_vehicle(bike1)
rental_service.add_vehicle(truck1)

# Register customers
customer1 = Customer("John Doe", "DL12345")
rental_service.register_customer(customer1)

# Customer rents a vehicle
customer1.rent_vehicle(car1)

# View available vehicles
print("\nAvailable vehicles after renting:")
rental_service.view_available_vehicles()

# Customer returns the vehicle
customer1.return_vehicle(car1)

# View available vehicles again
print("\nAvailable vehicles after returning:")
rental_service.view_available_vehicles()

# View rental history of the customer
print("\nRental history of customer:")
for record in customer1.view_rental_history():
    vehicle = record['vehicle']
    rented_at = record['rented']
