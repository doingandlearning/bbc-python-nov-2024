import csv

# try:
#     print("Creating a CSV file")
#     with open("sample.csv", "w") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["The Shawshank Redemption", 1994, "Drama"])
#         writer.writerow(["The Matrix", 1999, "Action, Sci-fi"])
#         writer.writerow(["Wall-e", 2012, "Sci-fi, Family"])
# except Exception as e:
#     print(e)

try:
    print("Reading from a CSV file")
    with open("sample.csv") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            print(row)
except Exception as e:
    print(e)

try:
    print("Reading from a CSV file")
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
except Exception as e:
    print(e)