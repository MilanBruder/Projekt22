Lista = []




def f1(label):
    print(label)
    InputFile("Adat.txt")
    print(Lista)

def InputFile(File):
    f= open(File, "r")
    for sor in f:
        sor=sor[0:-1].split(";")
        példány = str(sor[0]),str(sor[1])
        Lista.append(példány)
    f.close()



def f2(label):
    print(label)
    x = int(input("Kérek egy számot 1-5: "))
    for i in range():


    


f1("Teszt")
f2("IRASKEP")
