---
redirect_from:
  - "/chapters/06/tables"
interact_link: content/chapters/06/Tables.ipynb
kernel_name: python3
has_widgets: false
title: 'Tables'
prev_page:
  url: /chapters/05/3/More_on_Arrays
  title: 'More on Arrays'
next_page:
  url: /chapters/06/1/Sorting_Rows
  title: 'Sorting Rows'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Tables

Tables are a fundamental object type for representing data sets. A table can be viewed in two ways:
* a sequence of named columns that each describe a single aspect of all entries in a data set, or
* a sequence of rows that each contain all information about a single entry in a data set.

In order to use tables, import all of the module called `datascience`, a module created for this text.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from datascience import *

```
</div>

</div>



Empty tables can be created using the `Table` function. An empty table is usefuly because it can be extended to contain new rows and columns.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Table()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            
        </tr>
    </thead>
    <tbody>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The `with_columns` method on a table constructs a new table with additional labeled columns. Each column of a table is an array. To add one new column to a table, call `with_columns` with a label and an array. (The `with_column` method can be used with the same effect.)

Below, we begin each example with an empty table that has no columns. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Table().with_columns('Number of petals', make_array(8, 34, 5))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td>
        </tr>
        <tr>
            <td>34              </td>
        </tr>
        <tr>
            <td>5               </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



To add two (or more) new columns, provide the label and array for each column. All columns must have the same length, or an error will occur.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Table().with_columns(
    'Number of petals', make_array(8, 34, 5),
    'Name', make_array('lotus', 'sunflower', 'rose')
)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th> <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td> <td>lotus    </td>
        </tr>
        <tr>
            <td>34              </td> <td>sunflower</td>
        </tr>
        <tr>
            <td>5               </td> <td>rose     </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



We can give this table a name, and then extend the table with another column.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
flowers = Table().with_columns(
    'Number of petals', make_array(8, 34, 5),
    'Name', make_array('lotus', 'sunflower', 'rose')
)

flowers.with_columns(
    'Color', make_array('pink', 'yellow', 'red')
)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th> <th>Name</th> <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td> <td>lotus    </td> <td>pink  </td>
        </tr>
        <tr>
            <td>34              </td> <td>sunflower</td> <td>yellow</td>
        </tr>
        <tr>
            <td>5               </td> <td>rose     </td> <td>red   </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The `with_columns` method creates a new table each time it is called, so the original table is not affected. For example, the table `flowers` still has only the two columns that it had when it was created.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
flowers

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th> <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td> <td>lotus    </td>
        </tr>
        <tr>
            <td>34              </td> <td>sunflower</td>
        </tr>
        <tr>
            <td>5               </td> <td>rose     </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Creating tables in this way involves a lot of typing. If the data have already been entered somewhere, it is usually possible to use Python to read it into a table, instead of typing it all in cell by cell.

Often, tables are created from files that contain comma-separated values. Such files are called CSV files.

Below, we use the Table method `read_table` to read a CSV file that contains some of the data used by Minard in his graphic about Napoleon's Russian campaign. The data are placed in a table named `minard`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard = Table.read_table(path_data + 'minard.csv')
minard

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



We will use this small table to demonstrate some useful Table methods. We will then use those same methods, and develop other methods, on much larger tables of data.



### The Size of the Table

The method `num_columns` gives the number of columns in the table, and `num_rows` the number of rows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.num_columns

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
5
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.num_rows

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
8
```


</div>
</div>
</div>



### Column Labels
The method `labels` can be used to list the labels of all the columns. With `minard` we don't gain much by this, but it can be very useful for tables that are so large that not all columns are visible on the screen.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.labels

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
('Longitude', 'Latitude', 'City', 'Direction', 'Survivors')
```


</div>
</div>
</div>



We can change column labels using the `relabeled` method. This creates a new table and leaves `minard` unchanged.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.relabeled('City', 'City Name')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



However, this method does not change the original table. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



A common pattern is to assign the original name `minard` to the new table, so that all future uses of `minard` will refer to the relabeled table.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard = minard.relabeled('City', 'City Name')
minard

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Accessing the Data in a Column
We can use a column's label to access the array of data in the column.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.column('Survivors')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([145000, 140000, 127100, 100000,  55000,  24000,  20000,  12000])
```


</div>
</div>
</div>



The 5 columns are indexed 0, 1, 2, 3, and 4. The column `Survivors` can also be accessed by using its column index.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.column(4)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([145000, 140000, 127100, 100000,  55000,  24000,  20000,  12000])
```


</div>
</div>
</div>



The 8 items in the array are indexed 0, 1, 2, and so on, up to 7. The items in the column can be accessed using `item`, as with any array.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.column(4).item(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
145000
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.column(4).item(5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
24000
```


</div>
</div>
</div>



