class Pet:
    def __init__(self, name, species, age, available=True):
        self.name = name
        self.species = species
        self.age = age
        self.available = available

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} years old) - {'Available' if self.available else 'Not Available'}"


class PetAdoptionSystem:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def list_available_pets(self):
        available_pets = [pet for pet in self.pets if pet.available]
        if available_pets:
            for pet in available_pets:
                print(pet)
        else:
            print("No available pets at the moment.")

    def adopt_pet(self, name):
        for pet in self.pets:
            if pet.name == name and pet.available:
                pet.available = False
                print(f"Congratulations! You adopted {pet.name}.")
                return
        print(f"Sorry, {name} is not available for adoption or does not exist in our system.")

    def menu(self):
        while True:
            print("\nPet Adoption System Menu:")
            print("1. List available pets")
            print("2. Adopt a pet")
            print("3. Exit")
            choice = input("Please enter your choice (1/2/3): ")
            
            if choice == "1":
                self.list_available_pets()
            elif choice == "2":
                name = input("Enter the name of the pet you want to adopt: ")
                self.adopt_pet(name)
            elif choice == "3":
                print("Thank you for using the Pet Adoption System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    system = PetAdoptionSystem()

    # Sample pets
    system.add_pet(Pet("Buddy", "Dog", 3))
    system.add_pet(Pet("Whiskers", "Cat", 2))
    system.add_pet(Pet("Rocky", "Dog", 4))

    # Run the pet adoption system
    system.menu()
