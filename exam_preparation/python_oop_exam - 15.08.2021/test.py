from project.bakery import Bakery

bakery = Bakery('Random name')
print(bakery.add_food('Cake', 'Carrot', 3.4))
print(bakery.add_food('Bread', 'Banana', 4))
print(bakery.add_food('Cake', 'Chocolate', 2.4))
print(bakery.add_drink('Water', 'Spring', 250, 'Gorna Banya'))
print(bakery.add_drink('Water', 'Natural', 500, 'Bankya'))
print(bakery.add_drink('Tea', 'Cold', 250, 'Nestle'))

print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.reserve_table(10))
print(bakery.reserve_table(5))
print(bakery.add_table('InsideTable', 15, 15))
print(bakery.reserve_table(10))
print(bakery.order_food(55, 'Banana', 'Carrot', 'Chocolate', 'Rise Pudding', 'Pancake'))
print(bakery.order_drink(15, 'Spring', 'Natural', 'Cold', 'Coke', 'Hot Milk'))
print(bakery.leave_table(55))
print(bakery.add_table('InsideTable', 12, 5))
print(bakery.get_free_tables_info())

print('-------')

print(bakery.get_total_income())


