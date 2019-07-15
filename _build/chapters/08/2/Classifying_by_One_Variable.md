---
redirect_from:
  - "/chapters/08/2/classifying-by-one-variable"
interact_link: content/chapters/08/2/Classifying_by_One_Variable.ipynb
kernel_name: python3
has_widgets: false
title: 'Classifying by One Variable'
prev_page:
  url: /chapters/08/1/Applying_a_Function_to_a_Column
  title: 'Applying Functions to Columns'
next_page:
  url: /chapters/08/3/Cross-Classifying_by_More_than_One_Variable
  title: 'Cross-Classifying'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Classifying by One Variable

Data scientists often need to classify individuals into groups according to shared features, and then identify some characteristics of the groups. For example, in the example using Galton's data on heights, we saw that it was useful to classify families according to the parents' midparent heights, and then find the average height of the children in each group.

This section is about classifying individuals into categories that are not numerical. We begin by recalling the basic use of `group`. 



### Counting the Number in Each Category
The `group` method with a single argument counts the number of rows for each category in a column. The result contains one row per unique value in the grouped column.

Here is a small table of data on ice cream cones. The `group` method can be used to list the distinct flavors and provide the counts of each flavor.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cones = Table().with_columns(
    'Flavor', make_array('strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate'),
    'Price', make_array(3.55, 4.75, 6.55, 5.25, 5.25)
)
cones

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>3.55 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>4.75 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>6.55 </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>5.25 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>5.25 </td>
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
cones.group('Flavor')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>3    </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>2    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



There are two distinct categories, chocolate and strawberry. The call to `group` creates a table of counts in each category. The column is called `count` by default, and contains the number of rows in each category.

Notice that this can all be worked out from just the `Flavor` column. The `Price` column has not been used.

But what if we wanted the total price of the cones of each different flavor? That's where the second argument of `group` comes in.



### Finding a Characteristic of Each Category
The optional second argument of `group` names the function that will be used to aggregate values in other columns for all of those rows. For instance, `sum` will sum up the prices in all rows that match each category. This result also contains one row per unique value in the grouped column, but it has the same number of columns as the original table.

