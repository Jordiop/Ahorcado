#Ahorcado by Jordi Osarenkhoe Petro
#No és especialment eficient però funciona
#Sa excepció són es simbols i els espais que no he sabut implementar

import random
intentos = 7   
alfabet = "abcdefghijklmnopqrstuvwxyz"
signes = [" " , "," , "." , ":" , ";"]
frase = ""
palabra = ""
incorrecta = ""
correcta = ""
listaPalabras = ["programacio", "pc", "lol", "clase", "ahorcado"]
seleccio = ""

#Funció ahorcado per evitar reiteracions de dibuixets
def Ahorcado(intentos):
    if intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)

#Menú per seleccionar si volem jugar amb una paraula/frase nostra, una paraula random o sortir
#Sa llista es curta perquè l'he emprada per fer testing
#Es podria importar un diccionari per una variació més amplia de paraules
def menu():
    global seleccio
    print ("Posa el nombre del que vulguis fer")
    print ("| 1. JUGAR AMB FRASE O PARAULA PRÒPIA | 2. JUGAR AMB PARAULA ALEATÒRIA | 3. SORTIR")
    while seleccio != 1 or seleccio != 2 or seleccio != 3:
        seleccio = int(input())
        if seleccio == 1:
            frase = input("Escriu la paraula o frase que vols: ")
            juego(frase)
        elif seleccio == 2:
            b = random.randint(0, len(listaPalabras) - 1)
            frase = listaPalabras[b]
            juego(frase)
        elif seleccio == 3:
            break
        
#While true emprat per un bucle "infinit" del ahorcado fins que es compleixi una de les condicions
def juego(frase):
    global palabra
    global correcta
    global incorrecta
    global intentos
    global alfabet
    while True:
        comprobador = 0
        #Lo que fa això és verificar quan de guions queden per esbrinar. 
        #Quan veu que no en queda ningun, automàticament acaba el joc
        for lletra in frase:
            if lletra in palabra:
                print(lletra,end='')
            #Imprimeix les lletres que son dins frase a sa posició que toca
            else:
                for alfabet in frase:
                    print(" _",end="")
                    comprobador = comprobador + 1
                #Per cada guió que hi ha, afegeix 1. 
                # Si la paraula té 4 lletres i n'hi ha 2 de esbrinades serà 2, 
                # si n'esbrinam una altra, serà 1 i quan acabem serà 0.

        #Si es comprobador arriba aqui siguent 0 (només pot passar si adivines la paraula) acabarà el joc 
        if comprobador == 0:
            print ("Has guanyat!")
            print ("El que havies de esbrinar era" ,frase,)
            print ("Vols tornar a jugar?")
            print ("| 1. JUGAR AMB FRASE O PARAULA PRÒPIA | 2. JUGAR AMB PARAULA ALEATÒRIA | 3. SORTIR")
            break
            menu()
            

        #Input de les lletres    
        print ("\nDona una lletra")
        lletra=input()
        palabra = palabra + lletra

        #Afegim les lletres a la variable correcta
        if lletra in frase:
            correcta = correcta + lletra
            print ("Lletres correctes: " ,correcta,)
            print ("Lletres incorrectes: " ,incorrecta,)
        
        #Condició si sa lletra no està bé    
        if lletra not in frase:
            intentos = intentos - 1
            incorrecta = incorrecta + lletra
            print (Ahorcado(intentos))
            print (intentos)
            print ("Aquesta lletra no és correcte")
            print ("Te queden" ,intentos, "intents")
            print ("Lletres correctes: " ,correcta,)
            print ("Lletres incorrectes: " ,incorrecta,)

        if len(lletra) != 1:
            print ("Aixo no es nomes una lletra")
            print ("Aixo te llevara una vida. Has d'anar amb alerta es pròxim pic")
            intentos = intentos - 1
            print (Ahorcado(intentos))
            print (intentos)

        if intentos == 0:
            print ("Has perdut")
            break
            menu()

    else:
        print ("Gracies per jugar")
        print ("La paraula era" ,frase,)
        menu()
        
print ("Quin es el teu nom?")
nom = str(input())
print ("Hola" ,nom, "")
menu()


        
        
    

    
