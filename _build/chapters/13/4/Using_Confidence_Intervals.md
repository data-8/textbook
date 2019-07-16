---
redirect_from:
  - "/chapters/13/4/using-confidence-intervals"
interact_link: content/chapters/13/4/Using_Confidence_Intervals.ipynb
kernel_name: Python [Root]
has_widgets: false
title: 'Using Confidence Intervals'
prev_page:
  url: /chapters/13/3/Confidence_Intervals
  title: 'Confidence Intervals'
next_page:
  url: /chapters/14/Why_the_Mean_Matters
  title: 'Why the Mean Matters'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bootstrap_median(original_sample, label, replications):
    
    """Returns an array of bootstrapped sample medians:
    original_sample: table containing the original sample
    label: label of column containing the variable
    replications: number of bootstrap samples
    """
    
    just_one_column = original_sample.select(label)
    medians = make_array()
    for i in np.arange(replications):
        bootstrap_sample = just_one_column.sample()
        resampled_median = percentile(50, bootstrap_sample.column(0))
        medians = np.append(medians, resampled_median)
        
    return medians

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bootstrap_mean(original_sample, label, replications):
    
    """Returns an array of bootstrapped sample means:
    original_sample: table containing the original sample
    label: label of column containing the variable
    replications: number of bootstrap samples
    """
    
    just_one_column = original_sample.select(label)
    means = make_array()
    for i in np.arange(replications):
        bootstrap_sample = just_one_column.sample()
        resampled_mean = np.mean(bootstrap_sample.column(0))
        means = np.append(means, resampled_mean)
        
    return means

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bootstrap_proportion(original_sample, label, replications):
    
    """Returns an array of bootstrapped sample proportions:
    original_sample: table containing the original sample
    label: label of column containing the Boolean variable
    replications: number of bootstrap samples
    """
    
    just_one_column = original_sample.select(label)
    proportions = make_array()
    for i in np.arange(replications):
        bootstrap_sample = just_one_column.sample()
        resample_array = bootstrap_sample.column(0)
        resampled_proportion = np.count_nonzero(resample_array)/len(resample_array)
        proportions = np.append(proportions, resampled_proportion)
        
    return proportions

