
# print(stringg.upper().find(keywordd.upper()))

doc_listt = ['The Learn Python Challenge Casino has a big casino full of casino games',
             'They bought a car', 'Casinoville', 'here lies the casino']

keywordd = ["casino", "they"]


'''
def multi_word_search(word, keyword):
    book = {}
    sub_list = []
    for w in range(0, len(word)):
        splitted = word[w].split()
        print(splitted)

        for n in splitted:
            if any(x.upper() == n.upper().rstrip('.,') for x in keyword):
                print(n)
                print(w)
                pass

        for n in splitted:
            if n.upper().rstrip('.,') == keyword.upper():
                if w not in sub_list:
                    sub_list.append(w)

    return book
'''


def multi_word_search(words, keywords):
    book = {}

    for w in range(0, len(words)):
        #print(words[w], end='\n \n')
        modified = [z.upper().rstrip('.,') for z in words[w].split()]
        print(end='\n \n')
        for m in modified:
            #print(m, end='\n')
            if any(x.upper() == m.rstrip('.,') for x in keywords):
                print(True, w, m)
    # pass


print(multi_word_search(doc_listt, keywordd))
