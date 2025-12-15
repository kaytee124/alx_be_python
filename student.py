class student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def change_name(self, new_name):
        self.name = new_name

s1 = student("Alice", 20)
s1.display()

s2 = student("Bob", 22)
s2.display()

s2.change_name("Charlie")
s2.display()