---
redirect_from:
  - "/chapters/08/3/cross-classifying-by-more-than-one-variable"
interact_link: content/chapters/08/3/Cross-Classifying_by_More_than_One_Variable.ipynb
kernel_name: python3
has_widgets: false
title: 'Cross-Classifying'
prev_page:
  url: /chapters/08/2/Classifying_by_One_Variable
  title: 'Classifying by One Variable'
next_page:
  url: /chapters/08/4/Joining_Tables_by_Columns
  title: 'Joining Tables by Columns'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Cross-Classifying by More than One Variable

When individuals have multiple features, there are many different ways to classify them. For example, if we have a population of college students for each of whom we have recorded a major and the number of years in college, then the students could be classified by major, or by year, or by a combination of major and year.

The `group` method also allows us to classify individuals according to multiple variables. This is called *cross-classifying*.



### Two Variables: Counting the Number in Each Paired Category
The table `more_cones` records the flavor, color, and price of six ice cream cones.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones = Table().with_columns(
    'Flavor', make_array('strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate', 'bubblegum'),
    'Color', make_array('pink', 'light brown', 'dark brown', 'pink', 'dark brown', 'pink'),
    'Price', make_array(3.55, 4.75, 5.25, 5.25, 5.25, 4.75)
)

more_cones

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>3.55 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>4.75 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>4.75 </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



We know how to use `group` to count the number of cones of each flavor:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.group('Flavor')

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
            <td>bubblegum </td> <td>1    </td>
        </tr>
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



But now each cone has a color as well. To classify the cones by both flavor and color, we will pass a list of labels as an argument to `group`. The resulting table has one row for every *unique combination* of values that appear together in the grouped columns. As before, a single argument (a list, in this case, but an array would work too) gives row counts.



