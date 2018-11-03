---
redirect_from:
  - "/chapters/09/2/iteration"
interact_link: content/chapters/09/2/Iteration.ipynb
title: 'Iteration'
prev_page:
  url: /chapters/09/1/Conditional_Statements
  title: 'Conditional Statements'
next_page:
  url: /chapters/09/3/Simulation
  title: 'Simulation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Iteration
It is often the case in programming – especially when dealing with randomness – that we want to repeat a process multiple times. For example, we might want to assign each person in a study to the treatment group or to control, based on tossing a coin. We can do this without actually tossing a coin for each person; we can just use `np.random.choice` instead.

Here is a reminder of how `np.random.choice` works. Run the cell a few times to see how the output changes.



{:.input_area}
```python
np.random.choice(make_array('Heads', 'Tails'))
```





{:.output_data_text}
```
'Heads'
```



To come up with Heads or Tails for each individual in our study, we could copy-paste the code multiple times, but that's tedious and prone to typos, and if we wanted to do it a thousand times or a million times, forget it.  

A more automated solution is to use a `for` statement to loop over the contents of a sequence. This is called *iteration*. A `for` statement begins with the word `for`, followed by a name we want to give each item in the sequence, followed by the word `in`, and ending with an expression that evaluates to a sequence. The indented body of the `for` statement is executed once *for each item in that sequence*.



{:.input_area}
```python
for i in np.arange(3):
    print(i)
```


{:.output_stream}
```
0
1
2

```

It is instructive to imagine code that exactly replicates a `for` statement without the `for` statement.  This is called *unrolling* the loop.  

A `for` statement simple replicates the code inside it, but before each iteration, it assigns a new value from the given sequence to the name we chose.  For example, here is an unrolled version of the loop above:



{:.input_area}
```python
i = np.arange(3).item(0)
print(i)
i = np.arange(3).item(1)
print(i)
i = np.arange(3).item(2)
print(i)
```


{:.output_stream}
```
0
1
2

```

Notice that the name `i` is arbitrary, just like any name we assign with `=`.

Here we use a `for` statement in a more realistic way: we print 5 random choices from `coin`, thus *simulating* the results five tosses of a coin. We use the word *simulating* to remind ourselves that we are not physically tossing coins but using Python to mimic the process.



{:.input_area}
```python
coin = make_array('Heads', 'Tails')

for i in np.arange(5):
    print(np.random.choice(coin))
```


{:.output_stream}
```
Heads
Heads
Heads
Tails
Heads

```

In this case, we simply perform exactly the same (random) action several times, so the code inside our `for` statement does not actually refer to `i`.

### Augmenting Arrays

While the `for` statement above does simulate the results of five tosses of a coin, the results are simply printed and aren't in a form that we can use for computation. Thus a typical use of a `for` statement is to create an array of results, by augmenting it each time.

The `append` method in `numpy` helps us do this. The call `np.append(array_name, value)` evaluates to a new array that is `array_name` augmented by `value`. When you use `append`, keep in mind that all the entries of an array must have the same type.



{:.input_area}
```python
pets = make_array('Cat', 'Dog')
np.append(pets, 'Another Pet')
```





{:.output_data_text}
```
array(['Cat', 'Dog', 'Another Pet'], dtype='<U11')
```



This keeps the array `pets` unchanged:



{:.input_area}
```python
pets
```





{:.output_data_text}
```
array(['Cat', 'Dog'], dtype='<U3')
```



But often while using `for` loops it will be convenient to mutate an array – that is, change it – when augmenting it. This is done by assigning the augmented array to the same name as the original.



{:.input_area}
```python
pets = np.append(pets, 'Another Pet')
pets
```





{:.output_data_text}
```
array(['Cat', 'Dog', 'Another Pet'], dtype='<U11')
```



### Example: Counting the Number of Heads

We can now simulate five tosses of a coin and place the results into an array. We will start by creating an empty array and then appending the outcome of each toss. Notice that the body of the `for` loop contains two statements. Both statements are executed for each value in the given sequence `np.arange(5)`.



{:.input_area}
```python
coin = make_array('Heads', 'Tails')

outcomes = make_array()

for i in np.arange(5):
    outcome_of_toss = np.random.choice(coin)
    outcomes = np.append(outcomes, outcome_of_toss)
    
outcomes
```





{:.output_data_text}
```
array(['Tails', 'Tails', 'Tails', 'Heads', 'Tails'], dtype='<U32')
```



Let us rewrite the cell with the `for` statement unrolled:



{:.input_area}
```python
coin = make_array('Heads', 'Tails')

outcomes = make_array()

i = np.arange(5).item(0)
outcome_of_toss = np.random.choice(coin)
outcomes = np.append(outcomes, outcome_of_toss)

i = np.arange(5).item(1)
outcome_of_toss = np.random.choice(coin)
outcomes = np.append(outcomes, outcome_of_toss)

i = np.arange(5).item(2)
outcome_of_toss = np.random.choice(coin)
outcomes = np.append(outcomes, outcome_of_toss)

i = np.arange(5).item(3)
outcome_of_toss = np.random.choice(coin)
outcomes = np.append(outcomes, outcome_of_toss)

i = np.arange(5).item(4)
outcome_of_toss = np.random.choice(coin)
outcomes = np.append(outcomes, outcome_of_toss)

outcomes
```





{:.output_data_text}
```
array(['Heads', 'Heads', 'Heads', 'Tails', 'Heads'], dtype='<U32')
```



By capturing the results in an array we have given ourselves the ability to use array methods to do computations. For example, we can use `np.count_nonzero` to count the number of heads in the five tosses.



{:.input_area}
```python
np.count_nonzero(outcomes == 'Heads')
```





{:.output_data_text}
```
4
```



Keep in mind that we have used the `for` loop to simulate a random experiment, and therefore if you run the cell again, the array `outcomes` is likely to be different. In upcoming sections of the course we will study how different the outcomes could be.

Iteration is a powerful technique. For example, by running exactly the same code for 1000 tosses instead of 5, we can count the number of heads in 1000 tosses.



{:.input_area}
```python
outcomes = make_array()

for i in np.arange(1000):
    outcome_of_toss = np.random.choice(coin)
    outcomes = np.append(outcomes, outcome_of_toss)

np.count_nonzero(outcomes == 'Heads')
```





{:.output_data_text}
```
515
```


