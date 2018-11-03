---
redirect_from:
  - "/chapters/12/1/ab-testing"
interact_link: content/chapters/12/1/AB_Testing.ipynb
title: 'A/B Testing'
prev_page:
  url: /chapters/12/Comparing_Two_Samples
  title: 'Comparing Two Samples'
next_page:
  url: /chapters/12/2/Deflategate
  title: 'Deflategate'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### A/B Testing
In modern data analytics, deciding whether two numerical samples come from the same underlying distribution is called *A/B testing*. The name refers to the labels of the two samples, A and B.

We will develop the method in the context of an example. The data come from a sample of newborns in a large hospital system. We will treat it as if it were a simple random sample though the sampling was done in multiple stages. [Stat Labs](https://www.stat.berkeley.edu/~statlabs/) by Deborah Nolan and Terry Speed has details about a larger dataset from which this set is drawn. 

### Smokers and Nonsmokers
The table `baby` contains the following variables for 1,174 mother-baby pairs: the baby's birth weight in ounces, the number of gestational days, the mother's age in completed years, the mother's height in inches, pregnancy weight in pounds, and whether or not the mother smoked during pregnancy.



{:.input_area}
```python
baby = Table.read_table(path_data + 'baby.csv')
baby
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Birth Weight</th> <th>Gestational Days</th> <th>Maternal Age</th> <th>Maternal Height</th> <th>Maternal Pregnancy Weight</th> <th>Maternal Smoker</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>120         </td> <td>284             </td> <td>27          </td> <td>62             </td> <td>100                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>113         </td> <td>282             </td> <td>33          </td> <td>64             </td> <td>135                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>128         </td> <td>279             </td> <td>28          </td> <td>64             </td> <td>115                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>108         </td> <td>282             </td> <td>23          </td> <td>67             </td> <td>125                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>136         </td> <td>286             </td> <td>25          </td> <td>62             </td> <td>93                       </td> <td>False          </td>
        </tr>
        <tr>
            <td>138         </td> <td>244             </td> <td>33          </td> <td>62             </td> <td>178                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>132         </td> <td>245             </td> <td>23          </td> <td>65             </td> <td>140                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>120         </td> <td>289             </td> <td>25          </td> <td>62             </td> <td>125                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>143         </td> <td>299             </td> <td>30          </td> <td>66             </td> <td>136                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>140         </td> <td>351             </td> <td>27          </td> <td>68             </td> <td>120                      </td> <td>False          </td>
        </tr>
    </tbody>
</table>
<p>... (1164 rows omitted)</p>
</div>



One of the aims of the study was to see whether maternal smoking was associated with birth weight. Let's see what we can say about the two variables.

We'll start by selecting just `Birth Weight` and `Maternal Smoker`. There are 715 non-smokers among the women in the sample, and 459 smokers.



{:.input_area}
```python
smoking_and_birthweight = baby.select('Maternal Smoker', 'Birth Weight')
```




{:.input_area}
```python
smoking_and_birthweight.group('Maternal Smoker')
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>715  </td>
        </tr>
        <tr>
            <td>True           </td> <td>459  </td>
        </tr>
    </tbody>
</table>
</div>



Let's look at the distribution of the birth weights of the babies of the non-smoking mothers compared to those of the smoking mothers. To generate two overlaid histograms, we will use `hist` with the optional `group` argument which is a column label or index. The rows of the table are first grouped by this column and then a histogram is drawn for each one.



{:.input_area}
```python
smoking_and_birthweight.hist('Birth Weight', group = 'Maternal Smoker')
```



![png](../../../images/chapters/12/1/AB_Testing_7_0.png)


The distribution of the weights of the babies born to mothers who smoked appears to be shifted slightly to the left of the distribution corresponding to non-smoking mothers. The weights of the babies of the mothers who smoked seem lower, on average than the weights of the babies of the non-smokers. 

This raises the question of whether the difference reflects just chance variation or a difference in the distributions in the larger population. Could it be that there is no difference between the two distributions in the population, but we are seeing a difference in the samples just because of the mothers who happened to be selected?

### The Hypotheses
We can try to answer this question by a test of hypotheses. The chance model that we will test says that there is no underlying difference; the distributions in the samples are different just due to chance. Formally, this is the null hypothesis.

**Null hypothesis:** In the population, the distribution of birth weights of babies is the same for mothers who don't smoke as for mothers who do. The difference in the sample is due to chance.

**Alternative hypothesis:** In the population, the babies of the mothers who smoke have a lower birth weight, on average, than the babies of the non-smokers.

### Test Statistic
The alternative hypothesis compares the average birth weights of the two groups and says that the average for the mothers who smoke is smaller. Therefore it is reasonable for us to use the difference between the two group means as our statistic. 

We will do the subtraction in the order "average weight of the smoking group $-$ average weight of the non-smoking group". Small values (that is, large negative values) of this statistic will favor the alternative hypothesis. 

The observed value of the test statistic is about $-9.27$ ounces.



{:.input_area}
```python
means_table = smoking_and_birthweight.group('Maternal Smoker', np.average)
means_table
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>Birth Weight average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>123.085             </td>
        </tr>
        <tr>
            <td>True           </td> <td>113.819             </td>
        </tr>
    </tbody>
</table>
</div>





{:.input_area}
```python
means = means_table.column(1)
observed_difference = means.item(1) - means.item(0)
observed_difference
```





{:.output_data_text}
```
-9.266142572024918
```



### Predicting the Statistic Under the Null Hypothesis

To see how the statistic should vary under the null hypothesis, we have to figure out how to simulate the statistic under that hypothesis. A clever method based on *random permutations* does just that.

If there were no difference between the two distributions in the underlying population, then whether a birth weight has the label `True` or `False` with respect to maternal smoking should make no difference to the average. The idea, then, is to shuffle all the birth weights randomly among the mothers. This is called *random permutation*. 

Take the difference of the two new group means: the mean of the shuffled weights assigned to the smokers and the mean of the shuffled weights assigned to the non-smokers. This is a simulated value of the test statistic under the null hypothesis.

Let's see how to do this. It's always a good idea to start with the data.



{:.input_area}
```python
smoking_and_birthweight
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>Birth Weight</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>120         </td>
        </tr>
        <tr>
            <td>False          </td> <td>113         </td>
        </tr>
        <tr>
            <td>True           </td> <td>128         </td>
        </tr>
        <tr>
            <td>True           </td> <td>108         </td>
        </tr>
        <tr>
            <td>False          </td> <td>136         </td>
        </tr>
        <tr>
            <td>False          </td> <td>138         </td>
        </tr>
        <tr>
            <td>False          </td> <td>132         </td>
        </tr>
        <tr>
            <td>False          </td> <td>120         </td>
        </tr>
        <tr>
            <td>True           </td> <td>143         </td>
        </tr>
        <tr>
            <td>False          </td> <td>140         </td>
        </tr>
    </tbody>
</table>
<p>... (1164 rows omitted)</p>
</div>



There are 1,174 rows in the table. To shuffle all the birthweights, we will draw a random sample of 1,174 rows without replacement. Then the sample will include all the rows of the table, in random order. 

We can use the Table method `sample` with the optional `with_replacement=False` argument. We don't have to specify a sample size, because by default, `sample` draws as many times as there are rows in the table.



{:.input_area}
```python
shuffled_weights = smoking_and_birthweight.sample(with_replacement = False).column(1)
original_and_shuffled = smoking_and_birthweight.with_column('Shuffled Birth Weight', shuffled_weights)
```




{:.input_area}
```python
original_and_shuffled
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>Birth Weight</th> <th>Shuffled Birth Weight</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>120         </td> <td>94                   </td>
        </tr>
        <tr>
            <td>False          </td> <td>113         </td> <td>96                   </td>
        </tr>
        <tr>
            <td>True           </td> <td>128         </td> <td>102                  </td>
        </tr>
        <tr>
            <td>True           </td> <td>108         </td> <td>101                  </td>
        </tr>
        <tr>
            <td>False          </td> <td>136         </td> <td>55                   </td>
        </tr>
        <tr>
            <td>False          </td> <td>138         </td> <td>122                  </td>
        </tr>
        <tr>
            <td>False          </td> <td>132         </td> <td>116                  </td>
        </tr>
        <tr>
            <td>False          </td> <td>120         </td> <td>163                  </td>
        </tr>
        <tr>
            <td>True           </td> <td>143         </td> <td>110                  </td>
        </tr>
        <tr>
            <td>False          </td> <td>140         </td> <td>137                  </td>
        </tr>
    </tbody>
</table>
<p>... (1164 rows omitted)</p>
</div>



Each mother now has a random birth weight assigned to her. If the null hypothesis is true, all these random arrangements should be equally likely.

Let's see how different the average weights are in the two randomly selected groups.



{:.input_area}
```python
all_group_means = original_and_shuffled.group('Maternal Smoker', np.average)
all_group_means
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>Birth Weight average</th> <th>Shuffled Birth Weight average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>123.085             </td> <td>118.91                       </td>
        </tr>
        <tr>
            <td>True           </td> <td>113.819             </td> <td>120.322                      </td>
        </tr>
    </tbody>
</table>
</div>



The averages of the two randomly selected groups are quite a bit closer than the averages of the two original groups.



{:.input_area}
```python
shuffled_means = original_and_shuffled.group('Maternal Smoker', np.average).column(2)
difference = shuffled_means.item(1) - shuffled_means.item(0)
difference
```





{:.output_data_text}
```
1.4119505766564515
```



But could a different shuffle have resulted in a larger difference between the group averages? To get a sense of the variability, we must simulate the difference many times. 

Let's collect all the code that we need for simulating one value of the difference between averages, under the null hypothesis. Notice that because we are using the same label each time for the column of shuffled weights, the existing column just gets overwritten by the newly generated one. This works well for us because we don't need to save all the shuffled values. We just need to save the value of the statistic.



{:.input_area}
```python
# Generate one value of the test statistic under the null hypothesis

# Shuffle all the weights and assign the shuffled weights to the two groups of mothers
shuffled_weights = smoking_and_birthweight.sample(with_replacement = False).column(1)
original_and_shuffled = smoking_and_birthweight.with_column('Shuffled Birth Weight', shuffled_weights)

# Find the difference between the means of two randomly assigned groups
shuffled_means = original_and_shuffled.group('Maternal Smoker', np.average).column(2)
difference = shuffled_means.item(1) - shuffled_means.item(0)
difference
```





{:.output_data_text}
```
-0.48756951109892555
```



### Permutation Test
Tests based on random permutations of the data are called *permutation tests*. We are performing one in this example. In the cell below, we will simulate our test statistic – the difference between the averages of the two groups – many times and collect the differences in an array. The code in the body of the for loop is just copied over from the cell above.



{:.input_area}
```python
differences = make_array()

repetitions = 5000
for i in np.arange(repetitions):
    
    shuffled_weights = smoking_and_birthweight.sample(with_replacement = False).column(1)
    original_and_shuffled = smoking_and_birthweight.with_column('Shuffled Birth Weight', shuffled_weights)

    shuffled_means = original_and_shuffled.group('Maternal Smoker', np.average).column(2)
    simulated_difference = shuffled_means.item(1) - shuffled_means.item(0)
    
    differences = np.append(differences, simulated_difference)
    
```


The array `differences` contains 5,000 simulated values of our test statistic – the difference between the mean weight in the smoking group and the mean weight in the non-smoking group. 

### Conclusion of the Test
The histogram below shows the distribution of these 5,000 values. It is the empirical distribution of the test statistic simulated under the null hypothesis. It is a prediction made by the null hypothesis, about the statistic.



{:.input_area}
```python
Table().with_column('Difference Between Group Averages', differences).hist()
print('Observed Difference:', observed_difference)
plots.title('Prediction Under the Null Hypothesis');
```


{:.output_stream}
```
Observed Difference: -9.266142572024918

```


![png](../../../images/chapters/12/1/AB_Testing_27_1.png)


Notice how the distribution is centered around 0. This makes sense, because under the null hypothesis the two groups should have roughly the same average. Therefore the difference between the group averages should be around 0.

The observed difference in the original sample is about $-9.27$ ounces, which doesn't even appear on the horizontal scale of the histogram. The observed value of the statistic and the predicted behavior of the statistic under the null hypothesis are inconsistent. 

The conclusion of the test is that the data support the alternative more than they support the null. The average birth weight of babies born to mothers who smoke is less than the average birth weight of babies born to non-smokers.

If you want to compute an empirical P-value, remember that low values of the statistic favor the alternative hypothesis. 



{:.input_area}
```python
empirical_P = np.count_nonzero(differences <= observed_difference) / repetitions
empirical_P
```





{:.output_data_text}
```
0.0
```



The empirical P-value is 0, meaning that none of the 5,000 observed samples resulted in a difference of -9.27 or lower. This is an approximation; the exact chance of getting a difference in that range is not 0 but it is vanishingly small.

### A Function to Simulate the Differences Under the Null Hypothesis
We will want to perform permutation tests for the difference between averages in other contexts as well. Let us define a function that generates the array of simulated differences, based on the code that we wrote above. That will save us time later.

The function `difference_of_permuted_sample_means` takes four arguments:
- the name of the data table
- the label of the column containing the variable whose average is of interest
- the label of the column of group labels
- the number of repetitions

It returns and array of simulated differences in group means, each computed by first randomly permuting the data and assigning random values to each group. The length of the array is equal to the number of repetitions.



{:.input_area}
```python
def permuted_sample_average_difference(table, label, group_label, repetitions):
    
    tbl = table.select(group_label, label)
    
    differences = make_array()
    for i in np.arange(repetitions):
        shuffled = tbl.sample(with_replacement = False).column(1)
        original_and_shuffled = tbl.with_column('Shuffled Data', shuffled)

        shuffled_means = original_and_shuffled.group(group_label, np.average).column(2)
        simulated_difference = shuffled_means.item(1) - shuffled_means.item(0)
    
        differences = np.append(differences, simulated_difference)
    
    return differences   
```


As an example of the use of this function, we will test whether there was any difference in the ages of the smoking and non-smoking mothers. The histograms of the two distributions in the sample are a little different. The smokers seem a little younger on average.



{:.input_area}
```python
smoking_and_age = baby.select('Maternal Smoker', 'Maternal Age')
smoking_and_age.hist('Maternal Age', group = 'Maternal Smoker')
```



![png](../../../images/chapters/12/1/AB_Testing_34_0.png)




{:.input_area}
```python
smoking_and_age.group('Maternal Smoker', np.average)
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Maternal Smoker</th> <th>Maternal Age average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>False          </td> <td>27.5441             </td>
        </tr>
        <tr>
            <td>True           </td> <td>26.7364             </td>
        </tr>
    </tbody>
</table>
</div>



The observed difference between the average ages is about $-0.8$ years.



{:.input_area}
```python
observed_means = smoking_and_age.group('Maternal Smoker', np.average).column(1)
observed_difference = observed_means.item(1) - observed_means.item(0)
observed_difference
```





{:.output_data_text}
```
-0.8076725017901509
```



If the underlying distributions of ages in the two groups are the same, then the empirical distribution of the difference based on permuted samples will predict how the statistic will vary due to chance.

We can generate such differences using the function we just defined.



{:.input_area}
```python
differences = permuted_sample_average_difference(baby, 'Maternal Age', 'Maternal Smoker', 5000)
```


The observed difference is in the tail of the empirical distribution of the differences simulated under the null hypothesis. 



{:.input_area}
```python
Table().with_column('Difference Between Group Averages', differences).hist()
plots.scatter(observed_difference, 0, color='red', s=30)
plots.title('Prediction Under the Null Hypothesis')
print('Observed Difference:', observed_difference)
```


{:.output_stream}
```
Observed Difference: -0.8076725017901509

```


![png](../../../images/chapters/12/1/AB_Testing_41_1.png)


The empirical P-value of the test is the proportion of simulated differences that were equal to or less than the observed difference. This is because low values of the difference favor the alternative hypothesis that the smokers were younger on average.



{:.input_area}
```python
empirical_P = np.count_nonzero(differences <= observed_difference) / 5000
empirical_P
```





{:.output_data_text}
```
0.01
```



The empirical P-value is just over 1%, which is less than 5% and therefore the result is statistically significant. The test supports the hypothesis that the smokers were younger on average.
