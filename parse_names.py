import re

names = set()

with open("unparsed_names.txt") as file:
    file = file.readlines()
    for line in file:
        name = re.search(r'(?<=<strong>).*(?=</strong>)', line)
        if name:
            names.add(str(name.group()))


if __name__ == "__main__":
    print(names)