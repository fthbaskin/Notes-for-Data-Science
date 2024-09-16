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
