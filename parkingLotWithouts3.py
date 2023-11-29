import json
import random
import string

class ParkingLot:
    def __init__(self, squareFootage, spotSize):
        """
        Initialize a ParkingLot object.
        """
        self.squareFootage = squareFootage
        self.spotSize = spotSize
        self.parkingLotSize = self.calculateParkingLotSize()
        self.parkingLot = [None] * self.parkingLotSize
        self.parkedCars = {}

    def calculateParkingLotSize(self):
        """
        Calculate the total number of parking spots in the parking lot.
        """
        spotArea = self.spotSize[0] * self.spotSize[1]
        return self.squareFootage // spotArea

    def parkCar(self, car, spot):
        """
        Park a car in the specified spot.
        """
        if self.parkingLot[spot] is None:
            self.parkingLot[spot] = car
            self.parkedCars[car.licensePlate] = spot
            return True
        else:
            return False

    def mapParkedCarsToSpots(self):
        """
        Map parked cars to their respective parking spots.
        """
        return {car: spot for car, spot in self.parkedCars.items()}

class Car:
    def __init__(self, licensePlate):
        """
        Initialize a Car object.
        """
        self.licensePlate = licensePlate

    def __str__(self):
        """
        Return a string representation of the Car object.
        """
        return f"Car with license plate {self.licensePlate}"

    def park(self, parkingLot):
        """
        Park the car randomly in an available spot in the parking lot.
        """
        spot = random.randint(0, len(parkingLot.parkingLot) - 1)
        while parkingLot.parkCar(self, spot) is False:
            spot = random.randint(0, len(parkingLot.parkingLot) - 1)

    def park2(self, parkingLot, spot):
        """
        Park the car in a specific spot in the parking lot.
        """
        if spot < 0 or spot >= len(parkingLot.parkingLot):
            return "Invalid spot number. Please choose a valid spot."
        if parkingLot.parkCar(self, spot):
            print(f"Car with license plate {self.licensePlate} parked successfully in spot {spot}.")
        else:
            print(f"Spot {spot} is occupied. Unable to park the car.")

def main():
    # Example with a parking lot of 2000ft2 and car array
    squareFootage = int(input("Enter the square footage size of the parking lot: "))
    
    parkingLot = ParkingLot(squareFootage, (8, 12))
    cars = [Car(''.join(random.choices(string.ascii_uppercase + string.digits, k=7))) for _ in range(15)]

    for car in cars:
        car.park(parkingLot)
        if parkingLot.parkedCars.get(car.licensePlate) is not None:
            print(f"{car} parked successfully in spot {parkingLot.parkedCars[car.licensePlate]}")
        else:
            print(f"{car} couldn't find a spot.")

    car1 = Car("ABC1234")
    car1.park2(parkingLot, 2)
    car2 = Car("ABC1254")
    car2.park2(parkingLot, 15)

    # Optional: Map and save parked cars to a JSON file
    parkingLotMap = parkingLot.mapParkedCarsToSpots()
    with open('parking_lot_map.json', 'w') as file:
        json.dump(parkingLotMap, file)

if __name__ == "__main__":
    main()
