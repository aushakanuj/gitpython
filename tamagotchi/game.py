class pet ():
    
    bt=10
    ht=6
    def __init__(self,name ="kitty"):
        self.name=name
        self.hunger=randrange(self.ht)
        self.boredom=randrange(self.bt)
        