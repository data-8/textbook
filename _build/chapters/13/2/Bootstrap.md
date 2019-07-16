---
redirect_from:
  - "/chapters/13/2/bootstrap"
interact_link: content/chapters/13/2/Bootstrap.ipynb
kernel_name: python3
has_widgets: false
title: 'The Bootstrap'
prev_page:
  url: /chapters/13/1/Percentiles
  title: 'Percentiles'
next_page:
  url: /chapters/13/3/Confidence_Intervals
  title: 'Confidence Intervals'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### The Bootstrap
A data scientist is using the data in a random sample to estimate an unknown parameter. She uses the sample to calculate the value of a statistic that she will use as her estimate. 

Once she has calculated the observed value of her statistic, she could just present it as her estimate and go on her merry way. But she's a data scientist. She knows that her random sample is just one of numerous possible random samples, and thus her estimate is just one of numerous plausible estimates. 

By how much could those estimates vary? To answer this, it appears as though she needs to draw another sample from the population, and compute a new estimate based on the new sample. But she doesn't have the resources to go back to the population and draw another sample.

It looks as though the data scientist is stuck.

Fortunately, a brilliant idea called *the bootstrap* can help her out. Since it is not feasible to generate new samples from the population, the bootstrap generates new random samples by a method called *resampling*: the new samples are drawn at random *from the original sample*.



In this section, we will see how and why the bootstrap works. In the rest of the chapter, we will use the bootstrap for inference.





