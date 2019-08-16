
def inc(x):return x +10

counters = [1,2,3,4,5,6,7,8]
mapa = map(inc,counters)
mapaL = list(mapa)
print(mapaL)


mapa2 = map((lambda x : x+3),counters)

mapaL = list(mapa2)
print(mapaL)

print(pow(3,4))

mapa3=map(pow,[1,2,3],[1,2,3])

mapaL = list(mapa3)
print(mapaL)
