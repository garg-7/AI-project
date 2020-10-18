"""
    Contains implementations of local search functions
    for a generalized problem containing following functions -
    problem.getObjectiveFnValue()
    problem.getNeighbours()
    problem.getStartState()
    problem.getRandomNeighbour()
    problem.isBetter()
"""

def hillClimbing_S(problem, state):
    """
        'Steepest Direction Hill Climbing'

        Inputs: 
            problem - A problem class with required functions
            state - The state at which the problem is right now
        Output:
            state - The state returned from Steepest Hill Climbing
    """

    current_state = problem.getStartState()
    current_obj_fn_value = problem.getObjectiveFnValue(current_state)
    while True:
        neighbours = problem.getNeighbours(current_state)
        best_neighbour = None
        for n in neighbours:
            if problem.isBetter(problem.getObjectiveFnValue(n), current_obj_fn_value):
                best_neighbour = n
        if best_neighbour:
            current_state = best_neighbour
        else:
            return current_state

def hillClimbing_FC(problem, state, maxTrials=100):
    """
        'First-Choice Hill Climbing'

        Inputs: 
            problem - A problem class with required functions
            state - The state at which the problem is right now
            maxTrials (optional) - Number of random neighbours to try before giving up
        Output:
            state - The state returned from one step of First-Choice Hill Climbing
    """

    current_state = problem.getStartState()
    current_obj_fn_value = problem.getObjectiveFnValue(current_state)
    while True:
        trials = 0
        while trials < maxTrials:
            neighbour = problem.getRandomNeighbour(current_state)
            obj_fn_val = problem.getObjectiveFnValue(neighbour)
            if problem.isBetter(obj_fn_val, current_obj_fn_value):
                return neighbour
            trials+=1
        print(f"After {maxTrials} trials too, couldn't find a better neighbour for {problem.getInfo(current_state)} ")
    return current_state

def hillClimbingStep_RR(problem, state):
