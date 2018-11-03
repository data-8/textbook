---
redirect_from:
  - "/chapters/09/1/conditional-statements"
interact_link: content/chapters/09/1/Conditional_Statements.ipynb
title: 'Conditional Statements'
prev_page:
  url: /chapters/09/Randomness
  title: 'Randomness'
next_page:
  url: /chapters/09/2/Iteration
  title: 'Iteration'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Conditional Statements
In many situations, actions and results depends on a specific set of conditions being satisfied. For example, individuals in randomized controlled trials receive the treatment if they have been assigned to the treatment group. A gambler makes money if she wins her bet. 

In this section we will learn how to describe such situations using code. A *conditional statement* is a multi-line statement that allows Python to choose among different alternatives based on the truth value of an expression. While conditional statements can appear anywhere, they appear most often within the body of a function in order to express alternative behavior depending on argument values.

A conditional statement always begins with an `if` header, which is a single line followed by an indented body. The body is only executed if the expression directly following `if` (called the *if expression*) evaluates to a true value. If the *if expression* evaluates to a false value, then the body of the `if` is skipped.

Let us start defining a function that returns the sign of a number.



{:.input_area}
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
```




{:.input_area}
```python
sign(3)
```





{:.output_data_text}
```
'Positive'
```



This function returns the correct sign if the input is a positive number. But if the input is not a positive number, then the *if expression* evaluates to a false value, and so the `return` statement is skipped and the function call has no value.



{:.input_area}
```python
sign(-3)
```


So let us refine our function to return `Negative` if the input is a negative number. We can do this by adding an `elif` clause, where `elif` if Python's shorthand for the phrase "else, if".



{:.input_area}
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'
```


Now `sign` returns the correct answer when the input is -3:



{:.input_area}
```python
sign(-3)
```





{:.output_data_text}
```
'Negative'
```



What if the input is 0? To deal with this case, we can add another `elif` clause:



{:.input_area}
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'
    
    elif x == 0:
        return 'Neither positive nor negative'
```




{:.input_area}
```python
sign(0)
```





{:.output_data_text}
```
'Neither positive nor negative'
```



Equivalently, we can replaced the final `elif` clause by an `else` clause, whose body will be executed only if all the previous comparisons are false; that is, if the input value is equal to 0.



{:.input_area}
```python
def sign(x):
    
    if x > 0:
        return 'Positive'
    
    elif x < 0:
        return 'Negative'
    
    else:
        return 'Neither positive nor negative'
```




{:.input_area}
```python
sign(0)
```





{:.output_data_text}
```
'Neither positive nor negative'
```



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

### Example: "The Other One"
We will now use conditional statements to define a function that seems rather artificial and contrary, but will come in handy later in the chapter. It takes an array with two elements (for example, `red` and `blue`), and another element to compare. If that element is `red`, the function returns `blue`. If the element is (for example) `blue`, the function returns `red`. That is why we'll call the function `other_one`.



{:.input_area}
```python
def other_one(x, a_b):
    
    """Compare x with the two elements of a_b;
    if it is equal to one of them, return the other one;
    if it is not equal to either of them, return an error message.
    """
    if x == a_b.item(0):
        return a_b.item(1)
    
    elif x == a_b.item(1):
        return a_b.item(0)
    
    else:
        return 'The input is not valid.'
```




{:.input_area}
```python
colors = make_array('red', 'blue')
other_one('red', colors)
```





{:.output_data_text}
```
'blue'
```





{:.input_area}
```python
other_one('blue', colors)
```





{:.output_data_text}
```
'red'
```





{:.input_area}
```python
other_one('potato', colors)
```





{:.output_data_text}
```
'The input is not valid.'
```