To find the total price of each flavor, we call `group` again, with `Flavor` as its first argument as before. But this time there is a second argument: the function name `sum`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cones.group('Flavor', sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>16.55    </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>8.8      </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



To create this new table, `group` has calculated the sum of the `Price` entries in all the rows corresponding to each distinct flavor. The prices in the three `chocolate` rows add up to $\$16.55$ (you can assume that price is being measured in dollars). The prices in the two `strawberry` rows have a total of $\$8.80$.

The label of the newly created "sum" column is `Price sum`, which is created by taking the label of the column being summed, and appending the word `sum`. 

Because `group` finds the `sum` of all columns other than the one with the categories, there is no need to specify that it has to `sum` the prices.

To see in more detail what `group` is doing, notice that you could have figured out the total prices yourself, not only by mental arithmetic but also using code. For example, to find the total price of all the chocolate cones, you could start by creating a new table consisting of only the chocolate cones, and then accessing the column of prices:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cones.where('Flavor', are.equal_to('chocolate')).column('Price')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([4.75, 6.55, 5.25])
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sum(cones.where('Flavor', are.equal_to('chocolate')).column('Price'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
16.55
```


</div>
</div>
</div>



This is what `group` is doing for each distinct value in `Flavor`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# For each distinct value in `Flavor, access all the rows
# and create an array of `Price`

cones_choc = cones.where('Flavor', are.equal_to('chocolate')).column('Price')
cones_strawb = cones.where('Flavor', are.equal_to('strawberry')).column('Price')

# Display the arrays in a table

grouped_cones = Table().with_columns(
    'Flavor', make_array('chocolate', 'strawberry'),
    'Array of All the Prices', make_array(cones_choc, cones_strawb)
)

# Append a column with the sum of the `Price` values in each array

price_totals = grouped_cones.with_column(
    'Sum of the Array', make_array(sum(cones_choc), sum(cones_strawb))
)
price_totals

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Array of All the Prices</th> <th>Sum of the Array</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>[4.75 6.55 5.25]       </td> <td>16.55           </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>[3.55 5.25]            </td> <td>8.8             </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



You can replace `sum` by any other functions that work on arrays. For example, you could use `max` to find the largest price in each category:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
cones.group('Flavor', max)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price max</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>6.55     </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>5.25     </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Once again, `group` creates arrays of the prices in each `Flavor` category. But now it finds the `max` of each array:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
price_maxes = grouped_cones.with_column(
    'Max of the Array', make_array(max(cones_choc), max(cones_strawb))
)
price_maxes

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Array of All the Prices</th> <th>Max of the Array</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>[4.75 6.55 5.25]       </td> <td>6.55            </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>[3.55 5.25]            </td> <td>5.25            </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Indeed, the original call to `group` with just one argument has the same effect as using `len` as the function and then cleaning up the table.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
lengths = grouped_cones.with_column(
    'Length of the Array', make_array(len(cones_choc), len(cones_strawb))
)
lengths

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Array of All the Prices</th> <th>Length of the Array</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>[4.75 6.55 5.25]       </td> <td>3                  </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>[3.55 5.25]            </td> <td>2                  </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Example: NBA Salaries
The table `nba` contains data on the 2015-2016 players in the National Basketball Association. We have examined these data earlier. Recall that salaries are measured in millions of dollars.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba1 = Table.read_table(path_data + 'nba_salaries.csv')
nba = nba1.relabeled("'15-'16 SALARY", 'SALARY')
nba

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap    </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>18.6717</td>
        </tr>
        <tr>
            <td>Al Horford      </td> <td>C       </td> <td>Atlanta Hawks</td> <td>12     </td>
        </tr>
        <tr>
            <td>Tiago Splitter  </td> <td>C       </td> <td>Atlanta Hawks</td> <td>9.75625</td>
        </tr>
        <tr>
            <td>Jeff Teague     </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>8      </td>
        </tr>
        <tr>
            <td>Kyle Korver     </td> <td>SG      </td> <td>Atlanta Hawks</td> <td>5.74648</td>
        </tr>
        <tr>
            <td>Thabo Sefolosha </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>4      </td>
        </tr>
        <tr>
            <td>Mike Scott      </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>3.33333</td>
        </tr>
        <tr>
            <td>Kent Bazemore   </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>2      </td>
        </tr>
        <tr>
            <td>Dennis Schroder </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>1.7634 </td>
        </tr>
        <tr>
            <td>Tim Hardaway Jr.</td> <td>SG      </td> <td>Atlanta Hawks</td> <td>1.30452</td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>
</div>


</div>
</div>
</div>



**1.** How much money did each team pay for its players' salaries?

The only columns involved are `TEAM` and `SALARY`. We have to `group` the rows by `TEAM` and then `sum` the salaries of the groups. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
teams_and_money = nba.select('TEAM', 'SALARY')
teams_and_money.group('TEAM', sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>TEAM</th> <th>SALARY sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Atlanta Hawks        </td> <td>69.5731   </td>
        </tr>
        <tr>
            <td>Boston Celtics       </td> <td>50.2855   </td>
        </tr>
        <tr>
            <td>Brooklyn Nets        </td> <td>57.307    </td>
        </tr>
        <tr>
            <td>Charlotte Hornets    </td> <td>84.1024   </td>
        </tr>
        <tr>
            <td>Chicago Bulls        </td> <td>78.8209   </td>
        </tr>
        <tr>
            <td>Cleveland Cavaliers  </td> <td>102.312   </td>
        </tr>
        <tr>
            <td>Dallas Mavericks     </td> <td>65.7626   </td>
        </tr>
        <tr>
            <td>Denver Nuggets       </td> <td>62.4294   </td>
        </tr>
        <tr>
            <td>Detroit Pistons      </td> <td>42.2118   </td>
        </tr>
        <tr>
            <td>Golden State Warriors</td> <td>94.0851   </td>
        </tr>
    </tbody>
</table>
<p>... (20 rows omitted)</p>
</div>


</div>
</div>
</div>



**2.** How many NBA players were there in each of the five positions?

We have to classify by `POSITION`, and count. This can be done with just one argument to group:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.group('POSITION')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>POSITION</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>C       </td> <td>69   </td>
        </tr>
        <tr>
            <td>PF      </td> <td>85   </td>
        </tr>
        <tr>
            <td>PG      </td> <td>85   </td>
        </tr>
        <tr>
            <td>SF      </td> <td>82   </td>
        </tr>
        <tr>
            <td>SG      </td> <td>96   </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



**3.** What was the average salary of the players at each of the five positions?

This time, we have to group by `POSITION` and take the mean of the salaries. For clarity, we will work with a table of just the positions and the salaries.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
positions_and_money = nba.select('POSITION', 'SALARY')
positions_and_money.group('POSITION', np.mean)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>POSITION</th> <th>SALARY mean</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>C       </td> <td>6.08291    </td>
        </tr>
        <tr>
            <td>PF      </td> <td>4.95134    </td>
        </tr>
        <tr>
            <td>PG      </td> <td>5.16549    </td>
        </tr>
        <tr>
            <td>SF      </td> <td>5.53267    </td>
        </tr>
        <tr>
            <td>SG      </td> <td>3.9882     </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Center was the most highly paid position, at an average of over 6 million dollars.

If we had not selected the two columns as our first step, `group` would not attempt to "average" the categorical columns in `nba`. (It is impossible to average two strings like "Atlanta Hawks" and "Boston Celtics".) It performs arithmetic only on numerical columns and leaves the rest blank.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.group('POSITION', np.mean)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>POSITION</th> <th>PLAYER mean</th> <th>TEAM mean</th> <th>SALARY mean</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>C       </td> <td>           </td> <td>         </td> <td>6.08291    </td>
        </tr>
        <tr>
            <td>PF      </td> <td>           </td> <td>         </td> <td>4.95134    </td>
        </tr>
        <tr>
            <td>PG      </td> <td>           </td> <td>         </td> <td>5.16549    </td>
        </tr>
        <tr>
            <td>SF      </td> <td>           </td> <td>         </td> <td>5.53267    </td>
        </tr>
        <tr>
            <td>SG      </td> <td>           </td> <td>         </td> <td>3.9882     </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>

