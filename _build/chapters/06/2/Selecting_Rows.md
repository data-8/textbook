---
redirect_from:
  - "/chapters/06/2/selecting-rows"
interact_link: content/chapters/06/2/Selecting_Rows.ipynb
kernel_name: python3
has_widgets: false
title: 'Selecting Rows'
prev_page:
  url: /chapters/06/1/Sorting_Rows
  title: 'Sorting Rows'
next_page:
  url: /chapters/06/3/Example_Trends_in_the_Population_of_the_United_States
  title: 'Example: Population Trends'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



# Selecting Rows

Often, we would like to extract just those rows that correspond to entries with a particular feature. For example, we might want only the rows corresponding to the Warriors, or to players who earned more than $\$10$ million. Or we might just want the top five earners.



### Specified Rows
The Table method `take` does just that – it takes a specified set of rows. Its argument is a row index or array of indices, and it creates a new table consisting of only those rows.

For example, if we wanted just the first row of `nba`, we could use `take` as follows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.take(0)

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
            <td>Paul Millsap</td> <td>PF      </td> <td>Atlanta Hawks</td> <td>18.6717</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



This is a new table with just the single row that we specified.

We could also get the fourth, fifth, and sixth rows by specifying a range of indices as the argument.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.take(np.arange(3, 6))

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
            <td>Jeff Teague    </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>8      </td>
        </tr>
        <tr>
            <td>Kyle Korver    </td> <td>SG      </td> <td>Atlanta Hawks</td> <td>5.74648</td>
        </tr>
        <tr>
            <td>Thabo Sefolosha</td> <td>SF      </td> <td>Atlanta Hawks</td> <td>4      </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



If we want a table of the top 5 highest paid players, we can first sort the list by salary and then `take` the first five rows:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.sort('SALARY', descending=True).take(np.arange(5))

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
            <td>Kobe Bryant    </td> <td>SF      </td> <td>Los Angeles Lakers </td> <td>25     </td>
        </tr>
        <tr>
            <td>Joe Johnson    </td> <td>SF      </td> <td>Brooklyn Nets      </td> <td>24.8949</td>
        </tr>
        <tr>
            <td>LeBron James   </td> <td>SF      </td> <td>Cleveland Cavaliers</td> <td>22.9705</td>
        </tr>
        <tr>
            <td>Carmelo Anthony</td> <td>SF      </td> <td>New York Knicks    </td> <td>22.875 </td>
        </tr>
        <tr>
            <td>Dwight Howard  </td> <td>C       </td> <td>Houston Rockets    </td> <td>22.3594</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Rows Corresponding to a Specified Feature
More often, we will want to access data in a set of rows that have a certain feature, but whose indices we don't know ahead of time. For example, we might want data on all the players who made more than $\$10$ million, but we don't want to spend time counting rows in the sorted table.

The method `where` does the job for us. Its output is a table with the same columns as the original but only the rows *where* the feature occurs.

The first argument of `where` is the label of the column that contains the information about whether or not a row has the feature we want. If the feature is "made more than $\$10$ million", the column is `SALARY`.

The second argument of `where` is a way of specifying the feature. A couple of examples will make the general method of specification easier to understand.

In the first example, we extract the data for all those who earned more than $\$10$ million.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('SALARY', are.above(10))

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
            <td>Paul Millsap  </td> <td>PF      </td> <td>Atlanta Hawks    </td> <td>18.6717</td>
        </tr>
        <tr>
            <td>Al Horford    </td> <td>C       </td> <td>Atlanta Hawks    </td> <td>12     </td>
        </tr>
        <tr>
            <td>Joe Johnson   </td> <td>SF      </td> <td>Brooklyn Nets    </td> <td>24.8949</td>
        </tr>
        <tr>
            <td>Thaddeus Young</td> <td>PF      </td> <td>Brooklyn Nets    </td> <td>11.236 </td>
        </tr>
        <tr>
            <td>Al Jefferson  </td> <td>C       </td> <td>Charlotte Hornets</td> <td>13.5   </td>
        </tr>
        <tr>
            <td>Nicolas Batum </td> <td>SG      </td> <td>Charlotte Hornets</td> <td>13.1253</td>
        </tr>
        <tr>
            <td>Kemba Walker  </td> <td>PG      </td> <td>Charlotte Hornets</td> <td>12     </td>
        </tr>
        <tr>
            <td>Derrick Rose  </td> <td>PG      </td> <td>Chicago Bulls    </td> <td>20.0931</td>
        </tr>
        <tr>
            <td>Jimmy Butler  </td> <td>SG      </td> <td>Chicago Bulls    </td> <td>16.4075</td>
        </tr>
        <tr>
            <td>Joakim Noah   </td> <td>C       </td> <td>Chicago Bulls    </td> <td>13.4   </td>
        </tr>
    </tbody>
