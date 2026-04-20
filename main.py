1-misol
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Mening ismim {self.name}, yoshim {self.age}")


s1 = Student("Ali", 20)
s1.introduce()

# 2-misol
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(f"Bu {self.model}, rangi {self.color}")

c1 = Car("Cobalt", "oq")
c1.info()

# 3-misol
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_price(self):
        print(f"{self.brand} narxi {self.price}")


p1 = Phone("Iphone", "1200$")
p1.show_price()

# 4-misol
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def about(self):
        print(f"Kitob: {self.title}, Muallif: {self.author}")

b1 = Book("Python", "Aliyev")
b1.about()


# 5-misol
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print(f"User: {self.username}, Email: {self.email}")

u1 = User("admin", "admin@gmail.com")
u1.display()

# 6-misol
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def show_population(self):
        print(f"{self.name} aholisi {self.population}")

c1 = City("Toshkent", "3 mln")
c1.show_population()


# 7-misol
class Animal:
    def __init__(self, type, sound):
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"{self.type} {self}")


a1 = Animal("Mushuk", "miyovlaydi")
a1.make_sound()

# 8-misol
class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def info(self):
        print(f"Film: {self.title}, Janr: {self.genre}")

m1 = Movie("Avatar", "Fantasy")
m1.info()

# 9-misol
class Laptop:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_specs(self):
        print(f"{self.model} {self.ram} Ram")

l1 = Laptop("HP", "16GB")
l1.show_specs()

# 10-misol
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} {self.subject}")

t1 = Teacher("Ali", "matematika")
t1.teach()
