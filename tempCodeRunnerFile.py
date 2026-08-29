import json
data = {
    "name": "Soniya",
    "age": 20,
    "isTeacher": True
}
with open("data.json","w") as f:
    json.dump(data, f,indent=4,sort_keys=True)