</table>
<p>... (59 rows omitted)</p>
</div>


</div>
</div>
</div>



The use of the argument `are.above(10)` ensured that each selected row had a value of `SALARY` that was greater than 10.

There are 69 rows in the new table, corresponding to the 69 players who made more than $10$ million dollars. Arranging these rows in order makes the data easier to analyze. DeMar DeRozan of the Toronto Raptors was the "poorest" of this group, at a salary of just over $10$ million dollars.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('SALARY', are.above(10)).sort('SALARY')

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
            <td>DeMar DeRozan  </td> <td>SG      </td> <td>Toronto Raptors     </td> <td>10.05  </td>
        </tr>
        <tr>
            <td>Gerald Wallace </td> <td>SF      </td> <td>Philadelphia 76ers  </td> <td>10.1059</td>
        </tr>
        <tr>
            <td>Luol Deng      </td> <td>SF      </td> <td>Miami Heat          </td> <td>10.1516</td>
        </tr>
        <tr>
            <td>Monta Ellis    </td> <td>SG      </td> <td>Indiana Pacers      </td> <td>10.3   </td>
        </tr>
        <tr>
            <td>Wilson Chandler</td> <td>SF      </td> <td>Denver Nuggets      </td> <td>10.4494</td>
        </tr>
        <tr>
            <td>Brendan Haywood</td> <td>C       </td> <td>Cleveland Cavaliers </td> <td>10.5225</td>
        </tr>
        <tr>
            <td>Jrue Holiday   </td> <td>PG      </td> <td>New Orleans Pelicans</td> <td>10.5955</td>
        </tr>
        <tr>
            <td>Tyreke Evans   </td> <td>SG      </td> <td>New Orleans Pelicans</td> <td>10.7346</td>
        </tr>
        <tr>
            <td>Marcin Gortat  </td> <td>C       </td> <td>Washington Wizards  </td> <td>11.2174</td>
        </tr>
        <tr>
            <td>Thaddeus Young </td> <td>PF      </td> <td>Brooklyn Nets       </td> <td>11.236 </td>
        </tr>
    </tbody>
</table>
<p>... (59 rows omitted)</p>
</div>


</div>
</div>
</div>



How much did Stephen Curry make? For the answer, we have to access the row where the value of `PLAYER` is equal to `Stephen Curry`. That is placed a table consisting of just one line:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('PLAYER', are.equal_to('Stephen Curry'))

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
            <td>Stephen Curry</td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Curry made just under $\$11.4$ million dollars. That's a lot of money, but it's less than half the salary of LeBron James. You'll find that salary in the "Top 5" table earlier in this section, or you could find it replacing `'Stephen Curry'` by `'LeBron James'` in the line of code above.

In the code, `are` is used again, but this time with the *predicate* `equal_to` instead of `above`. Thus for example you can get a table of all the Warriors:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('TEAM', are.equal_to('Golden State Warriors')).show()

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
            <td>Klay Thompson    </td> <td>SG      </td> <td>Golden State Warriors</td> <td>15.501  </td>
        </tr>
        <tr>
            <td>Draymond Green   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>14.2609 </td>
        </tr>
        <tr>
            <td>Andrew Bogut     </td> <td>C       </td> <td>Golden State Warriors</td> <td>13.8    </td>
        </tr>
        <tr>
            <td>Andre Iguodala   </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105 </td>
        </tr>
        <tr>
            <td>Stephen Curry    </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708 </td>
        </tr>
        <tr>
            <td>Jason Thompson   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>7.00847 </td>
        </tr>
        <tr>
            <td>Shaun Livingston </td> <td>PG      </td> <td>Golden State Warriors</td> <td>5.54373 </td>
        </tr>
        <tr>
            <td>Harrison Barnes  </td> <td>SF      </td> <td>Golden State Warriors</td> <td>3.8734  </td>
        </tr>
        <tr>
            <td>Marreese Speights</td> <td>C       </td> <td>Golden State Warriors</td> <td>3.815   </td>
        </tr>
        <tr>
            <td>Leandro Barbosa  </td> <td>SG      </td> <td>Golden State Warriors</td> <td>2.5     </td>
        </tr>
        <tr>
            <td>Festus Ezeli     </td> <td>C       </td> <td>Golden State Warriors</td> <td>2.00875 </td>
        </tr>
        <tr>
            <td>Brandon Rush     </td> <td>SF      </td> <td>Golden State Warriors</td> <td>1.27096 </td>
        </tr>
        <tr>
            <td>Kevon Looney     </td> <td>SF      </td> <td>Golden State Warriors</td> <td>1.13196 </td>
        </tr>
        <tr>
            <td>Anderson Varejao </td> <td>PF      </td> <td>Golden State Warriors</td> <td>0.289755</td>
        </tr>
    </tbody>
