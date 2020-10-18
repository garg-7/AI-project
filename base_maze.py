

#####################
#                   #
#      .    #########
#           #.      #
#####     . ###     #
#  P#               #
#   # .      ########
#   ##       #Q     #
#                   #
#####################

# First, read such a maze.

MAZE_PATH = 'maze.txt'

f = open(MAZE_PATH, 'r')

width = 0
height = 0
walls = []
food = []

p_init = None
q_init = None

for row, line in enumerate(f.readlines()):
    if width == 0:
        width = len(line.strip().strip('\n'))
    if len(line.strip().strip('\n'))!=width:
        # print(len(line.strip().strip('\n')))
        print("[ABORT] Inconsistent maze size!")
        exit(2)
    if not (line.strip().startswith('#') and line.strip().endswith('#')):
        print("[ABORT] Incorrectly bound maze!")
        exit(2)
    else:
        row_walls = []
        row_food = []
        for col, c in enumerate(line):
            if c=='#':
                row_walls.append(True)
                row_food.append(False)
            elif c=='.':
                row_food.append(True)
                row_walls.append(False)
            elif c.lower()=='p':
                if p_init == None:
                    p_init = (row, col)
                    row_food.append(False)
                    row_walls.append(False)
                else: 
                    print("[ABORT] Imposter players (P)!")
                    exit(2)
            elif c.lower()=='q':
                if q_init == None:
                    q_init = (row, col)
                    row_food.append(False)
                    row_walls.append(False)
                else: 
                    print("[ABORT] Imposter players (Q)!")
                    exit(2)
            elif c==' ':
                row_food.append(False)
                row_walls.append(False)
            elif c=='\n':
                pass
            else:
                print("[ABORT] Invalid character detected!")
                exit(2)
    height+=1
    walls.append(row_walls)
    food.append(row_food)

print("[DONE] Maze successfully generated!")
print("[.] Maze height:", height)
print("[.] Maze width:", width)
if p_init:
    print("[.] P is at", (p_init[0]+1, p_init[1]+1))
if q_init:
    print("[.] Q is at", (q_init[0]+1, q_init[1]+1))
print("[.] Food is at:", end=' ')
fList = []
for row, f in enumerate(food):
    for col, e in enumerate(f):
        if e==True:
            fList.append((row, col))

for f in fList:
    print((f[0]+1, f[1]+1), end=' ')


class GameState:
    def __init__(self, walls, food, pLoc, qLoc, height, width):
        self.walls = walls
        self.food = food
        self.pLoc = pLoc
        self.qLoc = qLoc
        self.pEaten = 0
        self.qEaten = 0
        self.height = height
        self.width = width

    def isGameOver(self):
        if True not in food:
            return True
        else:
            return False


def getSuccessors(state, turn='p'):
    print()
    walls = state.walls
    if turn == 'p':
        x, y = state.pLoc
        xe, ye = state.qLoc
    elif turn=='q':
        x, y = state.qLoc
        xe, ye = state.pLoc
    else:
        print('[ABORT] Wrong Player!')
        exit(2)
    possible = []
    if walls[x-1][y] == False and (xe!=x-1 or ye!=y):
        possible.append(((x-1, y), 'North'))
    if walls[x][y+1] == False and (ye!=y+1 or xe!=x):
        possible.append(((x, y+1), 'East'))
    if walls[x][y-1] == False and (ye!=y-1 or xe!=x):
        possible.append(((x, y-1), 'West'))
    if walls[x+1][y] == False and (xe!=x+1 or ye!=y):
        possible.append(((x+1, y), 'South'))
    # print(possible)
    return possible

def getMaze(state):
    walls = state.walls
    food = state.food
    h = state.height
    w = state.width
    pLoc = state.pLoc
    qLoc = state.qLoc
    for row in range(height):
        for col in range(w):
            if walls[row][col]==True:
                print('#',end='')
            elif food[row][col]==True:
                print('.',end='')
            elif pLoc == (row, col):
                print('P',end='')
            elif qLoc == (row, col):
                print('Q',end='')
            else: print(' ',end='')
        print()


state = GameState(walls, food, p_init, q_init, height, width)
# getSuccessors(state, 'q')
# getMaze(state)


def movePlayer(state, action, player):
    if state.food[action[0][0]][action[0][1]]==True:
        state.food[action[0][0]][action[0][1]]=False
        if player=='p':
            state.pEaten += 1
        else:
            state.qEaten += 1
    
    if player=='p':
        state.pLoc = action[0]
    else:
        state.qLoc = action[0]

    return

i=0

while i<10:
    move = getSuccessors(state, 'p')
    if len(move)!=0:
        movePlayer(state, move[-1], 'p')
    getMaze(state)
    move = getSuccessors(state, 'q')
    if len(move)!=0:
        movePlayer(state, move[-1], 'q')
    getMaze(state)
    i+=1
    if len(getSuccessors(state, 'p'))==0 and \
        len(getSuccessors(state, 'q'))==0:
        break