# file_obj = open('text1.txt', mode='w')
# file_obj.write("Hello all")
# file_obj.close()

# Way 01:
file_obj = open('text2.txt', mode='w')
for i in range(1, 11):
    file_obj.write(f"Hello all, its id list: {i} \n")
print(file_obj.closed)
file_obj.close()
print(file_obj.closed)


# Way 02:
with open('text3.txt', mode='w') as file:
    for i in range(1, 11):
        file.write(f"Hello all, its id list: {i} \n")


with open('text4.txt', 'w') as f_obj:
    for i in range(1, 21):
        f_obj.write(f'5 * {i} = {5 * i} \n')