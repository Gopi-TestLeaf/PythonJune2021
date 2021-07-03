# with open('text1.txt', mode='r') as file:
#     data = file.read()
#     for i in data:
#         if(ord(i) >= 48 and ord(i) <= 57):
#             print(i)
#


# input     A1B2C3
# output    B2C3D4

for i in 'A1B2C3':
    print(chr(ord(i) + 1), end="")