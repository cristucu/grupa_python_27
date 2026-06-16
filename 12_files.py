import json
from pathlib import Path

from pprint import pprint

f = open("input_file.json", "r", encoding="utf-8")
print(f)

# citim fisierul

content = f.read()
print(content)

print("Citim iar fisierul")

content2 = f.read()
print(content2)

f.close()


print("========Proper file reading: ======")

with open("input_file.json", "r", encoding="utf-8") as f:
    #altfel de citire
    lines = f.readlines()
    pprint(lines)
    #fclose() se face automat la finalul acestui "with"

print("=======Next Chapter: =======")

output_data = {
    "data": [50, 100, 300, "hello","gif"],
    "title": "My love story",
    "author": "Ms. Jackson",
    "extra_data":["I'm sorry", "Ms. Jackson"]
}

file_name = "output_file.json"

def write_data(file_name, data):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    # write data to file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        print("Data saved successfully!")


write_data(file_name, output_data)

with open(file_name, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)


def read_data(file_name):
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "r", encoding="utf-8") as f:
         data = json.load(f)
         return data

file_data = read_data(file_name)
print(file_data)
