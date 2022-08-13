from project.software.software import Software


class LightSoftware(Software):
    SOFTWARE_TYPE = 'Light'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE, capacity_consumption, memory_consumption)
        self.capacity_consumption = int(capacity_consumption + capacity_consumption / 2)
        self.memory_consumption = int(memory_consumption - memory_consumption / 2)

    # @property
    # def capacity_consumption(self):
    #     return self.__capacity_consumption
    #
    # @capacity_consumption.setter
    # def capacity_consumption(self, value):
    #     value += value / 2
    #     self.__capacity_consumption = round(value)

    # @property
    # def memory_consumption(self):
    #     return self.__memory_consumption
    #
    # @memory_consumption.setter
    # def memory_consumption(self, value):
    #     value -= value / 2
    #     self.__memory_consumption = math.floor(value)
