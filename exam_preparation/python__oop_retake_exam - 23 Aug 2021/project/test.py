from project.astronaut import astronaut_repository
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist


# result = astronaut_repository.add()
# print(astronaut_repository.add(astro2))
from project.space_station import SpaceStation

station1 = SpaceStation()
print(station1.add_astronaut('Geodesist', 'name1'))
print(station1.add_planet('Neptun', 'item1, item2, item3'))
print(station1.add_planet('Neptun', 'item1, item2, item3'))
print(station1.add_astronaut('Biologist', 'name4'))
print(station1.add_astronaut('Meteorologist', 'name3'))
print(station1.add_astronaut('Geodesist', 'name5'))
print(station1.retire_astronaut('name1'))
print(station1.add_planet('Mars', 'item4, item5, item6'))
print(station1.add_astronaut('Geodesist', 'name2'))
print(station1.recharge_oxygen())
print(station1.add_astronaut('Biologist', 'name4'))
print(station1.add_astronaut('Meteorologist', 'name3'))
print(station1.send_on_mission('Neptun'))
print(station1.send_on_mission('Mars'))
print(station1.report())

# astro1 = Geodesist('astro1')
# astro2 = Biologist('astro2')
# print(station1.add_astronaut('Geodesist', 'astro1'))
# print(station1.new_astro_repository)
# print(station1.add_astronaut('Geodesist', 'astro1'))
# print(station1.add_planet('planet1', 'item1, item2, item3'))
# print(station1.new_planet_repository)


