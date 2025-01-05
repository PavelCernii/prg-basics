class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print('Receipt: ')
        print(f'Distance: {self.distance}km')
        print(f'Rate: €{self.rate_per_km}per km')
        print(f'Fare: €{self.fare}')

def main():
    ride1 = TaxiRide(rate_per_km=2)
    ride1.calculate_fare(distance=10)
    print('First ride: ')
    ride1.print_receipt()

    ride2 = TaxiRide(rate_per_km=3)
    ride2.calculate_fare(distance=20)
    print('Secont ride: ')
    ride2.print_receipt()

if __name__ == "__main__":
    main()