"""
    Implementations of local search functions for a generalized problem containing following functions -
    --------
        problem.getObjValue()
        problem.getNeighbours()
        problem.getRandomNeighbour()
        problem.isBetter()
        problem.getRandomState()
"""


# ------- Deterministic Algorithms ------- #

def hillClimbingSearch_S(problem):
    """
        `'Steepest Direction Hill Climbing'`

        Inputs:
        -------
        `problem`
            A problem class with required functions
        `state`
            The state at which the problem is right now
        
        Output:
        -------
        `state`
            The state returned after Steepest Hill Climbing
    """

    currentState = problem.state
    problem.visualize(currentState)
    steps=0
    while True:
        if problem.isGlobalOptimum(currentState):
            return steps, currentState
        neighbours = problem.getNeighbours(currentState)
        runningBest = currentState
        for n in neighbours:
            nObjVal = problem.getObjValue(n)
            runningBestVal = problem.getObjValue(runningBest)
            if problem.isBetter(nObjVal, runningBestVal):
                runningBest = n

        if runningBest is currentState:
            # no neighbour is better, optimum reached
            return steps, currentState
        else:
            # jump to best neighbour
            currentState = runningBest
            input("Press enter to continue ")
            steps+=1
            problem.visualize(currentState)

def tabuSearch(problem, tabuSize=32, maxSteps=-1):
    """
        `'Tabu Search'`

        Inputs:
        -------
        `problem`
            A problem class with required functions
        `state`
            The state at which the problem is right now
        `tabuSize` (optional)
            Number of elements to be remembered in the Tabu Tenure
        `maxSteps` (optional)
            Maximum number of steps allowed. Default: -1 means keep going till an optimum.
        
        Output:
        -------
        `state`
            The state returned after Tabu Search
    """

    currentState = problem.state
    problem.visualize(currentState)
    tabuList = list()
    tabuList.append(currentState)
    steps = 0
    while maxSteps == -1 or steps<maxSteps:
        runningBest = currentState
        if problem.isGlobalOptimum(currentState):
            return steps, currentState
        neighbours = problem.getNeighbours(currentState)
        for n in neighbours:
            runningBestVal = problem.getObjValue(runningBest)
            nObjVal = problem.getObjValue(n)
            if n not in tabuList and \
                problem.isBetter(nObjVal, runningBestVal):
                runningBest = n
        
        if runningBest!=currentState:
            # better neighbour found

            # add it to the tabu list
            tabuList.append(runningBest)
            if len(tabuList) > tabuSize:
                # if tabu list size exceeds, pop the oldest element
                tabuList.pop(0)
            
            # make the jump to the better neighbour
            currentState = runningBest
            input("Press enter to continue ")
            steps+=1
            problem.visualize(currentState)
        else:
            # no better neighbour
            return steps, currentState
    return steps, currentState


# ------- Stochastic Algorithms ------- #

def hillClimbingSearch_FC(problem, maxTrials=100):
    """
        `'First-Choice Hill Climbing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
        `state`
            The state at which the problem is right now
        `maxTrials` (optional)
            Number of random neighbours to try before giving up.
        
        Output
        ------
        `state`
            The state returned after First-Choice Hill Climbing
    """


    currentState = problem.state
    problem.visualize(currentState)
    steps = 0
    while True:
        currentObjVal = problem.getObjValue(currentState)
        if problem.isGlobalOptimum(currentState):
            return steps, currentState
        trials = 0
        betterState = None
        while trials < maxTrials:
            neighbour = problem.getRandomNeighbour(currentState)
            nObjVal = problem.getObjValue(neighbour)
            if problem.isBetter(nObjVal, currentObjVal):
                betterState = neighbour
                break
            trials+=1
        if betterState:
            # jump to neighbour better than current state
            currentState = betterState
            input("Press enter to continue ")
            steps+=1
            problem.visualize(currentState)
        else:
            print(f"{maxTrials} trials for random neighbours exhausted. No better neighbour found.")
            return steps, currentState


