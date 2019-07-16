---
redirect_from:
  - "/chapters/17/1/nearest-neighbors"
interact_link: content/chapters/17/1/Nearest_Neighbors.ipynb
kernel_name: python3
has_widgets: false
title: 'Nearest Neighbors'
prev_page:
  url: /chapters/17/Classification
  title: 'Classification'
next_page:
  url: /chapters/17/2/Training_and_Testing
  title: 'Training and Testing'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



### Nearest Neighbors
In this section we'll develop the *nearest neighbor* method of classification. Just focus on the ideas for now and don't worry if some of the code is mysterious. Later in the chapter we'll see how to organize our ideas into code that performs the classification.



### Chronic kidney disease

Let's work through an example.  We're going to work with a data set that was collected to help doctors diagnose chronic kidney disease (CKD).  Each row in the data set represents a single patient who was treated in the past and whose diagnosis is known.  For each patient, we have a bunch of measurements from a blood test.  We'd like to find which measurements are most useful for diagnosing CKD, and develop a way to classify future patients as "has CKD" or "doesn't have CKD" based on their blood test results.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ckd = Table.read_table(path_data + 'ckd.csv').relabeled('Blood Glucose Random', 'Glucose')
ckd

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Age</th> <th>Blood Pressure</th> <th>Specific Gravity</th> <th>Albumin</th> <th>Sugar</th> <th>Red Blood Cells</th> <th>Pus Cell</th> <th>Pus Cell clumps</th> <th>Bacteria</th> <th>Glucose</th> <th>Blood Urea</th> <th>Serum Creatinine</th> <th>Sodium</th> <th>Potassium</th> <th>Hemoglobin</th> <th>Packed Cell Volume</th> <th>White Blood Cell Count</th> <th>Red Blood Cell Count</th> <th>Hypertension</th> <th>Diabetes Mellitus</th> <th>Coronary Artery Disease</th> <th>Appetite</th> <th>Pedal Edema</th> <th>Anemia</th> <th>Class</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>48  </td> <td>70            </td> <td>1.005           </td> <td>4      </td> <td>0    </td> <td>normal         </td> <td>abnormal</td> <td>present        </td> <td>notpresent</td> <td>117    </td> <td>56        </td> <td>3.8             </td> <td>111   </td> <td>2.5      </td> <td>11.2      </td> <td>32                </td> <td>6700                  </td> <td>3.9                 </td> <td>yes         </td> <td>no               </td> <td>no                     </td> <td>poor    </td> <td>yes        </td> <td>yes   </td> <td>1    </td>
        </tr>
        <tr>
            <td>53  </td> <td>90            </td> <td>1.02            </td> <td>2      </td> <td>0    </td> <td>abnormal       </td> <td>abnormal</td> <td>present        </td> <td>notpresent</td> <td>70     </td> <td>107       </td> <td>7.2             </td> <td>114   </td> <td>3.7      </td> <td>9.5       </td> <td>29                </td> <td>12100                 </td> <td>3.7                 </td> <td>yes         </td> <td>yes              </td> <td>no                     </td> <td>poor    </td> <td>no         </td> <td>yes   </td> <td>1    </td>
        </tr>
        <tr>
            <td>63  </td> <td>70            </td> <td>1.01            </td> <td>3      </td> <td>0    </td> <td>abnormal       </td> <td>abnormal</td> <td>present        </td> <td>notpresent</td> <td>380    </td> <td>60        </td> <td>2.7             </td> <td>131   </td> <td>4.2      </td> <td>10.8      </td> <td>32                </td> <td>4500                  </td> <td>3.8                 </td> <td>yes         </td> <td>yes              </td> <td>no                     </td> <td>poor    </td> <td>yes        </td> <td>no    </td> <td>1    </td>
        </tr>
        <tr>
            <td>68  </td> <td>80            </td> <td>1.01            </td> <td>3      </td> <td>2    </td> <td>normal         </td> <td>abnormal</td> <td>present        </td> <td>present   </td> <td>157    </td> <td>90        </td> <td>4.1             </td> <td>130   </td> <td>6.4      </td> <td>5.6       </td> <td>16                </td> <td>11000                 </td> <td>2.6                 </td> <td>yes         </td> <td>yes              </td> <td>yes                    </td> <td>poor    </td> <td>yes        </td> <td>no    </td> <td>1    </td>
        </tr>
        <tr>
            <td>61  </td> <td>80            </td> <td>1.015           </td> <td>2      </td> <td>0    </td> <td>abnormal       </td> <td>abnormal</td> <td>notpresent     </td> <td>notpresent</td> <td>173    </td> <td>148       </td> <td>3.9             </td> <td>135   </td> <td>5.2      </td> <td>7.7       </td> <td>24                </td> <td>9200                  </td> <td>3.2                 </td> <td>yes         </td> <td>yes              </td> <td>yes                    </td> <td>poor    </td> <td>yes        </td> <td>yes   </td> <td>1    </td>
        </tr>
        <tr>
            <td>48  </td> <td>80            </td> <td>1.025           </td> <td>4      </td> <td>0    </td> <td>normal         </td> <td>abnormal</td> <td>notpresent     </td> <td>notpresent</td> <td>95     </td> <td>163       </td> <td>7.7             </td> <td>136   </td> <td>3.8      </td> <td>9.8       </td> <td>32                </td> <td>6900                  </td> <td>3.4                 </td> <td>yes         </td> <td>no               </td> <td>no                     </td> <td>good    </td> <td>no         </td> <td>yes   </td> <td>1    </td>
        </tr>
        <tr>
            <td>69  </td> <td>70            </td> <td>1.01            </td> <td>3      </td> <td>4    </td> <td>normal         </td> <td>abnormal</td> <td>notpresent     </td> <td>notpresent</td> <td>264    </td> <td>87        </td> <td>2.7             </td> <td>130   </td> <td>4        </td> <td>12.5      </td> <td>37                </td> <td>9600                  </td> <td>4.1                 </td> <td>yes         </td> <td>yes              </td> <td>yes                    </td> <td>good    </td> <td>yes        </td> <td>no    </td> <td>1    </td>
        </tr>
        <tr>
            <td>73  </td> <td>70            </td> <td>1.005           </td> <td>0      </td> <td>0    </td> <td>normal         </td> <td>normal  </td> <td>notpresent     </td> <td>notpresent</td> <td>70     </td> <td>32        </td> <td>0.9             </td> <td>125   </td> <td>4        </td> <td>10        </td> <td>29                </td> <td>18900                 </td> <td>3.5                 </td> <td>yes         </td> <td>yes              </td> <td>no                     </td> <td>good    </td> <td>yes        </td> <td>no    </td> <td>1    </td>
        </tr>
        <tr>
            <td>73  </td> <td>80            </td> <td>1.02            </td> <td>2      </td> <td>0    </td> <td>abnormal       </td> <td>abnormal</td> <td>notpresent     </td> <td>notpresent</td> <td>253    </td> <td>142       </td> <td>4.6             </td> <td>138   </td> <td>5.8      </td> <td>10.5      </td> <td>33                </td> <td>7200                  </td> <td>4.3                 </td> <td>yes         </td> <td>yes              </td> <td>yes                    </td> <td>good    </td> <td>no         </td> <td>no    </td> <td>1    </td>
        </tr>
        <tr>
            <td>46  </td> <td>60            </td> <td>1.01            </td> <td>1      </td> <td>0    </td> <td>normal         </td> <td>normal  </td> <td>notpresent     </td> <td>notpresent</td> <td>163    </td> <td>92        </td> <td>3.3             </td> <td>141   </td> <td>4        </td> <td>9.8       </td> <td>28                </td> <td>14600                 </td> <td>3.2                 </td> <td>yes         </td> <td>yes              </td> <td>no                     </td> <td>good    </td> <td>no         </td> <td>no    </td> <td>1    </td>
        </tr>
    </tbody>
