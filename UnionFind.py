class UnionFind:
    def __init__(self,n):
        #par[x]==xならxというノードが根。xに親がいない
        self.par = [i for i in range(n+1)]
        self.rank = [0]*(n+1) 
    
    def find(self,x): #xの根を検索
        #xが根ならxを返す
        if self.par[x] == x:
            return x
        else:

            self.par[x] = self.find(self.par[x]) #パス圧縮
            return self.par[x]

    def unite(self,x,y):
        #根を探す
        x = self.find(x)
        y = self.find(y)        
        #木の深さを比較し、小さい方を大きい方につなげる
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1 #rankが同じ木を繋げたとき根のランクを一つ上げる
    
    def same_check(self,x,y): #xとyが同じ集合に属しているか
        return self.find(x) == self.find(y)
n, q = map(int,input().split())
uf = UnionFind(n)