def hillClimbingSearch_RR(problem, p=0.1, maxSteps=10_000):
    """
        `'Random-Restart Hill Climbing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
        `state`
            The state at which the problem is right now
        `p` (optional)
            The probability of random restart
        `maxSteps` (optional)
            Maximum number of steps allowed. Default = 10,000
        
        Output
        ------
        `state`
            The state returned after Random-Restart Hill Climbing
    """

    import random
    currentState = problem.state
    problem.visualize(currentState)
    steps = 0
    restarts=0
    bestYet = currentState
    while steps<maxSteps:
        currentObjVal = problem.getObjValue(currentState)
        if problem.isGlobalOptimum(currentState):
            print(f"\nTotal random restarts done: {restarts}.")
            return steps, currentState
        if random.random()>=p:
            # make a greedy step
            neighbours = problem.getNeighbours(currentState)
            runningBest = currentState
            for n in neighbours:
                nObjVal = problem.getObjValue(n)
                runningBestVal = problem.getObjValue(runningBest)
                if problem.isBetter(nObjVal, runningBestVal):
                    runningBest = n
            if runningBest is currentState:
                # no neighbour is better, check against the bestYet
                runningBestVal = problem.getObjValue(runningBest)
                bestYetVal = problem.getObjValue(bestYet)
                if problem.isBetter(runningBestVal, bestYetVal):
                    bestYet = runningBest
            else:
                # jump to best neighbour
                currentState = runningBest
                input("Press enter to continue ")
                print("Greedy step taken.")
                problem.visualize(currentState)
                steps+=1
        else:
            # do a random restart
            currentState = problem.getRandomState()
            input("Press enter to continue ")
            print("Random restart done.")
            problem.visualize(currentState)
            restarts+=1
            steps+=1
    # after running out of steps, return the best yet state
    print(f"\nTotal random restarts done: {restarts}.")
    return steps, bestYet


def simulatedAnnealing(problem, schedule):
    """
        `'Simulated Annealing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
        `state`
            The state at which the problem is right now
        `schedule`
            The schedule according to which temperature varies.
        
        Output
        ------
        `state`
            The state returned after Simulated Annealing
    """
    
    import random
    from math import exp
    
    currentState = problem.state
    for i in range(len(schedule)):
        temperature = schedule[i]
        if temperature == 0:
            return currentState
        neighbour = problem.getRandomNeighbour(currentState)
        changeInObj = problem.getObjValue(neighbour) - \
                        problem.getObjValue(currentState)
        if changeInObj > 0:
            # if the neighbour is better, jump
            currentState = neighbour
        else:
            # if the neighbour is worse, jump with some probability
            if exp(changeInObj/temperature) >= random.random():
                currentState = neighbour
    return currentState




#--------------Continuous Worlds----------------#
import math

def gradDescent(problem, maxIterations=5000, stepSize=0.1):

    currentWeights = problem.weights
    loss = problem.getObjValue(currentWeights)
    bestLoss = loss
    # for visualization
    problem.losses.append(loss)
    lossSchedule = []
    lossSchedule.append(loss)
    i=0
    print(f"Iter:[{i}/{maxIterations}]\tLoss: {problem.getObjValue(currentWeights)} StepSize was {stepSize}")    
    while i < maxIterations:
        derivatives = problem.getDerivatives(currentWeights)
        currentWeights = problem.updateWeights(currentWeights, derivatives, stepSize)
        i+=1
        loss = problem.getObjValue(currentWeights)
        lossSchedule.append(loss)
        problem.losses.append(loss)
        if loss < bestLoss:
            bestWeights = currentWeights
            bestLoss = loss
        if len(lossSchedule)>5:
            lossSchedule.pop(0)
        if lossSchedule[-1] > lossSchedule[-2]:
            stepSize /= 10
        # if len(lossSchedule)==5:
        #     if abs(lossSchedule[0] - lossSchedule[4]) < 2:
        #         stepSize = math.fsum([stepSize, 0.002])
        
        # if i%100==0:
        #     stepSize /= 
        print(f"Iter:[{i}/{maxIterations}]\tLoss: {loss}  StepSize was {stepSize}")


    return bestWeights

# def stochasticLocalBeamSearch(problem, k=10):
#     initStates = set()
#     while len(initStates) < 10:
#         while True:
#             genState = problem.getRandomState()
#             if genState in initStates:
#                 continue
#             else:
#                 initStates.add(genState)
#                 break
#     for state in initStates:
#         neighbours = 

# def geneticAlgorithm(population, state, p=0.01):
#     import random
#     while Time is left or We get a superfit person:
#         new_population = set()
#         weights = [problem.getObjValue(element) for element in population]
#         for i in range(len(population)):
#             x = random.choice(population, weights=weights)
#             y = random.choice(population, weights=weights)
#             offSpring = Reproduce(x, y)
#             # if random.random() < p:
#             #     offSpring = Mutate(offSpring)
#             new_population.add(offSpring)
#         population.append(list(new_population))
    
#     # return the best in the current population
#     for element in population:
