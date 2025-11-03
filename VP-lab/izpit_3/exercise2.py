class Shoes:
    def __init__(self, brand, price, color, size, quantity):
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size
        self.quantity = quantity
        
    def __repr__(self):
        return f"{self.brand}, {self.price}, {self.color}, {self.size}, {self.quantity}"
         
    def info(self):
        return f"{self.brand}, {self.price}, {self.color}, {self.size}, {self.quantity}"
    
    def Sale(self, quantity):
        return(f"Trqbva da se prodadat {quantity} obuvki")
    
    def Purchase(self, quantity):
        return(f"Trqbva da se zaredqt {quantity} obuvki")
    
    
def sort_price(list):
    return list.sort(key = lambda p: p.price , reverse = True)

def shoes_searching(shoes, brand, size):
    sum = 0
    for shoe in shoes:
        sum += shoe.price
    average = sum/len(shoes)
    list_of_shoes = [x for x in shoes if x.brand == brand and x.size == size and x.price <= average]
            
    return list_of_shoes

def cheapest_shoes(shoes, color):
    color_shoes = []
    for shoe in shoes:
        if shoe.color == color:
            color_shoes.append(shoe)      
    if color_shoes:
        color_shoes.sort(key=lambda x: x.price)
        print(color_shoes[0])
    else:
        print("color is not available")
        for shoe in shoes:
            print(shoe.color, end=", ")
        print()
        
def delete_shoe(shoes, brand):
    for shoe in shoes:
        if shoe.brand == brand:
            shoes.remove(shoe)
    
    
shoes1 = Shoes("Nike", 200, "Blue", 39, 300)
shoes2 = Shoes("Nike", 100, "Orange", 41, 100)
shoes3 = Shoes("Addidas", 290, "Purple", 41, 60)
shoes4 = Shoes("Nike", 280, "Black", 44, 70)
shoes5 = Shoes("Addidas", 500, "Red", 42, 100)
shoes6 = Shoes("Nike", 800, "Magenta", 40, 19)
shoes7 = Shoes("Addidas", 180, "White", 39, 20)

shoes_list = [shoes1, shoes2, shoes3, shoes4, shoes5, shoes6, shoes7]

print(sort_price(shoes_list))
print(shoes_list)
print(shoes_searching(shoes_list, "Addidas", 41))
cheapest_shoes(shoes_list, "Blue")
delete_shoe(shoes_list, "Addidas")
print(shoes_list)