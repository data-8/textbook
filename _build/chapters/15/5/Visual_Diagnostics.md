---
redirect_from:
  - "/chapters/15/5/visual-diagnostics"
interact_link: content/chapters/15/5/Visual_Diagnostics.ipynb
title: 'Visual Diagnostics'
prev_page:
  url: /chapters/15/4/Least_Squares_Regression
  title: 'Least Squares Regression'
next_page:
  url: /chapters/15/6/Numerical_Diagnostics
  title: 'Numerical Diagnostics'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Visual Diagnostics
Suppose a data scientist has decided to use linear regression to estimate values of a response variable based on a predictor. To see how well this method of estmation performs, the data scientist must how far off the estimates are from the actual values. These differences are called *residuals*.

$$
\mbox{residual} ~=~ \mbox{observed value} ~-~ \mbox{regression estimate}
$$

A residual is what's left over – the residue – after estimation. 

Residuals are the vertical distances of the points from the regression line. There is one residual for each point in the scatter plot. The residual is the difference between the observed value of $y$ and the fitted value of $y$, so fr the point $(x, y)$,

$$
\mbox{residual} ~~ = ~~ y ~-~
\mbox{fitted value of }y
~~ = ~~ y ~-~
\mbox{height of regression line at }x
$$

The function `residual` calculates the residuals. The calculation assumes all the relevant functions we have already defined: `standard_units`, `correlation`, `slope`, `intercept`, and `fit`.



{:.input_area}
```python
def residual(table, x, y):
    return table.column(y) - fit(table, x, y)
```


Continuing our example of using Galton's data to estimate the heights of adult children (the response) based on the midparent height (the predictor), let us calculate the fitted values and the residuals.



{:.input_area}
```python
heights = heights.with_columns(
        'Fitted Value', fit(heights, 'MidParent', 'Child'),
        'Residual', residual(heights, 'MidParent', 'Child')
    )
heights
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>MidParent</th> <th>Child</th> <th>Fitted Value</th> <th>Residual</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>75.43    </td> <td>73.2 </td> <td>70.7124     </td> <td>2.48763  </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69.2 </td> <td>70.7124     </td> <td>-1.51237 </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69   </td> <td>70.7124     </td> <td>-1.71237 </td>
        </tr>
        <tr>
            <td>75.43    </td> <td>69   </td> <td>70.7124     </td> <td>-1.71237 </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>73.5 </td> <td>69.5842     </td> <td>3.91576  </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>72.5 </td> <td>69.5842     </td> <td>2.91576  </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>65.5 </td> <td>69.5842     </td> <td>-4.08424 </td>
        </tr>
        <tr>
            <td>73.66    </td> <td>65.5 </td> <td>69.5842     </td> <td>-4.08424 </td>
        </tr>
        <tr>
            <td>72.06    </td> <td>71   </td> <td>68.5645     </td> <td>2.43553  </td>
        </tr>
        <tr>
            <td>72.06    </td> <td>68   </td> <td>68.5645     </td> <td>-0.564467</td>
        </tr>
    </tbody>
</table>
<p>... (924 rows omitted)</p>
</div>



When there are so many variables to work with, it is always helpful to start with visualization. The function `scatter_fit` draws the scatter plot of the data, as well as the regression line. 



{:.input_area}
```python
def scatter_fit(table, x, y):
    table.scatter(x, y, s=15)
    plots.plot(table.column(x), fit(table, x, y), lw=4, color='gold')
    plots.xlabel(x)
    plots.ylabel(y)
```




{:.input_area}
```python
scatter_fit(heights, 'MidParent', 'Child')
```



![png](../../../images/chapters/15/5/Visual_Diagnostics_6_0.png)


A *residual plot* can be drawn by plotting the residuals against the predictor variable. The function `residual_plot` does just that. 



{:.input_area}
```python
def residual_plot(table, x, y):
    x_array = table.column(x)
    t = Table().with_columns(
            x, x_array,
            'residuals', residual(table, x, y)
        )
    t.scatter(x, 'residuals', color='r')
    xlims = make_array(min(x_array), max(x_array))
    plots.plot(xlims, make_array(0, 0), color='darkblue', lw=4)
    plots.title('Residual Plot')
```




{:.input_area}
```python
residual_plot(heights, 'MidParent', 'Child')
```



![png](../../../images/chapters/15/5/Visual_Diagnostics_9_0.png)


The midparent heights are on the horizontal axis, as in the original scatter plot. But now the vertical axis shows the residuals. Notice that the plot appears to be centered around the horizontal line at the level 0 (shown in dark blue). Notice also that the plot shows no upward or downward trend. We will observe later that this is true of all regressions.

### Regression Diagnostics
Residual plots help us make visual assessments of the quality of a linear regression analysis. Such assessments are called *diagnostics*. The function ``regression_diagnostic_plots`` draws the original scatter plot as well as the residual plot for ease of comparison.



{:.input_area}
```python
def regression_diagnostic_plots(table, x, y):
    scatter_fit(table, x, y)
    residual_plot(table, x, y)
