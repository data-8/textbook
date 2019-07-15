---
redirect_from:
  - "/chapters/07/visualization"
interact_link: content/chapters/07/Visualization.ipynb
kernel_name: python3
has_widgets: false
title: 'Visualization'
prev_page:
  url: /chapters/06/4/Example_Gender_Ratio_in_the_US_Population
  title: 'Example: Trends in Gender'
next_page:
  url: /chapters/07/1/Visualizing_Categorical_Distributions
  title: 'Categorical Distributions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Visualization



Tables are a powerful way of organizing and visualizing data. However, large tables of numbers can be difficult to interpret, no matter how organized they are. Sometimes it is much easier to interpret graphs than numbers.

In this chapter we will develop some of the fundamental graphical methods of data analysis. Our source of data is the [Internet Movie Database](http://www.imdb.com), an online database that contains information about movies, television shows, video games, and so on. The site [Box Office Mojo](http://www.boxofficemojo.com) provides many summaries of IMDB data, some of which we have adapted. We have also used data summaries from [The Numbers](http://www.the-numbers.com), a site with a tagline that says it is "where data and the movie business meet."



### Scatter Plots and Line Graphs



The table `actors` contains data on Hollywood actors, both male and female. The columns are:

| ** Column **        | Contents |
|---------------------|----------|
|`Actor`              | Name of actor |
|`Total Gross`        | Total gross domestic box office receipt, in millions of dollars, of all of the actor's movies |
| `Number of Movies`  | The number of movies the actor has been in |
| `Average per Movie` | Total gross divided by number of movies |
| `#1 Movie`          | The highest grossing movie the actor has been in |
| `Gross`             | Gross domestic box office receipt, in millions of dollars, of the actor's `#1 Movie` |

In the calculation of the gross receipt, the data tabulators did not include movies where an actor had a cameo role or a speaking role that did not involve much screen time.

The table has 50 rows, corresponding to the 50 top grossing actors. The table is already sorted by `Total Gross`, so it is easy to see that Harrison Ford is the highest grossing actor. In total, his movies have brought in more money at domestic box office than the movies of any other actor.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
actors = Table.read_table(path_data + 'actors.csv')
actors

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Actor</th> <th>Total Gross</th> <th>Number of Movies</th> <th>Average per Movie</th> <th>#1 Movie</th> <th>Gross</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Harrison Ford     </td> <td>4871.7     </td> <td>41              </td> <td>118.8            </td> <td>Star Wars: The Force Awakens</td> <td>936.7</td>
        </tr>
        <tr>
            <td>Samuel L. Jackson </td> <td>4772.8     </td> <td>69              </td> <td>69.2             </td> <td>The Avengers                </td> <td>623.4</td>
        </tr>
        <tr>
            <td>Morgan Freeman    </td> <td>4468.3     </td> <td>61              </td> <td>73.3             </td> <td>The Dark Knight             </td> <td>534.9</td>
        </tr>
        <tr>
            <td>Tom Hanks         </td> <td>4340.8     </td> <td>44              </td> <td>98.7             </td> <td>Toy Story 3                 </td> <td>415  </td>
        </tr>
        <tr>
            <td>Robert Downey, Jr.</td> <td>3947.3     </td> <td>53              </td> <td>74.5             </td> <td>The Avengers                </td> <td>623.4</td>
        </tr>
        <tr>
            <td>Eddie Murphy      </td> <td>3810.4     </td> <td>38              </td> <td>100.3            </td> <td>Shrek 2                     </td> <td>441.2</td>
        </tr>
        <tr>
            <td>Tom Cruise        </td> <td>3587.2     </td> <td>36              </td> <td>99.6             </td> <td>War of the Worlds           </td> <td>234.3</td>
        </tr>
        <tr>
            <td>Johnny Depp       </td> <td>3368.6     </td> <td>45              </td> <td>74.9             </td> <td>Dead Man's Chest            </td> <td>423.3</td>
        </tr>
        <tr>
            <td>Michael Caine     </td> <td>3351.5     </td> <td>58              </td> <td>57.8             </td> <td>The Dark Knight             </td> <td>534.9</td>
        </tr>
        <tr>
            <td>Scarlett Johansson</td> <td>3341.2     </td> <td>37              </td> <td>90.3             </td> <td>The Avengers                </td> <td>623.4</td>
        </tr>
    </tbody>
</table>
<p>... (40 rows omitted)</p>
</div>


</div>
</div>
</div>



**Terminology.**
A *variable* is a formal name for what we have been calling a "feature", such as 'number of movies.' The term *variable* emphasizes that the feature can have different values for different individuals – the numbers of movies that actors have been in varies across all the actors.

Variables that have numerical values, such as 'number of movies' or 'average gross receipts per movie' are called *quantitative* or *numerical* variables.



### Scatter Plots
A *scatter plot* displays the relation between two numerical variables. You saw an example of a scatter plot in an early section where we looked at the number of periods and number of characters in two classic novels.

The Table method `scatter` draws a scatter plot consisting of one point for each row of the table. Its first argument is the label of the column to be plotted on the horizontal axis, and its second argument is the label of the column on the vertical.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
actors.scatter('Number of Movies', 'Total Gross')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_8_0.png)

