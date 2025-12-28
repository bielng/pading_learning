class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on. ')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on. ')
    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off. ')
        else:
            print(f'Microwave ({self.brand}) is already turned off. ')  

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        
        else:
            print(f'A mystical force whispers: "Turn on your microwave first...."')
        


smeg: Microwave = Microwave(brand="Smeg", power_rating="B")
smeg.turn_on()
# smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(50)

# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)


bosch: Microwave = Microwave(brand="Bosch", power_rating="A")
bosch.turn_on()
# bosch.turn_on()
bosch.run(50)
bosch.turn_off()
bosch.run(100)


pading: Microwave = Microwave(brand="Pading", power_rating="A")
pading.turn_on()
# pading.turn_on()
pading.run(37)
pading.turn_off()
pading.run(23)
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)