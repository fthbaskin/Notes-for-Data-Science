# Fundamental Operations

## Custom Decorators

### Function Decorators
Function decorators are commonly used for adding repeating tasks that needs to be executed when the function is called. Most common use case of this is logging and application paths.

#### Basic Decorator
You can define a basic decorator by having a wrapper around it as shown in the example. You pass parameters into the function by wrapper `*args` and `**kwargs`.
```Python
def function_decorator1(func):
    # You pass the parameters of the function to the wrapper function by using *args and **kwargs
    def wrapper(*args, **kwargs):
        # Do whatever you want to do before the function is called or after, logging is a common use case.
        print(f"Function {func.__name__} is called.")
        return func(*args, **kwargs)
    return wrapper

@function_decorator1
def function1(arg1: str, arg2: int) -> None:
    print(f"Function1 is called, {arg1}, {arg2}")

function1("Deneme", 123)
# Output: Function function1 is called.
#         Function1 is called, Deneme, 123
```

#### Decorators that Take Parameters
Decorator functions themselves can take parameters. When a function is __defined__ (not called), code in the outer decorator is executed. You can pass the same parameter in the inner decorator which executes when the function is __called__.
```Python
def function_decorator2(param1):
    # If you put a code here, it will be executed when decorated function is called.
    print(f"Decorator parameter: {param1}")
    # You can pass parameters to the decorator by using a function that returns the inner decorator
    def inner_decorator(func):
        # You pass the parameters of the function to the wrapper function by using *args and **kwargs
        def wrapper(*args, **kwargs):
            # Do whatever you want to do before the function is called or after with decorator parameter, logging is a common use case.
            print(f"Function {func.__name__} is called. Decorator parameter: {param1}")
            return func(*args, **kwargs)
        return wrapper
    # If you put a code here, it will be executed when decorated function is called.
    return inner_decorator

@function_decorator2("Apple")
def function2(arg1: str, arg2: int) -> None:
    print(f"Function2 is called, {arg1}, {arg2}")
# Output: Decorator parameter: Apple

function2("Deneme", 123)
# Output: Function function2 is called. Decorator parameter: Apple
#         Function2 is called, Deneme, 123
```

#### Decorator Call Order
Decorators on the top wraps the decorator on the bottom. Therefore ordering of the decorators matter.
```Python
def function_decorator3(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called inside function_decorator3.")
        return func(*args, **kwargs)
    return wrapper

def function_decorator4(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called inside function_decorator4.")
        return func(*args, **kwargs)
    return wrapper

@function_decorator3
@function_decorator4
def function3(arg1: str, arg2: int) -> None:
    print(f"Function3 is called, {arg1}, {arg2}")

function3("Deneme", 123)
# Output: Function wrapper is called inside function_decorator3.
#         Function function3 is called inside function_decorator4.
#         Function3 is called, Deneme, 123

@function_decorator4
@function_decorator3
def function4(arg1: str, arg2: int) -> None:
    print(f"Function4 is called, {arg1}, {arg2}")

function4("Deneme", 123)
# Output: Function wrapper is called inside function_decorator4.
#         Function function4 is called inside function_decorator3.
#         Function4 is called, Deneme, 123
```

## Dataclass Operations

### Defining Dataclasses
It is quite easy to define dataclasses, you only need to define members. Dataclasses will define initializers automatically.
```Python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    position: str
    salary: float

# It is possible to initialize a dataclass very easily.
john1 = Employee('John', 30, 'Developer', 1000.0)
print(john1)
# Output: Employee(name='John', age=30, position='Developer, salary=1000.0)
```

### Serializing Dataclasses into Dictionaries
There are two methods to get a dataclass object into a dictionary format. Normally objects have `__dict__` protperty, which shows every attribute of that object in a dictionary, but `asdict()` is specificly designed for dataclasses. For simple operations, `__dict__` is fine but it can show attributes that is not a part of the dataclass definition.
```Python
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
```

#### Differances Between `asdict()` and `__dict__`
According to ChatGPT:
| Feature                                 | `__dict__`                                      | `asdict()`                                  |
|-----------------------------------------|-------------------------------------------------|---------------------------------------------|
| **Scope**                               | Works for any object                            | Designed specifically for dataclasses       |
| **Handles nested dataclasses**          | No                                              | Yes                                         |
| **Ignores private/internal attributes** | No                                              | Yes                                         |
| **Recursion**                           | No (shallow)                                    | Yes (deep)                                  |
| **Custom dataclass fields**             | Includes everything (including non-init fields) | Only includes public fields by default      |

### Deserializing Dictionaries
It is possible to deserialize dictionaries into specific dataclasses. But, dictionary must contain all of the fields in the dataclass. In the initialization, parameters are passed by using `**kwargs` method.
```Python
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    position: str
    salary: float

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
```

## JSON Operations
`json` is a commonly used data representation format in which there are key-value pairs (dictionarites) and arrays. It is easy to turn objects into `json` format therefore it is quite popular among web-development with using languages like `python` and `javascript`.

### JSON Dumps
`json dumps` is used to store a dictionary into a `json` file. It is possible to serialize objects into dictionaries by defining corresponding methods or by using dataclasses.
```Python
import json

# You can store a dictionary as a json file
example_dict = {1: "1", 2: "2", 3: "3"}
json_text = json.dumps(example_dict)
with open("example.json", "w", encoding='utf-8') as f:
    f.write(json_text)
```

### JSON Loads
`json loads` is used to create a dictionary from a `json` file. It is possible to deserialize dictionaries into objects by defining corresponding methods or using dataclasses.
```Python
import json

# You can load a json file or text as a dictionary
json_text_example = '{"1": 1, "2": 2, "3": 3}'
json_dict_example = json.loads(json_text_example)
for key, value in json_dict_example.items():
    print(key, value)
```