</div>
</div>
</div>



The plot contains 50 points, one point for each actor in the table. You can see that it slopes upwards, in general. The more movies an actor has been in, the more the total gross of all of those movies – in general.

Formally, we say that the plot shows an *association* between the variables, and that the association is *positive*: high values of one variable tend to be associated with high values of the other, and low values of one with low values of the other, in general. 

Of course there is some variability. Some actors have high numbers of movies but middling total gross receipts. Others have middling numbers of movies but high receipts. That the association is positive is simply a statement about the broad general trend.

Later in the course we will study how to quantify association. For the moment, we will just think about it qualitatively.



Now that we have explored how the number of movies is related to the *total* gross receipt, let's turn our attention to how it is related to the *average* gross receipt per movie.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
actors.scatter('Number of Movies', 'Average per Movie')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_11_0.png)

</div>
</div>
</div>



This is a markedly different picture and shows a *negative* association. In general, the more movies an actor has been in, the *less* the average receipt per movie.

Also, one of the points is quite high and off to the left of the plot. It corresponds to one actor who has a low number of movies and high average per movie. This point is an *outlier*. It lies outside the general range of the data. Indeed, it is quite far from all the other points in the plot.



We will examine the negative association further by looking at points at the right and left ends of the plot. 

For the right end, let's zoom in on the main body of the plot by just looking at the portion that doesn't have the outlier.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
no_outlier = actors.where('Number of Movies', are.above(10))
no_outlier.scatter('Number of Movies', 'Average per Movie')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_14_0.png)

</div>
</div>
</div>



The negative association is still clearly visible. Let's identify the actors corresponding to the points that lie on the right hand side of the plot where the number of movies is large:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
actors.where('Number of Movies', are.above(60))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Actor</th> <th>Total Gross</th> <th>Number of Movies</th> <th>Average per Movie</th> <th>#1 Movie</th> <th>Gross</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Samuel L. Jackson</td> <td>4772.8     </td> <td>69              </td> <td>69.2             </td> <td>The Avengers      </td> <td>623.4</td>
        </tr>
        <tr>
            <td>Morgan Freeman   </td> <td>4468.3     </td> <td>61              </td> <td>73.3             </td> <td>The Dark Knight   </td> <td>534.9</td>
        </tr>
        <tr>
            <td>Robert DeNiro    </td> <td>3081.3     </td> <td>79              </td> <td>39               </td> <td>Meet the Fockers  </td> <td>279.3</td>
        </tr>
        <tr>
            <td>Liam Neeson      </td> <td>2942.7     </td> <td>63              </td> <td>46.7             </td> <td>The Phantom Menace</td> <td>474.5</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



The great actor Robert DeNiro has the highest number of movies and the lowest average receipt per movie. Other fine actors are at points that are not very far away, but DeNiro's is at the extreme end.

To understand the negative association, note that the more movies an actor is in, the more variable those movies might be, in terms of style, genre, and box office draw. For example, an actor might be in some high-grossing action movies or comedies (such as Meet the Fockers), and also in a large number of smaller films that may be excellent but don't draw large crowds. Thus the actor's value of average receipts per movie might be relatively low.

