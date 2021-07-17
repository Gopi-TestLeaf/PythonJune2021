import os
#print(dir(os)) # returns all the attributes in the given module name
#
print(os.getcwd()) # its return current path
#
# os.chdir("D:/") # its chage working dir
#
# print(os.getcwd())
#
# os.chdir("C:\workspace\PythonWorkspace\Python_June")
#
# print(os.getcwd())
#
# print(os.listdir())
#
# os.mkdir("xyz")
#
# print(os.listdir())
#
# os.rmdir("aaa")
#
# print(os.listdir())
os.chdir(f'''C:\workspace\PythonWorkspace\Python_June\lnew''')

for x, y, z in os.walk('C:\workspace\PythonWorkspace\Python_June\lnew'):
    print(x)
    print(y)
    print(z)

print(__file__)
print(os.path.abspath(__file__))
app_root = os.path.dirname(os.path.abspath(__file__))
print(app_root)



