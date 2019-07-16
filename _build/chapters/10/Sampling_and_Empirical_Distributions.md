---
redirect_from:
  - "/chapters/10/sampling-and-empirical-distributions"
interact_link: content/chapters/10/Sampling_and_Empirical_Distributions.ipynb
kernel_name: Python [Root]
has_widgets: false
title: 'Sampling and Empirical Distributions'
prev_page:
  url: /chapters/09/5/Finding_Probabilities
  title: 'Finding Probabilities'
next_page:
  url: /chapters/10/1/Empirical_Distributions
  title: 'Empirical Distributions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Sampling and Empirical Distributions
An important part of data science consists of making conclusions based on the data in random samples. In order to correctly interpret their results, data scientists have to first understand exactly what random samples are.

In this chapter we will take a more careful look at sampling, with special attention to the properties of large random samples. 

Let's start by drawing some samples. Our examples are based on the <code><a href="imdb.csv">top_movies.csv</a></code> data set.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
top1 = Table.read_table(path_data + 'top_movies.csv')
top2 = top1.with_column('Row Index', np.arange(top1.num_rows))
top = top2.move_to_start('Row Index')

top.set_format(make_array(3, 4), NumberFormatter)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Row Index</th> <th>Title</th> <th>Studio</th> <th>Gross</th> <th>Gross (Adjusted)</th> <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0        </td> <td>Star Wars: The Force Awakens             </td> <td>Buena Vista (Disney)</td> <td>906,723,418</td> <td>906,723,400     </td> <td>2015</td>
        </tr>
        <tr>
            <td>1        </td> <td>Avatar                                   </td> <td>Fox                 </td> <td>760,507,625</td> <td>846,120,800     </td> <td>2009</td>
        </tr>
        <tr>
            <td>2        </td> <td>Titanic                                  </td> <td>Paramount           </td> <td>658,672,302</td> <td>1,178,627,900   </td> <td>1997</td>
        </tr>
        <tr>
            <td>3        </td> <td>Jurassic World                           </td> <td>Universal           </td> <td>652,270,625</td> <td>687,728,000     </td> <td>2015</td>
        </tr>
        <tr>
            <td>4        </td> <td>Marvel's The Avengers                    </td> <td>Buena Vista (Disney)</td> <td>623,357,910</td> <td>668,866,600     </td> <td>2012</td>
        </tr>
        <tr>
            <td>5        </td> <td>The Dark Knight                          </td> <td>Warner Bros.        </td> <td>534,858,444</td> <td>647,761,600     </td> <td>2008</td>
        </tr>
        <tr>
            <td>6        </td> <td>Star Wars: Episode I - The Phantom Menace</td> <td>Fox                 </td> <td>474,544,677</td> <td>785,715,000     </td> <td>1999</td>
        </tr>
        <tr>
            <td>7        </td> <td>Star Wars                                </td> <td>Fox                 </td> <td>460,998,007</td> <td>1,549,640,500   </td> <td>1977</td>
        </tr>
        <tr>
            <td>8        </td> <td>Avengers: Age of Ultron                  </td> <td>Buena Vista (Disney)</td> <td>459,005,868</td> <td>465,684,200     </td> <td>2015</td>
        </tr>
        <tr>
            <td>9        </td> <td>The Dark Knight Rises                    </td> <td>Warner Bros.        </td> <td>448,139,099</td> <td>500,961,700     </td> <td>2012</td>
        </tr>
    </tbody>
</table>
<p>... (190 rows omitted)</p>
</div>


</div>
</div>
</div>



### Sampling Rows of a Table
Each row of a data table represents an individual; in `top`, each individual is a movie. Sampling individuals can thus be achieved by sampling the rows of a table.

The contents of a row are the values of different variables measured on the same individual. So the contents of the sampled rows form samples of values of each of the variables.



### Deterministic Samples

When you simply specify which elements of a set you want to choose, without any chances involved, you create a *deterministic sample*.

