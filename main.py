from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal = Animal("Generic", "Unkown")
    
    # TODO: Print the Animal instance
    print(animal)
    
    # TODO: Call the method to make a generic animal sound
    animal.speak()

    # TODO: Create an instance of the Dog class
    brown_dog = Dog("Fred","Canine","Golden Retriver")
    
    # TODO: Print the Dog instance
    print(brown_dog)
    
    # TODO: Call the method to make the dog-specific sound
    brown_dog.speak()

    # TODO print out all the animals
    print("All Animals:")
    for a in Animal.all_animals:
        print(a)