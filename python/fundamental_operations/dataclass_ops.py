from dataclasses import dataclass, asdict


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Employee(Person):
    position: str
    salary: float


# It is possible to convert a dataclass object to a dictionary using the asdict() or __dict__
john1 = Employee('John', 30, 'Developer', 1000.0)
print(john1)
# Output: Employee(name='John', age=30, position='Developer, salary=1000.0)
print(john1.__dict__)
# Output: {'name': 'John', 'age': 30, 'position': 'Developer, 'salary'=1000.0}
print(asdict(john1))
# Output: {'name': 'John', 'age': 30, 'position': 'Developer', 'salary': 1000.0}

# It is possible to convert a dictionary to a dataclass object using the kwargs unpacking
person_dict = {'name': 'John', 'age': 30}
john2 = Person(**person_dict)
print(asdict(john2))
# Output: {'name': 'John', 'age': 30}

# It requires all the fields to be present in the dictionary
try:
    john3 = Employee(**person_dict)
    print(asdict(john2))
except TypeError as e:
    print(e)
    # Output: Employee.__init__() missing 2 required positional arguments: 'position' and 'salary'
