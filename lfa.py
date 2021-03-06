def check(transition_list, word):
    """
    This is a recursive function that check
    the transition for every symbol in word
    """
    global ok
    if len(word) == 0:
        if transition_list[0][0] in final_states:
            ok = 1
    elif len(transition_list[0]) is 1:
        return 0
    else:
        for transition in transition_list:
            if transition[1] is word[0]:
                new_word = word[1:]
                if transition[2] in lafn:
                    check(lafn[transition[2]], new_word)
            if('.' in transition):
                if transition[2] in lafn:
                    check(lafn[transition[2]], word)
        
lafn = {}
f = open("lafn.txt", "r")
date_in = f.readlines()

symbols = date_in[0]
states = date_in[1]
final_states = date_in[2]
for state in states:
    lafn[state] = [state]
i = 0
for line in date_in[3:]:
    lafn[states[i]] = line.split()
    i += 2
print states
print lafn

f.close()
f = open("test.in.txt", "r")
test_words = f.readlines()
test_words = [word.strip('\n') for word in test_words]
print test_words

for word in test_words:
    ok = 0
    check(lafn[states[0]], word)
    if ok:
        print "Accept!"
    else:
        print "NO!"  

