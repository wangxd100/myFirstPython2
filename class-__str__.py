

#####
# It provides human readable version of output
# rather "Object": Example:
#####
class Pet():
    # class attributes
    pet_address = "627 ..."
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def Norm(self):
        return "%s is a %s" % (self.name, self.species)

if __name__=='__main__':
    a = Pet("jax", "human")
    print(a)
    # print Class Attributes - Static Attributes
    print(Pet.pet_address)

#####
# It provides human readable version of output
# rather "Object": Example:
# __str__
#####
class Pet():

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

if __name__=='__main__':
    a = Pet("jax", "human")
    print(a)