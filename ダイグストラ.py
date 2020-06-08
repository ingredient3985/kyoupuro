from heapq import heappop, heappush
INF = 10**12
v,e,r = map(int,input().split())
edge = [[] for _ in range(v)]
d = [INF]*v
for i in range(e):
    s,t,c = map(int,input().split())
    edge[s].append([t,c])
d[r]=0
q = [(d[r],r)]
while q:
    du,u = heappop(q)
    for t,c in edge[u]:
        if d[t] > du + c:
            d[t] = du + c
            heappush(q,(d[t],t))
for D in d:
    print('INF' if D == INF else D)
