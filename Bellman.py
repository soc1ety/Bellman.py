# the graph 

g = {
    (0,1) : 1,
    (0,2) : 4,
    (0,4) : 5,
    (0,5) : 2,
    (1,2) : 2,
    (1,5) : 3,
    (2,3) : 3,
    (2,4) : 1,
    (4,3) : 3,
    (5,4) : 3
}

n = 6
a = 10

# successors and predecessors

S = range(6)
Succ = {s : [] for s in S}
Pred = {s : [] for s in S}

for (x,y) in g:
    Succ[x].append(y)
    Pred[y].append(x)

# marque = lower degree

Marques = {}
for s in S:
    Marques[s] = len(Pred[s])


# Bellman

r = int(input("Starting point : "))
C = []
Pi = {}
A = {}

for s in S:
    if Marques[s] == 0:
     C.append(s)

while len(C) > 0:
    s = C.pop(0)
    if s == r:
        Pi[s] = 0
        A[s] = None
    else:
        Pi[s] = None
        A[s] = s
        for x in Pred[s]:
            if Pi[x] == None:
                continue
            if Pi[s] == None or Pi[x] + g[(x,s)] < Pi[s]:
                Pi[s] = Pi[x] + g[(x,s)]
                A[s] = x
    for x in Succ[s]:
        Marques[x] -= 1
        if Marques[x] == 0:
            C.append(x)

print("s\t Pi\t A")
print("---------------------")
for x in S:
    print(x, '\t', Pi[x], '\t', A[x])
