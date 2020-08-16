import string
from collections import Counter
from itertools import permutations

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalLetters = 26
sequence = [19, 17, 17, 19, 14, 20, 23, 18, 19, 8, 12, 16, 19, 8, 3, 21, 8, 25, 18, 14, 18, 6, 3, 18, 8, 15, 18, 22, 18, 11]  #type your message here

counts = Counter(sequence)
sorted_counts = sorted(counts.items(), key=lambda tup: tup[1], reverse=True)

for (k, v) in sorted_counts:
    print(k, v)

letter_frequency_in_order = 'etaoinshrdlcumwfgypbvkjxqz'#from google
# 18 6 assume e
# 19 4 probably a
# 8  4 might be in 'oiu'
# 17 2 probably t
# 14 2 probably c
# 3  2
# 20 1 probably k
# 23 1
# 12 1
# 16 1
# 21 1
# 25 1
# 6  1
# 15 1
# 22 1
# 11 1

mappings = {
    19: 'a',
    17: 't',
    14: 'c',
    20: 'k',
    18: 'e'
}

print("".join([mappings.get(i, '?') for i in sequence]))
# attack?ea???a?????ece??e??e?e?
#       ^ is this the start of pearl?

mappings[23] = 'p'
mappings[8] = 'r'
mappings[12] = 'l'

print("".join([mappings.get(i, '?') for i in sequence]))
# attackpearl?ar??r?ece??er?e?e?
#            ^ looking like the start of harbor

mappings[16] = 'h'
mappings[3] = 'b'
mappings[21] = 'o'

print("".join([mappings.get(i, '?') for i in sequence]))
# attackpearlharbor?ece?ber?e?e?
#                  ^ december? It would make sense for it to be a date

mappings[25] = 'd'
mappings[6] = 'm'

print("".join([mappings.get(i, '?') for i in sequence]))
# attackpearlharbordecember?e?e?
#                          ^ seven

mappings[15] = 's'
mappings[22] = 'v'
mappings[11] = 'n'

print("".join([mappings.get(i, '?') for i in sequence]))
# attackpearlharbordecemberseven

exit()

lowercase = 'abcdefghijklmnopqrstuvwxyz'
message = "".join([lowercase[i] for i in sequence])
print('message', message)
# trrtouxstimqtidvizsosgdsipswsl
# SHOULD MAP TO
# attack????????????????????????

domain = set(message)
print("Domain size", len(domain))  # 16

assert (len(letter_frequency_in_order) == 26)

attack_table = {
    't': 'a',
    'r': 't',
    'o': 'c',
    'u': 'k',
}

next_most_frequent_without_attack = "".join([i for i in letter_frequency_in_order if i not in 'attack'])
remaining_12 = next_most_frequent_without_attack[:12]
print(remaining_12)
# we already know the mappings for 4 of the characters, and we know the domain is 16 characters

known_domain_mappings = set("trou")
unknown_domain_mappings = domain - known_domain_mappings

for permutation in permutations(remaining_12):
    # map the unknown domain onto the remaing most frequent letters
    rest_table = dict(zip(unknown_domain_mappings, permutation))
    combined_table = {**attack_table, **rest_table}

    candidate = "".join([combined_table[i] for i in message])
    print(candidate)
