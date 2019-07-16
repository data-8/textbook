---
redirect_from:
  - "/chapters/06/4/example-gender-ratio-in-the-us-population"
interact_link: content/chapters/06/4/Example_Gender_Ratio_in_the_US_Population.ipynb
kernel_name: python3
has_widgets: false
title: 'Example: Trends in Gender'
prev_page:
  url: /chapters/06/3/Example_Trends_in_the_Population_of_the_United_States
  title: 'Example: Population Trends'
next_page:
  url: /chapters/07/Visualization
  title: 'Visualization'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



# Example: Trends in Gender

We are now equipped with enough coding skills to examine features and trends in subgroups of the U.S. population. In this example, we will look at the distribution of males and females across age groups. We will continue using the `us_pop` table from the previous section.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
us_pop

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3951330</td> <td>3949775</td>
        </tr>
        <tr>
            <td>0   </td> <td>1   </td> <td>3957888</td> <td>3949776</td>
        </tr>
        <tr>
            <td>0   </td> <td>2   </td> <td>4090862</td> <td>3959664</td>
        </tr>
        <tr>
            <td>0   </td> <td>3   </td> <td>4111920</td> <td>4007079</td>
        </tr>
        <tr>
            <td>0   </td> <td>4   </td> <td>4077551</td> <td>4005716</td>
        </tr>
        <tr>
            <td>0   </td> <td>5   </td> <td>4064653</td> <td>4006900</td>
        </tr>
        <tr>
            <td>0   </td> <td>6   </td> <td>4073013</td> <td>4135930</td>
        </tr>
        <tr>
            <td>0   </td> <td>7   </td> <td>4043046</td> <td>4155326</td>
        </tr>
        <tr>
            <td>0   </td> <td>8   </td> <td>4025604</td> <td>4120903</td>
        </tr>
        <tr>
            <td>0   </td> <td>9   </td> <td>4125415</td> <td>4108349</td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



As we know from having examined this dataset earlier, a [description of the table](http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.pdf) appears online. Here is a reminder of what the table contains. 

Each row represents an age group. The `SEX` column contains numeric codes: `0` stands for the total, `1` for male, and `2` for female. The `AGE` column contains ages in completed years, but the special value `999` represents the entire population regardless of age. The rest of the columns contain estimates of the US population.



### Understanding `AGE` = 100
As a preliminary, let's interpret data in the final age category in the table, where `AGE` is 100. The code below extracts the rows for the combined group of men and women (`SEX` code 0) for the highest ages.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
us_pop.where('SEX', are.equal_to(0)).where('AGE', are.between(97, 101))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>97  </td> <td>68893</td> <td>83089</td>
        </tr>
        <tr>
            <td>0   </td> <td>98  </td> <td>47037</td> <td>59726</td>
        </tr>
        <tr>
            <td>0   </td> <td>99  </td> <td>32178</td> <td>41468</td>
        </tr>
        <tr>
            <td>0   </td> <td>100 </td> <td>54410</td> <td>71626</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Not surprisingly, the numbers of people are smaller at higher ages – for example, there are fewer 99-year-olds than 98-year-olds. 

It does come as a surprise, though, that the numbers for `AGE` 100 are quite a bit larger than those for age 99. A closer examination of the documentation shows that it's because the Census Bureau used 100 as the code for everyone aged 100 or more. 

The row with `AGE` 100 doesn't just represent 100-year-olds – it also includes those who are older than 100. That is why the numbers in that row are larger than in the row for the 99-year-olds.



### Overall Proportions of Males and Females
We will now begin looking at gender ratios in 2014. First, let's look at all the age groups together. Remember that this means looking at the rows where the "age" is coded 999. The table `all_ages` contains this information. There are three rows: one for the total of both genders, one for males (`SEX` code 1), and one for females (`SEX` code 2).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
us_pop_2014 = us_pop.drop('2010')
all_ages = us_pop_2014.where('AGE', are.equal_to(999))
all_ages

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>999 </td> <td>318907401</td>
        </tr>
        <tr>
            <td>1   </td> <td>999 </td> <td>156955337</td>
        </tr>
        <tr>
            <td>2   </td> <td>999 </td> <td>161952064</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Row 0 of `all_ages` contains the total U.S. population in each of the two years. The United States had just under 319 million in 2014.

Row 1 contains the counts for males and Row 2 for females. Compare these two rows to see that in 2014, there were more females than males in the United States. 

The population counts in Row 1 and Row 2 add up to the total population in Row 0. 

For comparability with other quantities, we will need to convert these counts to percents out of the total population. Let's access the total for 2014 and name it. Then, we'll show a population table with a proportion column. Consistent with our earlier observation that there were more females than males, about 50.8% of the population in 2014 was female and about 49.2% male in each of the two years. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pop_2014 = all_ages.column('2014').item(0)
all_ages.with_column(
    'Proportion', all_ages.column('2014')/pop_2014
).set_format('Proportion', PercentFormatter)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th> <th>Proportion</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>999 </td> <td>318907401</td> <td>100.00%   </td>
        </tr>
        <tr>
            <td>1   </td> <td>999 </td> <td>156955337</td> <td>49.22%    </td>
        </tr>
        <tr>
            <td>2   </td> <td>999 </td> <td>161952064</td> <td>50.78%    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Proportions of Boys and Girls among Infants



