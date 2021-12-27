
def paths(graph):
    p = 0
    q = [['start']] # started paths
    c = [] # completed paths
    
    while len(q) > 0:
        n = q.pop()
        f = n[0]
        if (f == 'end'):
            c.append(n)
        else:
            q.extend([[c] + n for c in graph[f] if c.isupper() or not c in n])
    
    return c


def compute(data):
    connections = [(l.split('-')[0], l.split('-')[1]) for l in data.split('\n')]
    print(connections)

    graph = {}
    for edge in connections + [(b, a) for (a,b) in connections]:
        graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]

    print(graph)

    p = paths(graph)
    print(p)
    print(len(p))



test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

td2="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

td3="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

data="""start-kc
pd-NV
start-zw
UI-pd
HK-end
UI-kc
pd-ih
ih-end
start-UI
kc-zw
end-ks
MF-mq
HK-zw
LF-ks
HK-kc
ih-HK
kc-pd
ks-pd
MF-pd
UI-zw
ih-NV
ks-HK
MF-kc
zw-NV
NV-ks"""

compute(data)