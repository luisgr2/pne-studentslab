class Seq:   # Template to create objects to it be an instance of that class. Inside we define all the methods
    """A class for representing sequences"""
    def __init__(self, strbases):       # __init__method : Actions that the objects perform.
        # Method called every time a new object is created with a special parameter.
        self.strbases = strbases        # Adding data: attribute strbases
        print("New sequence created!")  # It's not good practice to print here but let's make an exception!

    def __str__(self):  # Method called when the object is being printed.
        return self.strbases  # We just return the string with the sequence

    def len(self):  # Calculate length of the sequence
        return len(self.strbases)


# Main program
# Create an object of the class Seq
s1 = Seq("AGCCACGATCGTA")
s2 = Seq("ATCAGCAT")

# Printing objects
print(f"Sequence 1: {s1}")
print(f" Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f" Length: {s2.len()}")
print("Testing...")


class Gene(Seq):
    """This class is derived from the Seq Class"""
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self): # Print the Gene name along with the sequence
        return self.name + "-" + self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")

