class Car:
    def __init__(self,name,brand,price) -> None:
        self.name=name
        self.brand=brand
        self.price=price
    def drive(self):
        return "Manual"

car_1 = Car("X6","BMW",10000000)
car_2 = Car("R8","AUDI",20000000)

print(car_1.brand)
print(car_1.drive())