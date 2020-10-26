import argparse, sys, re
from problems import nQueensProblem, propertyProblem
from local import *

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
optional.add_argument("-i", "--userInit",
                    help="Optional user initialization for the N-Queens problem")
optional.add_argument("-da", "--dAlgo",
                    help="Name of algorithm to work with in the discrete case. Default: HC_S",
                    # choices=['HC_S', 'TS', 'HC_FC', 'HC_RR', 'SA'],
                    default='HC_S')
optional.add_argument("-ca", "--cAlgo",
                    help="Name of algorithm to work with in the continuous case. Default: BGD",
                    # choices=['BGD'],
                    default='BGD') 
optional.add_argument("-u", "--userInteraction",
                    help="Keep the search interactive",
                    action='store_true')
optional.add_argument("-qt", "--quiet",
                    help="No intermediate visualizations. Only show results.",
                    action='store_true')
optional.add_argument("-tt", "--tabuTenure",
                    help="[TS] Size of Tabu Tenure. Default: 32",
                    type=int,
                    default=32)
optional.add_argument("-s", "--maxSteps",
                    help="[TS] [HC_RR] [SA] Maximum number of steps to take. Default: TS - Till optimum; HC_RR/SA - 1000",
                    type=int)
optional.add_argument("-mt", "--maxTrials",
                    help="[HC_FC] Max number of random neighbours to try before declaring optimum. Default: 100",
                    type=int,
                    default=100)
optional.add_argument("-p", "--pRestart",
                    help="[HC_RR] Probability of random restart. Default: 0.1",
                    type=float,
                    default=0.1)
optional.add_argument("-f", "--listingsPath",
                    help="[BGD] Path to known listings file. Default: './listings.txt'",
                    type=str,
                    default="./listings.txt")
optional.add_argument("-ss", "--stepSize",
                    help="[BGD] Step size factor to begin with. Default: 0.1",
                    type=float,
                    default=0.1)
optional.add_argument("-itr", "--maxIterations",
                    help="[BGD] Number of iterations to run gradient descent for. Default: 5000",
                    type=int,
                    default=5_000)

            

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
            steps, problem.state = hillClimbingSearch_S(problem, args.userInteraction, args.quiet)
            if problem.getObjValue(problem.state)==0:
                print(f"[END] Global Optimum Reached i.e. hVal=0 in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            else:
                print(f"[END] Local Optimum Reached with hVal={problem.getObjValue(problem.state)} in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            print("[PLOT] Plotting the landscape explored...")
            problem.visualizeLandscape()

        
        elif args.dAlgo=='TS':
            if args.maxSteps is None:
                args.maxSteps = -1 # default is go till optimum

            print("[INFO] Tabu Search Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = tabuSearch(problem, args.tabuTenure, args.maxSteps, args.userInteraction, args.quiet)
            if problem.getObjValue(problem.state)==0:
                print(f"[END] Global Optimum Reached i.e. hVal=0 in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            else:
                print(f"[END] Local Optimum Reached with hVal={problem.getObjValue(problem.state)} in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            print("[PLOT] Plotting the landscape explored...")
            problem.visualizeLandscape()

        elif args.dAlgo=='HC_FC':
            print("[INFO] First-Choice Hill Climbing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, problem.state = hillClimbingSearch_FC(problem, args.maxTrials, args.userInteraction, args.quiet)
            if problem.getObjValue(problem.state)==0:
                print(f"[END] Global Optimum Reached i.e. hVal=0 in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            else:
                print(f"[END] Local Optimum Reached with hVal={problem.getObjValue(problem.state)} in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            print("[PLOT] Plotting the landscape explored...")
            problem.visualizeLandscape()

        elif args.dAlgo=='HC_RR':
            if args.maxSteps is None:
                args.maxSteps = 10_000 # default is 10,000

            print("[INFO] Random-Restart Hill Climbing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, state = hillClimbingSearch_RR(problem, args.pRestart, args.maxSteps, args.userInteraction, args.quiet)
            if problem.getObjValue(state)==0:
                print(f"[END] Global Optimum Reached i.e. hVal=0 in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            else:
                print(f"[END] Local Optimum Reached with hVal={problem.getObjValue(state)} in {steps} steps")
                print("Best state yet: ")
                problem.visualize(state)
            print("[PLOT] Plotting the landscape explored...")
            problem.visualizeLandscape()

        elif args.dAlgo=='SA':
            if args.maxSteps is None:
                args.maxSteps = 10_000 # default is 10,000
            
            print("[INFO] Simulated Annealing Chosen")
            print(f"[START] Running the algorithm for {args.queens}-Queens Problem")
            steps, state = simulatedAnnealing(problem, args.maxSteps, args.userInteraction, args.quiet)
            if problem.getObjValue(state)==0:
                print(f"[END] Global Optimum Reached i.e. hVal=0 in {steps} steps")
                if args.quiet:
                    problem.visualize(problem.state)
            else:
                print(f"[END] Local Optimum Reached with hVal={problem.getObjValue(state)} in {steps} steps")
                print("Best state yet: ")
                problem.visualize(state)
            print("[PLOT] Plotting the landscape explored...")
            problem.visualizeLandscape()


    
    elif args.domain=='continuous':
        print("[INFO] Continuous Domain Picked.")
        print("[INFO] Problem to solve: Real estate price prediction")
        fHouses = open(args.listingsPath, 'r')
        priceList = []
        for line in fHouses.readlines():
            x, y_true = map(int, line.strip().split(','))
            priceList.append((x, y_true))
        problem = propertyProblem(priceList)
        print("[INFO] Algorithm to run: Gradient Descent")
        print(f"[START] Running the algorithm for Property Price Prediction Problem")
        optimizedWeights, bestLoss = gradDescent(problem, 
                                        maxIterations=args.maxIterations,
                                        stepSize=args.stepSize, 
                                        beQuiet=args.quiet)
        print(f"[END] Completed descent for {args.maxIterations} iterations. Best loss: {bestLoss}")
        print("[PLOT] Plotting the result, post optimization along with loss values...")
        problem.visualize(optimizedWeights)
        # print("[PLOT] Plotting the loss values...")
        # problem.visualizeLoss()

if __name__=='__main__':
    main()