from problems import nQueensProblem, propertyProblem
from local import *

QUEENS = 8
HOUSES_FILE = 'houses.txt'

# q = nQueensProblem(QUEENS, [5,6,1,7,2,3,0,4])
# print("Steepest Hill Climbing:")
# print(f"Starting Obj fn val = {q.getObjValue(q.state)}")
# steps, q.state = hillClimbingSearch_S(q)
# # q.visualize(q.state)
# print(f"Steps: {steps}")
# print(f"Obj fn val = {q.getObjValue(q.state)}")


# print("Tabu Search:")
# q = nQueensProblem(QUEENS, None)
# steps, q.state = tabuSearch(q, 1024, 500000)
# # q.visualize(q.state)
# print(f"Steps: {steps}")
# print(f"Obj fn val = {q.getObjValue(q.state)}")

# q = nQueensProblem(QUEENS, None)
# print("First Choice Hill Climbing:")
# print(f"Starting Obj fn val = {q.getObjValue(q.state)}")
# steps, q.state = hillClimbingSearch_FC(q)
# # q.visualize(q.state)
# print(f"Steps: {steps}")
# print(f"Obj fn val = {q.getObjValue(q.state)}")

# q = nQueensProblem(QUEENS, None)
# print("RR Hill Climbing:")
# print(f"Starting Obj fn val = {q.getObjValue(q.state)}")
# steps, q.state = hillClimbingSearch_RR(q)
# q.visualize(q.state)
# print(f"Steps: {steps}")
# print(f"Obj fn val = {q.getObjValue(q.state)}")

fHouses = open(HOUSES_FILE, 'r')
priceList = []
for line in fHouses.readlines():
    x, y_true = map(int, line.strip().split(','))
    priceList.append((x, y_true))
p = propertyProblem(priceList)
optimizedWeights = gradDescent(p, 10000)
p.visualize(optimizedWeights)
# resp = input('Do you wish to see the loss plot?')
# if resp.lower() == 'yes' or resp.lower() == 'y':
p.visualizeLoss()


print("***** GENERALIZED LOCAL SEARCH SOLVER *****")
print("\nThere are various algorithms available for different domains. Select a domain:")
print("\n1. Discrete Domain")
print("2. Continuous Domain")


while True:
    resp = input("1/2?")
    if resp == '1':
        print("[INFO] Discrete Domain Picked.")
        print("[INFO] Problem to run on: N Queens Problem")
        queens = input("\n Enter the number of Queens")
        print("\nHow should the search proceed?")
        print("\n1. Random Initialization")
        print("2. You wish to enter the initial state")
        how = input("1/2?")
        if how=='1':
            problem = nQueensProblem(queens, None)
        elif how=='2':
            print("For every column, enter comma-separated row numbers in which queens are present:")
            placement = input()
            placement = placement.strip().split(',')
            # TODO: check validity of input state
            problem = nQueensProblem(queens, placement)
        print("\nNow, pick a local search algorithm to run: ")
        print("\n1. Steepest Hill Climbing")
        print("2. Tabu Search")
        print("3. First Choice Hill Climbing")
        print("4. Random Restart Hill Climbing")
        print("5. Simulated Annealing")
        algo = int(input("Enter a number - "))
        if algo=='1':
            print("[INFO] Steepest Hill Climbing Chosen")



    elif resp == '2': 
        print("[INFO] Continuous Domain Picked.")
        print("ALgorithm to run: Gradient Descent")
        print("")

    else:
        print('[ISSUE] Invalid Choice')