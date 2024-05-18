"""Check whether a given variable-length code is uniquely decodable.
This is a direct/naive implementation of the Sardinas-Patterson algorithm.
It can be used to check if e.g. a given phoneme inventory yields unambiguous
transcriptions.
"""

def LeftQuotientOfWord(ps, w):
    """Yields the suffixes of w after removing any prefix in ps."""
    for p in ps:
        if w.startswith(p):
            yield w[len(p):]
    return

def LeftQuotient(ps, ws):
    """Returns the set of suffixes of any word in ws after removing any prefix
    in ps. This is the quotient set which results from dividing ws on the
    left by ps."""
    qs = set()
    for w in ws:
        for q in LeftQuotientOfWord(ps, w):
            qs.add(q)
    return qs

def IsUniquelyDecodable(cs):
    """Checks if the set of codewords cs is uniquely decodable via the
    Sardinas-Patterson algorithm."""
    NL, i = len(str(cs)) * len(str(max(len(x) for x in cs))), 1 # Levenstein's upper bound for termination
    s = LeftQuotient(cs, cs)
    s.discard('')
    if len(s) == 0:
        #Uniquely decodable prefix code.
        return True
    while '' not in s and len(s & cs) == 0:
        t = LeftQuotient(cs, s) | LeftQuotient(s, cs)
        if t == s or i > NL + 1:
            # Uniquely decodable.
            return True
        s = t
        i += 1
    # if '' in s:
    #     print('Dangling empty suffix.')
    # for x in s & cs:
    #     print('Dangling suffix: {}'.format(x))
    return False