```
</div>

</div>



### Using Confidence Intervals
A confidence interval has a single purpose – to estimate an unknown parameter based on data in a random sample. In the last section, we said that the interval (36%, 42%) was an approximate 95% confidence interval for the percent of smokers among mothers in the population. That was a formal way of saying that by our estimate, the percent of smokers among the mothers in the population was somewhere between 36% and 42%, and that our process of estimation is correct about 95% of the time.

It is important to resist the impulse to use confidence intervals for other purposes. For example, recall that we calculated the interval (26.9 years, 27.6 years) as an approximate 95% confidence interval for the average age of mothers in the population. A dismayingly common misuse of the interval is to conclude that about 95% of the women were between 26.9 years and 27.6 years old. You don't need to know much about confidence intervals to see that this can't be right – you wouldn't expect 95% of mothers to all be within a few months of each other in age. Indeed, the histogram of the sampled ages shows quite a bit of variation.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
baby = Table.read_table(path_data + 'baby.csv')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
baby.select('Maternal Age').hist()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/4/Using_Confidence_Intervals_6_0.png)

</div>
</div>
</div>



A small percent of the sampled ages are in the (26.9, 27.6) interval, and you would expect a similar small percent in the population. The interval just estimates one number: the *average* of all the ages in the population.



However, estimating a parameter by confidence intervals does have an important use besides just telling us roughly how big the parameter is. 



### Using a Confidence Interval to Test Hypotheses
Our approximate 95% confidence interval for the average age in the population goes from 26.9 years to 27.6 years. Suppose someone wants to test the following hypotheses:

**Null hypothesis.** The average age in the population is 30 years.

**Alternative hypothesis.** The average age in the population is not 30 years.

Then, if you were using the 5% cutoff for the P-value, you would reject the null hypothesis. This is because 30 is not in the 95% confidence interval for the population average. At the 5% level of significance, 30 is not a plausible value for the population average.

This use of confidence intervals is the result of a *duality* between confidence intervals and tests: if you are testing whether or not the population mean is a particular value *x*, and you use the 5% cutoff for the P-value, then you will reject the null hypothesis if *x* is not in your 95% confidence interval for the mean. 

This can be established by statistical theory. In practice, it just boils down to checking whether or not the value specified in the null hypothesis lies in the confidence interval.

If you were using the 1% cutoff for the P-value, you would have to check if the value specified in the null hypothesis lies in a 99% confidence interval for the population mean.

To a rough approximation, these statements are also true for population proportions, provided the sample is large.



While we now have a way of using confidence intervals to test a particular kind of hypothesis, you might wonder about the value of testing whether or not the average age in a population is equal to 30. Indeed, the value isn't clear. But there are some situations in which a test of this kind of hypothesis is both natural and useful.



We will study this in the context of data that are a subset of the information gathered in a randomized controlled trial about treatments for Hodgkin's disease. Hodgkin's disease is a cancer that typically affects young people. The disease is curable but the treatment can be very harsh. The purpose of the trial was to come up with dosage that would cure the cancer but minimize the adverse effects on the patients. 

This table ``hodgkins`` contains data on the effect that the treatment had on the lungs of 22 patients. The columns are:

- Height in cm
- A measure of radiation to the mantle (neck, chest, under arms)
- A measure of chemotherapy
- A score of the health of the lungs at baseline, that is, at the start of the treatment; higher scores correspond to more healthy lungs
- The same score of the health of the lungs, 15 months after treatment



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hodgkins = Table.read_table(path_data + 'hodgkins.csv')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hodgkins

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>height</th> <th>rad</th> <th>chemo</th> <th>base</th> <th>month15</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>164   </td> <td>679 </td> <td>180  </td> <td>160.57</td> <td>87.77  </td>
        </tr>
        <tr>
            <td>168   </td> <td>311 </td> <td>180  </td> <td>98.24 </td> <td>67.62  </td>
        </tr>
        <tr>
            <td>173   </td> <td>388 </td> <td>239  </td> <td>129.04</td> <td>133.33 </td>
        </tr>
        <tr>
            <td>157   </td> <td>370 </td> <td>168  </td> <td>85.41 </td> <td>81.28  </td>
        </tr>
        <tr>
            <td>160   </td> <td>468 </td> <td>151  </td> <td>67.94 </td> <td>79.26  </td>
        </tr>
        <tr>
            <td>170   </td> <td>341 </td> <td>96   </td> <td>150.51</td> <td>80.97  </td>
        </tr>
        <tr>
            <td>163   </td> <td>453 </td> <td>134  </td> <td>129.88</td> <td>69.24  </td>
        </tr>
        <tr>
            <td>175   </td> <td>529 </td> <td>264  </td> <td>87.45 </td> <td>56.48  </td>
        </tr>
        <tr>
            <td>185   </td> <td>392 </td> <td>240  </td> <td>149.84</td> <td>106.99 </td>
        </tr>
        <tr>
            <td>178   </td> <td>479 </td> <td>216  </td> <td>92.24 </td> <td>73.43  </td>
        </tr>
    </tbody>
</table>
<p>... (12 rows omitted)</p>
</div>


</div>
</div>
</div>



We will compare the baseline and 15-month scores. As each row corresponds to one patient, we say that the sample of baseline scores and the sample of 15-month scores are *paired* - they are not just two sets of 22 values each, but 22 pairs of values, one for each patient.

At a glance, you can see that the 15-month scores tend to be lower than the baseline scores – the sampled patients' lungs seem to be doing worse 15 months after the treatment. This is confirmed by the mostly positive values in the column `drop`, the amount by which the score dropped from baseline to 15 months.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hodgkins = hodgkins.with_column(
    'drop', hodgkins.column('base') - hodgkins.column('month15')
)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hodgkins

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>height</th> <th>rad</th> <th>chemo</th> <th>base</th> <th>month15</th> <th>drop</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>164   </td> <td>679 </td> <td>180  </td> <td>160.57</td> <td>87.77  </td> <td>72.8  </td>
        </tr>
        <tr>
            <td>168   </td> <td>311 </td> <td>180  </td> <td>98.24 </td> <td>67.62  </td> <td>30.62 </td>
        </tr>
        <tr>
            <td>173   </td> <td>388 </td> <td>239  </td> <td>129.04</td> <td>133.33 </td> <td>-4.29 </td>
        </tr>
        <tr>
            <td>157   </td> <td>370 </td> <td>168  </td> <td>85.41 </td> <td>81.28  </td> <td>4.13  </td>
        </tr>
        <tr>
            <td>160   </td> <td>468 </td> <td>151  </td> <td>67.94 </td> <td>79.26  </td> <td>-11.32</td>
        </tr>
        <tr>
            <td>170   </td> <td>341 </td> <td>96   </td> <td>150.51</td> <td>80.97  </td> <td>69.54 </td>
        </tr>
        <tr>
            <td>163   </td> <td>453 </td> <td>134  </td> <td>129.88</td> <td>69.24  </td> <td>60.64 </td>
        </tr>
        <tr>
            <td>175   </td> <td>529 </td> <td>264  </td> <td>87.45 </td> <td>56.48  </td> <td>30.97 </td>
        </tr>
        <tr>
            <td>185   </td> <td>392 </td> <td>240  </td> <td>149.84</td> <td>106.99 </td> <td>42.85 </td>
        </tr>
        <tr>
            <td>178   </td> <td>479 </td> <td>216  </td> <td>92.24 </td> <td>73.43  </td> <td>18.81 </td>
        </tr>
    </tbody>
</table>
<p>... (12 rows omitted)</p>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hodgkins.select('drop').hist(bins=np.arange(-20, 81, 20))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/4/Using_Confidence_Intervals_17_0.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.mean(hodgkins.column('drop'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
28.615909090909096
```


