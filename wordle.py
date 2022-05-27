a="a"
b="b"
c="c"
d="d"
e="e"
f="f"
g="g"
h="h"
i="i"
j="j"
k="k"
l="l"
m="m"
n="n"
o="o"
p="p"
q="q"
r="r"
s="s"
t="t"
u="u"
v="v"
w="w"
x="x"
y="y"
z="z"

exclude=[]
yellow=[]#format : letter, letter index
green=[0,0,0,0,0]
possible=[]

wordlist=open("wordlist.txt","r")
rawwordlist=wordlist.read()
wordlist.close()
wordlist=rawwordlist.split("\n")

pw=1
for word in wordlist:
    pw=1
    #check all green letters
    for i1 in range(0,5):
        if green[i1]!=0:
            if word[i1]!=green[i1]:
                pw=0
                break
    if pw==1:
        #check all yellow letters
        x1=0
        while x1<len(yellow):
            if not(yellow[x1] in word):
                pw=0
            if word[yellow[x1+1]]==yellow[x1]:
                pw=0
            x1=x1+2
        if pw==1:
            #check all excluded letters
            for letter in exclude:
                if letter in word:
                    pw=0
                    break
            if pw==1:
                possible.append(word)
print(len(possible))

scores=[z,0,q,0,j,0,x,0,k,1,v,1,b,2,p,3,y,3,g,3,f,3,w,3,m,3,u,4,c,4,l,5,d,5,r,6,h,6,s,7,n,7,i,8,o,8,a,9,t,10,e,11]
pfreq=[]
pfreq2=[]
for word in possible:
    tmp=0
    ll=[]
    for i1 in range(0,5):
        if word[i1] in ll:
            tmp=tmp-22
        tmp=tmp+scores[scores.index(word[i1])+1]
        ll.append(word[i1])
    pfreq.append(word)
    pfreq2.append(tmp)
new=[sl for _,sl in sorted(zip(pfreq2,pfreq))]
new.reverse()
print(new[0:300])