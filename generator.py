def numbers():

    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

def squares():

    for i in range(1, 6):
        yield i * i

for value in squares():
    print(value)



def dataset():

    for i in range(100):
        yield i
for value in dataset():
    print(value)


def countdown(start):
    while start > 0:
        yield start
        start -= 1


for value in countdown(5):
    print(value)


def tickets():
    yield "Ticket-1"
    yield "Ticket-2"
    yield "Ticket-3"


for ticket in tickets():
    print(ticket)

