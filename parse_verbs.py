import re

if __name__ == "__main__":
    past = []
    present = []
    with open("unparsed_verbs.txt", "r") as file:
        file = file.readlines()
        for line in file:
            verbs = re.findall(r'<li[^>]*>(.*?)</li>', line)
            for verb in verbs:
                if len(verb.split(' ')) > 1: #ignore bullshit like "Hunt Down", i don't care to conjugate that
                    continue
                
                present_verb = verb

                if verb[-1] == "e": # -e ending, add d
                    verb = verb + "d"
                elif verb[-1] == "y":
                    verb = verb[:-1] # -y ending, remove y and add ied
                    verb = verb + "ied"
                else: # regular case, just add ed
                    verb += "ed"

                past.append(verb.lower())

                # now, do the same but for present tense

                present_verb = present_verb + "s"
                present.append(present_verb.lower())
            # print(output)
            print("length", len(past))

    with open("parsed_past_verbs.txt", "w") as file:
        for verb in past:
            file.write(str(verb) + '\n')

    with open("parsed_present_verbs.txt", "w") as file:
        for verb in present:
            file.write(str(verb) + '\n')