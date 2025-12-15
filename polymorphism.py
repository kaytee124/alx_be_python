class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

class Bird(Animal):
  def make_sound(self):
    print("Sqwak")

buddy = Bird()
buddy.make_sound()

