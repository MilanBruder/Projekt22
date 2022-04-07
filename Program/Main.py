import webbrowser
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
    ut="T:\Bruder Milán10D\Projekt22"
    while True:
        print(label)
        print("1 - ",(listarendezes(Lista[0])))
        print("2 - ",(listarendezes(Lista[1])))
        print("3 - ",(listarendezes(Lista[2])))
        print("4 - ",(listarendezes(Lista[3])))
        print("5 - ",(listarendezes(Lista[4])))
        
        x = int(input("Kérek egy számot 1-5: "))
        
        if(x == 1):
            print(listarendezes(Lista[0]))
        #Megnyitja illetve a .show argumentummal meg is mutatja azt bármely képszerkesztőben
            O = Image.open(r"kep\Hosoktere.jpeg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/H%C5%91s%C3%B6k_tere')
            
        if(x == 2):
            print(listarendezes(Lista[1]))
            O = Image.open(r"kep\NotreDame.jpg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/H%C5%91s%C3%B6k_tere')
            
        if(x == 3):
            
            print(listarendezes(Lista[2]))
            O = Image.open(r"kep\orszaghaz.jpg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/Orsz%C3%A1gh%C3%A1z')
        if(x == 4):
            print(listarendezes(Lista[3]))
            O = Image.open(r"kep\Casino.jpg")
            O.show()
            webbrowser.open('https://www.montecarlosbm.com/en/casino-monaco')
        if(x == 5):
            print(listarendezes(Lista[4]))
            O = Image.open(r"kep\Hungaroring.jpg")
            O.show()
            webbrowser.open('https://hungaroring.hu/')
        
        
def listarendezes(lista):
    return '{}'.format(','.join(str(s) for s in lista))


    

    


f1("POST")
f2("FI1")
