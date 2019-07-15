---
redirect_from:
  - "/chapters/05/1/arrays"
interact_link: content/chapters/05/1/Arrays.ipynb
kernel_name: python3
has_widgets: false
title: 'Arrays'
prev_page:
  url: /chapters/05/Sequences
  title: 'Sequences'
next_page:
  url: /chapters/05/2/Ranges
  title: 'Ranges'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Arrays

While there are many kinds of collections in Python, we will work primarily with arrays in this class. We've already seen that the `make_array` function can be used to create arrays of numbers.

Arrays can also contain strings or other types of values, but a single array can only contain a single kind of data. (It usually doesn't make sense to group together unlike data anyway.)  For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
english_parts_of_speech = make_array("noun", "pronoun", "verb", "adverb", "adjective", "conjunction", "preposition", "interjection")
english_parts_of_speech

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array(['noun', 'pronoun', 'verb', 'adverb', 'adjective', 'conjunction',
       'preposition', 'interjection'], dtype='<U12')
```


</div>
</div>
</div>



Returning to the temperature data, we create arrays of average daily [high temperatures](http://berkeleyearth.lbl.gov/auto/Regional/TMAX/Text/global-land-TMAX-Trend.txt) for the decades surrounding 1850, 1900, 1950, and 2000.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, 
                   baseline_high - 0.093,
                   baseline_high + 0.105, 
                   baseline_high + 0.684)
highs

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([13.6  , 14.387, 14.585, 15.164])
```


</div>
</div>
</div>



Arrays can be used in arithmetic expressions to compute over their contents. When an array is combined with a single number, that number is combined with each element of the array. Therefore, we can convert all of these temperatures to Fahrenheit by writing the familiar conversion formula.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(9/5) * highs + 32

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([56.48  , 57.8966, 58.253 , 59.2952])
```


</div>
</div>
</div>



<img src="../../../images/array_arithmetic.png" />



Arrays also have *methods*, which are functions that operate on the array values. The `mean` of a collection of numbers is its average value: the sum divided by the length. Each pair of parentheses in the examples below is part of a call expression; it's calling a function with no arguments to perform a computation on the array called `highs`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
highs.size

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
4
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
highs.sum()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
57.736000000000004
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
highs.mean()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
14.434000000000001
```


</div>
</div>
</div>



#### Functions on Arrays
The `numpy` package, abbreviated `np` in programs, provides Python programmers with convenient and powerful functions for creating and manipulating arrays.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import numpy as np

```
</div>

</div>



For example, the `diff` function computes the difference between each adjacent pair of elements in an array. The first element of the `diff` is the second element minus the first. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.diff(highs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([0.787, 0.198, 0.579])
```


</div>
</div>
</div>



The [full Numpy reference](http://docs.scipy.org/doc/numpy/reference/) lists these functions exhaustively, but only a small subset are used commonly for data processing applications. These are grouped into different packages within `np`. Learning this vocabulary is an important part of learning the Python language, so refer back to this list often as you work through examples and problems.

However, you **don't need to memorize these**.  Use this as a reference.

Each of these functions takes an array as an argument and returns a single value.

| **Function**       | Description                                                          |
|--------------------|----------------------------------------------------------------------|
| `np.prod`          | Multiply all elements together                                       |
| `np.sum`           | Add all elements together                                            |
| `np.all`           | Test whether all elements are true values (non-zero numbers are true)|
| `np.any`           | Test whether any elements are true values (non-zero numbers are true)|
| `np.count_nonzero` | Count the number of non-zero elements                                |

Each of these functions takes an array as an argument and returns an array of values.

| **Function**       | Description                                                          |
|--------------------|----------------------------------------------------------------------|
| `np.diff`          | Difference between adjacent elements                                 |
| `np.round`         | Round each number to the nearest integer (whole number)              |
| `np.cumprod`       | A cumulative product: for each element, multiply all elements so far |
| `np.cumsum`        | A cumulative sum: for each element, add all elements so far          |
| `np.exp`           | Exponentiate each element                                            |
| `np.log`           | Take the natural logarithm of each element                           |
| `np.sqrt`          | Take the square root of each element                                 |
| `np.sort`          | Sort the elements                                                    |

Each of these functions takes an array of strings and returns an array.

| **Function**        | **Description**                                              |
|---------------------|--------------------------------------------------------------|
| `np.char.lower`     | Lowercase each element                                       |
| `np.char.upper`     | Uppercase each element                                       |
| `np.char.strip`     | Remove spaces at the beginning or end of each element        |
| `np.char.isalpha`   | Whether each element is only letters (no numbers or symbols) |
| `np.char.isnumeric` | Whether each element is only numeric (no letters)  

Each of these functions takes both an array of strings and a *search string*; each returns an array.

| **Function**         | **Description**                                                                  |
|----------------------|----------------------------------------------------------------------------------|
| `np.char.count`      | Count the number of times a search string appears among the elements of an array |
| `np.char.find`       | The position within each element that a search string is found first             |
| `np.char.rfind`      | The position within each element that a search string is found last              |
| `np.char.startswith` | Whether each element starts with the search string  



