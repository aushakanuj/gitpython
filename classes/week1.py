class Cereal():

    def __init__(self,x,y,z):
        self.name=x
        self.brand=y
        self.fiber=z
    def __str__(self):
        return("{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber))


c1=Cereal("Corn Flakes","Kellogg's",2)
c2=Cereal("Honey Nut Cheerios","General Mills",3)

print(c1) 

