S=list(input().upper())
SS=list(set(S))
cnt=[0 for i in range(len(SS))]
for i in range(len(SS)):
    cnt[i]+=S.count(SS[i])

ans=SS[cnt.index(max(cnt))]
if cnt.count(max(cnt))>=2:
    ans='?'

print(ans)