import json

# Loads: convert json datatype to Python
pData = json.loads('{"name" : "GN", "active" : false, "Value" : null}')
print(pData)

# Load
with open('p_to_j.json', 'r') as file:
    data = json.load(file)
    pData = json.loads(data)
    print(pData)