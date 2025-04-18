class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy: {self.energy}")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played around! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        print(f"{self.name}'s tricks: {', '.join(self.tricks) if self.tricks else 'None yet!'}")

    def get_mood(self):
        if self.happiness >= 8 and self.energy >= 7 and self.hunger <= 3:
            return "😊 Happy"
        elif self.happiness >= 5:
            return "😐 Okay"
        elif self.happiness < 3 or self.energy < 3:
            return "😢 Sad"
        else:
            return "😠 Grumpy"

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}")
        print(f"  Energy: {self.energy}")
        print(f"  Happiness: {self.happiness}")
        print(f"  Mood: {self.get_mood()}")