```




{:.input_area}
```python
regression_diagnostic_plots(heights, 'MidParent', 'Child')
```



![png](../../../images/chapters/15/5/Visual_Diagnostics_13_0.png)



![png](../../../images/chapters/15/5/Visual_Diagnostics_13_1.png)


This residual plot indicates that linear regression was a reasonable method of estimation. Notice how the residuals are distributed fairly symmetrically above and below the horizontal line at 0, corresponding to the original scatter plot being roughly symmetrical above and below. Notice also that the vertical spread of the plot is fairly even across the most common values of the children's heights. In other words, apart from a few outlying points, the plot isn't narrower in some places and wider in others.

In other words, the accuracy of the regression appears to be about the same across the observed range of the predictor variable. 

**The residual plot of a good regression shows no pattern. The residuals look about the same, above and below the horizontal line at 0, across the range of the predictor variable.**

### Detecting Nonlinearity
Drawing the scatter plot of the data usually gives an indication of whether the relation between the two variables is non-linear. Often, however, it is easier to spot non-linearity in a residual plot than in the original scatter plot. This is usually because of the scales of the two plots: the residual plot allows us to zoom in on the errors and hence makes it easier to spot patterns.

<img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Dugong_dugon.jpg"/>

Our data are a [dataset](http://www.statsci.org/data/oz/dugongs.html)  on the age and length of dugongs, which are marine mammals related to manatees and sea cows (image from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dugong_dugon.jpg)). The data are in a table called `dugong`. Age is measured in years and length in meters. Because dugongs tend not to keep track of their birthdays, ages are estimated based on variables such as the condition of their teeth.



{:.input_area}
```python
dugong = Table.read_table('http://www.statsci.org/data/oz/dugongs.txt')
dugong = dugong.move_to_start('Length')
dugong
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Length</th> <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1.8   </td> <td>1   </td>
        </tr>
        <tr>
            <td>1.85  </td> <td>1.5 </td>
        </tr>
        <tr>
            <td>1.87  </td> <td>1.5 </td>
        </tr>
        <tr>
            <td>1.77  </td> <td>1.5 </td>
        </tr>
        <tr>
            <td>2.02  </td> <td>2.5 </td>
        </tr>
        <tr>
            <td>2.27  </td> <td>4   </td>
        </tr>
        <tr>
            <td>2.15  </td> <td>5   </td>
        </tr>
        <tr>
            <td>2.26  </td> <td>5   </td>
        </tr>
        <tr>
            <td>2.35  </td> <td>7   </td>
        </tr>
        <tr>
            <td>2.47  </td> <td>8   </td>
        </tr>
    </tbody>
</table>
<p>... (17 rows omitted)</p>
</div>



If we could measure the length of a dugong, what could we say about its age? Let's examine what our data say. Here is a regression of age (the response) on length (the predictor). The correlation between the two variables is substantial, at 0.83.



{:.input_area}
```python
correlation(dugong, 'Length', 'Age')
```





{:.output_data_text}
```
0.8296474554905714
```



High correlation notwithstanding, the plot shows a curved pattern that is much more visible in the residual plot.



{:.input_area}
```python
regression_diagnostic_plots(dugong, 'Length', 'Age')
```



![png](../../../images/chapters/15/5/Visual_Diagnostics_21_0.png)



![png](../../../images/chapters/15/5/Visual_Diagnostics_21_1.png)


While you can spot the non-linearity in the original scatter, it is more clearly evident in the residual plot.

At the low end of the lengths, the residuals are almost all positive; then they are almost all negative; then positive again at the high end of lengths. In other words the regression estimates have a pattern of being too high, then too low, then too high. That means it would have been better to use a curve instead of a straight line to estimate the ages.

**When a residual plot shows a pattern, there may be a non-linear relation between the variables.**

### Detecting Heteroscedasticity

*Heteroscedasticity* is a word that will surely be of interest to those who are preparing for Spelling Bees. For data scientists, its interest lies in its meaning, which is "uneven spread". 

Recall the table `hybrid` that contains data on hybrid cars in the U.S. Here is a regression of fuel efficiency on the rate of acceleration. The association is negative: cars that accelearate quickly tend to be less efficient.



{:.input_area}
```python
regression_diagnostic_plots(hybrid, 'acceleration', 'mpg')
```



![png](../../../images/chapters/15/5/Visual_Diagnostics_24_0.png)



![png](../../../images/chapters/15/5/Visual_Diagnostics_24_1.png)


Notice how the residual plot flares out towards the low end of the accelerations. In other words, the variability in the size of the errors is greater for low values of acceleration than for high values. Uneven variation is often more easily noticed in a residual plot than in the original scatter plot.

**If the residual plot shows uneven variation about the horizontal line at 0, the regression estimates are not equally accurate across the range of the predictor variable.**
