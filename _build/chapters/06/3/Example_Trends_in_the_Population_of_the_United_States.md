---
redirect_from:
  - "/chapters/06/3/example-trends-in-the-population-of-the-united-states"
interact_link: content/chapters/06/3/Example_Trends_in_the_Population_of_the_United_States.ipynb
kernel_name: python3
has_widgets: false
title: 'Example: Population Trends'
prev_page:
  url: /chapters/06/2/Selecting_Rows
  title: 'Selecting Rows'
next_page:
  url: /chapters/06/4/Example_Gender_Ratio_in_the_US_Population
  title: 'Example: Trends in Gender'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



# Example: Population Trends

We are now ready to work with large tables of data. The file below contains "Annual Estimates of the Resident Population by Single Year of Age and Sex for the United States." Notice that `read_table` can read data directly from a URL.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# As of Jan 2017, this census file is online here: 
data = 'http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv'

# A local copy can be accessed here in case census.gov moves the file:
# data = path_data + 'nc-est2015-agesex-res.csv'

full_census_table = Table.read_table(data)
full_census_table

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>CENSUS2010POP</th> <th>ESTIMATESBASE2010</th> <th>POPESTIMATE2010</th> <th>POPESTIMATE2011</th> <th>POPESTIMATE2012</th> <th>POPESTIMATE2013</th> <th>POPESTIMATE2014</th> <th>POPESTIMATE2015</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3944153      </td> <td>3944160          </td> <td>3951330        </td> <td>3963087        </td> <td>3926540        </td> <td>3931141        </td> <td>3949775        </td> <td>3978038        </td>
        </tr>
        <tr>
            <td>0   </td> <td>1   </td> <td>3978070      </td> <td>3978090          </td> <td>3957888        </td> <td>3966551        </td> <td>3977939        </td> <td>3942872        </td> <td>3949776        </td> <td>3968564        </td>
        </tr>
        <tr>
            <td>0   </td> <td>2   </td> <td>4096929      </td> <td>4096939          </td> <td>4090862        </td> <td>3971565        </td> <td>3980095        </td> <td>3992720        </td> <td>3959664        </td> <td>3966583        </td>
        </tr>
        <tr>
            <td>0   </td> <td>3   </td> <td>4119040      </td> <td>4119051          </td> <td>4111920        </td> <td>4102470        </td> <td>3983157        </td> <td>3992734        </td> <td>4007079        </td> <td>3974061        </td>
        </tr>
        <tr>
            <td>0   </td> <td>4   </td> <td>4063170      </td> <td>4063186          </td> <td>4077551        </td> <td>4122294        </td> <td>4112849        </td> <td>3994449        </td> <td>4005716        </td> <td>4020035        </td>
        </tr>
        <tr>
            <td>0   </td> <td>5   </td> <td>4056858      </td> <td>4056872          </td> <td>4064653        </td> <td>4087709        </td> <td>4132242        </td> <td>4123626        </td> <td>4006900        </td> <td>4018158        </td>
        </tr>
        <tr>
            <td>0   </td> <td>6   </td> <td>4066381      </td> <td>4066412          </td> <td>4073013        </td> <td>4074993        </td> <td>4097605        </td> <td>4142916        </td> <td>4135930        </td> <td>4019207        </td>
        </tr>
        <tr>
            <td>0   </td> <td>7   </td> <td>4030579      </td> <td>4030594          </td> <td>4043046        </td> <td>4083225        </td> <td>4084913        </td> <td>4108349        </td> <td>4155326        </td> <td>4148360        </td>
        </tr>
        <tr>
            <td>0   </td> <td>8   </td> <td>4046486      </td> <td>4046497          </td> <td>4025604        </td> <td>4053203        </td> <td>4093177        </td> <td>4095711        </td> <td>4120903        </td> <td>4167887        </td>
        </tr>
        <tr>
            <td>0   </td> <td>9   </td> <td>4148353      </td> <td>4148369          </td> <td>4125415        </td> <td>4035710        </td> <td>4063152        </td> <td>4104072        </td> <td>4108349        </td> <td>4133564        </td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