### Working with the Data in a Column
Because columns are arrays, we can use array operations on them to discover new information. For example, we can create a new column that contains the percent of all survivors at each city after Smolensk.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
initial = minard.column('Survivors').item(0)
minard = minard.with_columns(
    'Percent Surviving', minard.column('Survivors')/initial
)
minard

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>1                </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>0.965517         </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>0.876552         </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>0.689655         </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>0.37931          </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>0.165517         </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>0.137931         </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>0.0827586        </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



To make the proportions in the new columns appear as percents, we can use the method `set_format` with the option `PercentFormatter`. The `set_format` method takes `Formatter` objects, which exist for dates (`DateFormatter`), currencies (`CurrencyFormatter`), numbers, and percentages.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.set_format('Percent Surviving', PercentFormatter)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>100.00%          </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>96.55%           </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>87.66%           </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>68.97%           </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>37.93%           </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>16.55%           </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>13.79%           </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>8.28%            </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Choosing Sets of Columns
The method `select` creates a new table that contains only the specified columns.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.select('Longitude', 'Latitude')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The same selection can be made using column indices instead of labels.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.select(0, 1)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The result of using `select` is a new table, even when you select just one column.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.select('Survivors')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Survivors</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>145000   </td>
        </tr>
        <tr>
            <td>140000   </td>
        </tr>
        <tr>
            <td>127100   </td>
        </tr>
        <tr>
            <td>100000   </td>
        </tr>
        <tr>
            <td>55000    </td>
        </tr>
        <tr>
            <td>24000    </td>
        </tr>
        <tr>
            <td>20000    </td>
        </tr>
        <tr>
            <td>12000    </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Notice that the result is a table, unlike the result of `column`, which is an array.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.column('Survivors')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([145000, 140000, 127100, 100000,  55000,  24000,  20000,  12000])
```


</div>
</div>
</div>



Another way to create a new table consisting of a set of columns is to `drop` the columns you don't want.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard.drop('Longitude', 'Latitude', 'Direction')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>City Name</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Smolensk   </td> <td>145000   </td> <td>100.00%          </td>
        </tr>
        <tr>
            <td>Dorogobouge</td> <td>140000   </td> <td>96.55%           </td>
        </tr>
        <tr>
            <td>Chjat      </td> <td>127100   </td> <td>87.66%           </td>
        </tr>
        <tr>
            <td>Moscou     </td> <td>100000   </td> <td>68.97%           </td>
        </tr>
        <tr>
            <td>Wixma      </td> <td>55000    </td> <td>37.93%           </td>
        </tr>
        <tr>
            <td>Smolensk   </td> <td>24000    </td> <td>16.55%           </td>
        </tr>
        <tr>
            <td>Orscha     </td> <td>20000    </td> <td>13.79%           </td>
        </tr>
        <tr>
            <td>Moiodexno  </td> <td>12000    </td> <td>8.28%            </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Neither `select` nor `drop` change the original table. Instead, they create new smaller tables that share the same data. The fact that the original table is preserved is useful! You can generate multiple different tables that only consider certain columns without worrying that one analysis will affect the other.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
minard

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Longitude</th> <th>Latitude</th> <th>City Name</th> <th>Direction</th> <th>Survivors</th> <th>Percent Surviving</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>32       </td> <td>54.8    </td> <td>Smolensk   </td> <td>Advance  </td> <td>145000   </td> <td>100.00%          </td>
        </tr>
        <tr>
            <td>33.2     </td> <td>54.9    </td> <td>Dorogobouge</td> <td>Advance  </td> <td>140000   </td> <td>96.55%           </td>
        </tr>
        <tr>
            <td>34.4     </td> <td>55.5    </td> <td>Chjat      </td> <td>Advance  </td> <td>127100   </td> <td>87.66%           </td>
        </tr>
        <tr>
            <td>37.6     </td> <td>55.8    </td> <td>Moscou     </td> <td>Advance  </td> <td>100000   </td> <td>68.97%           </td>
        </tr>
        <tr>
            <td>34.3     </td> <td>55.2    </td> <td>Wixma      </td> <td>Retreat  </td> <td>55000    </td> <td>37.93%           </td>
        </tr>
        <tr>
            <td>32       </td> <td>54.6    </td> <td>Smolensk   </td> <td>Retreat  </td> <td>24000    </td> <td>16.55%           </td>
        </tr>
        <tr>
            <td>30.4     </td> <td>54.4    </td> <td>Orscha     </td> <td>Retreat  </td> <td>20000    </td> <td>13.79%           </td>
        </tr>
        <tr>
            <td>26.8     </td> <td>54.3    </td> <td>Moiodexno  </td> <td>Retreat  </td> <td>12000    </td> <td>8.28%            </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



All of the methods that we have used above can be applied to any table.

