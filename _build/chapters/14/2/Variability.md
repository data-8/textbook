---
redirect_from:
  - "/chapters/14/2/variability"
interact_link: content/chapters/14/2/Variability.ipynb
kernel_name: python3
has_widgets: false
title: 'Variability'
prev_page:
  url: /chapters/14/1/Properties_of_the_Mean
  title: 'Properties of the Mean'
next_page:
  url: /chapters/14/3/SD_and_the_Normal_Curve
  title: 'The SD and the Normal Curve'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Variability
The mean tells us where a histogram balances. But in almost every histogram we have seen, the values spread out on both sides of the mean. How far from the mean can they be? To answer this question, we will develop a measure of variability about the mean.

We will start by describing how to calculate the measure. Then we will see why it is a good measure to calcualte.



### The Rough Size of Deviations from Average
For simplicity, we will begin our calcuations in the context of a simple array `any_numbers` consisting of just four values. As you will see, our method will extend easily to any other array of values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
any_numbers = make_array(1, 2, 2, 10)

```
</div>

</div>



The goal is to measure roughly how far off the numbers are from their average. To do this, we first need the average: 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Step 1. The average.

mean = np.mean(any_numbers)
mean

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.75
```


</div>
</div>
</div>



Next, let's find out how far each value is from the mean. These are called the *deviations from the average*. A "deviation from average" is just a value minus the average. The table `calculation_steps` displays the results.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Step 2. The deviations from average.

deviations = any_numbers - mean
calculation_steps = Table().with_columns(
        'Value', any_numbers,
        'Deviation from Average', deviations
        )
calculation_steps

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Deviation from Average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1    </td> <td>-2.75                 </td>
        </tr>
        <tr>
            <td>2    </td> <td>-1.75                 </td>
        </tr>
        <tr>
            <td>2    </td> <td>-1.75                 </td>
        </tr>
        <tr>
            <td>10   </td> <td>6.25                  </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Some of the deviations are negative; those correspond to values that are below average. Positive deviations correspond to above-average values.

To calculate roughly how big the deviations are, it is natural to compute the mean of the deviations. But something interesting happens when all the deviations are added together:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(deviations)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>



The positive deviations exactly cancel out the negative ones. This is true of all lists of numbers, no matter what the histogram of the list looks like: **the sum of the deviations from average is zero.** 

Since the sum of the deviations is 0, the mean of the deviations will be 0 as well:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.mean(deviations)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>



Because of this, the mean of the deviations is not a useful measure of the size of the deviations. What we really want to know is roughly how big the deviations are, regardless of whether they are positive or negative. So we need a way to eliminate the signs of the deviations.

There are two time-honored ways of losing signs: the absolute value, and the square. It turns out that taking the square constructs a measure with extremely powerful properties, some of which we will study in this course.

So let's eliminate the signs by squaring all the deviations. Then we will take the mean of the squares:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Step 3. The squared deviations from average

squared_deviations = deviations ** 2
calculation_steps = calculation_steps.with_column(
   'Squared Deviations from Average', squared_deviations
    )
calculation_steps

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Deviation from Average</th> <th>Squared Deviations from Average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1    </td> <td>-2.75                 </td> <td>7.5625                         </td>
        </tr>
        <tr>
            <td>2    </td> <td>-1.75                 </td> <td>3.0625                         </td>
        </tr>
        <tr>
            <td>2    </td> <td>-1.75                 </td> <td>3.0625                         </td>
        </tr>
        <tr>
            <td>10   </td> <td>6.25                  </td> <td>39.0625                        </td>
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
# Step 4. Variance = the mean squared deviation from average

variance = np.mean(squared_deviations)
variance

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
13.1875
```


</div>
</div>
</div>



**Variance:** The mean squared deviation calculated above is called the *variance* of the values. 

While the variance does give us an idea of spread, it is not on the same scale as the original variable as its units are the square of the original. This makes interpretation very difficult. 

So we return to the original scale by taking the positive square root of the variance:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Step 5.
# Standard Deviation:    root mean squared deviation from average
# Steps of calculation:   5    4      3       2             1

sd = variance ** 0.5
sd

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.6314597615834874
```


