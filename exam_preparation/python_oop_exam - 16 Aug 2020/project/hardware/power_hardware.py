from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    HARDWARE_TYPE = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.HARDWARE_TYPE, capacity, memory)
        self.capacity = int(capacity - capacity * 0.75)
        self.memory = int(memory + memory * 0.75)


    # @property
    # def capacity(self):
    #     return self.__capacity
    #
    # @capacity.setter
    # def capacity(self, value):
    #     # Its capacity is 25% of the given value
    #     value = value - (value * 0.75)
    #     self.__capacity = math.floor(value)
    #
    # @property
    # def memory(self):
    #     return self.__memory
    #
    # @memory.setter
    # def memory(self, value):
    #     # It has 75% more memory than the given value
    #     value = value + (value * 0.75)
    #     self.__memory = math.floor(value)
