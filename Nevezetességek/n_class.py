class Nevezetességek:
    
    def __init__(self,country,name,city,year):
        self.country = country
        self.name = name
        self.city = city
        self.year = int(year)

    def rekordok(self):
        txt = self.country + ": " + self.name + " - " + self.city + " - " + str(self.year)

        return txt
