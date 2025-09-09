import pickle

class Character:
    def __init__(self, name):
        self.name = name
        self.tp = 0

    def add_tp(self, val):
        self.tp += val

    def __str__(self):
        return f"{self.name} (TP: {self.tp})"

class TechPointCounter:
    def __init__(self):
        self.sample_names = ['Chrono', 'Lucca', 'Marle', 'Robo', 'Frog', 'Ayla', 'Magus']
        self.sample = {name: Character(name) for name in self.sample_names}
        self.character = [None, None, None]

    def change_characters(self):
        for i in range(len(self.character)):
            print(', '.join([f"[{j+1}] {name}" for j, name in enumerate(self.sample_names)]))
            player = input(f'Who is in the party at position {i+1}? ')
            if player == '':
                self.character[i] = None
            else:
                self.character[i] = self.sample[self.sample_names[int(player) - 1]]
        self.show_character()

    def show_character(self):
        print([str(c) if c else 'None' for c in self.character])

    def add_tp(self, val):
        for char in self.character:
            if char is not None:
                char.add_tp(val)

    def save_data(self):
        with open('tech_point_data.pkl', 'wb') as f:
            pickle.dump((self.sample, self.character), f)
        print("Data saved successfully.")

    def load_data(self):
        try:
            with open('tech_point_data.pkl', 'rb') as f:
                self.sample, self.character = pickle.load(f)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found. Starting with default values.")

if __name__ == "__main__":
    tester = TechPointCounter()
    tester.load_data()
    run = True
    while run == True:
        print("\n1. Change Characters\n2. Show Characters\n3. Add TP\n4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            tester.change_characters()
        elif choice == '2':
            tester.show_character()
        elif choice == '3':
            tp_val = int(input("Enter TP value to add: "))
            tester.add_tp(tp_val)
        elif choice == '4':
            tester.save_data()
            run = False
        else:
            print("Invalid choice. Please try again.")
