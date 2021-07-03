import csv

# with open('testData.csv', 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         for column in row:
#             print(column)
#         print("         ")

# with open('testData.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[0].ljust(15), row[1].ljust(15), row[2])


with open('testData.csv') as file:
    data = csv.DictReader(file)
    for row in data:
        print(row['F_Name'].ljust(15), row['L_Name'].ljust(15), row['Email'])