### Employee Compensation in the City of San Francisco
[SF OpenData](https://data.sfgov.org) is a website where the City and County of San Francisco make some of their data publicly available. One of the data sets contains compensation data for employees of the City. These include medical professionals at City-run hospitals, police officers, fire fighters, transportation workers, elected officials, and all other employees of the City. 

Compensation data for the calendar year 2015 are in the table `sf2015`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015 = Table.read_table(path_data + 'san_francisco_2015.csv')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>WTR            </td> <td>PUC Water Department                  </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21   </td> <td>2400           </td> <td>Lab, Pharmacy & Med Techs    </td> <td>2481    </td> <td>Water Qualitytech I/II        </td> <td>21538              </td> <td>82146   </td> <td>0       </td> <td>0             </td> <td>82146       </td> <td>16942.2   </td> <td>12340.9      </td> <td>6337.73       </td> <td>35620.8       </td> <td>117767            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>DPW            </td> <td>General Services Agency - Public Works</td> <td>12        </td> <td>Carpet, Linoleum and Soft Tile Workers, Local 12  </td> <td>7300           </td> <td>Journeyman Trade             </td> <td>7393    </td> <td>Soft Floor Coverer            </td> <td>5459               </td> <td>32165.8 </td> <td>973.19  </td> <td>848.96        </td> <td>33987.9     </td> <td>0         </td> <td>4587.51      </td> <td>2634.42       </td> <td>7221.93       </td> <td>41209.8           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021                  </td> <td>1600           </td> <td>Payroll, Billing & Accounting</td> <td>1636    </td> <td>Health Care Billing Clerk 2   </td> <td>41541              </td> <td>71311   </td> <td>5757.98 </td> <td>0             </td> <td>77069       </td> <td>14697.6   </td> <td>12424.5      </td> <td>6370.06       </td> <td>33492.2       </td> <td>110561            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous   </td> <td>0900           </td> <td>Management                   </td> <td>2620    </td> <td>Food Service Mgr Administrator</td> <td>26718              </td> <td>28430.2 </td> <td>0       </td> <td>763.07        </td> <td>29193.3     </td> <td>0         </td> <td>4223.14      </td> <td>5208.51       </td> <td>9431.65       </td> <td>38625             </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>MTA            </td> <td>Municipal Transportation Agency       </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021                  </td> <td>8200           </td> <td>Protection & Apprehension    </td> <td>8201    </td> <td>School Crossing Guard         </td> <td>45810              </td> <td>7948.75 </td> <td>0       </td> <td>0             </td> <td>7948.75     </td> <td>0         </td> <td>2873.17      </td> <td>616.24        </td> <td>3489.41       </td> <td>11438.2           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                       </td> <td>POL            </td> <td>Police                                </td> <td>911       </td> <td>Police Officers' Association                      </td> <td>Q000           </td> <td>Police Services              </td> <td>Q002    </td> <td>Police Officer                </td> <td>32906              </td> <td>2235    </td> <td>0       </td> <td>0             </td> <td>2235        </td> <td>490.36    </td> <td>286.72       </td> <td>176.57        </td> <td>953.65        </td> <td>3188.65           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>791       </td> <td>SEIU - Staff and Per Diem Nurses, Local 1021      </td> <td>2300           </td> <td>Nursing                      </td> <td>2328    </td> <td>Nurse Practitioner            </td> <td>7506               </td> <td>187247  </td> <td>0       </td> <td>11704.1       </td> <td>198951      </td> <td>37683.7   </td> <td>12424.5      </td> <td>11221.7       </td> <td>61329.9       </td> <td>260281            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>MTA            </td> <td>Municipal Transportation Agency       </td> <td>253       </td> <td>Transport Workers - Transit Operators, Local 250-A</td> <td>9100           </td> <td>Street Transit               </td> <td>9163    </td> <td>Transit Operator              </td> <td>36773              </td> <td>66988.5 </td> <td>3512.88 </td> <td>2770.39       </td> <td>73271.8     </td> <td>19127.2   </td> <td>13203        </td> <td>5455.1        </td> <td>37785.3       </td> <td>111057            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance        </td> <td>CAT            </td> <td>City Attorney                         </td> <td>311       </td> <td>Municipal Attorneys' Association                  </td> <td>8100           </td> <td>Legal & Court                </td> <td>8177    </td> <td>Attorney (Civil/Criminal)     </td> <td>12963              </td> <td>135190  </td> <td>0       </td> <td>1562.5        </td> <td>136752      </td> <td>27501.8   </td> <td>12424.5      </td> <td>10103         </td> <td>50029.3       </td> <td>186781            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>3                      </td> <td>Human Welfare & Neighborhood Development</td> <td>DSS            </td> <td>Human Services                        </td> <td>535       </td> <td>SEIU - Human Services, Local 1021                 </td> <td>9700           </td> <td>Community Development        </td> <td>9703    </td> <td>Emp & Training Spec 2         </td> <td>35179              </td> <td>70474.8 </td> <td>147.28  </td> <td>1647.24       </td> <td>72269.3     </td> <td>14650.3   </td> <td>10696.9      </td> <td>5993.11       </td> <td>31340.3       </td> <td>103610            </td>
        </tr>
    </tbody>
</table>
<p>... (42979 rows omitted)</p>
</div>


</div>
</div>
</div>



There is one row for each of 42,979 employees. There are numerous columns containing information about City departmental affiliation and details of the different parts of the employee's compensation package. Here is the row correspoding to the late Edward Lee, the Mayor at that time.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015.where('Job', are.equal_to('Mayor'))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance</td> <td>MYR            </td> <td>Mayor     </td> <td>556       </td> <td>Elected Officials</td> <td>1100           </td> <td>Administrative & Mgmt (Unrep)</td> <td>1190    </td> <td>Mayor</td> <td>22433              </td> <td>288964  </td> <td>0       </td> <td>0             </td> <td>288964      </td> <td>58117     </td> <td>12424.5      </td> <td>20293         </td> <td>90834.5       </td> <td>379798            </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



We are going to study the final column, `Total Compensation`. That's the employee's salary plus the City's contribution towards his/her retirement and benefit plans.

Financial packages in a calendar year can sometimes be hard to understand as they depend on the date of hire, whether the employee is changing jobs within the City, and so on. For example, the lowest values in the `Total Compensation` column look a little strange.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015.sort('Total Compensation')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                      </td> <td>FIR            </td> <td>Fire Department                   </td> <td>798       </td> <td>Firefighters - Miscellaneous, Local 798        </td> <td>H000           </td> <td>Fire Services           </td> <td>H002    </td> <td>Firefighter                  </td> <td>43833              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-423.76       </td> <td>-423.76       </td> <td>-423.76           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                       </td> <td>DPH            </td> <td>Public Health                     </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021               </td> <td>9900           </td> <td>Public Service Aide     </td> <td>9924    </td> <td>PS Aide Health Services      </td> <td>27871              </td> <td>-292.4  </td> <td>0       </td> <td>0             </td> <td>-292.4      </td> <td>0         </td> <td>-95.58       </td> <td>-22.63        </td> <td>-118.21       </td> <td>-410.61           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                      </td> <td>JUV            </td> <td>Juvenile Probation                </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021               </td> <td>8300           </td> <td>Correction & Detention  </td> <td>8320    </td> <td>Counselor, Juvenile Hall     </td> <td>10517              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-159.12       </td> <td>-159.12       </td> <td>-159.12           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance       </td> <td>CPC            </td> <td>City Planning                     </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21</td> <td>1000           </td> <td>Information Systems     </td> <td>1053    </td> <td>IS Business Analyst-Senior   </td> <td>18961              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-26.53        </td> <td>-26.53        </td> <td>-26.53            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance       </td> <td>CPC            </td> <td>City Planning                     </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21</td> <td>5200           </td> <td>Professional Engineering</td> <td>5277    </td> <td>Planner 1                    </td> <td>19387              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-9.51         </td> <td>-9.51         </td> <td>-9.51             </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce</td> <td>PUC            </td> <td>PUC Public Utilities Commission   </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21</td> <td>1000           </td> <td>Information Systems     </td> <td>1044    </td> <td>IS Engineer-Principal        </td> <td>28988              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-3.1          </td> <td>-3.1          </td> <td>-3.1              </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                      </td> <td>JUV            </td> <td>Juvenile Probation                </td> <td>39        </td> <td>Stationary Engineers, Local 39                 </td> <td>7300           </td> <td>Journeyman Trade        </td> <td>7335    </td> <td>Senior Stationary Engineer   </td> <td>19125              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-0.01         </td> <td>-0.01         </td> <td>-0.01             </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                      </td> <td>ECD            </td> <td>Department of Emergency Management</td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous</td> <td>0900           </td> <td>Management              </td> <td>0922    </td> <td>Manager I                    </td> <td>30025              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>0             </td> <td>0             </td> <td>0                 </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>7                      </td> <td>General City Responsibilities          </td> <td>UNA            </td> <td>General Fund Unallocated          </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021               </td> <td>3200           </td> <td>Recreation              </td> <td>3280    </td> <td>Assistant Recreation Director</td> <td>49784              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>1.27          </td> <td>1.27          </td> <td>1.27              </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                       </td> <td>DPH            </td> <td>Public Health                     </td> <td>250       </td> <td>SEIU - Health Workers, Local 1021              </td> <td>2600           </td> <td>Dietary & Food          </td> <td>2654    </td> <td>Cook                         </td> <td>26768              </td> <td>0       </td> <td>0       </td> <td>2.21          </td> <td>2.21        </td> <td>0         </td> <td>0            </td> <td>0.17          </td> <td>0.17          </td> <td>2.38              </td>
        </tr>
    </tbody>
</table>
<p>... (42979 rows omitted)</p>
</div>


</div>
</div>
</div>



For clarity of comparison, we will focus our attention on those who had at least the equivalent of a half-time job for the whole year. At a minimum wage of about \\$10 per hour, and 20 hours per week for 52 weeks, that's a salary of about \\$10,000.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015 = sf2015.where('Salaries', are.above(10000))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015.num_rows

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
36569
```


</div>
</div>
</div>



### Population and Parameter
Let this table of just over 36,500 rows be our population. Here is a histogram of the total compensations.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf_bins = np.arange(0, 700000, 25000)
sf2015.select('Total Compensation').hist(bins=sf_bins)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_14_0.png)

</div>
</div>
</div>



While most of the values are below \\$300,000, a few are quite a bit higher. For example, the total compensation of the Chief Investment Officer was almost \\$650,000. That is why the horizontal axis stretches to \\$700,000.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
sf2015.sort('Total Compensation', descending=True).show(2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance</td> <td>RET            </td> <td>Retirement System                   </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous</td> <td>1100           </td> <td>Administrative & Mgmt (Unrep)</td> <td>1119    </td> <td>Chief Investment Officer</td> <td>46881              </td> <td>507832  </td> <td>0       </td> <td>0             </td> <td>507832      </td> <td>105053    </td> <td>12424.5      </td> <td>23566.2       </td> <td>141044        </td> <td>648875            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance</td> <td>ADM            </td> <td>General Services Agency - City Admin</td> <td>164       </td> <td>Physicians and Dentists - Miscellaneous        </td> <td>2500           </td> <td>Med Therapy & Auxiliary      </td> <td>2598    </td> <td>Asst Med Examiner       </td> <td>1016               </td> <td>279311  </td> <td>3829.36 </td> <td>114434        </td> <td>397574      </td> <td>56211.6   </td> <td>12424.5      </td> <td>14299.1       </td> <td>82935.2       </td> <td>480509            </td>
        </tr>
    </tbody>
</table>
<p>... (36567 rows omitted)</p>
</div>

</div>
</div>
</div>



Now let the parameter be the median of the total compensations.

Since we have the luxury of having all of the data from the population, we can simply calculate the parameter:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pop_median = percentile(50, sf2015.column('Total Compensation'))
pop_median

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
110305.79
```


</div>
</div>
</div>



The median total compensation of all employees was just over \\$110,300. 

From a practical perspective, there is no reason for us to draw a sample to estimate this parameter since we simply know its value. But in this section we are going to pretend we don't know the value, and see how well we can estimate it based on a random sample. 

In later sections, we will come down to earth and work in situations where the parameter is unknown. For now, we are all-knowing.



### A Random Sample and an Estimate
Let us draw a sample of 500 employees at random without replacement, and let the median total compensation of the sampled employees serve as our estimate of the parameter.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
our_sample = sf2015.sample(500, with_replacement=False)
our_sample.select('Total Compensation').hist(bins=sf_bins)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_21_0.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
est_median = percentile(50, our_sample.column('Total Compensation'))
est_median

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
108405.39
```


</div>
</div>
</div>



The sample size is large. By the law of averages, the distribution of the sample resembles that of the population, and consequently the sample median is not very far from the population median (though of course it is not exactly the same).

So now we have one estimate of the parameter. But had the sample come out differently, the estimate would have had a different value. We would like to be able to quantify the amount by which the estimate could vary across samples. That measure of variability will help us measure how accurately we can estimate the parameter.

To see how different the estimate would be if the sample had come out differently, we could just draw another sample from the population, but that would be cheating. We are trying to mimic real life, in which we won't have all the population data at hand.

Somehow, we have to get another random sample without sampling from the population.



### The Bootstrap: Resampling from the Sample
What we do have is a large random sample from the population. As we know, a large random sample is likely to resemble the population from which it is drawn. This observation allows data scientists to *lift themselves up by their own bootstraps*: the sampling procedure can be replicated by *sampling from the sample*. 

Here are the steps of *the bootstrap method* for generating another random sample that resembles the population:

- **Treat the original sample as if it were the population.**
- **Draw from the sample**, at random **with** replacement, **the same number of times as the original sample size**. 

It is important to resample the same number of times as the original sample size. The reason is that the variability of an estimate depends on the size of the sample. Since our original sample consisted of 500 employees, our sample median was based on 500 values. To see how different the sample could have been, we have to compare it to the median of other samples of size 500.

If we drew 500 times at random *without* replacement from our sample of size 500, we would just get the same sample back. By drawing *with* replacement, we create the possibility for the new samples to be different from the original, because some employees might be drawn more than once and others not at all.

Why is this a good idea? By the law of averages, the distribution of the original sample is likely to resemble the population, and the distributions of all the "resamples" are likely to resemble the original sample. So the distributions of all the resamples are likely to resemble the population as well. 



<div markdown="1" class="cell code_cell">


<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_25_0.png)


</div>
</div>
</div>



### A Resampled Median
Recall that when the `sample` method is used without specifying a sample size, by default the sample size equals the number of rows of the table from which the sample is drawn. That's perfect for the bootstrap! Here is one new sample drawn from the original sample, and the corresponding sample median.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resample_1 = our_sample.sample()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resample_1.select('Total Compensation').hist(bins=sf_bins)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_28_0.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resampled_median_1 = percentile(50, resample_1.column('Total Compensation'))
resampled_median_1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
108366.9
```


</div>
</div>
</div>



By resampling, we have another estimate of the population median. By resampling again and again, we will get many such estimates, and hence an empirical distribution of the estimates.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resample_2 = our_sample.sample()
resampled_median_2 = percentile(50, resample_2.column('Total Compensation'))
resampled_median_2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
110391.29
```


</div>
</div>
</div>



### Bootstrap Empirical Distribution of the Sample Median
Let us define a function `bootstrap_median` that takes our original sample, the label of the column containing the variable, and the number of bootstrap samples we want to take, and returns an array of the corresponding resampled medians. 

Each time we resample and find the median, we *replicate* the bootstrap process. So the number of bootstrap samples will be called the number of replications.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bootstrap_median(original_sample, label, replications):
    """Returns an array of bootstrapped sample medians:
    original_sample: table containing the original sample
    label: label of column containing the variable
    replications: number of bootstrap samples
    """
    just_one_column = original_sample.select(label)
    medians = make_array()
    for i in np.arange(replications):
        bootstrap_sample = just_one_column.sample()
        resampled_median = percentile(50, bootstrap_sample.column(0))
        medians = np.append(medians, resampled_median)
        
    return medians

```
</div>

</div>



We now replicate the bootstrap process 5,000 times. The array `bstrap_medians` contains the medians of all 5,000 bootstrap samples. Notice that the code takes longer to run than our previous code. It has a lot of resampling to do!



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
bstrap_medians = bootstrap_median(our_sample, 'Total Compensation', 5000)

```
</div>

</div>



Here is the histogram of the 5000 medians. The red dot is the population parameter: it is the median of the entire population, which we happen to know but did not use in the bootstrap process.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
resampled_medians = Table().with_column('Bootstrap Sample Median', bstrap_medians)

#median_bins=np.arange(100000, 130000, 2500)
#resampled_medians.hist(bins = median_bins)
resampled_medians.hist()

plots.scatter(pop_median, 0, color='red', s=30);

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_37_0.png)

</div>
</div>
</div>



It is important to remember that the red dot is fixed: it is \\$110,305.79, the population median. The empirical histogram is the result of random draws, and will be situated randomly relative to the red dot. 

Remember also that the point of all these computations is to estimate the population median, which is the red dot. Our estimates are all the randomly generated sampled medians whose histogram you see above. We want those estimates to contain the parameter – it they don't, then they are off.



### Do the Estimates Capture the Parameter?

How often does the empirical histogram of the resampled medians sit firmly over the red dot, and not just brush the dot with its tails? To answer this, we must define "sit firmly". Let's take that to mean "the middle 95% of the resampled medians contains the red dot". 

Here are the two ends of the "middle 95%" interval of resampled medians:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
left = percentile(2.5, bstrap_medians)
left

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
102285.4
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
right = percentile(97.5, bstrap_medians)
right

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
115557.27
```


</div>
</div>
</div>



The population median of \\$110,305 is between these two numbers. The interval and the population median are shown on the histogram below.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#median_bins=np.arange(100000, 130000, 2500)
#resampled_medians.hist(bins = median_bins)
resampled_medians.hist()

plots.plot(make_array(left, right), make_array(0, 0), color='yellow', lw=3, zorder=1)
plots.scatter(pop_median, 0, color='red', s=30, zorder=2);

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_43_0.png)

