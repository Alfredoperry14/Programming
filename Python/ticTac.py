board = {'TL': '', 'TM': '', 'TR': '',
         'ML': '', 'MM': '', 'MR': '',
         'LL': '', 'LM': '', 'LR': ''
        }

def printBoard():
    track = -1 
    for values in board.values():
        track+= 1
        if(track % 3 == 0):
            print("\n")
        print('|' + str(values) + '|', end=" ")