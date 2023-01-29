stringg = "casino is no"
keywordd = "Casino"
# print(stringg.upper().find(keywordd.upper()))

doc_listt = ['The Learn Python Challenge Casino has a big casino full of casino games',
             'They bought a car', 'Casinoville', 'here lies the casino']

keywordd = "casino"


def word_search(word, keyword):
    new_list = []
    for w in range(0, len(word)):
        splitted = word[w].split()
        for n in splitted:
            if n.upper().rstrip('.,') == keyword.upper():
                if w not in new_list:
                    new_list.append(w)

    return new_list


print(word_search(doc_listt, keywordd))
