from PIL import Image
Lista = []




def f1(label):
    print(label)
    InputFile("Adat.txt")
    print("A program készen áll a felhasználói inputra")

def InputFile(File):
    f= open(File, "r")
    for sor in f:
        sor=sor[0:-1].split(";")
        példány = str(sor[0]),str(sor[1])
        Lista.append(példány)
    f.close()



def f2(label):
<<<<<<< HEAD
    for i in range(5):
        print(label)
        print("1 - ",(listarendezes(Lista[0])))
        print("2 - ",(listarendezes(Lista[1])))
        print("3 - ",(listarendezes(Lista[2])))
        print("4 - ",(listarendezes(Lista[3])))
        print("5 - ",(listarendezes(Lista[4])))
        
        x = int(input("Kérek egy számot 1-5: "))
        if(x == 1):
            print(listarendezes(Lista[0]))
        #Megnyitja illetve a .show argumentummal megismutatja azt bármely képszerkesztőben
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Hosoktere.jpeg")
            O.show()
            
        if(x == 2):
            print(listarendezes(Lista[1]))
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\NotreDame.jpg")
            O.show()
        if(x == 3):
            
            print(listarendezes(Lista[2]))
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\orszaghaz.jpg")
            O.show()
        if(x == 4):
            print(listarendezes(Lista[3]))
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Casino.jpg")
            O.show()
        if(x == 5):
            print(listarendezes(Lista[4]))
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Hungaroring.jpg")
            O.show()
        
        
def listarendezes(lista):
    return '{}'.format(','.join(str(s) for s in lista))
=======
    print(label)
    x = int(input("Kérek egy számot 1-5: "))
    for i in range():

>>>>>>> dev

    


f1("POST")
f2("FI1")
