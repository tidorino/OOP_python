from project.baked_food.cake import Cake
from project.baked_food.bread import Bread


class FoodFactory:

    def create_food(self, food_type: str, name: str, price: float):
        if food_type == 'Cake':
            return Cake(name, price)
        if food_type == 'Bread':
            return Bread(name, price)