</table>
<p>... (148 rows omitted)</p>
</div>


</div>
</div>
</div>



Some of the variables are categorical (words like "abnormal"), and some quantitative. The quantitative variables all have different scales. We're going to want to make comparisons and estimate distances, often by eye, so let's select just a few of the variables and work in standard units. Then we won't have to worry about the scale of each of the different variables.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ckd = Table().with_columns(
    'Hemoglobin', standard_units(ckd.column('Hemoglobin')),
    'Glucose', standard_units(ckd.column('Glucose')),
    'White Blood Cell Count', standard_units(ckd.column('White Blood Cell Count')),
    'Class', ckd.column('Class')
)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ckd

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Hemoglobin</th> <th>Glucose</th> <th>White Blood Cell Count</th> <th>Class</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>-0.865744 </td> <td>-0.221549</td> <td>-0.569768             </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.45745  </td> <td>-0.947597</td> <td>1.16268               </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.00497  </td> <td>3.84123  </td> <td>-1.27558              </td> <td>1    </td>
        </tr>
        <tr>
            <td>-2.81488  </td> <td>0.396364 </td> <td>0.809777              </td> <td>1    </td>
        </tr>
        <tr>
            <td>-2.08395  </td> <td>0.643529 </td> <td>0.232293              </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.35303  </td> <td>-0.561402</td> <td>-0.505603             </td> <td>1    </td>
        </tr>
        <tr>
            <td>-0.413266 </td> <td>2.04928  </td> <td>0.360623              </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.28342  </td> <td>-0.947597</td> <td>3.34429               </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.10939  </td> <td>1.87936  </td> <td>-0.409356             </td> <td>1    </td>
        </tr>
        <tr>
            <td>-1.35303  </td> <td>0.489051 </td> <td>1.96475               </td> <td>1    </td>
        </tr>
    </tbody>
