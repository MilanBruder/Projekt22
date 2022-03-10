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
    print("1 - ",Lista[0])
    print("2 - ",Lista[1])
    print("3 - ",Lista[2])
    print("4 - ",Lista[3])
    print("5 - ",Lista[4])
    
    x = int(input("Kérek egy számot 1-5: "))
    if(x == 1):
        print(Lista[0])
    if(x == 2):
        print(Lista[1])
    if(x == 3):
        print(Lista[2])

    if(x == 4):
        print(Lista[3])
    if(x == 5):
        print(Lista[4])
        


    


f1("Teszt")
f2("IRASKEP")
