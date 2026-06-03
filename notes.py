note = input("Enter note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Saved")