To approach this argument from a different direction, let us now take a look at the outlier.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
actors.where('Number of Movies', are.below(10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Actor</th> <th>Total Gross</th> <th>Number of Movies</th> <th>Average per Movie</th> <th>#1 Movie</th> <th>Gross</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Anthony Daniels</td> <td>3162.9     </td> <td>7               </td> <td>451.8            </td> <td>Star Wars: The Force Awakens</td> <td>936.7</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



As an actor, Anthony Daniels might not have the stature of Robert DeNiro. But his 7 movies had an astonishingly high average receipt of nearly $452$ million dollars per movie.

What were these movies? You might know about the droid C-3PO in Star Wars:
![C-3PO](../../images/C-3PO_droid.png)
That's [Anthony Daniels](https://en.wikipedia.org/wiki/Anthony_Daniels) inside the metallic suit. He plays C-3PO.

Mr. Daniels' entire filmography (apart from cameos) consists of movies in the high-grossing Star Wars franchise. That explains both his high average receipt and his low number of movies.

Variables such as genre and production budget have an effect on the association between the number of movies and the average receipt per movie. This example is a reminder that studying the association between two variables often involves understanding other related variables as well. 



### Line Graphs
Line graphs are among the most common visualizations and are often used to study chronological trends and patterns.

The table `movies_by_year` contains data on movies produced by U.S. studios in each of the years 1980 through 2015. The columns are:

| **Column** | Content |
|------------|---------|
| `Year` | Year |
| `Total Gross` | Total domestic box office gross, in millions of dollars, of all movies released |
| `Number of Movies` | Number of movies released |
| `#1 Movie` | Highest grossing movie |



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
movies_by_year = Table.read_table(path_data + 'movies_by_year.csv')
movies_by_year

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Total Gross</th> <th>Number of Movies</th> <th>#1 Movie</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2015</td> <td>11128.5    </td> <td>702             </td> <td>Star Wars: The Force Awakens       </td>
        </tr>
        <tr>
            <td>2014</td> <td>10360.8    </td> <td>702             </td> <td>American Sniper                    </td>
        </tr>
        <tr>
            <td>2013</td> <td>10923.6    </td> <td>688             </td> <td>Catching Fire                      </td>
        </tr>
        <tr>
            <td>2012</td> <td>10837.4    </td> <td>667             </td> <td>The Avengers                       </td>
        </tr>
        <tr>
            <td>2011</td> <td>10174.3    </td> <td>602             </td> <td>Harry Potter / Deathly Hallows (P2)</td>
        </tr>
        <tr>
            <td>2010</td> <td>10565.6    </td> <td>536             </td> <td>Toy Story 3                        </td>
        </tr>
        <tr>
            <td>2009</td> <td>10595.5    </td> <td>521             </td> <td>Avatar                             </td>
        </tr>
        <tr>
            <td>2008</td> <td>9630.7     </td> <td>608             </td> <td>The Dark Knight                    </td>
        </tr>
        <tr>
            <td>2007</td> <td>9663.8     </td> <td>631             </td> <td>Spider-Man 3                       </td>
        </tr>
        <tr>
            <td>2006</td> <td>9209.5     </td> <td>608             </td> <td>Dead Man's Chest                   </td>
        </tr>
    </tbody>
</table>
<p>... (26 rows omitted)</p>
</div>


</div>
</div>
</div>



The Table method `plot` produces a line graph. Its two arguments are the same as those for `scatter`: first the column on the horizontal axis, then the column on the vertical. Here is a line graph of the number of movies released each year over the years 1980 through 2015.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
movies_by_year.plot('Year', 'Number of Movies')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_23_0.png)

</div>
</div>
</div>



The graph rises sharply and then has a gentle upwards trend though the numbers vary noticeably from year to year. The sharp rise in the early 1980's is due in part to studios returning to the forefront of movie production after some years of filmmaker driven movies in the 1970's. 

Our focus will be on more recent years. In keeping with the theme of movies, the table of rows corresponding to the years 2000 through 2015 have been assigned to the name `century_21`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
century_21 = movies_by_year.where('Year', are.above(1999))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
century_21.plot('Year', 'Number of Movies')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_26_0.png)

</div>
</div>
</div>



The global financial crisis of 2008 has a visible effect – in 2009 there is a sharp drop in the number of movies released.

The dollar figures, however, didn't suffer much.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
century_21.plot('Year', 'Total Gross')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/chapters/07/Visualization_28_0.png)

</div>
</div>
</div>



The total domestic gross receipt was higher in 2009 than in 2008, even though there was a financial crisis and a much smaller number of movies were released.

One reason for this apparent contradiction is that people tend to go to the movies when there is a recession. ["In Downturn, Americans Flock to the Movies,"](http://www.nytimes.com/2009/03/01/movies/01films.html?_r=0) said the New York Times in February 2009. The article quotes Martin Kaplan of the University of Southern California saying, "People want to forget their troubles, and they want to be with other people." When holidays and expensive treats are unaffordable, movies provide welcome entertainment and relief.

In 2009, another reason for high box office receipts was the movie Avatar and its 3D release. Not only was Avatar the \#1 movie of 2009, it is also by some calculations the second highest grossing movie of all time, as we will see later.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
century_21.where('Year', are.equal_to(2009))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Total Gross</th> <th>Number of Movies</th> <th>#1 Movie</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2009</td> <td>10595.5    </td> <td>521             </td> <td>Avatar  </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>

