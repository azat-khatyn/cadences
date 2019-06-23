import random as rnd


kadez = ['IV maj 7', 'VII-7b5', 'III-7', 'VI-7', 'II-7', 'V7']
sec_dom = ['VII7', 'III7', 'VI7', 'II7', 'V7', 'I7']
trit_sub = ['tr7', 'tr7', 'tr7', 'tr7', 'tr7', 'tr7']
total = [kadez, sec_dom, trit_sub]


def get_all_vollkadenzen():
    return [ (total[i6][0], total[i5][1], total[i4][2], total[i3][3], total[i2][4], total[i1][5]) for i6 in range(3) for i4 in range(3) for i3 in range(3) for i2 in range(3) for i1 in range(3) ]


def get_random_vollkadenz():
    return [total[rnd.randrange(3)][i] for i in range(5)]


def print_vollkadenz(vollkadenz):
    print('%s %s' % ('IVmaj7', ' '.join(vollkadenz)))


while (True):
    print_vollkadenz(get_random_vollkadenz())
    goon = input('One more? (y for yes): ')
    if goon != 'y':
        break

all_vollkadenzen = get_all_vollkadenzen()

for vollkadenz in all_vollkadenzen:
    print_vollkadenz(vollkadenz)

#print(len(all_vollkadenzen))
