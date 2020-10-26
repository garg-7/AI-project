# Generalized Local Search Tool
### (Course project for CS323 - AI)

## About the project:
This project is about local search algorithms like various variants of **Hill Climbing**, **Simulated Annealing**, **Gradient Descent** etc. The implementations have been done in a general manner and hence can be employed for **any kind of generalized problem** that can provide the required functions. Also, two exempler problems, one in the discrete domain - N-Queens and one in the continuous domain - Real Estate Price prediction (by Gradient descent) have been included.

## Environment:
The only dependencies are matplotlib and numpy for plotting results. You could install these via pip:  
`python -m pip install matplotlib`  
`python -m pip install numpy`

## Part A - Discrete Domain:
This is the major focus of this project. A total of five local search algorithms have been implemented. The first 2 are deterministic and the final 3 are stochastic in nature.  
_(Tests can be done for the N-Queens problem that is included.)_  

To run the algorithms for discrete domain, pass 'discrete' as the domain argument as follows:  
```bash
python main.py -d discrete
```  
_(By default, this would run steepest hill climbing on a randomly initialized 8-queens problem)_  

- You can specify the **number of queens** for the N-Queens problem by passing the -q argument:  
```bash
python main.py -d discrete -q 4
```  
_(This would run steepest hill climbing on a randomly-initialized 4-queens problem)_  

- You can provide an **initialization** yourself.  
E.g. [2,3,1,4] for a 4-Queens problem, where every i-th element of the list represents the row number in which the queen of the i-th column in present. (Note that the user works with 1-indexing which is more natural.)  
```bash
python main.py -d discrete -q 4 -i [2,3,1,4]
```  
_This would run steepest hill climbing on a 4-queens problem initialized as 2,3,1,4._  
_Note that you need to provide a correct initialization. Any incomplete initialization or one with impossible indices like 7 for a 4-queens problem will raise an exception._  

- You can also keep the algorithms **interactive** in the sense that you can study every step and the next step would be taken only when you want. For this, simply pass the `-u` flag.  
```bash
python main.py -d discrete -q 4 -u
```  
_This would run steepest hill climbing on a randomly-initialized 4-queens problem where you need to press enter before it takes a step._

In all the above cases the algorithm wasn't specified and by default steepest hill climbing was run. To run other algorithms you need to specify the algorithm and parameters for it (if any) with the help of the flags mentioned below.  
_To keep it simple, I haven't mentioned specification of number of queens or manual user initialization but just keep in mind that you could do that for any of the algorithms below._  

### 1. Hill Climbing - Steepest [HC_S]
A deterministic algorithm. This is the default when running discrete algorithms, but you could run it by passing the the `-da` (**d**iscrete**a**lgorithm) argument:  
```bash
python main.py -d discrete -da HC_S
```  
### 2. Tabu Seach [TS]
A deterministic algorithm.  
`-tt`:the size of the tabu tenure (or tabu list) (default: 32)  
`-s` :the max number of steps to run the search for (default: -1 i.e. keep going till optimum).  

```bash
python main.py -d discrete -da TS -tt 8 -s 100
```  
_This will run tabu search with tabu list size of 8 and for a max of 100 steps._
### 3. Hill Climbing - First-Choice [HC_FC]
A stochastic algorithm.  
`-mt`:the maximum number of random neighbours to try before declaring optimum. (default: 100)  

```bash
python main.py -d discrete -da HC_FC -mt 500
```  
_This will run first-choice hill climbing. If 500 random neighbours are tried and still no better neighbour is found, it will declare optimum._
### 4. Hill Climbing - Random Restarts [HC_RR]
A stochastic algorithm.  
`-p` :probability of random restart (default: 0.1)  
`-s` :the max number of steps to run the search for (default: 1000)  

```bash
python main.py -d discrete -da HC_RR -p 0.2 -s 300
```  
_This will run random-restart hill climbing with the probability of random restart being 0.2. The max number of steps taken if optimum isn't found is 300._
### 5. Simulated Annealing [SA]
A stochastic algorithm. To run it, one can optionally specify 1 paramter -  
`-s` :the max number of steps to run the search for (default: 1000)  

```bash
python main.py -d discrete -da SA -s 300
```  
_This will run simulated annealing. The max number of steps taken if optimum isn't found is 300._  
NOTE: The schedule that has been considered here, is:  
``temperature = 100*min(1, 1-stepsDone/maxSteps)``
## Part B - Continuous Domain:
For the sake of completeness, one local search algorithm for problems in the continuous domain has been added i.e. Gradient Descent.

### 1) Gradient Descent

## Further Extensions:


## References: