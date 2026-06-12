from models import MenuItem, Customer, Order, Payment

item = MenuItem(name="Spicy Burger", price=9.99, category="Burgers", popularity_rating=4.5)

print(item.name)
print(item.price)
print(item.category)
print(item.popularity_rating)

customer = Customer(name="Alex")
print(customer.name)
print(customer.purchase_history)

order = Order(datetime="2026-06-12 12:30")
drink = MenuItem(name="Large Soda", price=2.49, category="Drinks", popularity_rating=3.8)
order.add_item(item, quantity=2)
order.add_item(drink, quantity=1)
print(order.datetime)
print(order.items)
print(order.total())

order.remove_item(drink)
print(order.items)
print(order.total())

payment = Payment(order=order, method="credit card", amount=order.total(), success=True)
print(payment.get_receipt())