import csv

with open('testData.csv', 'w', newline="") as file:
    wt = csv.writer(file)
    header = ['F_Name', 'L_Name', 'Email']
    wt.writerow(header)

    data = [
        ['Gopi', 'Jayakumar', 'gopi@gmail.com'],
        ['Sarath', 'M', 'sarath@gmail.com'],
        ['Balaji', 'M', 'balaji@gmail.com']
    ]
    wt.writerows(data)



