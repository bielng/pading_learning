class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on. ')

    


smeg: Microwave = Microwave(brand="Smeg", power_rating="B")
# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)


# bosch: Microwave = Microwave(brand="Bosch", power_rating="A")
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)