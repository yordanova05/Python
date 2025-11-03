class Car:
    def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.brand = car_brand
        self.model = car_model
        self.price = car_price
        self.color = car_color
        self.year = manifacture_year
        
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Color: {self.color}, Year: {self.year}")
        
def sort_price(cars):
    cars.sort(key = lambda x: x.price, reverse=True)
    for car in cars:
        car.display_info()
            
def list_by_brand(mark, cars):
    for car in cars:
        if car.brand == mark:
            car.display_info()
                
def search_color(color, cars):
    price = 0
    for car in cars:
        if color == car.color:
            if price < car.price:
                price = car.price
                car_max = car
    car_max.display_info()
        
def newest_car(cars):
    list1=[]
    for car in cars:
        if car.year == 2022:
            list1.append(car)
    return list1


car1 = Car("audi", "q7", 23000, "metallic", 2016)
car2 = Car("bmw", "m7", 30000, "black", 2017)
car3 = Car("porshe", "911 gt3", 500000, "pink", 2022)
car4 = Car("ferrari", "turbo", 400000, "red", 2022)
car5 = Car("toyota", "supra", 43000, "black", 2007)
car6 = Car("toyota", "rav-4", 13000, "black", 2015)
car7 = Car("honda", "civic", 7000, "white", 2005)
cars = [car1,car2, car3, car4, car5, car6, car7]

list_by_brand("audi", cars)
print("----------")

search_color("black", cars)
print("----------")
result_list = newest_car(cars)
print("")
for car in result_list:
    car.display_info()
print("-------")
sort_price(cars)