</div>
</div>
</div>



But could this be the result of chance variation? It really doesn't seem so, but the data are from a random sample. Could it be that in the entire population of patients, the average drop is just 0?

To answer this, we can set up two hypotheses:

**Null hypothesis.** In the population, the average drop is 0.

**Alternative hypothesis.** In the population, the average drop is not 0.

To test this hypothesis with a 1% cutoff for the P-value, let's construct an approximate 99% confidence interval for the average drop in the population.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bstrap_means = bootstrap_mean(hodgkins, 'drop', 10000)

left = percentile(0.5, bstrap_means)
right = percentile(99.5, bstrap_means)

make_array(left, right)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([17.22636364, 40.54045455])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resampled_means = Table().with_column(
    'Bootstrap Sample Mean', bstrap_means
)
resampled_means.hist()
plots.plot(make_array(left, right), make_array(0, 0), color='yellow', lw=8);

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/4/Using_Confidence_Intervals_21_0.png)

</div>
</div>
</div>



The 99% confidence interval for the average drop in the population goes from about 17 to about 40. The interval doesn't contain 0. So we reject the null hypothesis.

But notice that we have done better than simply concluding that the average drop in the population isn't 0. We have estimated how big the average drop is. That's a more useful result than just saying, "It's not 0."

**A note on accuracy.** Our confidence interval is quite wide, for two main reasons:
- The confidence level is high (99%).
- The sample size is relatively small compared to those in our earlier examples.

In the next chapter, we will examine how the sample size affects accuracy. We will also examine how the empirical distributions of sample means so often come out bell shaped even though the distributions of the underlying data are not bell shaped at all.



### Endnote
The terminology of a field usually comes from the leading researchers in that field. [Brad Efron](https://en.wikipedia.org/wiki/Bradley_Efron), who first proposed the bootstrap technique, used a term that has [American origins](https://en.wikipedia.org/wiki/Bootstrapping). Not to be outdone, Chinese statisticians have [proposed their own method](http://econpapers.repec.org/article/eeestapro/v_3a37_3ay_3a1998_3ai_3a4_3ap_3a321-329.htm).

