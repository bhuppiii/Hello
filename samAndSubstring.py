n= "4101852174452269981498703517571992187514189408526665757008986077205157775937789367033735745553393831700413283339155628305950481794067030571004230794754242400691200123200302946117692"
b = []
l = len(n)
for i in range(l):
    c = ""
    for j in range(i, l):
        c += n[j]
        b.append(c)
b = list(map(int,b))
print(sum(b)%((10**9)+7))