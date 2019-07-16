---
redirect_from:
  - "/chapters/09/2/iteration"
interact_link: content/chapters/09/2/Iteration.ipynb
kernel_name: python3
has_widgets: false
title: 'Iteration'
prev_page:
  url: /chapters/09/1/Conditional_Statements
  title: 'Conditional Statements'
next_page:
  url: /chapters/09/3/Simulation
  title: 'Simulation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Iteration
It is often the case in programming – especially when dealing with randomness – that we want to repeat a process multiple times. For example, recall the game of betting on one roll of a die with the following rules:

- If the die shows 1 or 2 spots, my net gain is -1 dollar.
- If the die shows 3 or 4 spots, my net gain is 0 dollars.
- If the die shows 5 or 6 spots, my net gain is 1 dollar.

The function `bet_on_one_roll` takes no argument. Each time it is called, it simulates one roll of a fair die and returns the net gain in dollars.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bet_on_one_roll():
    """Returns my net gain on one bet"""
    x = np.random.choice(np.arange(1, 7))  # roll a die once and record the number of spots
    if x <= 2:
        return -1
    elif x <= 4:
        return 0
    elif x <= 6:
        return 1

```
</div>

</div>



Playing this game once is easy:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bet_on_one_roll()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
1
```


</div>
</div>
</div>



To get a sense of how variable the results are, we have to play the game over and over again. We could run the cell repeatedly, but that's tedious, and if we wanted to do it a thousand times or a million times, forget it.  

A more automated solution is to use a `for` statement to loop over the contents of a sequence. This is called *iteration*. A `for` statement begins with the word `for`, followed by a name we want to give each item in the sequence, followed by the word `in`, and ending with an expression that evaluates to a sequence. The indented body of the `for` statement is executed once *for each item in that sequence*.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for animal in make_array('cat', 'dog', 'rabbit'):
    print(animal)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
cat
dog
rabbit
```
</div>
</div>
</div>



It is helpful to write code that exactly replicates a `for` statement, without using the `for` statement.  This is called *unrolling* the loop.  

A `for` statement simple replicates the code inside it, but before each iteration, it assigns a new value from the given sequence to the name we chose.  For example, here is an unrolled version of the loop above.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
animal = make_array('cat', 'dog', 'rabbit').item(0)
print(animal)
animal = make_array('cat', 'dog', 'rabbit').item(1)
print(animal)
animal = make_array('cat', 'dog', 'rabbit').item(2)
print(animal)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
cat
dog
rabbit
```
</div>
</div>
</div>



Notice that the name `animal` is arbitrary, just like any name we assign with `=`.

Here we use a `for` statement in a more realistic way: we print the results of betting five times on the die as described earlier. This is called *simulating* the results of five bets. We use the word *simulating* to remind ourselves that we are not physically rolling dice and exchanging money but using Python to mimic the process.

To repeat a process `n` times, it is common to use the sequence `np.arange(n)` in the `for` statement. It is also common to use a very short name for each item. In our code we will use the name `i` to remind ourselves that it refers to an item.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in np.arange(5):
    print(bet_on_one_roll())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1
1
0
-1
1
```
</div>
</div>
</div>



In this case, we simply perform exactly the same (random) action several times, so the code in the body of our `for` statement does not actually refer to `i`.



### Augmenting Arrays

While the `for` statement above does simulate the results of five bets, the results are simply printed and are not in a form that we can use for computation. Any array of results would be more useful. Thus a typical use of a `for` statement is to create an array of results, by augmenting the array each time.

The `append` method in `NumPy` helps us do this. The call `np.append(array_name, value)` evaluates to a new array that is `array_name` augmented by `value`. When you use `append`, keep in mind that all the entries of an array must have the same type.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets = make_array('Cat', 'Dog')
np.append(pets, 'Another Pet')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array(['Cat', 'Dog', 'Another Pet'], dtype='<U11')
```


</div>
</div>
</div>



This keeps the array `pets` unchanged:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array(['Cat', 'Dog'], dtype='<U3')
```


</div>
</div>
</div>



But often while using `for` loops it will be convenient to mutate an array – that is, change it – when augmenting it. This is done by assigning the augmented array to the same name as the original.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pets = np.append(pets, 'Another Pet')
pets

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array(['Cat', 'Dog', 'Another Pet'], dtype='<U11')
```


</div>
</div>
</div>



### Example: Betting on 5 Rolls
We can now simulate five bets on the die and collect the results in an array that we will call the *collection array*. We will start out by creating an empty array for this, and then append the outcome of each bet. Notice that the body of the `for` loop contains two statements. Both statements are executed for each item in the given sequence.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
outcomes = make_array()

for i in np.arange(5):
    outcome_of_bet = bet_on_one_roll()
    outcomes = np.append(outcomes, outcome_of_bet)
    
outcomes

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([-1.,  0.,  0.,  1.,  0.])
```


</div>
</div>
</div>



Let us rewrite the cell with the `for` statement unrolled:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
outcomes = make_array()

i = np.arange(5).item(0)
outcome_of_bet = bet_on_one_roll()
outcomes = np.append(outcomes, outcome_of_bet)

i = np.arange(5).item(1)
outcome_of_bet = bet_on_one_roll()
outcomes = np.append(outcomes, outcome_of_bet)

i = np.arange(5).item(2)
outcome_of_bet = bet_on_one_roll()
outcomes = np.append(outcomes, outcome_of_bet)

i = np.arange(5).item(3)
outcome_of_bet = bet_on_one_roll()
outcomes = np.append(outcomes, outcome_of_bet)

i = np.arange(5).item(4)
outcome_of_bet = bet_on_one_roll()
outcomes = np.append(outcomes, outcome_of_bet)

outcomes

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([ 0., -1.,  0.,  1., -1.])
```


</div>
</div>
</div>



The contents of the array are likely to be different from the array that we got by running the previous cell, but that is because of randomness in rolling the die. The process for creating the array is exactly the same.

By capturing the results in an array we have given ourselves the ability to use array methods to do computations. For example, we can use `np.count_nonzero` to count the number of times money changed hands.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.count_nonzero(outcomes)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3
```


</div>
</div>
</div>



### Example: Betting on 300 Rolls
Iteration is a powerful technique. For example, we can see the variation in the results of 300 bets by running exactly the same code for 300 bets instead of five.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
outcomes = make_array()

for i in np.arange(300):
    outcome_of_bet = bet_on_one_roll()
    outcomes = np.append(outcomes, outcome_of_bet)

```
</div>

</div>



The array `outcomes` contains the results of all 300 bets.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len(outcomes)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
300
```


</div>
</div>
</div>



To see how often the three different possible results appeared, we can use the array `outcomes` and `Table` methods.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
outcome_table = Table().with_column('Outcome', outcomes)
outcome_table.group('Outcome').barh(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/09/2/Iteration_29_0.png)

</div>
</div>
</div>



Not surprisingly, each of the three outcomes -1, 0, and 1 appeared about about 100 of the 300 times, give or take. We will examine the "give or take" amounts more closely in later chapters.

