import argparse, sys, re
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

# fHouses = open(HOUSES_FILE, 'r')
# priceList = []
# for line in fHouses.readlines():
#     x, y_true = map(int, line.strip().split(','))
#     priceList.append((x, y_true))
# p = propertyProblem(priceList)
# optimizedWeights = gradDescent(p, 10000)
# p.visualize(optimizedWeights)
# resp = input('Do you wish to see the loss plot?')
# if resp.lower() == 'yes' or resp.lower() == 'y':
# p.visualizeLoss()





# while True:
#     print("***** GENERALIZED LOCAL SEARCH SOLVER *****")
#     print("\nThere are various algorithms available for different domains. Select a domain:")
#     print("\n1. Discrete Domain")
#     print("2. Continuous Domain")
#     resp = input("1/2? ")
#     if resp == '1':
#         print("[INFO] Discrete Domain Picked.")
#         print("[INFO] Problem to run on: N Queens Problem")
#         queens = int(input("\nEnter the number of Queens: "))
#         print("\nHow should the search proceed?")
#         print("\n1. Random Initialization")
#         print("2. You wish to enter the initial state")
#         how = input("1/2? ")
#         if how=='1':
#             problem = nQueensProblem(queens, None)
#         elif how=='2':
#             print("For every column, enter comma-separated row numbers in which queens are present:")
#             placement = input()
#             placement = placement.strip().split(',')
#             # TODO: check validity of input state
#             problem = nQueensProblem(queens, placement)
#         print("\nNow, pick a local search algorithm to run: ")
#         print("\n-------DETERMINISTIC ALGORITHMS-------")
#         print("1. Steepest Hill Climbing")
#         print("2. Tabu Search")
#         print("\n--------STOCHASTIC ALGORITHMS--------")
#         print("3. First Choice Hill Climbing")
#         print("4. Random Restart Hill Climbing")
#         print("5. Simulated Annealing")
#         algo = input("\nEnter a number - ")
#         if algo=='1':
#             print("[INFO] Steepest Hill Climbing Chosen")
#             print(f"[START] Running the algorithm for {queens}-Queens Problem")
#             steps, problem.state = hillClimbingSearch_S(problem)
#             print(f"[END] Completed in {steps} steps.")
#             print(f"      Final objective function value: {problem.getObjValue(problem.state)}")

#         elif algo=='2':
#             print("[INFO] Tabu Search Chosen")
#             print("OPTIONAL Parameters... Press enter to continue with default values.")
#             print("(Default values: Tabu Tenure = 32, maxSteps = Run till optimum)")
#             tabuTenure = input("Enter size of Tabu Tenure: ")
#             maxSteps = input("Enter maximum number of steps to take: ")
#             print(f"[START] Running the algorithm for {queens}-Queens Problem")
#             if len(tabuTenure)!=0:
#                 if len(maxSteps)!=0:
#                     print('both entered')
#                     steps, problem.state = tabuSearch(problem, int(tabuTenure), int(maxSteps))
#                 else:
#                     steps, problem.state = tabuSearch(problem, int(tabuTenure))
#             else:
#                 if len(maxSteps)!=0:
#                     steps, problem.state = tabuSearch(problem, maxSteps=int(maxSteps))
#                 else:
#                     print("none entered")
#                     steps, problem.state = tabuSearch(problem)
#             print(f"[END] Completed in {steps} steps.")
#             print(f"      Final objective function value: {problem.getObjValue(problem.state)}")
        
#         elif algo=='3':
#             print("[INFO] First-Choice Hill Climbing Chosen")
#             print("OPTIONAL Parameters... Press enter to continue with default values.")
#             print("(Default values: maxTrials = 100)")
#             maxTrials = input("Enter max number of random neighbours to try before declaring optimum: ")
#             print(f"[START] Running the algorithm for {queens}-Queens Problem")
#             if len(maxTrials)!=0:
#                 steps, problem.state = hillClimbingSearch_FC(problem, maxTrials=maxTrials)
#             else:
#                 steps, problem.state = hillClimbingSearch_FC(problem)
#             print(f"[END] Completed in {steps} steps.")
#             print(f"      Final objective function value: {problem.getObjValue(problem.state)}")
        
#         elif algo=='4':
#             print("[INFO] Random-Restart Hill Climbing Chosen")
#             print("OPTIONAL Parameters... Press enter to continue with default values.")
#             print("(Default values: pRestart = 0.1, maxSteps = 10,000)")
#             pRestart = input("Enter the probability of random restart: ")
#             maxSteps = input("Enter maximum number of steps to take: ")
#             print(f"[START] Running the algorithm for {queens}-Queens Problem")
#             if len(pRestart)!=0:
#                 if len(maxSteps)!=0:
#                     steps, problem.state = hillClimbingSearch_RR(problem, int(pRestart), int(maxSteps))
#                 else:
#                     steps, problem.state = hillClimbingSearch_RR(problem, int(pRestart))
#             else:
#                 if len(maxSteps)!=0:
#                     steps, problem.state = hillClimbingSearch_RR(problem, maxSteps=int(maxSteps))
#                 else:
#                     steps, problem.state = hillClimbingSearch_RR(problem)
        
#             print(f"[END] Completed in {steps} steps.")
#             print(f"      Final objective function value: {problem.getObjValue(problem.state)}")

#         else:
#             print("[ERROR] Incorrect Choice of Algorithm.")


