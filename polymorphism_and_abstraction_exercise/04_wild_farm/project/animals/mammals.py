from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_incremental(self):
        return 0.10

    def make_sound(self):
        return f'Squeak'


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 0.4

    def make_sound(self):
        return f'Woof!'


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Meat']

    @property
    def weight_incremental(self):
        return 0.3

    def make_sound(self):
        return f'Meow'


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 1.00

    def make_sound(self):
        return f'ROAR!!!'
