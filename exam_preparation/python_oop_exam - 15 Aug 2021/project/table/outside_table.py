from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 51 or value > 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value

    # @property
    # def min_table_number(self):
    #     return 51
    #
    # @property
    # def max_table_number(self):
    #     return 100
    #
    # @property
    # def table_number_error_message(self):
    #     return "Outside table's number must be between 51 and 100 inclusive!"