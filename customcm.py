class Hello:
    def __enter__(self):
        print("start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")

with Hello():
    print("working")

#database
class Database:

    def __enter__(self):
        print("Connected")

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):
        print("Disconnected")

with Database():
    print("Executing Query")