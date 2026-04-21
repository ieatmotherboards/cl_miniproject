import random

def generate_phrases(nouns: set, proper_nouns: set, verbs: set, determiners: set):
    output = []
    # generate 200 paraphrases
    for _ in range(3):
        out = ""

        verb = random.choice(list(verbs))
        verbs.remove(verb)

        n1 = None
        n2 = None

        # flip coin to determine if the first noun is regular or PN
        noun_or_pn_1 = random.randint(0,1)
        if noun_or_pn_1 == 0: # go with noun
            n1 = random.choice(list(nouns))
            nouns.remove(n1)
            # n1 = random.choice(list(determiners)).capitalize() + " " + n1
        
        else: # proper noun
            
            n1 = random.choice(list(proper_nouns))
            proper_nouns.remove(n1)

        # remove nouns from dataset
        # if noun_or_pn_1 == 0:
            
        # else:
            

        # flip coin to determine if the second noun is regular or PN
        noun_or_pn_2 = random.randint(0,1)

        if noun_or_pn_2 == 0: # go with noun
            n2 = random.choice(list(nouns))
            nouns.remove(n2)
            # n2 = random.choice(list(determiners)).capitalize() + " " + n2

        
        else: # proper noun
            n2 = random.choice(list(proper_nouns))
            proper_nouns.remove(n2)

        # if noun_or_pn_2 == 0:
           
        # else:
        #     proper_nouns.remove(n2)

        out += "1, "
        out += random.choice(list(determiners)).capitalize() + " " + n1 if noun_or_pn_1 == 0 else n1 
        out +=  " " + verb + " "
        out += random.choice(list(determiners)) + " " + n2 if noun_or_pn_2 == 0 else n2
        out += ", "

        out += random.choice(list(determiners)).capitalize() + " " + n2 if noun_or_pn_2 == 0 else n2
        out +=  " was " + verb + " by "
        out += random.choice(list(determiners)) + " " + n1 if noun_or_pn_1 == 0 else n1


        output.append(out)

    # generate 200 NOT paraphrases
    for _ in range(200):
        out = ""


        output.append(out)



    return output
# test
if __name__ == "__main__":
    nouns = {"dog", "cat", "eagle", "table", "house"}
    proper_nouns = {"Holden", "Kevin", "Rui", "Ethan", "Chad"}
    verbs = {"met", "killed", "touched", "saw"}
    determiners = {"a", "the"}
    print(generate_phrases(nouns=nouns, proper_nouns=proper_nouns, verbs=verbs, determiners=determiners))