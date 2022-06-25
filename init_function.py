class customers:
    greeting = "Janzenn Cafeteria"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
customer_1 = customers("Janzenn", "Matcha", "Pasta",69)

print(customers.greeting)
print(customer_1.name)
print(customer_1.beverage)
