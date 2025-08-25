# Basic Syntax in Python
a = 2
print(a)
print(2)
print("2")

# Data Types
a: str = "2"
print(type(a))
b: int = 2
print(type(b))
c: float = 2.5
print(type(c))
d: bool = True
print(type(d))

# Variables
a = 1
print(a)
# Math operation
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
# Basic conditional 
print(a | b)
print(a & b)
# Condtitional sentece
name = "Ahn Yujin"
age = 24
country = "South Korea"
if (name == name.lower()) or (age == 24) or (country == country.lower()):
  print("You're Ahn Yujin!")
else:
  print("You're not Ahn Yujin")

# Basic Program implementation one for all While and For Loop
Name = ["SeoYeon", "HyeRin", "JiWoo", "ChaeYeon", "YooYeon", "SooMin", "NaKyoung", "YuBin", "Kaede", "DaHyun", "Kotone", "YeonJi", "Nien", "SoHyun", "Xinyu", "Mayu", "Sion", "Lynn", "Jieun", "ChaeWon", "Sullin", "SeoA", "JiYeon", "HaYeon"]

for idx, name in enumerate(Name):
  print(f"{idx}. AnnyeongHaseyo {name}!")

# Dictionary
TripleS_Members = {
  "Name": Name,
  "Age": [],
  "Country": []
}
for i in range(1, 24):
  TripleS_Members['Age'].append(i)
  TripleS_Members['Country'].append('South Korea')

# Function Classes and Object
def add_members(name, number):
  TripleS_Members['Name'].append((name, number))

add_members('Karina', 'S25')
print(TripleS_Members["Name"])

# for i in TripleS_Members["Name"]:
  # print(f"This is {TripleS_Members["Name"][i]}")

# Classes and Objects
class Members: # This is class
  def __init__(self, name, age, country):
    self.name = name
    self.age = age
    self.country = country
  def birth_date(self):
    return 2025 - self.age
# class Groups(Members):
member1 = Members('Ahn Yujin', 25, 'South Korea')
print(member1.name)
print(member1.age)
print(member1.country)
print(member1.birth_date())