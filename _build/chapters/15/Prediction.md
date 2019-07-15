---
redirect_from:
  - "/chapters/15/prediction"
interact_link: content/chapters/15/Prediction.ipynb
kernel_name: Python [Root]
has_widgets: false
title: 'Prediction'
prev_page:
  url: /chapters/14/6/Choosing_a_Sample_Size
  title: 'Choosing a Sample Size'
next_page:
  url: /chapters/15/1/Correlation
  title: 'Correlation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Prediction

An important aspect of data science is to find out what data can tell us about the future. What do data about climate and pollution say about temperatures a few decades from now? Based on a person's internet profile, which websites are likely to interest them? How can a patient's medical history be used to judge how well he or she will respond to a treatment?

To answer such questions, data scientists have developed methods for making *predictions*. In this chapter we will study one of the most commonly used ways of predicting the value of one variable based on the value of another.



The foundations of the method were laid by [Sir Francis Galton](https://en.wikipedia.org/wiki/Francis_Galton). As we saw in Section 7.1, Galton studied how physical characteristics are passed down from one generation to the next. Among his best known work is the prediction of the heights of adults based on the heights of their parents. We have studied the dataset that Galton collected for this. The table `heights` contains his data on the midparent height and child's height (all in inches) for a population of 934 adult "children".



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Galton's data on heights of parents and their adult children
galton = Table.read_table(path_data + 'galton.csv')
heights = Table().with_columns(
    'MidParent', galton.column('midparentHeight'),
    'Child', galton.column('childHeight')
    )

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
heights

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>MidParent</th> <th>Child</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>75.43    </td> <td>73.2 </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69.2 </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69   </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69   </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>73.5 </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>72.5 </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>65.5 </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>65.5 </td>
        </tr>
        <tr>
            <td>72.06    </td> <td>71   </td>
        </tr>
        <tr>
            <td>72.06    </td> <td>68   </td>
        </tr>
    </tbody>
</table>
<p>... (924 rows omitted)</p>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
heights.scatter('MidParent')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/15/Prediction_5_0.png)

</div>
</div>
</div>



The primary reason for collecting the data was to be able to predict the adult height of a child born to parents similar to those in the dataset. We made these predictions in Section 7.1, after noticing the positive association between the two variables. 

Our approach was to base the prediction on all the points that correspond to a midparent height of around the midparent height of the new person. To do this, we wrote a function called `predict_child` which takes a midparent height as its argument and returns the average height of all the children who had midparent heights within half an inch of the argument.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def predict_child(mpht):
    """Return a prediction of the height of a child 
    whose parents have a midparent height of mpht.
    
    The prediction is the average height of the children 
    whose midparent height is in the range mpht plus or minus 0.5 inches.
    """
    
    close_points = heights.where('MidParent', are.between(mpht-0.5, mpht + 0.5))
    return close_points.column('Child').mean()                       

```
</div>

</div>



We applied the function to the column of `Midparent` heights, visualized our results.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Apply predict_child to all the midparent heights

heights_with_predictions = heights.with_column(
    'Prediction', heights.apply(predict_child, 'MidParent')
    )

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Draw the original scatter plot along with the predicted values

heights_with_predictions.scatter('MidParent')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/15/Prediction_10_0.png)

</div>
</div>
</div>



The prediction at a given midparent height lies roughly at the center of the vertical strip of points at the given height. This method of prediction is called *regression.* Later in this chapter we will see where this term came from. We will also see whether we can avoid our arbitrary definitions of "closeness" being "within 0.5 inches". But first we will develop a measure that can be used in many settings to decide how good one variable will be as a predictor of another.

