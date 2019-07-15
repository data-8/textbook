---
redirect_from:
  - "/chapters/04/3/comparison"
interact_link: content/chapters/04/3/Comparison.ipynb
kernel_name: python3
has_widgets: false
title: 'Comparisons'
prev_page:
  url: /chapters/04/2/1/String_Methods
  title: 'String Methods'
next_page:
  url: /chapters/05/Sequences
  title: 'Sequences'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Comparisons

Boolean values most often arise from comparison operators. Python includes a variety of operators that compare values. For example, `3` is larger than `1 + 1`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
3 > 1 + 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



The value `True` indicates that the comparison is valid; Python has confirmed this simple fact about the relationship between `3` and `1+1`. The full set of common comparison operators are listed below.

| Comparison         | Operator | True example | False Example |
|--------------------|----------|--------------|---------------|
| Less than          | <        | 2 < 3        | 2 < 2         |
| Greater than       | >        | 3>2          | 3>3           |
| Less than or equal | <=       | 2 <= 2       | 3 <= 2        |
| Greater or equal   | >=       | 3 >= 3       | 2 >= 3        |
| Equal              | ==       | 3 == 3       | 3 == 2        |
| Not equal          | !=       | 3 != 2       | 2 != 2        |



An expression can contain multiple comparisons, and they all must hold in order for the whole expression to be `True`. For example, we can express that `1+1` is between `1` and `3` using the following expression.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
1 < 1 + 1 < 3

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



The average of two numbers is always between the smaller number and the larger number. We express this relationship for the numbers `x` and `y` below. You can try different values of `x` and `y` to confirm this relationship.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = 12
y = 5
min(x, y) <= (x+y)/2 <= max(x, y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



Strings can also be compared, and their order is alphabetical. A shorter string is less than a longer string that begins with the shorter string.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"Dog" > "Catastrophe" > "Cat"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>