Only the first 10 rows of the table are displayed. Later we will see how to display the entire table; however, this is typically not useful with large tables.

a [description of the table](http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.pdf) appears online. The `SEX` column contains numeric codes: `0` stands for the total, `1` for male, and `2` for female. The `AGE` column contains ages in completed years, but the special value `999` is a sum of the total population. The rest of the columns contain estimates of the US population.

Typically, a public table will contain more information than necessary for a particular investigation or analysis. In this case, let us suppose that we are only interested in the population changes from 2010 to 2014. Let us `select` the relevant columns.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
partial_census_table = full_census_table.select('SEX', 'AGE', 'POPESTIMATE2010', 'POPESTIMATE2014')
partial_census_table

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>POPESTIMATE2010</th> <th>POPESTIMATE2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3951330        </td> <td>3949775        </td>
        </tr>
        <tr>
            <td>0   </td> <td>1   </td> <td>3957888        </td> <td>3949776        </td>
        </tr>
        <tr>
            <td>0   </td> <td>2   </td> <td>4090862        </td> <td>3959664        </td>
        </tr>
        <tr>
            <td>0   </td> <td>3   </td> <td>4111920        </td> <td>4007079        </td>
        </tr>
        <tr>
            <td>0   </td> <td>4   </td> <td>4077551        </td> <td>4005716        </td>
        </tr>
        <tr>
            <td>0   </td> <td>5   </td> <td>4064653        </td> <td>4006900        </td>
        </tr>
        <tr>
            <td>0   </td> <td>6   </td> <td>4073013        </td> <td>4135930        </td>
        </tr>
        <tr>
            <td>0   </td> <td>7   </td> <td>4043046        </td> <td>4155326        </td>
        </tr>
        <tr>
            <td>0   </td> <td>8   </td> <td>4025604        </td> <td>4120903        </td>
        </tr>
        <tr>
            <td>0   </td> <td>9   </td> <td>4125415        </td> <td>4108349        </td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



We can also simplify the labels of the selected columns.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
us_pop = partial_census_table.relabeled('POPESTIMATE2010', '2010').relabeled('POPESTIMATE2014', '2014')
us_pop

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2014</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3951330</td> <td>3949775</td>
        </tr>
        <tr>
            <td>0   </td> <td>1   </td> <td>3957888</td> <td>3949776</td>
        </tr>
        <tr>
            <td>0   </td> <td>2   </td> <td>4090862</td> <td>3959664</td>
        </tr>
        <tr>
            <td>0   </td> <td>3   </td> <td>4111920</td> <td>4007079</td>
        </tr>
        <tr>
            <td>0   </td> <td>4   </td> <td>4077551</td> <td>4005716</td>
        </tr>
        <tr>
            <td>0   </td> <td>5   </td> <td>4064653</td> <td>4006900</td>
        </tr>
        <tr>
            <td>0   </td> <td>6   </td> <td>4073013</td> <td>4135930</td>
        </tr>
        <tr>
            <td>0   </td> <td>7   </td> <td>4043046</td> <td>4155326</td>
        </tr>
        <tr>
            <td>0   </td> <td>8   </td> <td>4025604</td> <td>4120903</td>
        </tr>
        <tr>
            <td>0   </td> <td>9   </td> <td>4125415</td> <td>4108349</td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