Although there are six cones, there are only four unique combinations of flavor and color. Two of the cones were dark brown chocolate, and two pink strawberry.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.group(['Flavor', 'Color'])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>1    </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>2    </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>1    </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>2    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Two Variables: Finding a Characteristic of Each Paired Category
A second argument aggregates all other columns that are not in the list of grouped columns.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.group(['Flavor', 'Color'], sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>4.75     </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>10.5     </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>4.75     </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>8.8      </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



**Three or More Variables.** You can use `group` to classify rows by three or more categorical variables. Just include them all in the list that is the first argument. But cross-classifying by multiple variables can become complex, as the number of distinct combinations of categories can be quite large. 



### Pivot Tables: Rearranging the Output of `group`
Many uses of cross-classification involve just two categorical variables, like `Flavor` and `Color` in the example above. In these cases it is possible to display the results of the classification in a different kind of table, called a *pivot table*. Pivot tables, also known as *contingency tables*, make it easier to work with data that have been classified according to two variables.

Recall the use of `group` to count the number of cones in each paired category of flavor and color:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.group(['Flavor', 'Color'])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>1    </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>2    </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>1    </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>2    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The same data can be displayed differenly using the Table method `pivot`. Ignore the code for a moment, and just examine the table of outcomes.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.pivot('Flavor', 'Color')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Color</th> <th>bubblegum</th> <th>chocolate</th> <th>strawberry</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>dark brown </td> <td>0        </td> <td>2        </td> <td>0         </td>
        </tr>
        <tr>
            <td>light brown</td> <td>0        </td> <td>1        </td> <td>0         </td>
        </tr>
        <tr>
            <td>pink       </td> <td>1        </td> <td>0        </td> <td>2         </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Notice how this table displays all nine possible pairs of flavor and color, including pairs like "dark brown bubblegum" that don't exist in our data. Notice also that the count in each pair appears in the body of the table: to find the number of light brown chocolate cones, run your eye along the row `light brown` until it meets the column `chocolate`.

The `group` method takes a list of two labels because it is flexible: it could take one or three or more. On the other hand, `pivot` always takes two column labels, one to determine the columns and one to determine the rows.



**`pivot`** 

The `pivot` method is closely related to the `group` method: it groups together rows that share a combination of values. It differs from `group` because it organizes the resulting values in a grid. The first argument to `pivot` is the label of a column that contains the values that will be used to form new columns in the result. The second argument is the label of a column used for the rows. The result gives the count of all rows of the original table that share the combination of column and row values.

Like `group`, `pivot` can be used with additional arguments to find characteristics of each paired category. An optional third argument called `values` indicates a column of values that will replace the counts in each cell of the grid. All of these values will not be displayed, however; the fourth argument `collect` indicates how to collect them all into one aggregated value to be displayed in the cell.

An example will help clarify this. Here is `pivot` being used to find the total price of the cones in each cell.  



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.pivot('Flavor', 'Color', values='Price', collect=sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Color</th> <th>bubblegum</th> <th>chocolate</th> <th>strawberry</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>dark brown </td> <td>0        </td> <td>10.5     </td> <td>0         </td>
        </tr>
        <tr>
            <td>light brown</td> <td>0        </td> <td>4.75     </td> <td>0         </td>
        </tr>
        <tr>
            <td>pink       </td> <td>4.75     </td> <td>0        </td> <td>8.8       </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



And here is `group` doing the same thing.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
more_cones.group(['Flavor', 'Color'], sum)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>4.75     </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>10.5     </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>4.75     </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>8.8      </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Though the numbers in both tables are the same, table produced by `pivot` is easier to read and lends itself more easily to analysis. The advantage of `pivot` is that it places grouped values into adjacent columns, so that they can be combined and compared.



### Example: Education and Income of Californian Adults
The State of California's Open Data Portal is a rich source of information about the lives of Californians. It is our source of a [dataset](http://data.ca.gov/dataset/ca-educational-attainment-personal-income) on educational attainment and personal income among Californians over the years 2008 to 2014. The data are derived from the U.S. Census Current Population Survey.

For each year, the table records the `Population Count` of Californians in many different combinations of age, gender, educational attainment, and personal income. We will study only the data for the year 2014.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
full_table = Table.read_table(path_data + 'educ_inc.csv')
ca_2014 = full_table.where('Year', are.equal_to('1/1/14 0:00')).where('Age', are.not_equal_to('00 to 17'))
ca_2014

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Age</th> <th>Gender</th> <th>Educational Attainment</th> <th>Personal Income</th> <th>Population Count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1/1/14 0:00</td> <td>18 to 64 </td> <td>Female</td> <td>No high school diploma        </td> <td>H: 75,000 and over </td> <td>2058            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Male  </td> <td>No high school diploma        </td> <td>H: 75,000 and over </td> <td>2153            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Female</td> <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>4666            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Female</td> <td>High school or equivalent     </td> <td>H: 75,000 and over </td> <td>7122            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Female</td> <td>No high school diploma        </td> <td>F: 35,000 to 49,999</td> <td>7261            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Male  </td> <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>8569            </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>18 to 64 </td> <td>Female</td> <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>14635           </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Male  </td> <td>No high school diploma        </td> <td>F: 35,000 to 49,999</td> <td>15212           </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Male  </td> <td>College, less than 4-yr degree</td> <td>B: 5,000 to 9,999  </td> <td>15423           </td>
        </tr>
        <tr>
            <td>1/1/14 0:00</td> <td>65 to 80+</td> <td>Female</td> <td>Bachelor's degree or higher   </td> <td>A: 0 to 4,999      </td> <td>15459           </td>
        </tr>
    </tbody>
</table>
<p>... (117 rows omitted)</p>
</div>


</div>
</div>
</div>



Each row of the table corresponds to a combination of age, gender, educational level, and income. There are 127 such combinations in all! 

As a first step it is a good idea to start with just one or two variables. We will focus on just one pair: educational attainment and personal income. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
educ_inc = ca_2014.select('Educational Attainment', 'Personal Income', 'Population Count')
educ_inc

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Educational Attainment</th> <th>Personal Income</th> <th>Population Count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>No high school diploma        </td> <td>H: 75,000 and over </td> <td>2058            </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>H: 75,000 and over </td> <td>2153            </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>4666            </td>
        </tr>
        <tr>
            <td>High school or equivalent     </td> <td>H: 75,000 and over </td> <td>7122            </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>F: 35,000 to 49,999</td> <td>7261            </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>8569            </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>G: 50,000 to 74,999</td> <td>14635           </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>F: 35,000 to 49,999</td> <td>15212           </td>
        </tr>
        <tr>
            <td>College, less than 4-yr degree</td> <td>B: 5,000 to 9,999  </td> <td>15423           </td>
        </tr>
        <tr>
            <td>Bachelor's degree or higher   </td> <td>A: 0 to 4,999      </td> <td>15459           </td>
        </tr>
    </tbody>
</table>
<p>... (117 rows omitted)</p>
</div>


</div>
</div>
</div>



Let's start by looking at educational level alone. The categories of this variable have been subdivided by the different levels of income. So we will group the table by `Educational Attainment` and `sum` the `Population Count` in each category.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
education = educ_inc.select('Educational Attainment', 'Population Count')
educ_totals = education.group('Educational Attainment', sum)
educ_totals

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Educational Attainment</th> <th>Population Count sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Bachelor's degree or higher   </td> <td>8525698             </td>
        </tr>
        <tr>
            <td>College, less than 4-yr degree</td> <td>7775497             </td>
        </tr>
        <tr>
            <td>High school or equivalent     </td> <td>6294141             </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>4258277             </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



There are only four categories of educational attainment. The counts are so large that is is more helpful to look at percents. For this, we will use the function `percents` that we defined in an earlier section. It converts an array of numbers to an array of percents out of the total in the input array.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def percents(array_x):
    return np.round( (array_x/sum(array_x))*100, 2)

```
</div>

</div>



We now have the distribution of educational attainment among adult Californians. More than 30% have a Bachelor's degree or higher, while almost 16% lack a high school diploma.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
educ_distribution = educ_totals.with_column(
    'Population Percent', percents(educ_totals.column(1))
)
educ_distribution

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Educational Attainment</th> <th>Population Count sum</th> <th>Population Percent</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Bachelor's degree or higher   </td> <td>8525698             </td> <td>31.75             </td>
        </tr>
        <tr>
            <td>College, less than 4-yr degree</td> <td>7775497             </td> <td>28.96             </td>
        </tr>
        <tr>
            <td>High school or equivalent     </td> <td>6294141             </td> <td>23.44             </td>
        </tr>
        <tr>
            <td>No high school diploma        </td> <td>4258277             </td> <td>15.86             </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



By using `pivot`, we can get a contingency table (a table of counts) of adult Californians cross-classified by `Educational Attainment` and `Personal Income`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
totals = educ_inc.pivot('Educational Attainment', 'Personal Income', values='Population Count', collect=sum)
totals

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Personal Income</th> <th>Bachelor's degree or higher</th> <th>College, less than 4-yr degree</th> <th>High school or equivalent</th> <th>No high school diploma</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>A: 0 to 4,999      </td> <td>575491                     </td> <td>985011                        </td> <td>1161873                  </td> <td>1204529               </td>
        </tr>
        <tr>
            <td>B: 5,000 to 9,999  </td> <td>326020                     </td> <td>810641                        </td> <td>626499                   </td> <td>597039                </td>
        </tr>
        <tr>
            <td>C: 10,000 to 14,999</td> <td>452449                     </td> <td>798596                        </td> <td>692661                   </td> <td>664607                </td>
        </tr>
        <tr>
            <td>D: 15,000 to 24,999</td> <td>773684                     </td> <td>1345257                       </td> <td>1252377                  </td> <td>875498                </td>
        </tr>
        <tr>
            <td>E: 25,000 to 34,999</td> <td>693884                     </td> <td>1091642                       </td> <td>929218                   </td> <td>464564                </td>
        </tr>
        <tr>
            <td>F: 35,000 to 49,999</td> <td>1122791                    </td> <td>1112421                       </td> <td>782804                   </td> <td>260579                </td>
        </tr>
        <tr>
            <td>G: 50,000 to 74,999</td> <td>1594681                    </td> <td>883826                        </td> <td>525517                   </td> <td>132516                </td>
        </tr>
        <tr>
            <td>H: 75,000 and over </td> <td>2986698                    </td> <td>748103                        </td> <td>323192                   </td> <td>58945                 </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Here you see the power of `pivot` over other cross-classification methods. Each column of counts is a distribution of personal income at a specific level of educational attainment. Converting the counts to percents allows us to compare the four distributions.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distributions = totals.select(0).with_columns(
    "Bachelor's degree or higher", percents(totals.column(1)),
    'College, less than 4-yr degree', percents(totals.column(2)),
    'High school or equivalent', percents(totals.column(3)),
    'No high school diploma', percents(totals.column(4))   
    )

distributions

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Personal Income</th> <th>Bachelor's degree or higher</th> <th>College, less than 4-yr degree</th> <th>High school or equivalent</th> <th>No high school diploma</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>A: 0 to 4,999      </td> <td>6.75                       </td> <td>12.67                         </td> <td>18.46                    </td> <td>28.29                 </td>
        </tr>
        <tr>
            <td>B: 5,000 to 9,999  </td> <td>3.82                       </td> <td>10.43                         </td> <td>9.95                     </td> <td>14.02                 </td>
        </tr>
        <tr>
            <td>C: 10,000 to 14,999</td> <td>5.31                       </td> <td>10.27                         </td> <td>11                       </td> <td>15.61                 </td>
        </tr>
        <tr>
            <td>D: 15,000 to 24,999</td> <td>9.07                       </td> <td>17.3                          </td> <td>19.9                     </td> <td>20.56                 </td>
        </tr>
        <tr>
            <td>E: 25,000 to 34,999</td> <td>8.14                       </td> <td>14.04                         </td> <td>14.76                    </td> <td>10.91                 </td>
        </tr>
        <tr>
            <td>F: 35,000 to 49,999</td> <td>13.17                      </td> <td>14.31                         </td> <td>12.44                    </td> <td>6.12                  </td>
        </tr>
        <tr>
            <td>G: 50,000 to 74,999</td> <td>18.7                       </td> <td>11.37                         </td> <td>8.35                     </td> <td>3.11                  </td>
        </tr>
        <tr>
            <td>H: 75,000 and over </td> <td>35.03                      </td> <td>9.62                          </td> <td>5.13                     </td> <td>1.38                  </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



At a glance, you can see that over 35% of those with Bachelor's degrees or higher had incomes of $\$75,000$ and over, whereas fewer than 10% of the people in the other education categories had that level of income. 

The bar chart below compares the personal income distributions of adult Californians who have no high diploma with those who have completed a Bachelor's degree or higher. The difference in the distributions is striking. There is a clear positive association between educational attainment and personal income.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
distributions.select(0, 1, 4).barh(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/08/3/Cross-Classifying_by_More_than_One_Variable_37_0.png)

</div>
</div>
</div>