</div>
</div>
</div>



### Standard Deviation

The quantity that we have just computed is called the *standard deviation* of the list, and is abbreviated as SD. It measures roughly how far the numbers on the list are from their average.

**Definition.** The SD of a list is defined as the *root mean square of deviations from average*. That's a mouthful. But read it from right to left and you have the sequence of steps in the calculation.

**Computation.** The five steps described above result in the SD. You can also use the function ``np.std`` to compute the SD of values in an array:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.std(any_numbers)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.6314597615834874
```


</div>
</div>
</div>



### Working with the SD

To see what we can learn from the SD, let's move to a more interesting dataset than `any_numbers`. The table `nba13` contains data on the players in the National Basketball Association (NBA) in 2013. For each player, the table records the position at which the player usually played, his height in inches, his weight in pounds, and his age in years.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13 = Table.read_table(path_data + 'nba2013.csv')
nba13

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Name</th> <th>Position</th> <th>Height</th> <th>Weight</th> <th>Age in 2013</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DeQuan Jones   </td> <td>Guard   </td> <td>80    </td> <td>221   </td> <td>23         </td>
        </tr>
        <tr>
            <td>Darius Miller  </td> <td>Guard   </td> <td>80    </td> <td>235   </td> <td>23         </td>
        </tr>
        <tr>
            <td>Trevor Ariza   </td> <td>Guard   </td> <td>80    </td> <td>210   </td> <td>28         </td>
        </tr>
        <tr>
            <td>James Jones    </td> <td>Guard   </td> <td>80    </td> <td>215   </td> <td>32         </td>
        </tr>
        <tr>
            <td>Wesley Johnson </td> <td>Guard   </td> <td>79    </td> <td>215   </td> <td>26         </td>
        </tr>
        <tr>
            <td>Klay Thompson  </td> <td>Guard   </td> <td>79    </td> <td>205   </td> <td>23         </td>
        </tr>
        <tr>
            <td>Thabo Sefolosha</td> <td>Guard   </td> <td>79    </td> <td>215   </td> <td>29         </td>
        </tr>
        <tr>
            <td>Chase Budinger </td> <td>Guard   </td> <td>79    </td> <td>218   </td> <td>25         </td>
        </tr>
        <tr>
            <td>Kevin Martin   </td> <td>Guard   </td> <td>79    </td> <td>185   </td> <td>30         </td>
        </tr>
        <tr>
            <td>Evan Fournier  </td> <td>Guard   </td> <td>79    </td> <td>206   </td> <td>20         </td>
        </tr>
    </tbody>
</table>
<p>... (495 rows omitted)</p>
</div>


</div>
</div>
</div>



Here is a histogram of the players' heights.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.select('Height').hist(bins=np.arange(68, 88, 1))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/14/2/Variability_22_0.png)

</div>
</div>
</div>



It is no surprise that NBA players are tall! Their average height is just over 79 inches (6'7"), about 10 inches taller than the average height of men in the United States.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mean_height = np.mean(nba13.column('Height'))
mean_height

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
79.06534653465347
```


</div>
</div>
</div>



About how far off are the players' heights from the average? This is measured by the SD of the heights, which is about 3.45 inches.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sd_height = np.std(nba13.column('Height'))
sd_height

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.4505971830275546
```


</div>
</div>
</div>



The towering center Hasheem Thabeet of the Oklahoma City Thunder was the tallest player at a height of 87 inches.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.sort('Height', descending=True).show(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Name</th> <th>Position</th> <th>Height</th> <th>Weight</th> <th>Age in 2013</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hasheem Thabeet</td> <td>Center  </td> <td>87    </td> <td>263   </td> <td>26         </td>
        </tr>
        <tr>
            <td>Roy Hibbert    </td> <td>Center  </td> <td>86    </td> <td>278   </td> <td>26         </td>
        </tr>
        <tr>
            <td>Tyson Chandler </td> <td>Center  </td> <td>85    </td> <td>235   </td> <td>30         </td>
        </tr>
    </tbody>
</table>
<p>... (502 rows omitted)</p>
</div>

</div>
</div>
</div>



Thabeet was about 8 inches above the average height.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
87 - mean_height

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
7.934653465346528
```


