def compute(template, subs_s, iters):
    subs = {l.split(' -> ')[0]: l.split(' -> ')[1] for l in subs_s.split('\n')}

    pairs = {}
    for i in range(0, len(template)-1):
        pair = template[i] + template[i+1]
        pairs[pair] = pairs.get(pair, 0) + 1

    elements = set(template)
    counts = {e: template.count(e) for e in elements}
    for _ in range(0, iters):
        # for each pair ab - if it matches a substitution s, we 
        # add two new pairs of as and sb, and remove the pair ab
        # but this operation preserves element count for the elements
        # in the pair, and adds elements for the insertion
        np = {}
        for (p, c) in pairs.items():
            if p in subs:
                s = subs[p]
                np[p[0] + s] = np.get(p[0] + s, 0) + c
                np[s + p[1]] = np.get(s + p[1], 0) + c
                counts[s] = counts.get(s, 0) + c
            else: 
                np[p] = c
        pairs = np

    high = max(counts.items(), key=lambda x: x[1])
    low = min(counts.items(), key=lambda x: x[1])
    print(f'high = {high}, low = {low}, score = {high[1] - low[1]}')
    
test_template="""NNCB"""
test_subs="""CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

template="""OHFNNCKCVOBHSSHONBNF"""
subs="""SV -> O
KP -> H
FP -> B
VP -> V
KN -> S
KS -> O
SB -> K
BS -> K
OF -> O
ON -> S
VS -> F
CK -> C
FB -> K
CH -> K
HS -> H
PO -> F
NP -> N
FH -> C
FO -> O
FF -> C
CO -> K
NB -> V
PP -> S
BB -> N
HH -> B
KK -> H
OP -> K
OS -> V
KV -> F
VH -> F
OB -> S
CN -> H
SF -> K
SN -> P
NF -> H
HB -> V
VC -> S
PS -> P
NK -> B
CV -> P
BC -> S
NH -> K
FN -> P
SH -> F
FK -> P
CS -> O
VV -> H
OC -> F
CC -> N
HK -> N
FS -> P
VF -> B
SS -> V
PV -> V
BF -> V
OV -> C
HO -> F
NC -> F
BN -> F
HC -> N
KO -> P
KH -> F
BV -> S
SK -> F
SC -> F
VN -> V
VB -> V
BH -> O
CP -> K
PK -> K
PB -> K
FV -> S
HN -> K
PH -> B
VK -> B
PC -> H
BO -> H
SP -> V
NS -> B
OH -> N
KC -> H
HV -> F
HF -> B
HP -> S
CB -> P
PN -> S
BK -> K
PF -> N
SO -> P
CF -> B
VO -> C
OO -> K
FC -> F
NV -> F
OK -> K
NN -> O
NO -> O
BP -> O
KB -> O
KF -> O"""

compute(template, subs, 40)

