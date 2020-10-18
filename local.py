"""
    Implementations of local search functions for a generalized problem containing following functions -
    --------
        problem.getObjValue()
        problem.getNeighbours()
        problem.getRandomNeighbour()
        problem.isBetter()
"""


# ------- Deterministic Algorithms ------- #

def hillClimbingSearch_S(problem, state):
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

    currentState = state
    while True:
        neighbours = problem.getNeighbours(currentState)
        runningBest = currentState
        for n in neighbours:
            nObjVal = problem.getObjValue(n)
            runningBestVal = problem.getObjValue(runningBest)
            if problem.isBetter(nObjVal, runningBestVal):
                runningBest = n
        if runningBest is currentState:
            # no neighbour is better, optimum reached
            return currentState
        else:
            # jump to best neighbour
            currentState = runningBest


def tabuSearch(problem, state, tabuSize=32, maxSteps=-1):
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

    currentState = state
    tabuList = list()
    tabuList.add(currentState)
    steps = 0
    while maxSteps = -1 or steps<maxSteps:
        runningBest = currentState
        neighbours = problem.getNeighbours(currentState)
        for n in neighbours:
            runningBestVal = problem.getObjValue(runningBest)
            nObjVal = problem.getObjValue(n)
            if n not in tabuList and \
                problem.isBetter(nObjVal, runningBestVal):
                runningBest = n
        
        if bestNeighbour:
            tabuList.append(bestNeighbour)
            if len(tabuList) > tabuSize:
                tabuList.pop(0)
            currentState = bestNeighbour
            steps+=1
        else:
            print(f"{steps} completed. Nowhere else to go.")
            return currentState
    return currentState


# ------- Stochastic Algorithms ------- #

def hillClimbingSearch_FC(problem, state, maxTrials=100):
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

    currentState = state
    while True:
        currentObjVal = problem.getObjValue(currentState)
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
        else:
            # trials exhausted, no better neighbour found
            print(f"Even after {maxTrials} trials too, couldn't find a better neighbour for {problem.getInfo(currentState)} ")
            return currentState


def hillClimbingStep_RR(problem, state, p=0.1, maxSteps=10_000):
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
    currentState = state
    steps = 0
    bestYet = currentState
    while steps<maxSteps:
        currentObjVal = problem.getObjValue(currentState)
        if random.random()>p:
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
        else:
            # do a random restart
            currentState = problem.getRandomState()
    # after running out of steps, return the best yet state
    return bestYet


def simulatedAnnealing(problem, state, schedule):
    """
        `'Random-Restart Hill Climbing'`

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
    
    currentState = state
    for i in range(len(schedule)):
        temperature = schedule[i]
        if temperature = 0:
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

def geneticAlgorithm(problem, state):
    #TODO
    pass