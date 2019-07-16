---
redirect_from:
  - "/chapters/03/2/names"
interact_link: content/chapters/03/2/Names.ipynb
kernel_name: python3
has_widgets: false
title: 'Names'
prev_page:
  url: /chapters/03/1/Expressions
  title: 'Expressions'
next_page:
  url: /chapters/03/2/1/Growth
  title: 'Example: Growth Rates'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Names

Names are given to values in Python using an *assignment* statement. In an assignment, a name is followed by `=`, which is followed by any expression. The value of the expression to the right of `=` is *assigned* to the name. Once a name has a value assigned to it, the value will be substituted for that name in future expressions.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = 10
b = 20
a + b

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
30
```


</div>
</div>
</div>



A previously assigned name can be used in the expression to the right of `=`. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quarter = 1/4
half = 2 * quarter
half

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.5
```


</div>
</div>
</div>



However, only the current value of an expression is assigned to a name. If that value changes later, names that were defined in terms of that value will not change automatically.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
quarter = 4
half

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.5
```


</div>
</div>
</div>



Names must start with a letter, but can contain both letters and numbers. A name cannot contain a space; instead, it is common to use an underscore character `_` to replace each space. Names are only as useful as you make them; it's up to the programmer to choose names that are easy to interpret. Typically, more meaningful names can be invented than `a` and `b`. For example, to describe the sales tax on a $5 purchase in Berkeley, CA, the following names clarify the meaning of the various quantities involved.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
purchase_price = 5
state_tax_rate = 0.075
county_tax_rate = 0.02
city_tax_rate = 0
sales_tax_rate = state_tax_rate + county_tax_rate + city_tax_rate
sales_tax = purchase_price * sales_tax_rate
sales_tax

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.475
```


</div>
</div>
</div>

