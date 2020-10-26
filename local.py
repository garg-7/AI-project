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

def hillClimbingSearch_S(problem, userInteraction):
    """
        `'Steepest Direction Hill Climbing'`

        Inputs:
        -------
        `problem`
            A problem class with required functions
        
        Output:
        -------
        `state`
            The state returned after Steepest Hill Climbing
    """

    currentState = problem.state
    problem.visualize(currentState)

    # for visualization
    problem.hVals.append(problem.getObjValue(currentState))
    
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

            # for visualization later on
            problem.hVals.append(problem.getObjValue(currentState))
            
            if userInteraction:
                input("Press enter to continue ")
            steps+=1
            problem.visualize(currentState)

def tabuSearch(problem, tabuSize, maxSteps, userInteraction):
    """
        `'Tabu Search'`

        Inputs:
        -------
        `problem`
            A problem class with required functions
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

    # for visualization
    problem.hVals.append(problem.getObjValue(currentState))

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
            
            # for visualization later on
            problem.hVals.append(problem.getObjValue(currentState))
            
            if userInteraction:
                input("Press enter to continue ")
            steps+=1
            problem.visualize(currentState)
        else:
            # no better neighbour
            return steps, currentState
    return steps, currentState


# ------- Stochastic Algorithms ------- #

def hillClimbingSearch_FC(problem, maxTrials, userInteraction):
    """
        `'First-Choice Hill Climbing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
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

    # for visualization
    problem.hVals.append(problem.getObjValue(currentState))
    
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
            if userInteraction:
                input("Press enter to continue ")
            # jump to neighbour better than current state
            currentState = betterState
            
            # for visualization later on
            problem.hVals.append(problem.getObjValue(currentState))
            
            steps+=1
            problem.visualize(currentState)
        else:
            print(f"{maxTrials} trials for random neighbours exhausted. No better neighbour found.")
            return steps, currentState


def hillClimbingSearch_RR(problem, p, maxSteps, userInteraction):
    """
        `'Random-Restart Hill Climbing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
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

    # for visualization
    problem.hVals.append(problem.getObjValue(currentState))

    while steps<maxSteps:
        if problem.isGlobalOptimum(currentState):
            print(f"\nTotal random restarts done: {restarts}.")
            return steps, bestYet
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
                if userInteraction:
                    input("Press enter to continue ")
                currentState = runningBest

                # for visualization later on
                problem.hVals.append(problem.getObjValue(currentState))
                
                print("Greedy step taken.")
                problem.visualize(currentState)
                currentVal = problem.getObjValue(currentState)
                bestYetVal = problem.getObjValue(bestYet)
                if problem.isBetter(currentVal, bestYetVal):
                    bestYet = currentState
                steps+=1
        else:
            # do a random restart
            if userInteraction:
                input("Press enter to continue ")
            currentState = problem.getRandomState()
            
            # for visualization later on
            problem.hVals.append(problem.getObjValue(currentState))
            
            print("Random restart done.")
            problem.visualize(currentState)
            
            currentVal = problem.getObjValue(currentState)
            bestYetVal = problem.getObjValue(bestYet)
            if problem.isBetter(currentVal, bestYetVal):
                bestYet = currentState
            
            restarts+=1
            steps+=1
    # after running out of steps, return the best yet state
    print(f"\n[INFO] Total number of random restarts done: {restarts}.")
    return steps, bestYet

def tempSchedule(steps, maxSteps):
    ''' Returns the temperature depending on how many steps have been taken'''
    temperature = 100*min(1, 1 - float(steps)/maxSteps)
    return temperature


def simulatedAnnealing(problem, maxSteps, userInteraction):
    """
        `'Simulated Annealing'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
        `maxSteps`
            The number of steps according to which the temperature schedule is created.
        
        Output
        ------
        `state`
            The state returned after Simulated Annealing
    """

    import random
    from math import exp

    currentState = problem.state
    steps = 0
    bestYet = currentState
    # for visualization
    problem.hVals.append(problem.getObjValue(currentState))

    while steps<maxSteps:
        if problem.isGlobalOptimum(currentState):
            return steps, bestYet
        temperature = tempSchedule(steps, maxSteps)
        # print(temperature)
        if temperature == 0:
            return currentState
        neighbour = problem.getRandomNeighbour(currentState)
        changeInObj = problem.getObjValue(neighbour) - \
                        problem.getObjValue(currentState)
        if changeInObj > 0:
            # if the neighbour is better, jump
            if userInteraction:
                input("Press enter to continue ")
            currentState = neighbour
            print("Greedy step taken.")
            problem.visualize(currentState)
            steps+=1

            currentVal = problem.getObjValue(currentState)
            bestYetVal = problem.getObjValue(bestYet)
            if problem.isBetter(currentVal, bestYetVal):
                bestYet = currentState

            # for visualization later on
            problem.hVals.append(problem.getObjValue(currentState))

        else:
            # if the neighbour is worse, jump with some probability
            if exp(changeInObj/temperature) >= random.random():
                if userInteraction:
                    input("Press enter to continue ")
                currentState = neighbour
                print("Step in a worse direction taken.")
                problem.visualize(currentState)
                steps+=1

                currentVal = problem.getObjValue(currentState)
                bestYetVal = problem.getObjValue(bestYet)
                if problem.isBetter(currentVal, bestYetVal):
                    bestYet = currentState

                # for visualization later on
                problem.hVals.append(problem.getObjValue(currentState))
    return steps, bestYet




#--------------Continuous Domain----------------#
import math

def gradDescent(problem, maxIterations, stepSize):
    '''
        `'Batch Gradient Descent'`

        Inputs
        ------ 
        `problem`
            A problem class with required functions
        `maxIterations`
            The number of iterations to run gradient descent for
        `stepSize`
            The stepSize factor to begin gradient descent with
        
        Output
        ------
        `bestWeights`
            The optimized weights obtained using gradient descent

    '''
    currentWeights = problem.weights
    loss = problem.getObjValue(currentWeights)
    bestLoss = loss
    
    # for visualization
    problem.losses.append(loss)
    
    # mantain a list of last five loss values to be able to modify
    # the stepSize if descent is going very slowly or very quickly
    lossSchedule = []
    lossSchedule.append(loss)
    
    i=0
    print(f"Iter:[{i}/{maxIterations}]\tLoss: {problem.getObjValue(currentWeights)}")    
    while i < maxIterations:

        # get partial derivatives of the loss w.r.t. the weights
        derivatives = problem.getDerivatives(currentWeights)

        # update the values of the weights
        currentWeights = problem.updateWeights(currentWeights, derivatives, stepSize)
        
        i+=1
        loss = problem.getObjValue(currentWeights)
        lossSchedule.append(loss)
        
        # for visualization
        problem.losses.append(loss)
        
        if loss < bestLoss:
            # if the loss is the lowest yet
            bestWeights = currentWeights
            bestLoss = loss
        
        if len(lossSchedule)>5:
            # if size of loss schedule exceeds 5, remove the oldest loss value
            lossSchedule.pop(0)
        
        if lossSchedule[-1] > lossSchedule[-2]:
            # if the loss is increasing reduce the step size factor by 10
            stepSize /= 10
            print("Step size factor was reduced to 1/10th")

        print(f"Iter:[{i}/{maxIterations}]\t\tLoss: {loss}")

    return bestWeights


# ---------------- END for now --------------------- #

# TODO: add the functions below

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


# def stochasticGradientDescent(problem, ):
