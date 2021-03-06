import math

def bits(packet, m, length):
    return m - length, (packet >> (m - length)) & ((0b1 << length) - 1)

def literal(packet, s):
    v = 0
    c = 1
    while c != 0:
        s, c = bits(packet, s, 1)
        s, a = bits(packet, s, 4)
        v = (v << 4) + a

    return (s, v)

class node:
    def __init__(self, version, typeid, content):
        self.version = version
        self.typeid = typeid
        self.content = content

    def __repr__(self):
        return f'v={self.version} t={self.typeid} c={self.content}'

def decode(packet, s):
    s, version = bits(packet, s, 3)
    s, typeid = bits(packet, s, 3)
    if typeid == 4:
        s, v = literal(packet, s)
        return s, node(version, typeid, v)
    else:
        s, length_mode = bits(packet, s, 1)
        if length_mode == 0:
            s, bit_length = bits(packet, s, 15)
            end = s - bit_length
            children = []
            while s > end:
                s, child = decode(packet, s)
                children.append(child)
            return s, node(version, typeid, children)
        else:
            s, packet_length = bits(packet, s, 11)
            children = []
            for _ in range(0, packet_length):
                s, child = decode(packet, s)
                children.append(child)
            return s, node(version, typeid, children)

operators = {
    0: sum, 
    1: math.prod,
    2: min,
    3: max,
    5: lambda l: 1 if l[0] > l[1] else 0, # gt
    6: lambda l: 1 if l[0] < l[1] else 0, # lt
    7: lambda l: 1 if l[0] == l[1] else 0, # eq
}

def vsum(ast):
    if ast.typeid == 4:
        return ast.content
    else:
        return operators[ast.typeid]([vsum(v) for v in ast.content])

def compute(data):
    packet = int(data, 16)
    s, ast = decode(packet, len(data)*4)
    print(ast)
    print(vsum(ast))

test_literal="""D2FE28"""
test_bitlength="""38006F45291200"""
test_packetlength="""EE00D40C823060"""
test_16="""8A004A801A8002F478"""
test_12="""620080001611562C8802118E34"""
test_23="""C0015000016115A2E0802F182340"""
test_31="""A0016C880162017C3686B18A3D4780"""

data="""60556F980272DCE609BC01300042622C428BC200DC128C50FCC0159E9DB9AEA86003430BE5EFA8DB0AC401A4CA4E8A3400E6CFF7518F51A554100180956198529B6A700965634F96C0B99DCF4A13DF6D200DCE801A497FF5BE5FFD6B99DE2B11250034C00F5003900B1270024009D610031400E70020C0093002980652700298051310030C00F50028802B2200809C00F999EF39C79C8800849D398CE4027CCECBDA25A00D4040198D31920C8002170DA37C660009B26EFCA204FDF10E7A85E402304E0E60066A200F4638311C440198A11B635180233023A0094C6186630C44017E500345310FF0A65B0273982C929EEC0000264180390661FC403006E2EC1D86A600F43285504CC02A9D64931293779335983D300568035200042A29C55886200FC6A8B31CE647880323E0068E6E175E9B85D72525B743005646DA57C007CE6634C354CC698689BDBF1005F7231A0FE002F91067EF2E40167B17B503E666693FD9848803106252DFAD40E63D42020041648F24460400D8ECE007CBF26F92B0949B275C9402794338B329F88DC97D608028D9982BF802327D4A9FC10B803F33BD804E7B5DDAA4356014A646D1079E8467EF702A573FAF335EB74906CF5F2ACA00B43E8A460086002A3277BA74911C9531F613009A5CCE7D8248065000402B92D47F14B97C723B953C7B22392788A7CD62C1EC00D14CC23F1D94A3D100A1C200F42A8C51A00010A847176380002110EA31C713004A366006A0200C47483109C0010F8C10AE13C9CA9BDE59080325A0068A6B4CF333949EE635B495003273F76E000BCA47E2331A9DE5D698272F722200DDE801F098EDAC7131DB58E24F5C5D300627122456E58D4C01091C7A283E00ACD34CB20426500BA7F1EBDBBD209FAC75F579ACEB3E5D8FD2DD4E300565EBEDD32AD6008CCE3A492F98E15CC013C0086A5A12E7C46761DBB8CDDBD8BE656780"""

compute(data)