You have done this many times, for example by using `take`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
top.take(make_array(3, 18, 100))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Row Index</th> <th>Title</th> <th>Studio</th> <th>Gross</th> <th>Gross (Adjusted)</th> <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>3        </td> <td>Jurassic World    </td> <td>Universal</td> <td>652,270,625</td> <td>687,728,000     </td> <td>2015</td>
        </tr>
        <tr>
            <td>18       </td> <td>Spider-Man        </td> <td>Sony     </td> <td>403,706,375</td> <td>604,517,300     </td> <td>2002</td>
        </tr>
        <tr>
            <td>100      </td> <td>Gone with the Wind</td> <td>MGM      </td> <td>198,676,459</td> <td>1,757,788,200   </td> <td>1939</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



You have also used `where`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
top.where('Title', are.containing('Harry Potter'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Row Index</th> <th>Title</th> <th>Studio</th> <th>Gross</th> <th>Gross (Adjusted)</th> <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>22       </td> <td>Harry Potter and the Deathly Hallows Part 2</td> <td>Warner Bros.</td> <td>381,011,219</td> <td>417,512,200     </td> <td>2011</td>
        </tr>
        <tr>
            <td>43       </td> <td>Harry Potter and the Sorcerer's Stone      </td> <td>Warner Bros.</td> <td>317,575,550</td> <td>486,442,900     </td> <td>2001</td>
        </tr>
        <tr>
            <td>54       </td> <td>Harry Potter and the Half-Blood Prince     </td> <td>Warner Bros.</td> <td>301,959,197</td> <td>352,098,800     </td> <td>2009</td>
        </tr>
        <tr>
            <td>59       </td> <td>Harry Potter and the Order of the Phoenix  </td> <td>Warner Bros.</td> <td>292,004,738</td> <td>369,250,200     </td> <td>2007</td>
        </tr>
        <tr>
            <td>62       </td> <td>Harry Potter and the Goblet of Fire        </td> <td>Warner Bros.</td> <td>290,013,036</td> <td>393,024,800     </td> <td>2005</td>
        </tr>
        <tr>
            <td>69       </td> <td>Harry Potter and the Chamber of Secrets    </td> <td>Warner Bros.</td> <td>261,988,482</td> <td>390,768,100     </td> <td>2002</td>
        </tr>
        <tr>
            <td>76       </td> <td>Harry Potter and the Prisoner of Azkaban   </td> <td>Warner Bros.</td> <td>249,541,069</td> <td>349,598,600     </td> <td>2004</td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



While these are samples, they are not random samples. They don't involve chance.



Probability Samples
------------------



For describing random samples, some terminology will be helpful.

A *population* is the set of all elements from whom a sample will be drawn.

A *probability sample* is one for which it is possible to calculate, before the sample is drawn, the chance with which any subset of elements will enter the sample.

In a probability sample, all elements need not have the same chance of being chosen. 

### A Random Sampling Scheme

For example, suppose you choose two people from a population that consists of three people A, B, and C, according to the following scheme:

- Person A is chosen with probability 1.
- One of Persons B or C is chosen according to the toss of a coin: if the coin lands heads, you choose B, and if it lands tails you choose C.

This is a probability sample of size 2. Here are the chances of entry for all non-empty subsets:

    A: 1 
    B: 1/2
    C: 1/2
    AB: 1/2
    AC: 1/2
    BC: 0
    ABC: 0

Person A has a higher chance of being selected than Persons B or C; indeed, Person A is certain to be selected. Since these differences are known and quantified, they can be taken into account when working with the sample. 



### A Systematic Sample

Imagine all the elements of the population listed in a sequence. One method of sampling starts by choosing a random position early in the list, and then evenly spaced positions after that. The sample consists of the elements in those positions. Such a sample is called a *systematic sample*. 

Here we will choose a systematic sample of the rows of `top`. We will start by picking one of the first 10 rows at random, and then we will pick every 10th row after that.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"""Choose a random start among rows 0 through 9;
then take every 10th row."""

start = np.random.choice(np.arange(10))
top.take(np.arange(start, top.num_rows, 10))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Row Index</th> <th>Title</th> <th>Studio</th> <th>Gross</th> <th>Gross (Adjusted)</th> <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2        </td> <td>Titanic                                    </td> <td>Paramount   </td> <td>658,672,302</td> <td>1,178,627,900   </td> <td>1997</td>
        </tr>
        <tr>
            <td>12       </td> <td>The Hunger Games: Catching Fire            </td> <td>Lionsgate   </td> <td>424,668,047</td> <td>444,697,400     </td> <td>2013</td>
        </tr>
        <tr>
            <td>22       </td> <td>Harry Potter and the Deathly Hallows Part 2</td> <td>Warner Bros.</td> <td>381,011,219</td> <td>417,512,200     </td> <td>2011</td>
        </tr>
        <tr>
            <td>32       </td> <td>American Sniper                            </td> <td>Warner Bros.</td> <td>350,126,372</td> <td>374,796,000     </td> <td>2014</td>
        </tr>
        <tr>
            <td>42       </td> <td>Iron Man                                   </td> <td>Paramount   </td> <td>318,412,101</td> <td>385,808,100     </td> <td>2008</td>
        </tr>
        <tr>
            <td>52       </td> <td>Skyfall                                    </td> <td>Sony        </td> <td>304,360,277</td> <td>329,225,400     </td> <td>2012</td>
        </tr>
        <tr>
            <td>62       </td> <td>Harry Potter and the Goblet of Fire        </td> <td>Warner Bros.</td> <td>290,013,036</td> <td>393,024,800     </td> <td>2005</td>
        </tr>
        <tr>
            <td>72       </td> <td>Jaws                                       </td> <td>Universal   </td> <td>260,000,000</td> <td>1,114,285,700   </td> <td>1975</td>
        </tr>
        <tr>
            <td>82       </td> <td>Twister                                    </td> <td>Warner Bros.</td> <td>241,721,524</td> <td>475,786,700     </td> <td>1996</td>
        </tr>
        <tr>
            <td>92       </td> <td>Ghost                                      </td> <td>Paramount   </td> <td>217,631,306</td> <td>447,747,400     </td> <td>1990</td>
        </tr>
    </tbody>
</table>
<p>... (10 rows omitted)</p>
</div>


</div>
</div>
</div>



Run the cell a few times to see how the output varies. 

This systematic sample is a probability sample. In this scheme, all rows have chance $1/10$ of being chosen. For example, Row 23 is chosen if and only if Row 3 is chosen, and the chance of that is $1/10$. 

But not all subsets have the same chance of being chosen. Because the selected rows are evenly spaced, most subsets of rows have no chance of being chosen. The only subsets that are possible are those that consist of rows all separated by multiples of 10. Any of those subsets is selected with chance 1/10.  Other subsets, like the subset containing the first 11 rows of the table, are selected with chance 0.



### Random Samples Drawn With or Without Replacement
In this course, we will mostly deal with the two most straightforward methods of sampling. 

The first is random sampling with replacement, which (as we have seen earlier) is the default behavior of `np.random.choice` when it samples from an array. 

The other, called a "simple random sample", is a sample drawn at random *without* replacement. Sampled individuals are not replaced in the population before the next individual is drawn. This is the kind of sampling that happens when you deal a hand from a deck of cards, for example. 

In this chapter, we will use simulation to study the behavior of large samples drawn at random with or without replacement.



Drawing a random sample requires care and precision. It is not haphazard, even though that is a colloquial meaning of the word "random". If you stand at a street corner and take as your sample the first ten people who pass by, you might think you're sampling at random because you didn't choose who walked by. But it's not a random sample – it's a *sample of convenience*. You didn't know ahead of time the probability of each person entering the sample; perhaps you hadn't even specified exactly who was in the population.

