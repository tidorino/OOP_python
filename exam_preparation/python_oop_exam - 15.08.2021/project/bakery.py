from project.core.food_factory import FoodFactory
from project.core.drink_factory import DrinkFactory
from project.core.table_factory import TableFactory
from project.core.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, 'Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f'{food_type} {name} is already in the menu!')
        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f'{drink_type} {name} is already in the menu!')
        drink = self.drink_factory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f'Table {table_number} is already in the bakery!')
        table = self.table_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people):
        table = self.__find_free_table(number_of_people)
        if table is None:
            return f'No available table for {number_of_people} people'
        table.reserve(number_of_people)
        return f'Table {table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number: int, *foods: []):
        table = self.find_table_by_number(table_number)
        if not table:
            return f'Could not find table {table_number}'

        food_not_in_menu = []
        for food_name in foods:
            food = self.find_food_by_name(food_name)
            if not food:
                food_not_in_menu.append(food_name)
            else:
                table.order_food(food)

        result = f'Table {table_number} ordered:\n'
        for food in table.food_orders:
            result += repr(food) + '\n'
        result.strip()
        result += f'{self.name} does not have in the menu:\n'
        for food_name in food_not_in_menu:
            result += food_name + '\n'
        return result.strip()

    def order_drink(self, table_number: int, *drink_names: []):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f'Could not find table {table_number}'

        ordered_drinks = f'Table {table_number} ordered:\n'
        skipped_order_drinks = f'{self.name} does not have in the menu:\n'

        for drink_name in drink_names:
            drink = self.find_drink_by_name(drink_name)
            if drink is None:
                skipped_order_drinks += drink_name + '\n'
            else:
                table.order_drink(drink)
                ordered_drinks += str(drink) + '\n'

        return ordered_drinks + skipped_order_drinks.strip()

    def leave_table(self, table_number):
        table = self.find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f'Table: {table_number}\nBill: {bill:.2f}'

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return None

    def __find_free_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                return table
        return None


