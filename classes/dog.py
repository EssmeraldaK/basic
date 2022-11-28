class Dog():
    """
    Model of dogs, template for dogs.
    """
    # attribute (description) - variables, instance variables
    name = 'a'
    breed = ''
    size = ''
    age = ''
    color = ''

    # behaviour (actions) - functions
    def eat(self):
        print(f'{self.name} is eating ....')
        print(f'{self.name} wants more...')
        print(f'{self.name} done eating.')

    def run(self):
        print(f'{self.name} is running')

    def get_description(self):
        print(f"Breed of the dog: {self.breed}")

# instantiation - creating instance of the class - creating object
dog1 = Dog()
print('name of the dog before: ',dog1.name)
dog1.name = 'trex'  # assigning the value to the attributes
print('name of the dog, after assigning new name: ',dog1.name)
dog1.eat()