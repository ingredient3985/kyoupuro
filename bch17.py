n = int(input())
s = [input() for _ in range(n)]
a = 0
b = 0
ab = 0
for i in range(n):
    if s[i][0] == "B" and s[i][-1] == "A":
        ab += 1
        a += 1
        b += 1
    elif s[i][0] == "B":
        b += 1
    elif s[i][-1] == "A":
        a += 1
c = min(a, b)
ans = c
if ab > 0:
    ans += ab
if a== 0 and b==0:
    ans = ab - 1
for S in s:
    for i in range(len(S)-1):
        if S[i: i + 2] == "AB":
            ans += 1
print(ans)