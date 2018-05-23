#Wyznaczanie stopnia grafu nieskierowanego.
from collections import defaultdict

v = int(input("Podaj liczbe wierzcholkow w grafie: "))

graph = defaultdict(list)

dg = 0 #zerujemy stopien grafu

for i in range(1,v+1):
  print("Podaj sasiadow wierzcholka: "+str(i))
  graph[i] = [int(i) for i in input().split(',')]

for i in graph:
  print("Stopien "+str(i),"wierzcholka wynosi: "+str(len(graph[i])))
  if(len(graph[i]) > dg):
    dg = len(graph[i])
print("Stopien grafu wynosi: "+str(dg))

