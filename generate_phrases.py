import random
from parse_noun_professions import lst_of_noun_professions

def generate_phrases(nouns: set, proper_nouns: set, past_verbs: set, present_verbs:set, determiners: set):
    output = []
    # generate 200 paraphrases
    for _ in range(200):

        # coinflip for past and present tense: 0 for past, 1 for present
        is_present = random.randint(0,1)

        if is_present:
            verb = random.choice(list(present_verbs))
            present_verbs.remove(verb)
        else:
            verb = random.choice(list(past_verbs))
            past_verbs.remove(verb)
        
        out = ""

        

        n1 = None
        n2 = None

        # flip coin to determine if the first noun is regular or PN
        noun_or_pn_1 = random.randint(0,1)
        if noun_or_pn_1 == 0: # go with noun
            n1 = random.choice(list(nouns))
            nouns.remove(n1)
        
        else: # proper noun
            n1 = random.choice(list(proper_nouns))
            proper_nouns.remove(n1)

        # flip coin to determine if the second noun is regular or PN
        noun_or_pn_2 = random.randint(0,1)

        if noun_or_pn_2 == 0: # go with noun
            n2 = random.choice(list(nouns))
            nouns.remove(n2)
        
        else: # proper noun
            n2 = random.choice(list(proper_nouns))
            proper_nouns.remove(n2)

        det_n1 = random.choice(list(determiners)).capitalize()
        det_n2 = random.choice(list(determiners)).capitalize()

        out += "1, "
        out += det_n1 + " " + n1 if noun_or_pn_1 == 0 else n1 
        out +=  " " + verb + " "
        out += det_n2 + " " + n2 if noun_or_pn_2 == 0 else n2
        out += ", "

        out += det_n2 + " " + n2 if noun_or_pn_2 == 0 else n2

        if is_present:
            out += " is who " + det_n1.lower() + " " + n1 if noun_or_pn_1 == 0 else n1 
            out += " " + verb
        else:
            out +=  " was " + verb + " by "
            out += det_n1.lower() + " " + n1 if noun_or_pn_1 == 0 else n1

        output.append(out)

    # generate 200 NOT paraphrases
    for _ in range(200):
        out = ""

        is_present = random.randint(0,1)

        if is_present:
            verb = random.choice(list(present_verbs))
            present_verbs.remove(verb)
        else:
            verb = random.choice(list(past_verbs))
            past_verbs.remove(verb)

        n1 = None
        n2 = None

        # flip coin to determine if the first noun is regular or PN
        noun_or_pn_1 = random.randint(0,1)
        if noun_or_pn_1 == 0: # go with noun
            n1 = random.choice(list(nouns))
            nouns.remove(n1)
        
        else: # proper noun
            n1 = random.choice(list(proper_nouns))
            proper_nouns.remove(n1)
            
        # flip coin to determine if the second noun is regular or PN
        noun_or_pn_2 = random.randint(0,1)

        if noun_or_pn_2 == 0: # go with noun
            n2 = random.choice(list(nouns))
            nouns.remove(n2)
        
        else: # proper noun
            n2 = random.choice(list(proper_nouns))
            proper_nouns.remove(n2)
        
        det_n1 = random.choice(list(determiners))
        det_n2 = random.choice(list(determiners))

        out += "0, "
        out += det_n1.capitalize() + " " + n1 if noun_or_pn_1 == 0 else n1 
        out +=  " " + verb + " "
        out += det_n2 + " " + n2 if noun_or_pn_2 == 0 else n2
        out += ", "


        if is_present:
            out += det_n1.capitalize() + " " + n1 if noun_or_pn_1 == 0 else n1 
            out += " is who "
            out +=  det_n2 + " " + n2 if noun_or_pn_2 == 0 else n2 #TODO: change me
            out += " " + verb

        else:
            out += det_n2.capitalize() + " " + n2 if noun_or_pn_2 == 0 else n2 
            out += " was who "
            out +=  det_n1 + " " + n1 if noun_or_pn_1 == 0 else n1
            out += " was " + verb + " by"

        output.append(out)

    return output

def parse_phrases() -> list:
    phrases = []
    numbers = []
    with open("phrases.txt", "r") as f:
        f = f.readlines()
        # strip off beginning
        for line in f:
            num = line[0]
            line = line[3:]
            line = line[:-1]
            phrases.append(line)
            numbers.append(int(num))

    print(phrases)
    print(numbers)

# test
if __name__ == "__main__":

    pns = set()
    with open("parsed_names.txt", "r") as pns_f:
        pns_f = pns_f.readlines()
        for pn in pns_f:
            pns.add(pn[:-1])
        # pns.add(pn for pn in pns_f)


    past_verbs = set()
    with open("parsed_past_verbs.txt", "r") as verbs_f:
        verbs_f = verbs_f.readlines()
        # verbs.add(verb for verb in verbs_f)
        for verb in verbs_f:
            past_verbs.add(verb[:-1])

    present_verbs = set()
    with open("parsed_present_verbs.txt", "r") as verbs_f2:
        verbs_f2 = verbs_f2.readlines()
        for verb in verbs_f2:
            present_verbs.add(verb[:-1])


    # nouns = {"dog", "cat", "eagle", "table", "house"}
    # proper_nouns = {"Holden", "Kevin", "Rui", "Ethan", "Chad"}
    # verbs = {"met", "killed", "touched", "saw"}
    # print("nouns:", nouns)
    # print("PNs:", pns)
    # print("verbs:", verbs)
    determiners = {"a", "the", "that"}
    out = generate_phrases(nouns=lst_of_noun_professions, proper_nouns=pns, past_verbs=past_verbs, present_verbs=present_verbs, determiners=determiners)
    with open("phrases.txt", "w") as wf:
        for phrase in out:
            wf.write(phrase + '\n')
    parse_phrases()

