# 部分文字列
b = set()
for i in range(len(s)):
    for j in range(1,min(k+1,len(s)-i+1)):
        b.add(s[i:i+j])