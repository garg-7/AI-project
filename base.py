

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
    def __init__(self, walls, food, pLoc, qLoc):
        self.walls = walls
        self.food = food
        self.pLoc = pLoc
        self.qLoc = qLoc


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
        possible.append(((x, y+1), 'North'))
    if walls[x][y+1] == False and (ye!=y+1 or xe!=x):
        possible.append(((x+1, y+2), 'East'))
    if walls[x][y-1] == False and (ye!=y-1 or xe!=x):
        possible.append(((x+1, y), 'West'))
    if walls[x+1][y] == False and (xe!=x+1 or ye!=y):
        possible.append(((x+2, y+1), 'South'))
    print(possible)
    return "bYe"

state = GameState(walls, food, p_init, q_init)
getSuccessors(state, 'q')

