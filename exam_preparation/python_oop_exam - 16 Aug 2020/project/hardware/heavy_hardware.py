from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    HARDWARE_TYPE = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.HARDWARE_TYPE, capacity, memory)
        self.capacity = capacity * 2
        self.memory = int(memory - memory * 0.25)

    # @property
    # def capacity(self):
    #     return self.__capacity
    #
    # @capacity.setter
    # def capacity(self, value):
    #     value = value * 2
    #     self.__capacity = value
    #
    # @property
    # def memory(self):
    #     return self.__memory

    # @memory.setter
    # def memory(self, value):
    #     # Its memory is 75% from the given value
    #     value = value - (value * 0.25)
    #     self.__memory = math.floor(value)
