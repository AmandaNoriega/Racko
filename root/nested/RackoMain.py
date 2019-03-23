'''
Created on Apr 21, 2018

@author: Amanda Noriega
'''
from root.nested import RackoGame


if __name__ == '__main__':
    print('Welcome to Racko.')
    play_in = input('Would you like to play? (yes or no) ')
    
    if(play_in == 'yes'):
        print("Great!  Lets play!")
        name = input('Who is playing? ')

        racko = RackoGame.Racko(name)
        racko.playGame()
    
        print('Thanks for playing, ',name,'.  Goodbye.')

    else:
        print("Ok.  Maybe next time.")
        exit
    