We now have a table that is easy to work with. Each column of the table is an array of the same length, and so columns can be combined using arithmetic. Here is the change in population between 2010 and 2014.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
us_pop.column('2014') - us_pop.column('2010')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([  -1555,   -8112, -131198, ...,    6443,   12950, 4693244])
```


</div>
</div>
</div>



Let us augment `us_pop` with a column that contains these changes, both in absolute terms and as percents relative to the value in 2010.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
change = us_pop.column('2014') - us_pop.column('2010')
census = us_pop.with_columns(
    'Change', change,
    'Percent Change', change/us_pop.column('2010')
)
census.set_format('Percent Change', PercentFormatter)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2014</th> <th>Change</th> <th>Percent Change</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>0   </td> <td>3951330</td> <td>3949775</td> <td>-1555  </td> <td>-0.04%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>1   </td> <td>3957888</td> <td>3949776</td> <td>-8112  </td> <td>-0.20%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>2   </td> <td>4090862</td> <td>3959664</td> <td>-131198</td> <td>-3.21%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>3   </td> <td>4111920</td> <td>4007079</td> <td>-104841</td> <td>-2.55%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>4   </td> <td>4077551</td> <td>4005716</td> <td>-71835 </td> <td>-1.76%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>5   </td> <td>4064653</td> <td>4006900</td> <td>-57753 </td> <td>-1.42%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>6   </td> <td>4073013</td> <td>4135930</td> <td>62917  </td> <td>1.54%         </td>
        </tr>
        <tr>
            <td>0   </td> <td>7   </td> <td>4043046</td> <td>4155326</td> <td>112280 </td> <td>2.78%         </td>
        </tr>
        <tr>
            <td>0   </td> <td>8   </td> <td>4025604</td> <td>4120903</td> <td>95299  </td> <td>2.37%         </td>
        </tr>
        <tr>
            <td>0   </td> <td>9   </td> <td>4125415</td> <td>4108349</td> <td>-17066 </td> <td>-0.41%        </td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



**Sorting the data.** Let us sort the table in decreasing order of the absolute change in population.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
census.sort('Change', descending=True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SEX</th> <th>AGE</th> <th>2010</th> <th>2014</th> <th>Change</th> <th>Percent Change</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>999 </td> <td>309346863</td> <td>318907401</td> <td>9560538</td> <td>3.09%         </td>
        </tr>
        <tr>
            <td>1   </td> <td>999 </td> <td>152088043</td> <td>156955337</td> <td>4867294</td> <td>3.20%         </td>
        </tr>
        <tr>
            <td>2   </td> <td>999 </td> <td>157258820</td> <td>161952064</td> <td>4693244</td> <td>2.98%         </td>
        </tr>
        <tr>
            <td>0   </td> <td>67  </td> <td>2693707  </td> <td>3485241  </td> <td>791534 </td> <td>29.38%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>64  </td> <td>2706055  </td> <td>3487559  </td> <td>781504 </td> <td>28.88%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>66  </td> <td>2621335  </td> <td>3347060  </td> <td>725725 </td> <td>27.69%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>65  </td> <td>2678525  </td> <td>3382824  </td> <td>704299 </td> <td>26.29%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>71  </td> <td>1953607  </td> <td>2519705  </td> <td>566098 </td> <td>28.98%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>34  </td> <td>3822189  </td> <td>4364748  </td> <td>542559 </td> <td>14.19%        </td>
        </tr>
        <tr>
            <td>0   </td> <td>23  </td> <td>4217228  </td> <td>4702156  </td> <td>484928 </td> <td>11.50%        </td>
        </tr>
    </tbody>
</table>
<p>... (296 rows omitted)</p>
</div>


</div>
</div>
</div>



Not surprisingly, the top row of the sorted table is the line that corresponds to the entire population: both sexes and all age groups. From 2010 to 2014, the population of the United States increased by about 9.5 million people, a change of just over 3%.

The next two rows correspond to all the men and all the women respectively. The male population grew more than the female population, both in absolute and percentage terms. Both percent changes were around 3%.

Now take a look at the next few rows. The percent change jumps from about 3% for the overall population to almost 30% for the people in their late sixties and early seventies. This stunning change contributes to what is known as the greying of America.

By far the greatest absolute change was among those in the 64-67 agegroup in 2014. What could explain this large increase? We can explore this question by examining the years in which the relevant groups were born.

- Those who were in the 64-67 age group in 2010 were born in the years 1943 to 1946. The attack on Pearl Harbor was in late 1941, and by 1942 U.S. forces were heavily engaged in a massive war that ended in 1945. 

- Those who were 64 to 67 years old in 2014 were born in the years 1947 to 1950, at the height of the post-WWII baby boom in the United States. 

The post-war jump in births is the major reason for the large changes that we have observed.