When we look at infants, however, the opposite is true. Let's define infants to be babies who have not yet completed one year, represented in the row corresponding to `AGE` 0. Here are their numbers in the population. You can see that male infants outnumbered female infants.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
infants = us_pop_2014.where('AGE', are.equal_to(0))
infants

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3949775</td>
        </tr>
        <tr>
            <td>1   </td> <td>0   </td> <td>2020326</td>
        </tr>
        <tr>
            <td>2   </td> <td>0   </td> <td>1929449</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



As before, we can convert these counts to percents out of the total numbers of infants. The resulting table shows that in 2014, just over 51% of infants in the U.S. were male. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
infants_2014 = infants.column('2014').item(0)
infants.with_column(
    'Proportion', infants.column('2014')/infants_2014
).set_format('Proportion', PercentFormatter)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th> <th>Proportion</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3949775</td> <td>100.00%   </td>
        </tr>
        <tr>
            <td>1   </td> <td>0   </td> <td>2020326</td> <td>51.15%    </td>
        </tr>
        <tr>
            <td>2   </td> <td>0   </td> <td>1929449</td> <td>48.85%    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



In fact, it has long been observed that the proportion of boys among newborns is slightly more than 1/2. The reason for this is not thoroughly understood, and [scientists are still working on it](http://www.npr.org/sections/health-shots/2015/03/30/396384911/why-are-more-baby-boys-born-than-girls).



### Female:Male Gender Ratio at Each Age



We have seen that while there are more baby boys than baby girls, there are more females than males overall. So it's clear that the split between genders must vary across age groups.

To study this variation, we will separate out the data for the females and the males, and eliminate the row where all the ages are aggregated and `AGE` is coded as 999.

The tables `females` and `males` contain the data for each the two genders.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
females_all_rows = us_pop_2014.where('SEX', are.equal_to(2))
females = females_all_rows.where('AGE', are.not_equal_to(999))
females

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2   </td> <td>0   </td> <td>1929449</td>
        </tr>
        <tr>
            <td>2   </td> <td>1   </td> <td>1931375</td>
        </tr>
        <tr>
            <td>2   </td> <td>2   </td> <td>1935991</td>
        </tr>
        <tr>
            <td>2   </td> <td>3   </td> <td>1957483</td>
        </tr>
        <tr>
            <td>2   </td> <td>4   </td> <td>1961199</td>
        </tr>
        <tr>
            <td>2   </td> <td>5   </td> <td>1962561</td>
        </tr>
        <tr>
            <td>2   </td> <td>6   </td> <td>2024870</td>
        </tr>
        <tr>
            <td>2   </td> <td>7   </td> <td>2032494</td>
        </tr>
        <tr>
            <td>2   </td> <td>8   </td> <td>2015285</td>
        </tr>
        <tr>
            <td>2   </td> <td>9   </td> <td>2010659</td>
        </tr>
    </tbody>
</table>
<p>... (91 rows omitted)</p>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
males_all_rows = us_pop_2014.where('SEX', are.equal_to(1))
males = males_all_rows.where('AGE', are.not_equal_to(999))
males

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>0   </td> <td>2020326</td>
        </tr>
        <tr>
            <td>1   </td> <td>1   </td> <td>2018401</td>
        </tr>
        <tr>
            <td>1   </td> <td>2   </td> <td>2023673</td>
        </tr>
        <tr>
            <td>1   </td> <td>3   </td> <td>2049596</td>
        </tr>
        <tr>
            <td>1   </td> <td>4   </td> <td>2044517</td>
        </tr>
        <tr>
            <td>1   </td> <td>5   </td> <td>2044339</td>
        </tr>
        <tr>
            <td>1   </td> <td>6   </td> <td>2111060</td>
        </tr>
        <tr>
            <td>1   </td> <td>7   </td> <td>2122832</td>
        </tr>
        <tr>
            <td>1   </td> <td>8   </td> <td>2105618</td>
        </tr>
        <tr>
            <td>1   </td> <td>9   </td> <td>2097690</td>
        </tr>
    </tbody>
</table>
<p>... (91 rows omitted)</p>
</div>


</div>
</div>
</div>



The plan now is to compare the number of women and the number of men at each age, for each of the two years. Array and Table methods give us straightforward ways to do this. Both of these tables have one row for each age.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
males.column('AGE')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
        26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
        39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
        52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
        65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
        78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
        91,  92,  93,  94,  95,  96,  97,  98,  99, 100])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
females.column('AGE')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
        26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
        39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
        52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
        65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
        78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
        91,  92,  93,  94,  95,  96,  97,  98,  99, 100])
