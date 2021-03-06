from IPython.display import clear_output

def wanna_play():
    wynik = input('Hej wanna play tic tac toe: (Y/N) ' )
    wynik = wynik.upper()
    if wynik == 'Y':
        print('Super lets play')
    elif wynik == 'N':
        print('OK next time')
        
    else:
        print('Wrong letter. Choose Y or N')
        wanna_play()
    return wynik

def player1():
    decyzja1 = input('Wanna X or O: \n')
    decyzja1 = decyzja1.upper()
    
    while decyzja1 not in ('X', 'O'):
        decyzja1 = input('Give X or O: \n')
        decyzja1 = decyzja1.upper()
    
    if decyzja1 in ('X', 'O'):
        print (f'Player1 you are {decyzja1}\n')
    
    return decyzja1
    

def player2(decyzja1):
    decyzja2 = ''
    if decyzja1 == 'X':
        decyzja2 = 'O'
        print (f'Player2 you are {decyzja2}\n')
    elif decyzja1 == 'O':
        decyzja2 = "X"
        print (f'Player2 you are {decyzja2}\n')


    return decyzja2 


def tn_player1(decyzja1):
    number1 = 5
  
    if decyzja1 == 'X':      # ta zmienna musi być taka sama jak wyżej w nawiasie
        number1 = input("Player1 give a number to X: ")
        while int(number1)not in range(1,10):
            number1 = input("Player1 give a number between 1-9: ")
        while board[int(number1)-1] not in range(1,10) :
            number1 = input("This place is taken. Give another number: ")
     
    elif decyzja1 == 'O':
        number1 = input("Player1 give a number to O: ")
        while int(number1) not in range(1,10):
            number1 = input("Player1 give a number  between 1-9: ")
        while board[int(number1)-1] not in range(1,10) :
            number1 = input("This place is taken. Give another number: ")
  
    return number1 
           
def tn_player2(decyzja1):
    number2 = 5
    if decyzja1 in ('x', 'X'):      # ta zmienna musi być taka sama jak wyżej w nawiasie
        number2 = input("Player2 give a number to O: ")
        while int(number2) not in range(1,10):
            number2 = input("Player2 give a number to between 1-9: ")
        while board[int(number2)-1] not in range(1,10) :
            number2 = input("This place is taken. Give another number: ")

    elif decyzja1 in ('o', 'O'):
        number2 = input("Player2 give a number to X: ")
        while int(number2) not in range(1,10):
            number2 = input("Player2 give a number to  between 1-9: ")
        while board[int(number2)-1] not in range(1,10)  :
            number2 = input("This place is taken. Give another number: ")

    
    return number2
           
def make_turn1(decyzja1, number1): # tutaj ewentualnie rozdzielić na make_turn1 i make_turn2
    
    if decyzja1 == "X":
        board[int(number1)-1] = "X"
    else:
        board[int(number1)-1] = "O"
    return board[int(number1)-1]

def make_turn2(decyzja1, number2): # tutaj ewentualnie rozdzielić na make_turn1 i make_turn2
    
    if decyzja1 == "X":
        board[int(number2)-1] = "O"
    else:
        board[int(number2)-1] = "X"
        
    return board[int(number2)-1]  


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # na tej liście podczas gry wprwadzam zmiany w postaci wpisanych X oraz O
board1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # pozycje w board a nie same cyfry
again = 'n'


def draw_board():
    print('\n')
    clear_output()
    print(board[6], board[7], board[8])
    print(board[3], board[4], board[5])
    print(board[0], board[1], board[2])
           
def check_board(win_commbinations):   

    for a in win_commbinations:
        if board[a[0]] == 'X' and board[a[1]] == 'X' and board[a[2]] == 'X': # tutaj powinno być and
            print("Player with X wins!\n")
            print("Congratulations!\n")
            return True

        if board[a[0]] == 'O' and board[a[1]] == 'O' and board[a[2]] == 'O':
            print("Player with O wins!\n")
            print("Congratulations!\n")
            return True


def is_game_finished(win_commbinations):
    end = check_board(win_commbinations)
    if end:
        print("This is the end of the game")
        
    return end

def double(number1, number2):
    if board[int(number1)-1] == "X" or board[int(number2)-1] == "X" or board[int(number1)-1] == "O" or board[int(number2)-1] == "O" : 
        print("\nYou can't go there. Try another number")


def playAgain():
        #end = is_game_finished(win_commbinations)
        #if end == True:
        print('Do you want to play again? (y or n): ')
        again = input().lower()
        if again == 'y':
            clear_output()
            clean_board()
            main()
        elif again == 'n':
            clear_output()
            print('Thanks for the play')
                

def clean_board():
    for n, i in enumerate(board):
        board[n] = board1[n]

def isSpaceFree(board, move):
        if board[number1] not in board1:
            return False
            

def main():
    
    end = False
    count = 0
    
    wynik = wanna_play()
    if wynik  == 'N':
        end = None
        return end
    
    decyzja1 = player1()
    player2(decyzja1)
    
    
    
    while not end:
    
        print('\n')
        draw_board()
        print('\n')
        number1 = tn_player1(decyzja1)
        make_turn1(decyzja1, number1)
        count += 1
        draw_board()
        print('\n')
        end = is_game_finished(win_commbinations)
            
        if end:
            break
        if count == 9:
            print('This is the end of the game.\n The game ends in a Tie')
            print('\n')
            playAgain()
            break
        number2 = tn_player2(decyzja1)
        make_turn2(decyzja1, number2)
        count += 1
        print('\n')  
        end = is_game_finished(win_commbinations)
        
    
    if end == True:
        playAgain()
        count = 0



    

    
        

