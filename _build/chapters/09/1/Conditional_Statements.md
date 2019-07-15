---
redirect_from:
  - "/chapters/09/1/conditional-statements"
interact_link: content/chapters/09/1/Conditional_Statements.ipynb
kernel_name: python3
has_widgets: false
title: 'Conditional Statements'
prev_page:
  url: /chapters/09/Randomness
  title: 'Randomness'
next_page:
  url: /chapters/09/2/Iteration
  title: 'Iteration'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Conditional Statements
In many situations, actions and results depends on a specific set of conditions being satisfied. For example, individuals in randomized controlled trials receive the treatment if they have been assigned to the treatment group. A gambler makes money if she wins her bet. 

In this section we will learn how to describe such situations using code. A *conditional statement* is a multi-line statement that allows Python to choose among different alternatives based on the truth value of an expression. While conditional statements can appear anywhere, they appear most often within the body of a function in order to express alternative behavior depending on argument values.

A conditional statement always begins with an `if` header, which is a single line followed by an indented body. The body is only executed if the expression directly following `if` (called the *if expression*) evaluates to a true value. If the *if expression* evaluates to a false value, then the body of the `if` is skipped.

Let us start defining a function that returns the sign of a number.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sign(x):
    
    if x > 0:
        return 'Positive'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sign(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Positive'
```


</div>
</div>
</div>



This function returns the correct sign if the input is a positive number. But if the input is not a positive number, then the *if expression* evaluates to a false value, and so the `return` statement is skipped and the function call has no value.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sign(-3)

```
</div>

</div>



So let us refine our function to return `Negative` if the input is a negative number. We can do this by adding an `elif` clause, where `elif` if Python's shorthand for the phrase "else, if".



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'

```
</div>

</div>



Now `sign` returns the correct answer when the input is -3:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sign(-3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Negative'
```


</div>
</div>
</div>



What if the input is 0? To deal with this case, we can add another `elif` clause:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'
    
    elif x == 0:
        return 'Neither positive nor negative'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sign(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Neither positive nor negative'
```


</div>
</div>
</div>



Equivalently, we can replaced the final `elif` clause by an `else` clause, whose body will be executed only if all the previous comparisons are false; that is, if the input value is equal to 0.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'
    
    else:
        return 'Neither positive nor negative'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sign(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Neither positive nor negative'
```


</div>
</div>
</div>



### The General Form
A conditional statement can also have multiple clauses with multiple bodies, and only one of those bodies can ever be executed. The general format of a multi-clause conditional statement appears below.

    if <if expression>:
        <if body>
    elif <elif expression 0>:
        <elif body 0>
    elif <elif expression 1>:
        <elif body 1>
    ...
    else:
        <else body>
        
There is always exactly one `if` clause, but there can be any number of `elif` clauses. Python will evaluate the `if` and `elif` expressions in the headers in order until one is found that is a true value, then execute the corresponding body. The `else` clause is optional. When an `else` header is provided, its *else body* is executed only if none of the header expressions of the previous clauses are true. The `else` clause must always come at the end (or not at all).



### Example: Betting on a Die
Suppose I bet on a roll of a fair die. The rules of the game:

- If the die shows 1 spot or 2 spots, I lose a dollar.
- If the die shows 3 spots or 4 spots, I neither lose money nor gain money.
- If the die shows 5 spots or 6 spots, I gain a dollar.

We will now use conditional statements to define a function `one_bet` that takes the number of spots on the roll and returns my net gain.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def one_bet(x):
    """Returns my net gain if the die shows x spots"""
    if x <= 2:
        return -1
    elif x <= 4:
        return 0
    elif x <= 6:
        return 1

```
</div>

</div>



Let's check that the function does the right thing for each different number of spots.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
one_bet(1), one_bet(2), one_bet(3), one_bet (4), one_bet(5), one_bet(6)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
(-1, -1, 0, 0, 1, 1)
```


</div>
</div>
</div>



As a review of how conditional statements work, let's see what `one_bet` does when the input is 3.

- First it evaluates the `if` expression, which is `3 <= 2` which is `False`. So `one_bet` doesn't execute the `if` body.
- Then it evaluates the first `elif` expression, which is `3 <= 4`, which is `True`. So `one_bet` executes the first `elif` body and returns 0.
- Once the body has been executed, the process is complete. The next `elif` expression is not evaluated.

If for some reason we use an input greater than 6, then the `if` expression evaluates to `False` as do both of the `elif` expressions. So `one_bet` does not execute the `if` body nor the two `elif` bodies, and there is no value when you make the call below.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
one_bet(17)

```
</div>

</div>



To play the game based on one roll of a die, you can use `np.random.choice` to generate the number of spots and then use that as the argument to `one_bet`. Run the cell a few times to see how the output changes.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
one_bet(np.random.choice(np.arange(1, 7)))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-1
```


</div>
</div>
</div>



At this point it is natural to want to collect the results of all the bets so that we can analyze them. In the next section we develop a way to do this without running the cell over and over again.