```


</div>
</div>
</div>



For any given age, we can get the Female:Male gender ratio by dividing the number of females by the number of males. To do this in one step, we can use `column` to extract the array of female counts and the corresponding array of male counts, and then simply divide one array by the other. Elementwise division will create an array of gender ratios for all the years.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ratios = Table().with_columns(
    'AGE', females.column('AGE'),
    '2014 F:M RATIO', females.column('2014')/males.column('2014')
)
ratios

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>AGE</th> <th>2014 F:M RATIO</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0.955019      </td>
        </tr>
        <tr>
            <td>1   </td> <td>0.956884      </td>
        </tr>
        <tr>
            <td>2   </td> <td>0.956672      </td>
        </tr>
        <tr>
            <td>3   </td> <td>0.955058      </td>
        </tr>
        <tr>
            <td>4   </td> <td>0.959248      </td>
        </tr>
        <tr>
            <td>5   </td> <td>0.959998      </td>
        </tr>
        <tr>
            <td>6   </td> <td>0.959172      </td>
        </tr>
        <tr>
            <td>7   </td> <td>0.957445      </td>
        </tr>
        <tr>
            <td>8   </td> <td>0.957099      </td>
        </tr>
        <tr>
            <td>9   </td> <td>0.958511      </td>
        </tr>
    </tbody>
</table>
<p>... (91 rows omitted)</p>
</div>


</div>
</div>
</div>



You can see from the display that the ratios are all around 0.96 for children aged nine or younger. When the Female:Male ratio is less than 1, there are fewer females than males. Thus what we are seeing is that there were fewer girls than boys in each of the age groups 0, 1, 2, and so on through 9. Moreover, in each of these age groups, there were about 96 girls for every 100 boys.



So how can the overall proportion of females in the population be higher than the males? 

Something extraordinary happens when we examine the other end of the age range. Here are the Female:Male ratios for people aged more than 75.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ratios.where('AGE', are.above(75)).show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>AGE</th> <th>2014 F:M RATIO</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>76  </td> <td>1.23487       </td>
        </tr>
        <tr>
            <td>77  </td> <td>1.25797       </td>
        </tr>
        <tr>
            <td>78  </td> <td>1.28244       </td>
        </tr>
        <tr>
            <td>79  </td> <td>1.31627       </td>
        </tr>
        <tr>
            <td>80  </td> <td>1.34138       </td>
        </tr>
        <tr>
            <td>81  </td> <td>1.37967       </td>
        </tr>
        <tr>
            <td>82  </td> <td>1.41932       </td>
        </tr>
        <tr>
            <td>83  </td> <td>1.46552       </td>
        </tr>
        <tr>
            <td>84  </td> <td>1.52048       </td>
        </tr>
        <tr>
            <td>85  </td> <td>1.5756        </td>
        </tr>
        <tr>
            <td>86  </td> <td>1.65096       </td>
        </tr>
        <tr>
            <td>87  </td> <td>1.72172       </td>
        </tr>
        <tr>
            <td>88  </td> <td>1.81223       </td>
        </tr>
        <tr>
            <td>89  </td> <td>1.91837       </td>
        </tr>
        <tr>
            <td>90  </td> <td>2.01263       </td>
        </tr>
        <tr>
            <td>91  </td> <td>2.09488       </td>
        </tr>
        <tr>
            <td>92  </td> <td>2.2299        </td>
        </tr>
        <tr>
            <td>93  </td> <td>2.33359       </td>
        </tr>
        <tr>
            <td>94  </td> <td>2.52285       </td>
        </tr>
        <tr>
            <td>95  </td> <td>2.67253       </td>
        </tr>
        <tr>
            <td>96  </td> <td>2.87998       </td>
        </tr>
        <tr>
            <td>97  </td> <td>3.09104       </td>
        </tr>
        <tr>
            <td>98  </td> <td>3.41826       </td>
        </tr>
        <tr>
            <td>99  </td> <td>3.63278       </td>
        </tr>
        <tr>
            <td>100 </td> <td>4.25966       </td>
        </tr>
    </tbody>
</table>
</div>

</div>
</div>
</div>



Not only are all of these ratios greater than 1, signifying more women than men in all of these age groups, many of them are considerably greater than 1. 

- At ages 89 and 90 the ratios are close to 2, meaning that there were about twice as many women as men at those ages in 2014.
- At ages 98 and 99, there were about 3.5 to 4 times as many women as men. 

If you are wondering how many people there were at these advanced ages, you can use Python to find out:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
males.where('AGE', are.between(98, 100))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>98  </td> <td>13518</td>
        </tr>
        <tr>
            <td>1   </td> <td>99  </td> <td>8951 </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
females.where('AGE', are.between(98, 100))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2   </td> <td>98  </td> <td>46208</td>
        </tr>
        <tr>
            <td>2   </td> <td>99  </td> <td>32517</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The graph below shows the gender ratios plotted against age. The blue curve shows the 2014 ratio by age.

The ratios are almost 1 (signifying close to equal numbers of males and females) for ages 0 through 60, but they start shooting up dramatically (more females than males) starting at about age 65.

That females outnumber males in the U.S. is partly due to the marked gender imbalance in favor of women among senior citizens.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ratios.plot('AGE')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/06/4/Example_Gender_Ratio_in_the_US_Population_34_0.png)

</div>
</div>
</div>