</div>
</div>
</div>



The "middle 95%" interval of estimates captured the parameter in our example. But was that a fluke? 

To see how frequently the interval contains the parameter, we have to run the entire process over and over again. Specifically, we will repeat the following process 100 times:

- Draw an original sample of size 500 from the population.
- Carry out 5,000 replications of the bootstrap process and generate the "middle 95%" interval of resampled medians.

We will end up with 100 intervals, and count how many of them contain the population median.

**Spoiler alert:** The statistical theory of the bootstrap says that the number should be around 95. It may be in the low 90s or high 90s, but not much farther off 95 than that.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# THE BIG SIMULATION: This one takes several minutes.

# Generate 100 intervals, in the table intervals

left_ends = make_array()
right_ends = make_array()

total_comps = sf2015.select('Total Compensation')

for i in np.arange(100):
    first_sample = total_comps.sample(500, with_replacement=False)
    medians = bootstrap_median(first_sample, 'Total Compensation', 5000)
    left_ends = np.append(left_ends, percentile(2.5, medians))
    right_ends = np.append(right_ends, percentile(97.5, medians))

intervals = Table().with_columns(
    'Left', left_ends,
    'Right', right_ends
)    

```
</div>

</div>



For each of the 100 replications, we get one interval of estimates of the median.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
intervals

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Left</th> <th>Right</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>104850 </td> <td>116807</td>
        </tr>
        <tr>
            <td>106560 </td> <td>115858</td>
        </tr>
        <tr>
            <td>100109 </td> <td>115978</td>
        </tr>
        <tr>
            <td>109391 </td> <td>120038</td>
        </tr>
        <tr>
            <td>101859 </td> <td>115358</td>
        </tr>
        <tr>
            <td>98604.9</td> <td>110325</td>
        </tr>
        <tr>
            <td>101024 </td> <td>113680</td>
        </tr>
        <tr>
            <td>105506 </td> <td>116921</td>
        </tr>
        <tr>
            <td>103487 </td> <td>117259</td>
        </tr>
        <tr>
            <td>102741 </td> <td>112957</td>
        </tr>
    </tbody>
</table>
<p>... (90 rows omitted)</p>
</div>


</div>
</div>
</div>



The good intervals are those that contain the parameter we are trying to estimate. Typically the parameter is unknown, but in this section we happen to know what the parameter is.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pop_median

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
110305.79
```


