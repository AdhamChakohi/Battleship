## Code written by Aladham Chakohi
## this is a game of battleship, but with a twist that the ships move with the current

import layout
layout.competition = False
movingShips = True
listOfLists = []

for i in range(layout.rows):
    listOfLists.append([layout.marker.water]*layout.columns) ## this is to generate an empty size agnostic list of lists

## this loop is to add the ships


for ship in layout.ships:
    begin = ship[0]
    end =  ship[1]
    if begin[0] == end[0]:
        for col in range(begin[1],end[1]+1):
            listOfLists[begin[0]][col] = layout.marker.ship
    else:
        for row in range(begin[0],end[0]+1):
            listOfLists[row][begin[1]] = layout.marker.ship


## the following code is to generate the grid. it also checks the competition setting and prints accordingly 
for i in range(len(listOfLists)):
    print(((layout.board.corner+layout.board.top)*len(listOfLists[i]))+layout.board.corner)
    for j in listOfLists[i]:
        if not layout.competition:
            print(layout.board.side+str(j), end="")
        elif layout.competition:
            print(layout.board.side+layout.marker.water, end="")
    print(layout.board.side)
print(((layout.board.corner+layout.board.top)*len(listOfLists[-1]))+layout.board.corner)


## this for loop counts how many 'X's are in the grid. every time the
## player gets a hit, the number is subtracted by one, game ends when x becomes 0
x = 0
for i in listOfLists:
        for j in i:
            if j == layout.marker.ship:
                x += 1


hits = 0
misses = 0
guesses = 0
while x > 0:
    ## the following code is to move the items in the board according to the current.
    ## List insert method allows me to insert whatever I want wherever I want
    ## it also checks if movement is enabled
    movement = layout.current()
    
    if movingShips:
        if movement[1] == 1:
            for i in range(len(listOfLists)):
                listOfLists[i].insert(0,listOfLists[i].pop(-1))
            
        if movement[1] == -1:
            for i in range(len(listOfLists)):
                listOfLists[i].append(listOfLists[i].pop(0))
        if movement[0] == 1:
            listOfLists.insert(0,listOfLists.pop(-1))
        if movement[0] == -1:
            listOfLists.append(listOfLists.pop(0))
    
        print('current:',movement)
    ## this is for the user input. I have it setup so it'll end the game if the user types in 'stop'
    guesstimate = input('Enter your guess (x,y):')
    guess = guesstimate.split(',')

    if guesstimate == 'stop':
        break
    
    ## the following if statemenet checks if the guess is a hit, and replaces the marker with the appropriate symbol
    ## it also counts the hits and misses
    if listOfLists[int(guess[0])][int(guess[1])] == layout.marker.ship:
        listOfLists[int(guess[0])][int(guess[1])] = layout.marker.hit
        hits += 1
        x -= 1
                
    
    elif listOfLists[int(guess[0])][int(guess[1])] == layout.marker.water:
        listOfLists[int(guess[0])][int(guess[1])] = layout.marker.miss
        misses += 1
    
    elif listOfLists[int(guess[0])][int(guess[1])] == layout.marker.hit or listOfLists[int(guess[0])][int(guess[1])] == layout.marker.miss:
        misses += 1
    guesses += 1
    
   
    ## this for loop prints the updated board. It also prints it according to the competition setting
    for i in range(len(listOfLists)):
        print(((layout.board.corner+layout.board.top)*len(listOfLists[i]))+layout.board.corner)
        for j in listOfLists[i]:
            if not layout.competition:
                print(layout.board.side+str(j), end="")
            elif j == layout.marker.hit or j == layout.marker.miss:
                print(layout.board.side+str(j), end="")
            else:
                print(layout.board.side+layout.marker.water, end="")
        print(layout.board.side)
    print(((layout.board.corner+layout.board.top)*len(listOfLists[-1]))+layout.board.corner)
    print('hits:',hits,',','misses:',misses,',','guesses:',guesses)
    
    
    
    
print('game over!')
## this is here for if the user stops the game at 0 guesses, it won't have to divide by zero
if guesses == 0:
    print('hit ratio: 0.0')
if guesses != 0:
    ratio = hits/guesses
    print('hit ratio:',ratio)
                