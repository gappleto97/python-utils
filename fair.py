def flip():
    """A fair coin simulator"""
    from random import choice
    while True:
        r1, r2 = choice([0,1]), choice([0,1])
        if bool(r1) ^ bool(r2):  # exclusive or
            yield r1

def fairest(symbols="01"):
    """Uses an algorithm to generate an n-party Thue-Morse sequence"""
    seq = symbols
    transitions = {}
    for sym in symbols:
        loc = symbols.find(sym)
        transitions[sym] = symbols[loc:] + symbols[:loc]
    count = 0
    while True:
        if count >= len(seq):
            seq = ''.join((transitions[x] for x in seq))
        yield seq[count]
        count += 1

        
def fairest_2():
    """Uses an algorithm to generate an 2-party Thue-Morse sequence"""
    num = 0
    while True:
        temp, ret = num, 0
        num += 1
        while temp:
            ret += 1
            temp &= temp - 1
        yield ret & 1
