#Filter even numbers.
number = [7,5,89,36,21,45,10,20,24,26,82]
even_number = list(filter(lambda x : x % 2 == 0, number))
print("even_number:", even_number)
