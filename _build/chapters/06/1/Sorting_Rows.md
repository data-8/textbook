---
redirect_from:
  - "/chapters/06/1/sorting-rows"
interact_link: content/chapters/06/1/Sorting_Rows.ipynb
kernel_name: python3
has_widgets: false
title: 'Sorting Rows'
prev_page:
  url: /chapters/06/Tables
  title: 'Tables'
next_page:
  url: /chapters/06/2/Selecting_Rows
  title: 'Selecting Rows'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Sorting Rows

"The NBA is the highest paying professional sports league in the world," [reported CNN](http://edition.cnn.com/2015/12/04/sport/gallery/highest-paid-nba-players/) in March 2016. The table `nba_salaries` contains the salaries of all National Basketball Association players in 2015-2016.

Each row represents one player. The columns are:

| **Column Label**   | Description                                         |
|--------------------|-----------------------------------------------------|
| `PLAYER`           | Player's name                                       |
| `POSITION`         | Player's position on team                           |
| `TEAM`             | Team name                                           |
|`'15-'16 SALARY`    | Player's salary in 2015-2016, in millions of dollars|
 
The code for the positions is PG (Point Guard), SG (Shooting Guard), PF (Power Forward), SF (Small Forward), and C (Center). But what follows doesn't involve details about how basketball is played.

The first row shows that Paul Millsap, Power Forward for the Atlanta Hawks, had a salary of almost $\$18.7$ million in 2015-2016.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# This table can be found online: https://www.statcrunch.com/app/index.php?dataid=1843341
nba_salaries = Table.read_table(path_data + 'nba_salaries.csv')
nba_salaries

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>'15-'16 SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap    </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>18.6717       </td>
        </tr>
        <tr>
            <td>Al Horford      </td> <td>C       </td> <td>Atlanta Hawks</td> <td>12            </td>
        </tr>
        <tr>
            <td>Tiago Splitter  </td> <td>C       </td> <td>Atlanta Hawks</td> <td>9.75625       </td>
        </tr>
        <tr>
            <td>Jeff Teague     </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>8             </td>
        </tr>
        <tr>
            <td>Kyle Korver     </td> <td>SG      </td> <td>Atlanta Hawks</td> <td>5.74648       </td>
        </tr>
        <tr>
            <td>Thabo Sefolosha </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>4             </td>
        </tr>
        <tr>
            <td>Mike Scott      </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>3.33333       </td>
        </tr>
        <tr>
            <td>Kent Bazemore   </td> <td>SF      </td> <td>Atlanta Hawks</td> <td>2             </td>
        </tr>
        <tr>
            <td>Dennis Schroder </td> <td>PG      </td> <td>Atlanta Hawks</td> <td>1.7634        </td>
        </tr>
        <tr>
            <td>Tim Hardaway Jr.</td> <td>SG      </td> <td>Atlanta Hawks</td> <td>1.30452       </td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>
</div>


</div>
</div>
</div>



The table contains 417 rows, one for each player. Only 10 of the rows are displayed. The `show` method allows us to specify the number of rows, with the default (no specification) being all the rows of the table.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba_salaries.show(3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>'15-'16 SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap  </td> <td>PF      </td> <td>Atlanta Hawks</td> <td>18.6717       </td>
        </tr>
        <tr>
            <td>Al Horford    </td> <td>C       </td> <td>Atlanta Hawks</td> <td>12            </td>
        </tr>
        <tr>
            <td>Tiago Splitter</td> <td>C       </td> <td>Atlanta Hawks</td> <td>9.75625       </td>
        </tr>
    </tbody>
</table>
<p>... (414 rows omitted)</p>
</div>

</div>
</div>
</div>



Glance through about 20 rows or so, and you will see that the rows are in alphabetical order by team name. It's also possible to list the same rows in alphabetical order by player name using the `sort` method. The argument to `sort` is a column label or index.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba_salaries.sort('PLAYER').show(5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>'15-'16 SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Aaron Brooks  </td> <td>PG      </td> <td>Chicago Bulls         </td> <td>2.25          </td>
        </tr>
        <tr>
            <td>Aaron Gordon  </td> <td>PF      </td> <td>Orlando Magic         </td> <td>4.17168       </td>
        </tr>
        <tr>
            <td>Aaron Harrison</td> <td>SG      </td> <td>Charlotte Hornets     </td> <td>0.525093      </td>
        </tr>
        <tr>
            <td>Adreian Payne </td> <td>PF      </td> <td>Minnesota Timberwolves</td> <td>1.93884       </td>
        </tr>
        <tr>
            <td>Al Horford    </td> <td>C       </td> <td>Atlanta Hawks         </td> <td>12            </td>
        </tr>
    </tbody>
</table>
<p>... (412 rows omitted)</p>
</div>

</div>
</div>
</div>



To examine the players' salaries, it would be much more helpful if the data were ordered by salary.

To do this, we will first simplify the label of the column of salaries (just for convenience), and then sort by the new label `SALARY`. 

This arranges all the rows of the table in *increasing* order of salary, with the lowest salary appearing first. The output is a new table with the same columns as the original but with the rows rearranged.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba = nba_salaries.relabeled("'15-'16 SALARY", 'SALARY')
nba.sort('SALARY')

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
            <td>Thanasis Antetokounmpo</td> <td>SF      </td> <td>New York Knicks     </td> <td>0.030888</td>
        </tr>
        <tr>
            <td>Jordan McRae          </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.049709</td>
        </tr>
        <tr>
            <td>Cory Jefferson        </td> <td>PF      </td> <td>Phoenix Suns        </td> <td>0.049709</td>
        </tr>
        <tr>
            <td>Elliot Williams       </td> <td>SG      </td> <td>Memphis Grizzlies   </td> <td>0.055722</td>
        </tr>
        <tr>
            <td>Orlando Johnson       </td> <td>SG      </td> <td>Phoenix Suns        </td> <td>0.055722</td>
        </tr>
        <tr>
            <td>Phil Pressey          </td> <td>PG      </td> <td>Phoenix Suns        </td> <td>0.055722</td>
        </tr>
        <tr>
            <td>Keith Appling         </td> <td>PG      </td> <td>Orlando Magic       </td> <td>0.061776</td>
        </tr>
        <tr>
            <td>Sean Kilpatrick       </td> <td>SG      </td> <td>Denver Nuggets      </td> <td>0.099418</td>
        </tr>
        <tr>
            <td>Erick Green           </td> <td>PG      </td> <td>Utah Jazz           </td> <td>0.099418</td>
        </tr>
        <tr>
            <td>Jeff Ayres            </td> <td>PF      </td> <td>Los Angeles Clippers</td> <td>0.111444</td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>
</div>


</div>
</div>
</div>



These figures are somewhat difficult to compare as some of these players changed teams during the season and received salaries from more than one team; only the salary from the last team appears in the table. Point Guard Phil Pressey, for example, moved from Philadelphia to Phoenix during the year, and might be moving yet again to the Golden State Warriors. 

The CNN report is about the other end of the salary scale – the players who are among the highest paid in the world. 

To order the rows of the table in *decreasing* order of salary, we must use `sort` with the option `descending=True`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nba.sort('SALARY', descending=True)

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
            <td>Kobe Bryant    </td> <td>SF      </td> <td>Los Angeles Lakers   </td> <td>25     </td>
        </tr>
        <tr>
            <td>Joe Johnson    </td> <td>SF      </td> <td>Brooklyn Nets        </td> <td>24.8949</td>
        </tr>
        <tr>
            <td>LeBron James   </td> <td>SF      </td> <td>Cleveland Cavaliers  </td> <td>22.9705</td>
        </tr>
        <tr>
            <td>Carmelo Anthony</td> <td>SF      </td> <td>New York Knicks      </td> <td>22.875 </td>
        </tr>
        <tr>
            <td>Dwight Howard  </td> <td>C       </td> <td>Houston Rockets      </td> <td>22.3594</td>
        </tr>
        <tr>
            <td>Chris Bosh     </td> <td>PF      </td> <td>Miami Heat           </td> <td>22.1927</td>
        </tr>
        <tr>
            <td>Chris Paul     </td> <td>PG      </td> <td>Los Angeles Clippers </td> <td>21.4687</td>
        </tr>
        <tr>
            <td>Kevin Durant   </td> <td>SF      </td> <td>Oklahoma City Thunder</td> <td>20.1586</td>
        </tr>
        <tr>
            <td>Derrick Rose   </td> <td>PG      </td> <td>Chicago Bulls        </td> <td>20.0931</td>
        </tr>
        <tr>
            <td>Dwyane Wade    </td> <td>SG      </td> <td>Miami Heat           </td> <td>20     </td>
        </tr>
    </tbody>
</table>
<p>... (407 rows omitted)</p>
</div>


</div>
</div>
</div>



Kobe Bryant, in his final season with the Lakers, was the highest paid at a salary of $\$25$ million. Notice that the MVP Stephen Curry doesn't appear among the top 10. He is quite a bit further down the list, as we will see later.



### Named Arguments

The `descending=True` portion of this call expression is called a *named argument*. When a function or method is called, each argument has both a position and a name. Both are evident from the help text of a function or method.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(nba.sort)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on method sort in module datascience.tables:

sort(column_or_label, descending=False, distinct=False) method of datascience.tables.Table instance
    Return a Table of rows sorted according to the values in a column.
    
    Args:
        ``column_or_label``: the column whose values are used for sorting.
    
        ``descending``: if True, sorting will be in descending, rather than
            ascending order.
    
        ``distinct``: if True, repeated values in ``column_or_label`` will
            be omitted.
    
    Returns:
        An instance of ``Table`` containing rows sorted based on the values
        in ``column_or_label``.
    
    >>> marbles = Table().with_columns(
    ...    "Color", make_array("Red", "Green", "Blue", "Red", "Green", "Green"),
    ...    "Shape", make_array("Round", "Rectangular", "Rectangular", "Round", "Rectangular", "Round"),
    ...    "Amount", make_array(4, 6, 12, 7, 9, 2),
    ...    "Price", make_array(1.30, 1.30, 2.00, 1.75, 1.40, 1.00))
    >>> marbles
    Color | Shape       | Amount | Price
    Red   | Round       | 4      | 1.3
    Green | Rectangular | 6      | 1.3
    Blue  | Rectangular | 12     | 2
    Red   | Round       | 7      | 1.75
    Green | Rectangular | 9      | 1.4
    Green | Round       | 2      | 1
    >>> marbles.sort("Amount")
    Color | Shape       | Amount | Price
    Green | Round       | 2      | 1
    Red   | Round       | 4      | 1.3
    Green | Rectangular | 6      | 1.3
    Red   | Round       | 7      | 1.75
    Green | Rectangular | 9      | 1.4
    Blue  | Rectangular | 12     | 2
    >>> marbles.sort("Amount", descending = True)
    Color | Shape       | Amount | Price
    Blue  | Rectangular | 12     | 2
    Green | Rectangular | 9      | 1.4
    Red   | Round       | 7      | 1.75
    Green | Rectangular | 6      | 1.3
    Red   | Round       | 4      | 1.3
    Green | Round       | 2      | 1
    >>> marbles.sort(3) # the Price column
    Color | Shape       | Amount | Price
    Green | Round       | 2      | 1
    Red   | Round       | 4      | 1.3
    Green | Rectangular | 6      | 1.3
    Green | Rectangular | 9      | 1.4
    Red   | Round       | 7      | 1.75
    Blue  | Rectangular | 12     | 2
    >>> marbles.sort(3, distinct = True)
    Color | Shape       | Amount | Price
    Green | Round       | 2      | 1
    Red   | Round       | 4      | 1.3
    Green | Rectangular | 9      | 1.4
    Red   | Round       | 7      | 1.75
    Blue  | Rectangular | 12     | 2

```
</div>
</div>
</div>



At the very top of this `help` text, the *signature* of the `sort` method appears:

    sort(column_or_label, descending=False, distinct=False)
    
This describes the positions, names, and default values of the three arguments to `sort`. When calling this method, you can use either positional arguments or named arguments, so the following three calls do exactly the same thing.

    sort('SALARY', True)
    sort('SALARY', descending=True)
    sort(column_or_label='SALARY', descending=True)
    
When an argument is simply `True` or `False`, it's a useful convention to include the argument name so that it's more obvious what the argument value means.