</div>
</div>
</div>



How many of the 100 intervals contain the population median? That's the number of intervals where the left end is below the population median and the right end is above.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
intervals.where('Left', are.below(pop_median)).where('Right', are.above(pop_median)).num_rows

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
97
```


</div>
</div>
</div>



It takes a few minutes to construct all the intervals, but try it again if you have the patience. Most likely, about 95 of the 100 intervals will be good ones: they will contain the parameter.

It's hard to show you all the intervals on the horizontal axis as they have large overlaps – after all, they are all trying to estimate the same parameter. The graphic below shows each interval on the same axes by stacking them vertically. The vertical axis is simply the number of the replication from which the interval was generated.

The red line is where the parameter is. Good intervals cover the parameter; there are about 95 of these, typically. 

If an interval doesn't cover the parameter, it's a dud. The duds are the ones where you can see "daylight" around the red line. There are very few of them – about 5, typically – but they do happen. 

Any method based on sampling has the possibility of being off. The beauty of methods based on random sampling is that we can quantify how often they are likely to be off.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# HIDDEN 

replication_number = np.ndarray.astype(np.arange(1, 101), str)
intervals2 = Table(replication_number).with_rows(make_array(left_ends, right_ends))

plots.figure(figsize=(8,8))
for i in np.arange(100):
    ends = intervals2.column(i)
    plots.plot(ends, make_array(i+1, i+1), color='gold')
plots.plot(make_array(pop_median, pop_median), make_array(0, 100), color='red', lw=2)
plots.xlabel('Median (dollars)')
plots.ylabel('Replication')
plots.title('Population Median and Intervals of Estimates');

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../../images/chapters/13/2/Bootstrap_53_0.png)

</div>
</div>
</div>



To summarize what the simulation shows, suppose you are estimating the population median by the following process: 

- Draw a large random sample from the population.
- Bootstrap your random sample and get an estimate from the new random sample. 
- Repeat the above step thousands of times, and get thousands of estimates.
- Pick off the "middle 95%" interval of all the estimates.

That gives you one interval of estimates. Now if you repeat **the entire process** 100 times, ending up with 100 intervals, then about 95 of those 100 intervals will contain the population parameter.

In other words, this process of estimation captures the parameter about 95% of the time. 

You can replace 95% by a different value, as long as it's not 100. Suppose you replace 95% by 80% and keep the sample size fixed at 500. Then your intervals of estimates will be shorter than those we simulated here, because the "middle 80%" is a smaller range than the "middle 95%". Only about 80% of your intervals will contain the parameter.

