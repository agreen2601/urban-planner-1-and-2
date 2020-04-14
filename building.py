import datetime

date = datetime.datetime.now().strftime("%D")

class Building:
    def __init__(self, address, stories):
        self.designer = "Andrew Green"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = date

    def purchase(self, person):
        self.owner = person

Westin = Building("807 Clark Place", 26)
JW = Building("201 8th Ave S", 28)
Hilton = Building("121 4th Ave S", 18)
Sheraton = Building("623 Union St", 33)
Union_Station = Building("1001 Broadway", 9)

Westin.purchase("Mama Bear")
JW.purchase("Papa Bear")
Hilton.purchase("Sister Bear")
Sheraton.purchase("Brother Bear")
Union_Station.purchase("Honey Bear")

Westin.construct()
JW.construct()
Hilton.construct()
Sheraton.construct()
Union_Station.construct()

print(f'{Westin.address} was purchased by {Westin.owner} on {Westin.date_constructed} and has {Westin.stories} stories')
print()
print(f'{JW.address} was purchased by {JW.owner} on {JW.date_constructed} and has {JW.stories} stories')
print()
print(f'{Hilton.address} was purchased by {Hilton.owner} on {Hilton.date_constructed} and has {Hilton.stories} stories')
print()
print(f'{Sheraton.address} was purchased by {Sheraton.owner} on {Sheraton.date_constructed} and has {Sheraton.stories} stories')
print()
print(f'{Union_Station.address} was purchased by {Union_Station.owner} on {Union_Station.date_constructed} and has {Union_Station.stories} stories')
