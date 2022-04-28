f=open("állatok.txt","r",encoding="utf-8")
#beolvasunk
nagylista=[]
for sor in f:
    #print(sor)
    kislista=sor[:-1].split(";")
    #print(kislista)
    nagylista.append(kislista)
f.close()
