from project.software.software import Software


class ExpressSoftware(Software):
    SOFTWARE_TYPE = 'Express'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE, capacity_consumption, memory_consumption)
        self.memory_consumption = memory_consumption * 2

    # @property
    # def memory_consumption(self):
    #     return self.__memory_consumption
    #
    # @memory_consumption.setter
    # def memory_consumption(self, value):
    #     value = value * 2
    #     self.__memory_consumption = value
