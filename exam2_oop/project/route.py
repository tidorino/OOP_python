class Route:
    ERROR_MSG_START_POINT = 'Start point cannot be empty!'
    ERROR_MSG_END_POINT = 'End point cannot be empty!'
    ERROR_MSG_LENGTH = 'Length cannot be less than 1.00 kilometer!'

    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_START_POINT)
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_MSG_END_POINT)
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 1.00:
            raise ValueError(self.ERROR_MSG_LENGTH)
        self.__length = value
