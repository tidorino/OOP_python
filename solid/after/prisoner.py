from copy import copy


class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {(tuple(i for i in prisoner.PRISON_LOCATION))}")
print(f"The current position of the prisoner: {(tuple(i for i in prisoner.position))}")