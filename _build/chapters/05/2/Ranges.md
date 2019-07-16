---
redirect_from:
  - "/chapters/05/2/ranges"
interact_link: content/chapters/05/2/Ranges.ipynb
kernel_name: python3
has_widgets: false
title: 'Ranges'
prev_page:
  url: /chapters/05/1/Arrays
  title: 'Arrays'
next_page:
  url: /chapters/05/3/More_on_Arrays
  title: 'More on Arrays'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Ranges

A *range* is an array of numbers in increasing or decreasing order, each separated by a regular interval. 
Ranges are useful in a surprisingly large number of situations, so it's worthwhile to learn about them.

Ranges are defined  using the `np.arange` function, which takes either one, two, or three arguments: a start, and end, and a 'step'.

If you pass one argument to `np.arange`, this becomes the `end` value, with `start=0`, `step=1` assumed.  Two arguments give the `start` and `end` with `step=1` assumed.  Three arguments give the `start`, `end` and `step` explicitly.

A range always includes its `start` value, but does not include its `end` value.  It counts up by `step`, and it stops before it gets to the `end`.

    np.arange(end): An array starting with 0 of increasing consecutive integers, stopping before end.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.arange(5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([0, 1, 2, 3, 4])
```


</div>
</div>
</div>



Notice how the array starts at 0 and goes only up to 4, not to the end value of 5.




    np.arange(start, end): An array of consecutive increasing integers from start, stopping before end.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.arange(3, 9)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([3, 4, 5, 6, 7, 8])
```


</div>
</div>
</div>




    np.arange(start, end, step): A range with a difference of step between each pair of consecutive values, starting from start and stopping before end.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.arange(3, 30, 5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([ 3,  8, 13, 18, 23, 28])
```


</div>
</div>
</div>



This array starts at 3, then takes a step of 5 to get to 8, then another step of 5 to get to 13, and so on.

When you specify a step, the start, end, and step can all be either positive or negative and may be whole numbers or fractions. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.arange(1.5, -2, -0.5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([ 1.5,  1. ,  0.5,  0. , -0.5, -1. , -1.5])
```


</div>
</div>
</div>



#### Example: Leibniz's formula for $\pi$



The great German mathematician and philosopher [Gottfried Wilhelm Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) 
(1646 - 1716) discovered a wonderful formula for $\pi$ as an infinite sum of simple fractions. The formula is

$$\pi = 4 \cdot \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \dots\right)$$



Though some math is needed to establish this, we can use arrays to convince ourselves that the formula works. Let's calculate the first 5000 terms of Leibniz's infinite sum and see if it is close to $\pi$.

$$4 \cdot \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \dots - \frac{1}{9999} \right)$$

We will calculate this finite sum by adding all the positive terms first and then subtracting the sum of all the negative terms [[1]](#footnotes):

$$4 \cdot \left( \left(1 + \frac{1}{5} + \frac{1}{9} + \dots + \frac{1}{9997} \right) - \left(\frac{1}{3} + \frac{1}{7} + \frac{1}{11} + \dots + \frac{1}{9999} \right) \right)$$



The positive terms in the sum have 1, 5, 9, and so on in the denominators. The array `by_four_to_20` contains these numbers up to 17:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
by_four_to_20 = np.arange(1, 20, 4)
by_four_to_20

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([ 1,  5,  9, 13, 17])
```


</div>
</div>
</div>



To get an accurate approximation to $\pi$, we'll use the much longer array `positive_term_denominators`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
positive_term_denominators = np.arange(1, 10000, 4)
positive_term_denominators

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([   1,    5,    9, ..., 9989, 9993, 9997])
```


</div>
</div>
</div>



The positive terms we actually want to add together are just 1 over these denominators:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
positive_terms = 1 / positive_term_denominators

```
</div>

</div>



The negative terms have 3, 7, 11, and so on on in their denominators. This array is just 2 added to `positive_term_denominators`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
negative_terms = 1 / (positive_term_denominators + 2)

```
</div>

</div>



The overall sum is



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
4 * ( sum(positive_terms) - sum(negative_terms) )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.1413926535917955
```


</div>
</div>
</div>



This is very close to $\pi = 3.14159\dots$. Leibniz's formula is looking good!



<a id='footnotes'></a>
##### Footnotes
[1] Surprisingly, when we add  *infinitely* many fractions, the order can matter! But our approximation to $\pi$ uses only a large finite number of fractions, so it's okay to add the terms in any convenient order.

