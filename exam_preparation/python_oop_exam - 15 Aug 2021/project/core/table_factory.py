from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableFactory:
    @staticmethod
    def create_table(table_type, table_number, capacity):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        if table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)


