class Bird:
    def fly(self):
        print("The bird is flying.")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly.")