</div>
</div>
</div>



That's a deviation from average, and it is about 2.3 times the standard deviation:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(87 - mean_height)/sd_height

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2.2995015194397923
```


</div>
</div>
</div>



In other words, the height of the tallest player was about 2.3 SDs above average.

At 69 inches tall, Isaiah Thomas was one of the two shortest NBA players in 2013. His height was about 2.9 SDs below average.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.sort('Height').show(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Name</th> <th>Position</th> <th>Height</th> <th>Weight</th> <th>Age in 2013</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Isaiah Thomas </td> <td>Guard   </td> <td>69    </td> <td>185   </td> <td>24         </td>
        </tr>
        <tr>
            <td>Nate Robinson </td> <td>Guard   </td> <td>69    </td> <td>180   </td> <td>29         </td>
        </tr>
        <tr>
            <td>John Lucas III</td> <td>Guard   </td> <td>71    </td> <td>157   </td> <td>30         </td>
        </tr>
    </tbody>
</table>
<p>... (502 rows omitted)</p>
</div>

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(69 - mean_height)/sd_height

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-2.9169868288775844
```


</div>
</div>
</div>



What we have observed is that the tallest and shortest players were both just a few SDs away from the average height. This is an example of why the SD is a useful measure of spread. No matter what the shape of the histogram, the average and the SD together tell you a lot about where the histogram is situated on the number line.



### First main reason for measuring spread by the SD

**Informal statement.** In all numerical data sets, the bulk of the entries are within the range "average $\pm$ a few SDs".

For now, resist the desire to know exactly what fuzzy words like "bulk" and "few" mean. We wil make them precise later in this section. Let's just examine the statement in the context of some more examples.



We have already seen that *all* of the heights of the NBA players were in the range "average $\pm$ 3 SDs". 

What about the ages? Here is a histogram of the distribution, along with the mean and SD of the ages.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.select('Age in 2013').hist(bins=np.arange(15, 45, 1))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/14/2/Variability_39_0.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ages = nba13.column('Age in 2013')
mean_age = np.mean(ages)
sd_age = np.std(ages)
mean_age, sd_age

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
(26.19009900990099, 4.321200441720307)
```


</div>
</div>
</div>



The average age was just over 26 years, and the SD was about 4.3 years.

How far off were the ages from the average? Just as we did with the heights, let's look at the two extreme values of the ages.

Juwan Howard was the oldest player, at 40. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.sort('Age in 2013', descending=True).show(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Name</th> <th>Position</th> <th>Height</th> <th>Weight</th> <th>Age in 2013</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Juwan Howard</td> <td>Forward </td> <td>81    </td> <td>250   </td> <td>40         </td>
        </tr>
        <tr>
            <td>Marcus Camby</td> <td>Center  </td> <td>83    </td> <td>235   </td> <td>39         </td>
        </tr>
        <tr>
            <td>Derek Fisher</td> <td>Guard   </td> <td>73    </td> <td>210   </td> <td>39         </td>
        </tr>
    </tbody>
</table>
<p>... (502 rows omitted)</p>
</div>

</div>
</div>
</div>



Howard's age was about 3.2 SDs above average.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(40 - mean_age)/sd_age

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.1958482778922357
```


</div>
</div>
</div>



