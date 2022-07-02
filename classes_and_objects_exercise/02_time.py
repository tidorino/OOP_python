class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, h, min, s):
        self.hours = h
        self.minutes = min
        self.seconds = s

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        check_time = self.check_max_time()
        new_time = self.get_time()
        return new_time

    def check_max_time(self):
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.hours, self.minutes, self.seconds


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
