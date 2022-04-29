import M_class
import webbrowser
from PIL import Image
Lista = []




 
def f1(label):
    print(label)
    InputFile("Adat.txt")
    print("A program készen áll a felhasználói inputra")
    Y = input("Kérek egy várost: ")
    for i in range(len(Lista)):
        
        if (Lista[i].ország == Y):


        
            print(Lista[i].rekordkép())

def InputFile(File):
    f= open(File, "r")
    for sor in f:
        sor=sor[0:-1].split(";")
        példány =M_class.Orszag(str(sor[0]),str(sor[1]), str(sor[2]))
        Lista.append(példány)
    f.close()

    


def f2(label):
    ut="T:\Bruder Milán10D\Projekt22"
    
        
    while True:
        
        print("1 - ",(Lista[0].rekordkép()))
        print("2 - ",(Lista[1].rekordkép()))
        print("3 - ",(Lista[2].rekordkép()))
        print("4 - ",(Lista[3].rekordkép()))
        print("5 - ",(Lista[4].rekordkép()))
        x = int(input("Kérek egy számot 1-5: "))
    
        if(x == 1):
            print(Lista[0].rekordkép())
        #Megnyitja illetve a .show argumentummal meg is mutatja azt bármely képszerkesztőben
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Kep\Hosoktere.jpeg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/H%C5%91s%C3%B6k_tere')
            
        if(x == 2):
            print(Lista[1].rekordkép())
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Kep\NotreDame.jpg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/Notre-Dame-sz%C3%A9kesegyh%C3%A1z_(P%C3%A1rizs)')
            
        if(x == 3):
            
            print(Lista[2].rekordkép())
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Kep\orszaghaz.jpg")
            O.show()
            webbrowser.open('https://hu.wikipedia.org/wiki/Orsz%C3%A1gh%C3%A1z')
        if(x == 4):
            print(Lista[3].rekordkép())
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Kep\Casino.jpg")
            O.show()
            webbrowser.open('https://www.montecarlosbm.com/en/casino-monaco')
        if(x == 5):
            print(Lista[4].rekordkép())
            O = Image.open(r"C:\Users\lajha\Desktop\GIT\Projekt22\Kep\Hungaroring.jpg")
            O.show()
            webbrowser.open('https://hungaroring.hu/')
    
        



    

    


f1("POST")
#f2("FI1")
