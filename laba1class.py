class vauxHall: 
    def __init__(self, name, tPrice, seats, tSold):
        self.name = name
        self.tPrice = tPrice
        self.seats = seats
        self.tSold = tSold
    
    def Name(self):
        print("Name of the station is: " + self.name)
    
    def tLeft(self):
        print("Number of unsold tickets:", self.seats - self.tSold)
    
    def leftPrice(self):
        print("Price of unsold tickets:", (self.seats - self.tSold) * self.tPrice)

v1 = vauxHall(input(), 2.5, 89, 78)

v1.Name()
v1.tLeft()
v1.leftPrice()
