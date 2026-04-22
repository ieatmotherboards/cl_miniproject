import random
from parse_noun_professions import lst_of_noun_professions

def generate_phrases(nouns: set, proper_nouns: set, verbs: set, determiners: set):
    output = []
    # generate 200 paraphrases
    for _ in range(200):
        
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
        out +=  " was " + verb + " by "
        out += det_n1 + " " + n1 if noun_or_pn_1 == 0 else n1

        output.append(out)

    # generate 200 NOT paraphrases
    for _ in range(200):
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

        out += det_n2.capitalize() + " " + n2 if noun_or_pn_2 == 0 else n2 
        out += " was who "
        out +=  det_n1 + " " + n1 if noun_or_pn_1 == 0 else n1
        out += " was " + verb + " by"

        output.append(out)

    return output

# test
if __name__ == "__main__":

    pns = set()
    with open("parsed_names.txt", "r") as pns_f:
        pns_f = pns_f.readlines()
        for pn in pns_f:
            pns.add(pn[:-1])
        # pns.add(pn for pn in pns_f)


    verbs = set()
    with open("parsed_verbs.txt", "r") as verbs_f:
        verbs_f = verbs_f.readlines()
        # verbs.add(verb for verb in verbs_f)
        for verb in verbs_f:
            verbs.add(verb[:-1])

    # nouns = {"dog", "cat", "eagle", "table", "house"}
    # proper_nouns = {"Holden", "Kevin", "Rui", "Ethan", "Chad"}
    # verbs = {"met", "killed", "touched", "saw"}
    # print("nouns:", nouns)
    # print("PNs:", pns)
    # print("verbs:", verbs)
    determiners = {"a", "the", "that"}
    print(generate_phrases(nouns=lst_of_noun_professions, proper_nouns=pns, verbs=verbs, determiners=determiners))