def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()


def authenticate(func):
    def wrapper():
        print("Checking Credentials...")
        func()

    return wrapper


@authenticate
def login():
    print("Welcome User")


login()

