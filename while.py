def verifpassw():
    passw=""
    print("Ingrese su password ")
    while passw !="1234":
        print("Su password es incorrecta")
        passw=input()

        print("Bienvenido Usuario Admin")


        verifpassw()
        
        
        while cantMicros !=3:
            
            print("Ha pasado una micro?")
            resp=input()
            
            if resp=="si":
                cantMicros=cantMicros+1
                
                