</table>
<p>... (148 rows omitted)</p>
</div>


</div>
</div>
</div>



Let's look at two columns in particular: the hemoglobin level (in the patient's blood), and the blood glucose level (at a random time in the day; without fasting specially for the blood test). 

We'll draw a scatter plot to visualize the relation between the two variables. Blue dots are patients with CKD; gold dots are patients without CKD.  What kind of medical test results seem to indicate CKD?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
color_table = Table().with_columns(
    'Class', make_array(1, 0),
    'Color', make_array('darkblue', 'gold')
)
ckd = ckd.join('Class', color_table)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ckd.scatter('Hemoglobin', 'Glucose', group='Color')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_11_0.png)

</div>
</div>
</div>



Suppose Alice is a new patient who is not in the data set.  If I tell you Alice's hemoglobin level and blood glucose level, could you predict whether she has CKD?  It sure looks like it!  You can see a very clear pattern here: points in the lower-right tend to represent people who don't have CKD, and the rest tend to be folks with CKD.  To a human, the pattern is obvious.  But how can we program a computer to automatically detect patterns such as this one?



### A Nearest Neighbor Classifier

There are lots of kinds of patterns one might look for, and lots of algorithms for classification.  But I'm going to tell you about one that turns out to be surprisingly effective.  It is called *nearest neighbor classification*.  Here's the idea.  If we have Alice's hemoglobin and glucose numbers, we can put her somewhere on this scatterplot; the hemoglobin is her x-coordinate, and the glucose is her y-coordinate.  Now, to predict whether she has CKD or not, we find the nearest point in the scatterplot and check whether it is blue or gold; we predict that Alice should receive the same diagnosis as that patient.

In other words, to classify Alice as CKD or not, we find the patient in the training set who is "nearest" to Alice, and then use that patient's diagnosis as our prediction for Alice.  The intuition is that if two points are near each other in the scatterplot, then the corresponding measurements are pretty similar, so we might expect them to receive the same diagnosis (more likely than not).  We don't know Alice's diagnosis, but we do know the diagnosis of all the patients in the training set, so we find the patient in the training set who is most similar to Alice, and use that patient's diagnosis to predict Alice's diagnosis.



In the graph below, the red dot represents Alice. It is joined with a black line to the point that is nearest to it – its *nearest neighbor* in the training set. The figure is drawn by a function called `show_closest`. It takes an array that represents the $x$ and $y$ coordinates of Alice's point. Vary those to see how the closest point changes! Note especially when the closest point is blue and when it is gold.



<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# In this example, Alice's Hemoglobin attribute is 0 and her Glucose is 1.5.
alice = make_array(0, 1.5)
show_closest(alice)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_16_0.png)

</div>
</div>
</div>



Thus our *nearest neighbor classifier* works like this:
- Find the point in the training set that is nearest to the new point.
- If that nearest point is a "CKD" point, classify the new point as "CKD". If the nearest point is a "not CKD" point, classify the new point as "not CKD".

The scatterplot suggests that this nearest neighbor classifier should be pretty accurate.  Points in the lower-right will tend to receive a "no CKD" diagnosis, as their nearest neighbor will be a gold point.  The rest of the points will tend to receive a "CKD" diagnosis, as their nearest neighbor will be a blue point.  So the nearest neighbor strategy seems to capture our intuition pretty well, for this example.



### Decision boundary

