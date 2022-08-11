from project.astronaut import astronaut_repository
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist


# result = astronaut_repository.add()
# print(astronaut_repository.add(astro2))
from project.space_station import SpaceStation

station1 = SpaceStation()
astro1 = Geodesist('astro1')
astro2 = Biologist('astro2')
print(station1.add_astronaut('Geodesist', 'astro1'))
print(station1.new_astro_repository)
print(station1.add_astronaut('Geodesist', 'astro1'))
print(station1.add_planet('planet1', 'item1, item2, item3'))
print(station1.new_planet_repository)