</table>
</div>

</div>
</div>
</div>



This portion of the table is already sorted by salary, because the original table listed players sorted by salary within the same team. The `.show()` at the end of the line ensures that all rows are shown, not just the first 10.

It is so common to ask for the rows for which some column is equal to some value that the `are.equal_to` call is optional. Instead, the `where` method can be called with only a column name and a value to achieve the same effect.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('TEAM', 'Denver Nuggets') # equivalent to nba.where('TEAM', are.equal_to('Denver Nuggets'))

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
            <td>Danilo Gallinari </td> <td>SF      </td> <td>Denver Nuggets</td> <td>14     </td>
        </tr>
        <tr>
            <td>Kenneth Faried   </td> <td>PF      </td> <td>Denver Nuggets</td> <td>11.236 </td>
        </tr>
        <tr>
            <td>Wilson Chandler  </td> <td>SF      </td> <td>Denver Nuggets</td> <td>10.4494</td>
        </tr>
        <tr>
            <td>JJ Hickson       </td> <td>C       </td> <td>Denver Nuggets</td> <td>5.6135 </td>
        </tr>
        <tr>
            <td>Jameer Nelson    </td> <td>PG      </td> <td>Denver Nuggets</td> <td>4.345  </td>
        </tr>
        <tr>
            <td>Will Barton      </td> <td>SF      </td> <td>Denver Nuggets</td> <td>3.53333</td>
        </tr>
        <tr>
            <td>Emmanuel Mudiay  </td> <td>PG      </td> <td>Denver Nuggets</td> <td>3.10224</td>
        </tr>
        <tr>
            <td>Darrell Arthur   </td> <td>PF      </td> <td>Denver Nuggets</td> <td>2.814  </td>
        </tr>
        <tr>
            <td>Jusuf Nurkic     </td> <td>C       </td> <td>Denver Nuggets</td> <td>1.842  </td>
        </tr>
        <tr>
            <td>Joffrey Lauvergne</td> <td>C       </td> <td>Denver Nuggets</td> <td>1.70972</td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>
</div>


</div>
</div>
</div>



### Multiple Features
You can access rows that have multiple specified features, by using `where` repeatedly. For example, here is a way to extract all the Point Guards whose salaries were over $\$15$ million.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('POSITION', 'PG').where('SALARY', are.above(15))

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
            <td>Derrick Rose     </td> <td>PG      </td> <td>Chicago Bulls        </td> <td>20.0931</td>
        </tr>
        <tr>
            <td>Kyrie Irving     </td> <td>PG      </td> <td>Cleveland Cavaliers  </td> <td>16.4075</td>
        </tr>
        <tr>
            <td>Chris Paul       </td> <td>PG      </td> <td>Los Angeles Clippers </td> <td>21.4687</td>
        </tr>
        <tr>
            <td>Russell Westbrook</td> <td>PG      </td> <td>Oklahoma City Thunder</td> <td>16.7442</td>
        </tr>
        <tr>
            <td>John Wall        </td> <td>PG      </td> <td>Washington Wizards   </td> <td>15.852 </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



### General Form
By now you will have realized that the general way to create a new table by selecting rows with a given feature is to use `where` and `are` with the appropriate condition:

`original_table_name.where(column_label_string, are.condition)`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('SALARY', are.between(10, 10.3))

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
            <td>Luol Deng     </td> <td>SF      </td> <td>Miami Heat        </td> <td>10.1516</td>
        </tr>
        <tr>
            <td>Gerald Wallace</td> <td>SF      </td> <td>Philadelphia 76ers</td> <td>10.1059</td>
        </tr>
        <tr>
            <td>Danny Green   </td> <td>SG      </td> <td>San Antonio Spurs </td> <td>10     </td>
        </tr>
        <tr>
            <td>DeMar DeRozan </td> <td>SG      </td> <td>Toronto Raptors   </td> <td>10.05  </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



