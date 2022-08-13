from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 1 or value > 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value

    # @property
    # def min_table_number(self):
    #     return 1
    #
    # @property
    # def max_table_number(self):
    #     return 50
    #
    # @property
    # def table_number_error_message(self):
    #     return "Inside table's number must be between 1 and 50 inclusive!"