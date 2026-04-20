import re

if __name__ == "__main__":
    output = []
    with open("unparsed_verbs.txt", "r") as file:
        file = file.readlines()
        for line in file:
            verbs = re.findall(r'<li[^>]*>(.*?)</li>', line)
            for verb in verbs:
                if len(verb.split(' ')) > 1: #ignore bullshit like "Hunt Down", i don't care to conjugate that
                    continue
                
                if verb[-1] == "e": # -e ending, add d
                    verb = verb + "d"
                elif verb[-1] == "y":
                    verb = verb[:-1] # -y ending, remove y and add ied
                    verb = verb + "ied"
                else: # regular case, just add ed
                    verb += "ed"
                output.append(verb.lower())
            # print(output)
            print("length", len(output))

    with open("parsed_verbs.txt", "w") as file:
        for verb in output:
            file.write(str(verb) + '\n')