The youngest was 15-year-old Jarvis Varnado, who won the NBA Championship that year with the Miami Heat. His age was about 2.6 SDs below average.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba13.sort('Age in 2013').show(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Name</th> <th>Position</th> <th>Height</th> <th>Weight</th> <th>Age in 2013</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Jarvis Varnado       </td> <td>Forward </td> <td>81    </td> <td>230   </td> <td>15         </td>
        </tr>
        <tr>
            <td>Giannis Antetokounmpo</td> <td>Forward </td> <td>81    </td> <td>205   </td> <td>18         </td>
        </tr>
        <tr>
            <td>Sergey Karasev       </td> <td>Guard   </td> <td>79    </td> <td>197   </td> <td>19         </td>
        </tr>
    </tbody>
</table>
<p>... (502 rows omitted)</p>
</div>

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(15 - mean_age)/sd_age

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-2.589581103867081
```


</div>
</div>
</div>



What we have observed for the heights and ages is true in great generality. For *all* lists, the bulk of the entries are no more than 2 or 3 SDs away from the average. 



### Chebychev's Bounds
The Russian mathematician [Pafnuty Chebychev](https://en.wikipedia.org/wiki/Pafnuty_Chebyshev) (1821-1894) proved a result that makes our rough statements precise.

**For all lists, and all numbers $z$, the proportion of entries that are in the range
"average $\pm z$ SDs" is at least $1 - \frac{1}{z^2}$.**

It is important to note that the result gives a bound, not an exact value or an approximation.

What makes the result powerful is that it is true for all lists – all distributions, no matter how irregular. 

Specifically, it says that for every list:

- the proportion in the range "average $\pm$ 2 SDs" is **at least 1 - 1/4 = 0.75**

- the proportion in the range "average $\pm$ 3 SDs" is **at least 1 - 1/9 $\approx$ 0.89**

- the proportion in the range "average $\pm$ 4.5 SDs" is **at least 1 - 1/$\boldsymbol{4.5^2}$ $\approx$ 0.95**

As we noted above, Chebychev's result gives a lower bound, not an exact answer or an approximation. For example, the percent of entries in the range "average $\pm ~2$ SDs" might be quite a bit larger than 75%. But it cannot be smaller.



### Standard units

In the calculations above, the quantity $z$ measures *standard units*, the number of standard deviations above average.

Some values of standard units are negative, corresponding to original values that are below average. Other values of standard units are positive. But no matter what the distribution of the list looks like, Chebychev's bounds imply that standard units will typically be in the (-5, 5) range.

To convert a value to standard units, first find how far it is from average, and then compare that deviation with the standard deviation.
$$
z ~=~ \frac{\mbox{value }-\mbox{ average}}{\mbox{SD}}
$$

As we will see, standard units are frequently used in data analysis. So it is useful to define a function that converts an array of numbers to standard units.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def standard_units(numbers_array):
    "Convert any array of numbers to standard units."
    return (numbers_array - np.mean(numbers_array))/np.std(numbers_array)    

```
</div>

</div>



### Example
As we saw in an earlier section, the table `united` contains a column `Delay` consisting of the departure delay times, in minutes, of over thousands of United Airlines flights in the summer of 2015. We will create a new column called `Delay (Standard Units)` by applying the function `standard_units` to the column of delay times. This allows us to see all the delay times in minutes as well as their corresponding values in standard units. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
united = Table.read_table(path_data + 'united_summer2015.csv')
united = united.with_column(
    'Delay (Standard Units)', standard_units(united.column('Delay'))
)
united

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Date</th> <th>Flight Number</th> <th>Destination</th> <th>Delay</th> <th>Delay (Standard Units)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>6/1/15</td> <td>73           </td> <td>HNL        </td> <td>257  </td> <td>6.08766               </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>217          </td> <td>EWR        </td> <td>28   </td> <td>0.287279              </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>237          </td> <td>STL        </td> <td>-3   </td> <td>-0.497924             </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>250          </td> <td>SAN        </td> <td>0    </td> <td>-0.421937             </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>267          </td> <td>PHL        </td> <td>64   </td> <td>1.19913               </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>273          </td> <td>SEA        </td> <td>-6   </td> <td>-0.573912             </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>278          </td> <td>SEA        </td> <td>-8   </td> <td>-0.62457              </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>292          </td> <td>EWR        </td> <td>12   </td> <td>-0.117987             </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>300          </td> <td>HNL        </td> <td>20   </td> <td>0.0846461             </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>317          </td> <td>IND        </td> <td>-10  </td> <td>-0.675228             </td>
        </tr>
    </tbody>
</table>
<p>... (13815 rows omitted)</p>
</div>


</div>
</div>
</div>



The standard units that we can see are consistent with what we expect based on Chebychev's bounds. Most are of quite small size; only one is above 6.

But something rather alarming happens when we sort the delay times from highest to lowest. The standard units that we can see are extremely high!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
united.sort('Delay', descending=True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Date</th> <th>Flight Number</th> <th>Destination</th> <th>Delay</th> <th>Delay (Standard Units)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>6/21/15</td> <td>1964         </td> <td>SEA        </td> <td>580  </td> <td>14.269                </td>
        </tr>
        <tr>
            <td>6/22/15</td> <td>300          </td> <td>HNL        </td> <td>537  </td> <td>13.1798               </td>
        </tr>
        <tr>
            <td>6/21/15</td> <td>1149         </td> <td>IAD        </td> <td>508  </td> <td>12.4453               </td>
        </tr>
        <tr>
            <td>6/20/15</td> <td>353          </td> <td>ORD        </td> <td>505  </td> <td>12.3693               </td>
        </tr>
        <tr>
            <td>8/23/15</td> <td>1589         </td> <td>ORD        </td> <td>458  </td> <td>11.1788               </td>
        </tr>
        <tr>
            <td>7/23/15</td> <td>1960         </td> <td>LAX        </td> <td>438  </td> <td>10.6722               </td>
        </tr>
        <tr>
            <td>6/23/15</td> <td>1606         </td> <td>ORD        </td> <td>430  </td> <td>10.4696               </td>
        </tr>
        <tr>
            <td>6/4/15 </td> <td>1743         </td> <td>LAX        </td> <td>408  </td> <td>9.91236               </td>
        </tr>
        <tr>
            <td>6/17/15</td> <td>1122         </td> <td>HNL        </td> <td>405  </td> <td>9.83637               </td>
        </tr>
        <tr>
            <td>7/27/15</td> <td>572          </td> <td>ORD        </td> <td>385  </td> <td>9.32979               </td>
        </tr>
    </tbody>
</table>
<p>... (13815 rows omitted)</p>
</div>


</div>
</div>
</div>



What this shows is that it is possible for data to be many SDs above average (and for flights to be delayed by almost 10 hours). The highest value of delay is more than 14 in standard units. 

However, the proportion of these extreme values is small, and Chebychev's bounds still hold true. For example, let us calculate the percent of delay times that are in the range "average $\pm$ 3 SDs". This is the same as the percent of times for which the standard units are in the range (-3, 3). That is about 98%, as computed below, consistent with Chebychev's bound of "at least 89%". 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
within_3_sd = united.where('Delay (Standard Units)', are.between(-3, 3))
within_3_sd.num_rows/united.num_rows

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.9790235081374322
```


</div>
</div>
</div>



The histogram of delay times is shown below, with the horizontal axis in standard units. By the table above, the right hand tail continues all the way out to $z=14.27$ standard units (580 minutes). The area of the histogram outside the range $z=-3$ to $z=3$ is about 2%, put together in tiny little bits that are mostly invisible in the histogram.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
united.hist('Delay (Standard Units)', bins=np.arange(-5, 15.5, 0.5))
plots.xticks(np.arange(-6, 17, 3));

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/14/2/Variability_59_0.png)

</div>
</div>
</div>