Notice that the table above includes Danny Green who made $\$10$ million, but *not* Monta Ellis who made $\$10.3$ million. As elsewhere in Python, the range `between` includes the left end but not the right.



If we specify a condition that isn't satisfied by any row, we get a table with column labels but no rows.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('PLAYER', are.equal_to('Barack Obama'))

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
    </tbody>
</table>
</div>


</div>
</div>
</div>



### Some More Conditions
Here are some predicates of `are` that you might find useful. Note that `x` and `y` are numbers, `STRING` is a string, and `Z` is either a number or a string; you have to specify these depending on the feature you want.

| **Predicate**              | Description                              |
|----------------------------|------------------------------------------|
| `are.equal_to(Z)`          | Equal to `Z`                             |        
| `are.above(x)`             | Greater than `x`                         |
| `are.above_or_equal_to(x)` | Greater than or equal to `x`             |
| `are.below(x)`             | Less than `x`                            |
| `are.below_or_equal_to(x)` | Less than or equal to `x`                |
| `are.between(x, y)`        | Greater than or equal to `x`, and less than `y` |
| `are.strictly_between(x, y)` | Greater than `x` and less than `y`     |
| `are.between_or_equal_to(x, y)` | Greater than or equal to `x`, and less than or equal to `y` |
| `are.containing(S)`        | Contains the string `S`                   |         



You can also specify the negation of any of these conditions, by using `.not_` before the condition:

| **Predicate**              | Description                              |
|----------------------------|------------------------------------------|
| `are.not_equal_to(Z)`      | Not equal to `Z`                         |    
| `are.not_above(x)`         | Not above `x`                            |



... and so on. The usual rules of logic apply – for example, "not above x" is the same as "below or equal to x".



We end the section with a series of examples. 



The use of `are.containing` can help save some typing. For example, you can just specify `Warriors` instead of `Golden State Warriors`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('TEAM', are.containing('Warriors')).show()

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
            <td>Klay Thompson    </td> <td>SG      </td> <td>Golden State Warriors</td> <td>15.501  </td>
        </tr>
        <tr>
            <td>Draymond Green   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>14.2609 </td>
        </tr>
        <tr>
            <td>Andrew Bogut     </td> <td>C       </td> <td>Golden State Warriors</td> <td>13.8    </td>
        </tr>
        <tr>
            <td>Andre Iguodala   </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105 </td>
        </tr>
        <tr>
            <td>Stephen Curry    </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708 </td>
        </tr>
        <tr>
            <td>Jason Thompson   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>7.00847 </td>
        </tr>
        <tr>
            <td>Shaun Livingston </td> <td>PG      </td> <td>Golden State Warriors</td> <td>5.54373 </td>
        </tr>
        <tr>
            <td>Harrison Barnes  </td> <td>SF      </td> <td>Golden State Warriors</td> <td>3.8734  </td>
        </tr>
        <tr>
            <td>Marreese Speights</td> <td>C       </td> <td>Golden State Warriors</td> <td>3.815   </td>
        </tr>
        <tr>
            <td>Leandro Barbosa  </td> <td>SG      </td> <td>Golden State Warriors</td> <td>2.5     </td>
        </tr>
        <tr>
            <td>Festus Ezeli     </td> <td>C       </td> <td>Golden State Warriors</td> <td>2.00875 </td>
        </tr>
        <tr>
            <td>Brandon Rush     </td> <td>SF      </td> <td>Golden State Warriors</td> <td>1.27096 </td>
        </tr>
        <tr>
            <td>Kevon Looney     </td> <td>SF      </td> <td>Golden State Warriors</td> <td>1.13196 </td>
        </tr>
        <tr>
            <td>Anderson Varejao </td> <td>PF      </td> <td>Golden State Warriors</td> <td>0.289755</td>
        </tr>
    </tbody>
</table>
</div>

</div>
</div>
</div>



