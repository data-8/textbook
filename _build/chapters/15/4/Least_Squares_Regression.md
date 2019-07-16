---
redirect_from:
  - "/chapters/15/4/least-squares-regression"
interact_link: content/chapters/15/4/Least_Squares_Regression.ipynb
kernel_name: python3
has_widgets: false
title: 'Least Squares Regression'
prev_page:
  url: /chapters/15/3/Method_of_Least_Squares
  title: 'The Method of Least Squares'
next_page:
  url: /chapters/15/5/Visual_Diagnostics
  title: 'Visual Diagnostics'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



### Least Squares Regression
In an earlier section, we developed formulas for the slope and intercept of the regression line through a *football shaped* scatter diagram. It turns out that the slope and intercept of the least squares line have the same formulas as those we developed, *regardless of the shape of the scatter plot*.

We saw this in the example about Little Women, but let's confirm it in an example where the scatter plot clearly isn't football shaped. For the data, we are once again indebted to the rich [data archive of Prof. Larry Winner](http://www.stat.ufl.edu/~winner/datasets.html) of the University of Florida. A [2013 study](http://digitalcommons.wku.edu/ijes/vol6/iss2/10/) in the International Journal of Exercise Science studied collegiate shot put athletes and examined the relation between strength and shot put distance. The population consists of 28 female collegiate athletes. Strength was measured by the the biggest amount (in kilograms) that the athlete lifted in the "1RM power clean" in the pre-season. The distance (in meters) was the athlete's personal best.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
shotput = Table.read_table(path_data + 'shotput.csv')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
shotput

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Weight Lifted</th> <th>Shot Put Distance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>37.5         </td> <td>6.4              </td>
        </tr>
        <tr>
            <td>51.5         </td> <td>10.2             </td>
        </tr>
        <tr>
            <td>61.3         </td> <td>12.4             </td>
        </tr>
        <tr>
            <td>61.3         </td> <td>13               </td>
        </tr>
        <tr>
            <td>63.6         </td> <td>13.2             </td>
        </tr>
        <tr>
            <td>66.1         </td> <td>13               </td>
        </tr>
        <tr>
            <td>70           </td> <td>12.7             </td>
        </tr>
        <tr>
            <td>92.7         </td> <td>13.9             </td>
        </tr>
        <tr>
            <td>90.5         </td> <td>15.5             </td>
        </tr>
        <tr>
            <td>90.5         </td> <td>15.8             </td>
        </tr>
    </tbody>
</table>
<p>... (18 rows omitted)</p>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
shotput.scatter('Weight Lifted')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/15/4/Least_Squares_Regression_5_0.png)

</div>
</div>
</div>



That's not a football shaped scatter plot. In fact, it seems to have a slight non-linear component. But if we insist on using a straight line to make our predictions, there is still one best straight line among all straight lines.

Our formulas for the slope and intercept of the regression line, derived for football shaped scatter plots, give the following values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
slope(shotput, 'Weight Lifted', 'Shot Put Distance')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.09834382159781997
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
intercept(shotput, 'Weight Lifted', 'Shot Put Distance')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
5.959629098373952
```


</div>
</div>
</div>



Does it still make sense to use these formulas even though the scatter plot isn't football shaped? We can answer this by finding the slope and intercept of the line that minimizes the mse.

We will define the function `shotput_linear_mse` to take an arbirtary slope and intercept as arguments and return the corresponding mse. Then `minimize` applied to `shotput_linear_mse` will return the best slope and intercept.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def shotput_linear_mse(any_slope, any_intercept):
    x = shotput.column('Weight Lifted')
    y = shotput.column('Shot Put Distance')
    fitted = any_slope*x + any_intercept
    return np.mean((y - fitted) ** 2)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minimize(shotput_linear_mse)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([0.09834382, 5.95962911])
```


</div>
</div>
</div>



These values are the same as those we got by using our formulas. To summarize:

**No matter what the shape of the scatter plot, there is a unique line that minimizes the mean squared error of estimation. It is called the regression line, and its slope and intercept are given by**

$$
\mathbf{\mbox{slope of the regression line}} ~=~ r \cdot
\frac{\mbox{SD of }y}{\mbox{SD of }x}
$$

$$
\mathbf{\mbox{intercept of the regression line}} ~=~
\mbox{average of }y ~-~ \mbox{slope} \cdot \mbox{average of }x
$$



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fitted = fit(shotput, 'Weight Lifted', 'Shot Put Distance')
shotput.with_column('Best Straight Line', fitted).scatter('Weight Lifted')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/15/4/Least_Squares_Regression_13_0.png)

</div>
</div>
</div>



### Nonlinear Regression
The graph above reinforces our earlier observation that the scatter plot is a bit curved. So it is better to fit a curve than a straight line. The [study](http://digitalcommons.wku.edu/ijes/vol6/iss2/10/) postulated a quadratic relation between the weight lifted and the shot put distance. So let's use quadratic functions as our predictors and see if we can find the best one. 

We have to find the best quadratic function among all quadratic functions, instead of the best straight line among all straight lines. The method of least squares allows us to do this.

The mathematics of this minimization is complicated and not easy to see just by examining the scatter plot. But numerical minimization is just as easy as it was with linear predictors! We can get the best quadratic predictor by once again using `minimize`. Let's see how this works.



Recall that a quadratic function has the form

$$
f(x) ~=~ ax^2 + bx + c
$$
for constants $a$, $b$, and $c$.

To find the best quadratic function to predict distance based on weight lifted, using the criterion of least squares, we will first write a function that takes the three constants as its arguments, calculates the fitted values by using the quadratic function above, and then returns the mean squared error. 

The function is called `shotput_quadratic_mse`. Notice that the definition is analogous to that of `lw_mse`, except that the fitted values are based on a quadratic function instead of linear.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def shotput_quadratic_mse(a, b, c):
    x = shotput.column('Weight Lifted')
    y = shotput.column('Shot Put Distance')
    fitted = a*(x**2) + b*x + c
    return np.mean((y - fitted) ** 2)

```
</div>

</div>



We can now use `minimize` just as before to find the constants that minimize the mean squared error. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
best = minimize(shotput_quadratic_mse)
best

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([-1.04004838e-03,  2.82708045e-01, -1.53182115e+00])
```


</div>
</div>
</div>



Our prediction of the shot put distance for an athlete who lifts $x$ kilograms is about
$$
-0.00104x^2 ~+~ 0.2827x - 1.5318
$$
meters. For example, if the athlete can lift 100 kilograms, the predicted distance is 16.33 meters. On the scatter plot, that's near the center of a vertical strip around 100 kilograms.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
(-0.00104)*(100**2) + 0.2827*100 - 1.5318

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
16.3382
```


</div>
</div>
</div>



Here are the predictions for all the values of `Weight Lifted`. You can see that they go through the center of the scatter plot, to a rough approximation.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = shotput.column(0)
shotput_fit = best.item(0)*(x**2) + best.item(1)*x + best.item(2)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
shotput.with_column('Best Quadratic Curve', shotput_fit).scatter(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/15/4/Least_Squares_Regression_23_0.png)

</div>
</div>
</div>

