"""
    Contains problems for which local search is to be done.
"""

import random
import copy
import matplotlib.pyplot as plt
import numpy as np

class nQueensProblem:
    def __init__(self, n, colArrangement):
        self.n = n
        if colArrangement:
            self.state = colArrangement
        else:
            self.state = self.getRandomState()
        
        # for visualization
        self.hVals = []

    def getNeighbours(self, state):
        neighbours = []
        for i in range(self.n):
            for j in range(self.n):
                temp = copy.copy(state)
                if j!=state[i]:
                    temp[i] = j
                    neighbours.append(temp)
        return neighbours

    def getObjValue(self, state):
        hVal = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if state[i]==state[j]:
                    hVal+=1
                elif j-i==abs(state[i]-state[j]):
                    hVal+=1
        return hVal

    def getRandomNeighbour(self, state):
        # select a column randomly
        # make a move +1 or -1, randomly
        randomNeighbour = copy.copy(state)
        colToChange = random.sample(range(self.n), 1)[0]
        newRow = state[colToChange]
        while newRow is state[colToChange]:
            newRow = random.sample(range(self.n), 1)[0]
        randomNeighbour[colToChange] = newRow
        return randomNeighbour

    def getRandomState(self):
        # random arrangement of queens in all columns
        state = list(range(self.n))
        random.shuffle(state)
        return state

    def isBetter(self, val1, val2):
        # Here lower is better
        # Lower i.e. less number of attacking queens
        return val1<val2
    
    def isGlobalOptimum(self, state):
        val = self.getObjValue(state)
        return val==0

    def visualize(self, state):
        # import tkinter as tk
        # window = tk.Tk()
        # for i in range(self.n):
        #     for j in range(self.n):
        #         frame = tk.Frame(
        #             master=window,
        #             relief=tk.RAISED,
        #             borderwidth=1
        #         )
        #         frame.grid(row=i, column=j)
        #         if self.state[j]==i:
        #             text = 'X'
        #         else:
        #             text = ' '
        #         label = tk.Label(master=frame, text=text)
        #         label.pack()
        
        # window.mainloop()
        
        print()

        for i in range(self.n):
            for j in range(self.n):
                if state[j]==i:
                    text = 'X'
                else:
                    text = '_'
                print(text,end=" ")
            if i==self.n-1:
                print(f" : hVal = {self.getObjValue(state)}")
            print()

        print()
        return
    
    def visualizeLandscape(self):
        plt.plot(list(range(len(self.hVals))), self.hVals)
        plt.grid()
        plt.xlabel("Step number")
        plt.ylabel("Objective function value")
        print("Close the plot window to continue")
        plt.show()



class propertyProblem:
    def __init__(self, priceList, degree=1, stepSize=0.1):
        self.listings = priceList
        # create the required polynomial
        self.polynomial = []
        for d in range(degree+1):
            self.polynomial.append(0)
        # step size for the descent
        # self.stepSize = stepSize
        self.weights = copy.copy(self.polynomial)
        self.losses = []

    def getObjValue(self, weights):
        cumCost = 0
        for (x, y_true) in self.listings:
            y_predicted = self.getPrediction(weights, x)
            cumCost += (y_true - y_predicted)**2
        cumCost /= len(self.listings)
        return cumCost

    def getPrediction(self, weights, x):
        y_predicted = 0
        for i in range(len(weights)):
            y_predicted += weights[i]*(x**i)
        return y_predicted

    def getDerivatives(self, weights):
        # specific for 2 variable problem
        derivatives = [0, 0]
        for (x, y_true) in self.listings:
            y_predicted = self.getPrediction(weights, x)
            derivatives[0]+=2*(y_predicted - y_true)
            derivatives[1]+=2*(y_predicted - y_true)*x
        
        derivatives[0] /= len(self.listings)
        derivatives[1] /= len(self.listings)

        return derivatives

    def updateWeights(self, weights, derivatives, stepSize):
        newWeights = weights.copy()
        for i in range(len(weights)):
            newWeights[i] -= (stepSize * derivatives[i])
        return newWeights


    def visualize(self, weights):
        # plot the data and plot the prediction
        plt.subplot(1,2,1)
        plt.scatter([x for x,_ in self.listings], [y for _,y in self.listings])
        x = np.linspace(0, max(x for x,_ in self.listings)+5,50)
        y = weights[0] + weights[1]*x
        plt.plot(x, y, label='Optimized weights')
        plt.grid()
        plt.xlabel("Property Sizes (in sq. kms)")
        plt.ylabel("Property Costs (in million dollars)")

        plt.subplot(1,2,2)
        plt.plot(list(range(len(self.losses)))[100:], self.losses[100:])
        plt.grid()
        plt.xlabel("Number of Iterations")
        plt.ylabel("Loss Value")

        print("Close the plot window to continue")
        plt.show()
    
    # def visualizeLoss(self):
    #     # plt.scatter(list(range(len(self.losses)))[100:], self.losses[100:])
    #     plt.plot(list(range(len(self.losses)))[100:], self.losses[100:])
    #     plt.grid()
    #     plt.xlabel("Number of Iterations")
    #     plt.ylabel("Loss Value")
    #     print("Close the plot window to continue")
    #     plt.show()