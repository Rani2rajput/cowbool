import random
name=input("Hellow! enter your respective name:")
print("----------------",name,"--------------------")
print( "   | WELL COME TO COWS AND BULLS GAME |"       )
def guess():
    Number=[0,1,2,3,4,5,6,7,8,9]
    z=random.sample(Number,5)
    print(z)
    bull=[]
    cow=[]
    i=0
    chance=10
    while i<=10:
        guess=int(input("enter your guess number::="))
        position=int(input("enter the position of your guess number::="))
        if guess in z:
            index=z.index(guess)
            if index==position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("BULL",bull)
                else:
                    print("you already used this digit try any different digit")
            else:
                cow.append(guess)
                print("Cow",cow)
        else:
            print("Your number is not exist!")
        if bull==z:
            print(name," congrachulations you are win  the game")
            break
        if chance==1:
            print("**Soory!Your chances are finished!!**")
            break
        chance=chance-1
        print(chance,"Turn are left")
    else:
        print("you loose the Game please start again")
    return bull
guess()
def playagain():
    while True:
        play=input("you want to play again:y/n:-")
        if play=="y":
            guess()
        elif play=="n":
            print("Thanks for playing!!")
            break
playagain()
            
    
        
        
                      
            
            
    
    






