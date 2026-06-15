import csv

with open("record.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(
        [
            ["Name", "Age"],
            ["Yuvraj", 19],
            ["Rahul", 20],
        ]
    )

with open("record.csv","r")as file :
    reader = csv.reader(file)
    for row in reader:
        print(row)


