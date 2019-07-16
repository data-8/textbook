---
redirect_from:
  - "/chapters/03/2/1/growth"
interact_link: content/chapters/03/2/1/Growth.ipynb
kernel_name: python3
has_widgets: false
title: 'Example: Growth Rates'
prev_page:
  url: /chapters/03/2/Names
  title: 'Names'
next_page:
  url: /chapters/03/3/Calls
  title: 'Call Expressions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Example: Growth Rates

The relationship between two measurements of the same quantity taken at different times is often expressed as a *growth rate*. For example, the United States federal government [employed](http://www.bls.gov/opub/mlr/2013/article/industry-employment-and-output-projections-to-2022-1.htm) 2,766,000 people in 2002 and 2,814,000 people in 2012. To compute a growth rate, we must first decide which value to treat as the `initial` amount. For values over time, the earlier value is a natural choice. Then, we divide the difference between the `changed` and `initial` amount by the `initial` amount.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 2766000
changed = 2814000
(changed - initial) / initial

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.01735357917570499
```


</div>
</div>
</div>



It is also typical to subtract one from the ratio of the two measurements, which yields the same value.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(changed/initial) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.017353579175704903
```


</div>
</div>
</div>



This value is the growth rate over 10 years. A useful property of growth rates is that they don't change even if the values are expressed in different units. So, for example, we can express the same relationship between thousands of people in 2002 and 2012.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 2766
changed = 2814
(changed/initial) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.017353579175704903
```


</div>
</div>
</div>



In 10 years, the number of employees of the US Federal Government has increased by only 1.74%. In that time, the total expenditures of the US Federal Government increased from \\$2.37 trillion to \\$3.38 trillion in 2012.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 2.37
changed = 3.38
(changed/initial) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.4261603375527425
```


</div>
</div>
</div>



A 42.6% increase in the federal budget is much larger than the 1.74% increase in federal employees. In fact, the number of federal employees has grown much more slowly than the population of the United States, which increased 9.21% in the same time period from 287.6 million people in 2002 to 314.1 million in 2012.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 287.6
changed = 314.1
(changed/initial) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.09214186369958277
```


</div>
</div>
</div>



A growth rate can be negative, representing a decrease in some value. For example, the number of manufacturing jobs in the US decreased from 15.3 million in 2002 to 11.9 million in 2012, a -22.2% growth rate.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 15.3
changed = 11.9
(changed/initial) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-0.2222222222222222
```


</div>
</div>
</div>



An annual growth rate is a growth rate of some quantity over a single year. An annual growth rate of 0.035, accumulated each year for 10 years, gives a much larger ten-year growth rate of 0.41 (or 41%).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.410598760621121
```


</div>
</div>
</div>



This same computation can be expressed using names and exponents.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
annual_growth_rate = 0.035
ten_year_growth_rate = (1 + annual_growth_rate) ** 10 - 1
ten_year_growth_rate

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.410598760621121
```


</div>
</div>
</div>



Likewise, a ten-year growth rate can be used to compute an equivalent annual growth rate. Below, `t` is the number of years that have passed between measurements. The following computes the annual growth rate of federal expenditures over the last 10 years.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = 2.37
changed = 3.38
t = 10
(changed/initial) ** (1/t) - 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.03613617208346853
```


</div>
</div>
</div>



The total growth over 10 years is equivalent to a 3.6% increase each year.



In summary, a growth rate `g` is used to describe the relative size of an `initial` amount and a `changed` amount after some amount of time `t`. To compute $changed$, apply the growth rate `g` repeatedly, `t` times using exponentiation.

`initial * (1 + g) ** t`

To compute `g`, raise the total growth to the power of `1/t` and subtract one.

`(changed/initial) ** (1/t) - 1`

