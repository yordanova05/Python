from datetime import datetime

class Medicine:
    def __init__(self, med_name, manufacturer, price, quantity, exp_date):
        self.name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
        self.exp_date = datetime.strptime(exp_date, "%m.%Y")
        
    def __str__(self):
        return (f"{self.name}, {self.manufacturer}, {self.price}, {self.quantity}, {self.exp_date}")
    
    def __repr__(self):
        return (f"{self.name}, {self.manufacturer}, {self.price}, {self.quantity}, {self.exp_date}")
        
    def price_recalculation(self, date):
        p_date = datetime.strptime(date, "%m.%Y")
        months_difference = (self.exp_date.year - p_date.year)*12 + (self.exp_date.month - p_date.month)
        
        if months_difference == 0:
            self.price = self.price/2
        
        elif months_difference <= 6:
            self.price = self.price - self.price*12/100
            
        elif 6 < months_difference <= 12:
            self.price = self.price - self.price*8/100
            
def sort_med(medicines):
    medicines.sort(key = lambda x: x.name, reverse = True)
    print(medicines)
    
def max_quantity_manufacturer(medicines, manufacturer):
    matches = [x for x in medicines if x.manufacturer == manufacturer]
    result = 0
    if matches:
        # matches.sort(key= lambda x: x.quantity, reverse= True)
        # return matches[0]
        for x in matches:
            if x.quantity > result:
                result = x.quantity
        
        for x in matches:
            if x.quantity == result:
                print(x) 
    else:
        print("Not found!!")
        
        for x in medicines:
            print(x.manufacturer, end= ", ")
        print()
        
def delete_by_name(medicines, date):
    date_1 = datetime.strptime(date, "%m.%Y")
    for m in medicines:
        
        if date_1.year == m.exp_date.year:
            if date_1.month >= m.exp_date.month:
                medicines.remove(m)
                
        elif date_1.year > m.exp_date.year:
            medicines.remove(m)
            
def search_by_price_quantity(medicines, price, quantity):
    print([x for x in medicines if x.price < price and x.quantity > quantity])
    

n = int(input("Брой медикаменти:"))
medicines = []

for _ in range(n):
    name = input("Name: ")
    manufacturer = input("Manufacturer: ")
    price  = float(input("Price: "))
    quantity = int(input("Quantity: "))
    date = input("(mm.gggg): ")
    
    product = Medicine(name, manufacturer, price, quantity, date)
    medicines.append(product)
    
for m in medicines:
    m.price_recalculation("12.2024")
    print(m)
    
sort_med(medicines)
max_quantity_manufacturer(medicines, manufacturer="метро")
delete_by_name(medicines,"8.2025")
print(medicines)
search_by_price_quantity(medicines, 40, 5)
    
    
        
      
# 3
# ддз
# метро
# 60
# 60
# 12.2024
# ввв
# метро
# 30
# 6
# 8.2025
# ххх
# деkатлон
# 50
# 60
# 9.2025
        
        