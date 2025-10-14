---
tags:
  - ds/recursion
date: 2022-01-30
pageorder: 4
---
Recursion is a programming concept where a function calls itself to solve a smaller instance of the same problem.

- Base Case
- Recursion Function

- $ Each recursive function call is stored in the **call stack** (LIFO - Last In, First Out).

### Definition:
> The successive application of a rule or process multiple times to achieve the answer to a large problem.
> A  <u>programming technique</u> where a function calls itself in order to solve a problem.

#### function calls itself
- Variable inside a function and parameters for that function are local
- Local Variable are private, other function cannot touched, even the function calling it.

###### different between iteratively and recursion

| Aspect                | Iteration                                                                         | Recursion                                                                  |
|-----------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Definition            | A process where a set of instructions is repeated using loops (e.g., for, while). | A function that calls itself to solve smaller instances of a problem.      |
| Mechanism             | Uses explicit looping structures.                                                 | Uses function calls and the call stack.                                    |
| Memory Usage          | Generally uses less memory since it avoids ***function call overhead***.          | Uses more memory due to recursive function calls (stack frames).           |
| Performance           | Often more efficient in terms of speed and memory.                                | Can be slower due to repeated function calls and stack operations.         |
| Base Case Requirement | No base case is required. The loop runs until a condition is met.                 | Requires a base case to stop infinite recursion.                           |
| Complexity            | Usually easier to understand for simple loops.                                    | Can be more elegant for problems like tree traversal, but harder to debug. |
### How to solve recursion problem?
###### Point 1: Definition:
- **Input**: understand what data functions to process
- **Output**: return expected value
###### Point 2: Base Case
- The base case, is no future recursion calls:
	- ***Stop*** the recursion
	- usually use `if` condition
	- usually directly return a value
###### Point 3: Decomposition (Recursive Case)
- Decomposition, make the big problem to small problem
- Call the function again with a smaller input (e.g., removing one element from the list).


### Sample
#### Sample1_Factorial
```python
def factorial(n):
	if n == 1: return 1
	return n * factorial(n-1)
print(factorial(3)) # output = 3*2*1 = 6
```

> f(3)= 3 * f2
           |
		2 * f1
	        |
		    1 * f0
![[Pasted image 20250131083335.png|500]]
#### Sample2_Fibonacci
```python
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
return fib(n-1) + fib(n-2)

print(fib(10))
```

0 1 1 2 3 5 8 13 21 34
##### Sample3_for example
```python
def mystery(n):
	if n < 0:
		return 2 * n
	else:
		return mystery(n - 1) + n
```

what's the output to mystery(3)?
>Call 1: mystery(3)
  |
  -> Call 2: mystery(2)
      |
      -> Call 3: mystery(1)
          |
          -> Call 4: mystery(0)
              |
              -> Call 5: mystery(-1)  ← Base case reached

Stark: store the data (from bottom to top)  and left side do stark reverse:"unwinds" (from top to bottom, do`pop`)
>| mystery(-1)  |  n = -1 | Return value: 2 * (-1) |           Return from Call 5: mystery(-1) = -2 Base Case: -2
>| mystery(0)   |  n = 0  | Return to mystery(-1) + 0 |   Return from Call 4: mystery(0) = -2 + 0 = -2
>| mystery(1)   |  n = 1  | Return to mystery(0) + 1 |      Return from Call 3: mystery(1) = -2 + 1 = -1
>| mystery(2)   |  n = 2  | Return to mystery(1) + 2 |     Return from Call 2: mystery(2) = -1 + 2 = 1
>| mystery(3)   |  n = 3  | Return to mystery(2) + 3 |    Return from Call 1: mystery(3) = 1 + 3 = 4
