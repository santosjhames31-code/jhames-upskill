class Animal: 
    def __init__(self, name, type, voice):
        self.name = name
        self.type = type
        self.voice = voice 
    
    def sound(self):    #seld pertains to the created object(animal1)
        print(self.voice) 

    def introduce(self):
        print(f"Hello, I am {self.name}")

animal1 = Animal(voice="Arf", name="Jogras", type="Dog")
animal1.sound()
animal1.introduce()