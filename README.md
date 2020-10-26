# Generalized Local Search Tool
### (Course project for CS323 - AI)

## About the project:
This project is about local search algorithms like various variants of **Hill Climbing**, **Simulated Annealing**, **Gradient Descent** etc. The implementations have been done in a general manner and hence can be employed for **any kind of generalized problem** that can provide the required functions. Also, two exempler problems, one in the discrete domain - N-Queens and one in the continuous domain - Real Estate Price prediction (by Gradient descent) have been included.

## Dependencies:
The only dependencies are matplotlib and numpy for plotting results. You could install these via pip:  
`python -m pip install matplotlib`  
`python -m pip install numpy`

## Part A - Discrete Domain:
This is the major focus of this project. A total of five local search algorithms have been implemented. The first 2 are deterministic and the final 3 are stochastic in nature.  
_(Tests can be done for the N-Queens problem that is included.)_  
  

To run the algorithms for discrete domain, pass `discrete` as the domain argument as follows:  
```bash
python main.py -d discrete
```  
_(By default, this would run steepest hill climbing on a randomly initialized 8-queens problem)_  
  

- You can specify the **number of queens** for the N-Queens problem by passing the -q argument:  
```bash
python main.py -d discrete -q 4
```  
_(This would run steepest hill climbing on a randomly-initialized 4-queens problem)_  

- You can provide an **initialization** yourself using the `-i` flag.  
E.g. [2,3,1,4] for a 4-Queens problem, where i-th element of the list represents the row number in which the queen of the i-th column in present. (Note that the numbers are 1-indexed.)  
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
  
In all the above cases the algorithm wasn't specified and by default steepest hill climbing was run. To run other algorithms you need to **specify the algorithm and OPTIONAL parameters** for it (if any) with the help of the flags mentioned below.  
_(To keep it simple, I haven't mentioned specification of number of queens or manual user initialization but just keep in mind that you could do that for any of the algorithms below.)_  

### 1. Hill Climbing - Steepest [HC_S]
A deterministic algorithm. This is the default when running discrete algorithms, but you could run it by passing the the `-da` (**d**iscrete**a**lgorithm) argument:  
```bash
python main.py -d discrete -da HC_S
```  
### 2. Tabu Seach [TS]
A deterministic algorithm.  
`-tt`: the size of the tabu tenure (or tabu list) (default: 32)  
`-s` : the max number of steps to run the search for (default: -1 i.e. keep going till optimum).  

```bash
python main.py -d discrete -da TS -tt 8 -s 100
```  
_This will run tabu search with tabu list size of 8 and for a max of 100 steps._
### 3. Hill Climbing - First-Choice [HC_FC]
A stochastic algorithm.  
`-mt`: the maximum number of random neighbours to try before declaring optimum. (default: 100)  

```bash
python main.py -d discrete -da HC_FC -mt 500
```  
_This will run first-choice hill climbing. If 500 random neighbours are tried and still no better neighbour is found, it will declare optimum._
### 4. Hill Climbing - Random Restarts [HC_RR]
A stochastic algorithm.  
`-p` : probability of random restart (default: 0.1)  
`-s` : the max number of steps to run the search for (default: 1000)  

```bash
python main.py -d discrete -da HC_RR -p 0.2 -s 300
```  
_This will run random-restart hill climbing with the probability of random restart being 0.2. The max number of steps taken if optimum isn't found is 300._
### 5. Simulated Annealing [SA]
A stochastic algorithm.  
`-s` :the max number of steps to run the search for (default: 1000)  

```bash
python main.py -d discrete -da SA -s 300
```  
_This will run simulated annealing. The max number of steps taken if optimum isn't found is 300._  
NOTE: The schedule that has been considered here, is:  
``temperature = 100*min(1, 1-stepsDone/maxSteps)``
## Part B - Continuous Domain:
For the sake of completeness, one local search algorithm for problems in the continuous domain has been added which is Batch Gradient Descent.  
_(The exemplar problem here is that of real estate price prediction based on a given trend.)_  
  
To run the algorithm(s) for continuous domain, pass `continuous` as the domain argument as follows:
```bash
python main.py -d continuous
```  
_(By default this would run gradient descent for the data present in `listings.txt`)_  

### 1. Batch Gradient Descent [BGD]
A deterministic algorithm.  
`-f`  : path of the file containing listing prices (default: ./listings.txt)  
`-ss` : step size factor to begin with (default: 0.1)  
`-itr`: number of iterations to run gradient descent for (default: 5000)  

```bash
python main.py -d continuous -ca BGD -f houses.txt -ss 0.5 -itr 1000
```  
_This will run batch gradient descent. Data points given will be taken from the file `houses.txt`. Descent will begin with a step size of 0.5 and will run for 1000 iterations._  
NOTE: Here, we are basically trying to fit a line over the data points given. Optimization is happening w.r.t. the paramters of the line i.e. slope and intercept. The greedy step being taken is in the direction specified by the partial derivatives.

### NOTE:
Don't sweat over rememebering the above flags. You could get what these mean by simply passing the `--help` (or `-h`) flag:  
```bash
python main.py -h
```   
## Further Extensions:
- Further, more exemplar problems for constraint satisfaction in the discrete case and for value prediction in the continuous case are to be added.  
- Other discrete algorithms that can be looked into: Genetic Algorithms, Local Beam Search variants.
- Other continuous algorithms that can be looked into: variants of gradient descent like Stochastic Gradient Descent. 

## References:
- This project is based on local search algorithms as discussed in `Artifical Intelligence - A Modern Approach (3rd Ed.) by Russell and Norvig`.
- Help has been taken from wikipedia pages of the above search algorithms.