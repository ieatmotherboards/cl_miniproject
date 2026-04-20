import re

if __name__ == "__main__":
    names = set()

    with open("unparsed_names.txt") as file:
        file = file.readlines()
        for line in file:
            name = re.search(r'(?<=<strong>).*(?=</strong>)', line)
            if name:
                names.add(str(name.group()))

    with open('parsed_names.txt', 'w') as f:
        # f.write(name for name in names) # list comprehension didn't work here :(
        for name in names:
            f.write(name + '\n')
