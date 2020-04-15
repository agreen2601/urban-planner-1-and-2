import datetime

date = datetime.datetime.now().strftime("%D")

class Building:
    def __init__(self, name, address, stories):
        self.designer = "Chicken Monkey"
        self.date_constructed = ""
        self.owner = ""
        self.name = name
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = date

    def purchase(self, person):
        self.owner = person
