class Vet:
    animals = []
    space = 5

    def __init__(self,name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) >= Vet.space:
            return 'Not enough space'
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name):
        if animal_name in self.animals and animal_name in Vet.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f'{animal_name} unregistered successfully'

        return f'{animal_name} not in the clinic'

    def info(self):
        space_left = self.space_left()
        return f'{self.name} has {len(self.animals)} animals. {space_left} space left in clinic'

    def space_left(self):
        return Vet.space - len(Vet.animals)


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