Sometimes a helpful way to visualize a classifier is to map out the kinds of attributes where the classifier would predict 'CKD', and the kinds where it would predict 'not CKD'.  We end up with some boundary between the two, where points on one side of the boundary will be classified 'CKD' and points on the other side will be classified 'not CKD'.  This boundary is called the *decision boundary*.  Each different classifier will have a different decision boundary; the decision boundary is just a way to visualize what criteria the classifier is using to classify points.

For example, suppose the coordinates of Alice's point are (0, 1.5). Notice that the nearest neighbor is blue. Now try reducing the height (the $y$-coordinate) of the point. You'll see that at around $y = 0.95$ the nearest neighbor turns from blue to gold.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
alice = make_array(0, 0.97)
show_closest(alice)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_19_0.png)

</div>
</div>
</div>



Here are hundreds of new unclassified points, all in red.



<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_22_0.png)

</div>
</div>
</div>



Each of the red points has a nearest neighbor in the training set (the same blue and gold points as before). For some red points you can easily tell whether the nearest neighbor is blue or gold. For others, it's a little more tricky to make the decision by eye. Those are the points near the decision boundary.

But the computer can easily determine the nearest neighbor of each point. So let's get it to apply our nearest neighbor classifier to each of the red points: 

For each red point, it must find the closest point in the training set; it must then change the color of the red point to become the color of the nearest neighbor. 

The resulting graph shows which points will get classified as 'CKD' (all the blue ones), and which as 'not CKD' (all the gold ones).



<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


</div>



<div markdown="1" class="cell code_cell">


<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_26_0.png)

</div>
</div>
</div>



The decision boundary is where the classifier switches from turning the red points blue to turning them gold.



### k-Nearest Neighbors

However, the separation between the two classes won't always be quite so clean.  For instance, suppose that instead of hemoglobin levels we were to look at white blood cell count.  Look at what happens:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ckd.scatter('White Blood Cell Count', 'Glucose', group='Color')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/17/1/Nearest_Neighbors_29_0.png)

</div>
</div>
</div>



As you can see, non-CKD individuals are all clustered in the lower-left.  Most of the patients with CKD are above or to the right of that cluster... but not all.  There are some patients with CKD who are in the lower left of the above figure (as indicated by the handful of blue dots scattered among the gold cluster).  What this means is that you can't tell for certain whether someone has CKD from just these two blood test measurements.

If we are given Alice's glucose level and white blood cell count, can we predict whether she has CKD?  Yes, we can make a prediction, but we shouldn't expect it to be 100% accurate.  Intuitively, it seems like there's a natural strategy for predicting: plot where Alice lands in the scatter plot; if she is in the lower-left, predict that she doesn't have CKD, otherwise predict she has CKD.  

This isn't perfect -- our predictions will sometimes be wrong.  (Take a minute and think it through: for which patients will it make a mistake?)  As the scatterplot above indicates, sometimes people with CKD have glucose and white blood cell levels that look identical to those of someone without CKD, so any classifier is inevitably going to make the wrong prediction for them.

Can we automate this on a computer?  Well, the nearest neighbor classifier would be a reasonable choice here too.  Take a minute and think it through: how will its predictions compare to those from the intuitive strategy above?  When will they differ?

Its predictions will be pretty similar to our intuitive strategy, but occasionally it will make a different prediction.  In particular, if Alice's blood test results happen to put her right near one of the blue dots in the lower-left, the intuitive strategy would predict 'not CKD', whereas the nearest neighbor classifier will predict 'CKD'.

There is a simple generalization of the nearest neighbor classifier that fixes this anomaly.  It is called the *k-nearest neighbor classifier*.  To predict Alice's diagnosis, rather than looking at just the one neighbor closest to her, we can look at the 3 points that are closest to her, and use the diagnosis for each of those 3 points to predict Alice's diagnosis.  In particular, we'll use the majority value among those 3 diagnoses as our prediction for Alice's diagnosis.  Of course, there's nothing special about the number 3: we could use 4, or 5, or more.  (It's often convenient to pick an odd number, so that we don't have to deal with ties.)  In general, we pick a number $k$, and our predicted diagnosis for Alice is based on the $k$ patients in the training set who are closest to Alice.  Intuitively, these are the $k$ patients whose blood test results were most similar to Alice, so it seems reasonable to use their diagnoses to predict Alice's diagnosis.

The $k$-nearest neighbor classifier will now behave just like our intuitive strategy above.

