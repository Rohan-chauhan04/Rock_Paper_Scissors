import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=="p":
            return True
        
    elif comp == 's':
        if you == 'p':
            return False
        elif you=='r':
            return True
        
    elif comp == 'p':
        if you == 'r':
            return False
        elif you=='s':
            return True
        
randno =random.randint(1,3)
if randno==1:
    comp='r'
elif randno == 2:
    comp='p'
elif randno==3:
    comp='s'

you=input('Rock(r) Paper(p) or Scissors(s)')

print(f'You choose {you}')
print(f'computer choose {comp}')

a=gamewin(comp,you)
if a==None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print('You Lose!')



