---
redirect_from:
  - "/chapters/05/sequences"
interact_link: content/chapters/05/Sequences.ipynb
kernel_name: python3
has_widgets: false
title: 'Sequences'
prev_page:
  url: /chapters/04/3/Comparison
  title: 'Comparisons'
next_page:
  url: /chapters/05/1/Arrays
  title: 'Arrays'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Sequences

Values can be grouped together into collections, which allows programmers to organize those values and refer to all of them with a single name. By grouping values together, we can write code that performs a computation on many pieces of data at once.

Calling the function `make_array` on several values places them into an *array*, which is a kind of sequential collection. Below, we collect four different temperatures into an array called `highs`. These are the [estimated average daily high temperatures](http://berkeleyearth.lbl.gov/regions/global-land) over all land on Earth (in degrees Celsius) for the decades surrounding 1850, 1900, 1950, and 2000, respectively, expressed as deviations from the average absolute high temperature between 1951 and 1980, which was 14.48 degrees.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, baseline_high - 0.093,
                   baseline_high + 0.105, baseline_high + 0.684)
highs

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([ 13.6  ,  14.387,  14.585,  15.164])
```


</div>
</div>
</div>



Collections allow us to pass multiple values into a function using a single name. For instance, the `sum` function computes the sum of all values in a collection, and the `len` function computes its length. (That's the number of values we put in it.) Using them together, we can compute the average of a collection.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(highs)/len(highs)

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



The complete chart of daily high and low temperatures appears below. 

### Mean of Daily High Temperature

![Mean of Daily High Temperature](http://berkeleyearth.lbl.gov/auto/Regional/TMAX/Figures/global-land-TMAX-Trend.png)

### Mean of Daily Low Temperature

![Mean of Daily Low Temperature](http://berkeleyearth.lbl.gov/auto/Regional/TMIN/Figures/global-land-TMIN-Trend.png)

