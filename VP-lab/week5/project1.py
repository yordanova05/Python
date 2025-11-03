orders = []
unique_orders = set()

while True:
    order_number = input("Въведете номер на поръчка (или 'exit' за край): ")
    if order_number.lower() == 'exit':
        break
    customer_name = input("Въведете име на клиента: ")
    order_details = input("Въведете какво е поръчал клиентът: ")

    order = f"{order_number}: {customer_name}: {order_details}"
    orders.append(order)
    unique_orders.add(order_details)
    print(f"Поръчка добавена: {order}")

    print(f"Брой уникални поръчки: {len(unique_orders)}")

    # Проверка дали искаме да видим клиентите за конкретна поръчка
    if input("Искате ли да видите клиентите за конкретна поръчка? (да/не): ").lower() == 'да':
        specific_order = input("Въведете името на поръчката: ")
        customers_for_order = sorted([o.split(": ")[1] for o in orders if specific_order in o])
        
        if customers_for_order:
            print("Клиенти, направили поръчката:")
            for customer in customers_for_order:
                print(customer)
        else:
            print("Няма клиенти, направили тази поръчка.")

print("\nСписък с поръчки:")
for order in orders:
    print(order)





# book = []
# book_order = []
# count= 0
# d={}
# while True:
#     command = input("Command: ").lower()
#     if command == "add":
#         name = input("Name: ")
#         order = input("Order: ")
#         if order == 
#         count +=1
#         orders = (f"{name} : {order}")
#         book.append(orders)
#     elif command == "exit":
#         break
#     else: print("Error!")
# for i in range(count):
#     string = (f"{i+1} : {book[i]}")
#     book_order.append(string)
# print(book_order)


