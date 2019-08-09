def rihai(t):
    l=list(t)
    l.sort()
    res="".join(l)
    return res

def janto(t):
    res=[]
    for i in range(1,10):
        l=list(t)
        if l.count(str(i))>=2:
            l.remove(str(i))
            l.remove(str(i))
            p="".join(l)
            res.append(p)
    return res

from functools import lru_cache
@lru_cache(maxsize=10000)
def mentsu(t):
    if t=="":
        return True

    if t[0]==t[1] and t[0]==t[2]:
        l=list(t)
        l.remove(t[0])
        l.remove(t[0])
        l.remove(t[0])
        t="".join(l)
        return mentsu(t)
    if str(int(t[0])+1) in t:
            if str(int(t[0])+2) in t:
                l=list(t)
                l.remove(str(int(l[0])+2))
                l.remove(str(int(l[0])+1))
                l.remove(l[0])
                t="".join(l)
                return mentsu(t)
    return False

tehai=input()
ans=[]
for i in range(1,10):
    t=tehai
    if t.count(str(i))>=4:
        continue
    t=t+str(i)
    t=rihai(t)
    l=janto(t)
    if len(l)==7:
        ans.append(i)
        
    for j in l:
        if mentsu(j):
            ans.append(i)

tmp=set(ans)
ans=list(tmp)
ans.sort()
print(ans)