You can extract data for all the guards, both Point Guards and Shooting Guards:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.where('POSITION', are.containing('G'))

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
            <td>Jeff Teague     </td> <td>PG      </td> <td>Atlanta Hawks </td> <td>8       </td>
        </tr>
        <tr>
            <td>Kyle Korver     </td> <td>SG      </td> <td>Atlanta Hawks </td> <td>5.74648 </td>
        </tr>
        <tr>
            <td>Dennis Schroder </td> <td>PG      </td> <td>Atlanta Hawks </td> <td>1.7634  </td>
        </tr>
        <tr>
            <td>Tim Hardaway Jr.</td> <td>SG      </td> <td>Atlanta Hawks </td> <td>1.30452 </td>
        </tr>
        <tr>
            <td>Jason Richardson</td> <td>SG      </td> <td>Atlanta Hawks </td> <td>0.947276</td>
        </tr>
        <tr>
            <td>Lamar Patterson </td> <td>SG      </td> <td>Atlanta Hawks </td> <td>0.525093</td>
        </tr>
        <tr>
            <td>Terran Petteway </td> <td>SG      </td> <td>Atlanta Hawks </td> <td>0.525093</td>
        </tr>
        <tr>
            <td>Avery Bradley   </td> <td>PG      </td> <td>Boston Celtics</td> <td>7.73034 </td>
        </tr>
        <tr>
            <td>Isaiah Thomas   </td> <td>PG      </td> <td>Boston Celtics</td> <td>6.91287 </td>
        </tr>
        <tr>
            <td>Marcus Smart    </td> <td>PG      </td> <td>Boston Celtics</td> <td>3.43104 </td>
        </tr>
    </tbody>
</table>
<p>... (171 rows omitted)</p>
</div>


</div>
</div>
</div>



You can get all the players who were not Cleveland Cavaliers and had a salary of no less than $\$20$ million:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
other_than_Cavs = nba.where('TEAM', are.not_equal_to('Cleveland Cavaliers'))
other_than_Cavs.where('SALARY', are.not_below(20))

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
            <td>Joe Johnson    </td> <td>SF      </td> <td>Brooklyn Nets        </td> <td>24.8949</td>
        </tr>
        <tr>
            <td>Derrick Rose   </td> <td>PG      </td> <td>Chicago Bulls        </td> <td>20.0931</td>
        </tr>
        <tr>
            <td>Dwight Howard  </td> <td>C       </td> <td>Houston Rockets      </td> <td>22.3594</td>
        </tr>
        <tr>
            <td>Chris Paul     </td> <td>PG      </td> <td>Los Angeles Clippers </td> <td>21.4687</td>
        </tr>
        <tr>
            <td>Kobe Bryant    </td> <td>SF      </td> <td>Los Angeles Lakers   </td> <td>25     </td>
        </tr>
        <tr>
            <td>Chris Bosh     </td> <td>PF      </td> <td>Miami Heat           </td> <td>22.1927</td>
        </tr>
        <tr>
            <td>Dwyane Wade    </td> <td>SG      </td> <td>Miami Heat           </td> <td>20     </td>
        </tr>
        <tr>
            <td>Carmelo Anthony</td> <td>SF      </td> <td>New York Knicks      </td> <td>22.875 </td>
        </tr>
        <tr>
            <td>Kevin Durant   </td> <td>SF      </td> <td>Oklahoma City Thunder</td> <td>20.1586</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The same table can be created in many ways. Here is another, and no doubt you can think of more.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
other_than_Cavs.where('SALARY', are.above_or_equal_to(20))

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
            <td>Joe Johnson    </td> <td>SF      </td> <td>Brooklyn Nets        </td> <td>24.8949</td>
        </tr>
        <tr>
            <td>Derrick Rose   </td> <td>PG      </td> <td>Chicago Bulls        </td> <td>20.0931</td>
        </tr>
        <tr>
            <td>Dwight Howard  </td> <td>C       </td> <td>Houston Rockets      </td> <td>22.3594</td>
        </tr>
        <tr>
            <td>Chris Paul     </td> <td>PG      </td> <td>Los Angeles Clippers </td> <td>21.4687</td>
        </tr>
        <tr>
            <td>Kobe Bryant    </td> <td>SF      </td> <td>Los Angeles Lakers   </td> <td>25     </td>
        </tr>
        <tr>
            <td>Chris Bosh     </td> <td>PF      </td> <td>Miami Heat           </td> <td>22.1927</td>
        </tr>
        <tr>
            <td>Dwyane Wade    </td> <td>SG      </td> <td>Miami Heat           </td> <td>20     </td>
        </tr>
        <tr>
            <td>Carmelo Anthony</td> <td>SF      </td> <td>New York Knicks      </td> <td>22.875 </td>
        </tr>
        <tr>
            <td>Kevin Durant   </td> <td>SF      </td> <td>Oklahoma City Thunder</td> <td>20.1586</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



As you can see, the use of `where` with `are` gives you great flexibility in accessing rows with features that interest you. Don't hesitate to experiment!

