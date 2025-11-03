class ClothesShop:
    def __init__(self, id, type, brand, price, quantity):
        self.id = id
        self.type = type
        self.brand = brand
        self.price = price
        self.quantity = quantity
        
    def clothes_info(self):
        return (f"ID: {self.id}, type:{self.type}, brand: {self.brand},\
 price:{self.price}$, quantity:{self.quantity}")
        
    def change_price(self):
        new_price = float(input("New price: "))
        self.price = new_price
        
    def change_qty(self):
        new_quantity = int(input("New quantity: "))
        self.quantity = new_quantity
        
        
def search_by_id(clothes_list, id):
    for cloth in clothes_list:
        if cloth.id == id:
            return cloth.clothes_info()
        
def search_by_brand(clothes_list, brand):
    matches = [x.clothes_info() for x in clothes_list if x.brand == brand]
    # for cloth in clothes_list:
    #     if cloth.brand == brand:
    #         matches.append(cloth.clothes_info())
    return matches

def clothe_by_id(clothes_list, id, num):
    for cloth in clothes_list:
        if cloth.id == id:
            if cloth.quantity >= num:
                cloth.quantity -= num
                return ("Успешна продажба!")
            
            else:
                return ("Недостатъчна наличност!")
    print("Не е открит такъв продукт!")

dress = ClothesShop(121224, "dress", "Guess", 2500, 5)
boots = ClothesShop(1256, "shoes", "Nike", 340, 25)
hat = ClothesShop(31, "Hat", "Nike", 35, 100)
clothes_list = [dress, boots, hat]

print(search_by_id(clothes_list, 31))
print()
print(search_by_brand(clothes_list, "Nike"))
print()
print(clothe_by_id(clothes_list, 121224, 5))
print(dress.clothes_info())
dress.change_price()
print(dress.clothes_info())
dress.change_qty()
print(dress.clothes_info())