#     elif resp == '2': 
#         print("[INFO] Continuous Domain Picked.")
#         print("[INFO] Problem to solve: Real Estate property price prediction")
#         fHouses = open(HOUSES_FILE, 'r')
#         priceList = []
#         for line in fHouses.readlines():
#             x, y_true = map(int, line.strip().split(','))
#             priceList.append((x, y_true))
#         problem = propertyProblem(priceList)
#         print("[INFO] ALgorithm to run: Gradient Descent")
#         print("OPTIONAL Parameters... Press enter to continue with default values.")
#         print("(Default values: stepSize = 0.1, maxIterations = 5000)")
#         stepSize = input("Enter the step size to begin with: ")
#         maxIterations = input("Enter maximum number of iterations to work for: ")
#         print(f"[START] Running the algorithm for Property Price Prediction Problem")
#         if len(stepSize)!=0:
#             if len(maxIterations)!=0:
#                 optimizedWeights = gradDescent(problem, 
#                                         maxIterations=int(maxIterations),
#                                         stepSize=int(stepSize))
#             else:
#                 optimizedWeights = gradDescent(problem,
#                                         stepSize=int(stepSize))
#         else:
#             if len(maxIterations)!=0:
#                 optimizedWeights = gradDescent(problem,
#                                         maxIterations=int(maxIterations))
#             else:
#                 optimizedWeights = gradDescent(problem)
        
#         problem.visualize(optimizedWeights)
#         problem.visualizeLoss()

#     else:
#         print('[ERROR] Invalid Choice')

parser = argparse.ArgumentParser(description="Generalized Local Search Tool")

optional =  parser._action_groups.pop()
required = parser.add_argument_group('required argument(s)')
required.add_argument("-d", "--domain",
                    help="Continuous or Discrete Local Search",
                    # choices=['discrete', 'continuous']
                    required=True)
optional.add_argument("-q", "--queens",
                    help="Number of Queens for the N-Queens problem. Default: 8",
                    type=int,
                    default=8)
optional.add_argument("-u", "--userInit",
                    help="Optional user initialization for the N-Queens problem")
optional.add_argument("-da", "--dAlgo",
                    help="Name of algorithm to work with in the discrete case. Default: HC_S",
                    default='HC_S'
                    # choices=['HC_S', 'TS', 'HC_FC', 'HC_RR', 'SA']
                    )
optional.add_argument("-ca", "--cAlgo",
                    help="Name of algorithm to work with in the continuous case. Default: BGD",
                    # choices=['BGD'],
                    default='BGD') 

optional.add_argument("-tt", "--tabuTenure",
                    help="[TS] Size of Tabu Tenure. Default: 32",
                    type=int,
                    default=32)
optional.add_argument("-s", "--maxSteps",
                    help="[TS] [HC_RR] Maximum number of steps to take. Default: TS - Go till optimum; HC_RR - 10,000",
                    type=int)
optional.add_argument("-mt", "--maxTrials",
                    help="[HC_FC] Max number of random neighbours to try before declaring optimum. Default: 100",
                    type=int,
                    default=100)
optional.add_argument("-p", "--pRestart",
                    help="[HC_RR] Probability of random restart. Default: 0.1",
                    type=float,
                    default=0.1)
parser._action_groups.append(optional)
args = parser.parse_args()

def main():
    global args
    global parser
    if args.domain=='discrete':

        # initialize the problem
        if args.userInit is not None:
            # if user wants to give initial state
            userInit = list(map(int, args.userInit.strip().replace('[','').replace(']','').split(',')))
            manualInit = []
            if len(userInit)==args.queens:
                for v in userInit:
                    if v>args.queens or v<1:
                        print("[ERROR] Invalid Initialization!")
                        sys.exit()
                    else:
                        manualInit.append(v-1)
                problem = nQueensProblem(args.queens, manualInit)
            else:
                print("[ERROR] Incomplete Initialization!")
                sys.exit()
        else:
            # random initialization of input
            problem = nQueensProblem(args.queens, None)
        
        # pick the algorithm and run it
        if args.dAlgo=='HC_S':
            print("[INFO] Steepest Hill Climbing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = hillClimbingSearch_S(problem)
            print(f"[END] Completed in {steps} steps.")
            print(f"      Final objective function value: {problem.getObjValue(problem.state)}")
        
        elif args.dAlgo=='TS':
            if args.maxSteps is None:
                args.maxSteps = -1 # default is go till optimum

            print("[INFO] Tabu Search Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = tabuSearch(problem, args.tabuTenure, args.maxSteps)
            print(f"[END] Completed in {steps} steps.")
            print(f"      Final objective function value: {problem.getObjValue(problem.state)}")

        elif args.dAlgo=='HC_FC':
            print("[INFO] First-Choice Hill Climbing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = hillClimbingSearch_FC(problem, maxTrials=args.maxTrials)
            print(f"[END] Completed in {steps} steps.")
            print(f"      Final objective function value: {problem.getObjValue(problem.state)}")

        elif args.dAlgo=='HC_RR':
            if args.maxSteps is None:
                args.maxSteps = 10_000 # default is go till optimum

            print("[INFO] Random-Restart Hill Climbing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = hillClimbingSearch_RR(problem, args.pRestart, args.maxSteps)
            print(f"[END] Completed in {steps} steps.")
            print(f"      Final objective function value: {problem.getObjValue(problem.state)}")

    elif args.domain=='continuous':
        pass

if __name__=='__main__':
    main()

