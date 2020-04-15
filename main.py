from building import Building
from city import City

westin = Building("Westin", "807 Clark Place", 26)
jw = Building("JW", "201 8th Ave S", 28)
hilton = Building("Hilton", "121 4th Ave S", 18)
sheraton = Building("Sheraton", "623 Union St", 33)
union_station = Building("Union Station", "1001 Broadway", 9)

westin.purchase("Mama Bear")
jw.purchase("Papa Bear")
hilton.purchase("Sister Bear")
sheraton.purchase("Brother Bear")
union_station.purchase("Honey Bear")

westin.construct()
jw.construct()
hilton.construct()
sheraton.construct()
union_station.construct()

megalopolis = City("Megalopolis", "Kitty Baby", 2012)

megalopolis.add_building(westin)
megalopolis.add_building(jw)
megalopolis.add_building(hilton)
megalopolis.add_building(sheraton)
megalopolis.add_building(union_station)

print(f'{megalopolis.mayor} is the mayor of the wonderful city of {megalopolis.name}, which was founded in {megalopolis.year}. The following lavish building are located in {megalopolis.name}:')
print()
print()

for building in megalopolis.buildings:
    print(f'The {building.name} is located at {building.address}. It was designed by {building.designer} and construction began on {building.date_constructed}. It is currently owned by {building.owner} and has {building.stories} stories.')
    print()