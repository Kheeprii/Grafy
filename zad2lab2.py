from collections import defaultdict

v = int(input("Podaj liczbe wierzcholkow w grafie: "))

graph = defaultdict(list)

for i in range(1,v+1):
  print("Podaj sasiadow wierzcholka: "+str(i))
  graph[i] = [int(i) for i in input().split(',')]

print()
for klucz, wartosc in graph.items():
  print("Wierzcholek "+str(klucz),"ma sasiadow: "+str(wartosc))
