
import random 
num_aleatorio = random.randint(1,10)
num_aleatorio2=random.randint(1,4)
p = "casi,casi intentalo de nuevo si te quedan intentos :)"
r = "cerca,muuuuuy cerca "
d = "vamos te falta poco"
i = "muy cercaaaaa"
intentos = 3
numero_introducido =0

j=str( input("""Vamos a jugar a adivinar el numero, quieres intenarlo?: (y/n) """))
if j == "y":
    
    print("----------------------------------------------------------")
    print(" Numero generado,trata de adivinar :) ")
    while intentos > 0:
        print("----------------------------------------------------------")
            
        print(f"Numero de intentos: {intentos} ")
        intentos -=1
        numero_introducido=int(input("ingrese el numero que crees que es: "))
        print("----------------------------------------------------------")
        if num_aleatorio==numero_introducido:
            print(f"Felicidades el numero: {numero_introducido} corresponde con el numero que se genero :D ")
            otra=str(input("Desea jugar intentar otra vez? (y/n)"))
            if otra == "n":
                    intentos = -2
            elif otra=="y":
                    intentos = 3
        elif num_aleatorio>numero_introducido and numero_introducido!=9 and num_aleatorio!=10:
                print("el numero generado es mayor al numero que introducistes ")
        elif numero_introducido == 2 and num_aleatorio == 1 :
            if num_aleatorio2==1:
                print(p)
            elif num_aleatorio2==2:
                print(r)
            elif num_aleatorio2==3:
                print(d)
            else:
                print(i)
        elif numero_introducido == 9 and num_aleatorio == 10:
            if num_aleatorio2==1:
                print(p)
            elif num_aleatorio2==2:
                print(r)
            elif num_aleatorio2==3:
                print(d)
            else:
                print(i)
        elif num_aleatorio < numero_introducido and num_aleatorio !=1 and numero_introducido!=2:
            print("el numero generado generado es menor al numero que introducistes ")
        if intentos == 0:
            otra=str(input("Desea jugar intentar otra vez? (y/n)"))
            if otra == "n":
                    intentos = -2
            elif otra=="y":
                    intentos = 3       
else:
    print("oh, bueno :(")       
        
        
        
    
    