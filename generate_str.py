

if __name__ == "__main__":
    output = ""
    with open("parsed_names.txt", "r") as file:
        for line in file.readlines():
            if line[-1] == '\n': # handles last line
                line = line[:-1] #shave off newline
                
            output += "'" + line + "' | "
    #shave off last 3 characters (" | ")
    output = output[:-3]
    print(output)