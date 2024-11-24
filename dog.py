class Dog():
    """
    Derived class representing a dog, which is a type of Animal.
    """
    all_dogs = []
    
    # TODO: Initialize the Dog class and add the breed attribute.
    def __init__(self, name, species, breed):
            self.breed = breed
            self.name = name
            self.species = species
            Dog.all_dogs.append(self)
            
    # The constructor should accept name, species, and breed as parameters.
    # TODO: Override the __str__ method to include the breed.
    def __str__(self):
        return (f"name:'{self.name}'. species:'{self.species}' breed: '{self.breed}'")
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.
    @classmethod
    def get_all_dogs(speak):
        speak = 'bark'
        return Dog.all_dogs
    
    