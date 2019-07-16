---
redirect_from:
  - "/chapters/18/updating-predictions"
interact_link: content/chapters/18/Updating_Predictions.ipynb
kernel_name: python3
has_widgets: false
title: 'Updating Predictions'
prev_page:
  url: /chapters/17/6/Multiple_Regression
  title: 'Multiple Regression'
next_page:
  url: /chapters/18/1/More_Likely_than_Not_Binary_Classifier
  title: 'A "More Likely Than Not" Binary Classifier'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">


</div>



### Updating Predictions
We know how to use training data to classify a point into one of two categories. Our classification is just a prediction of the class, based on the most common class among the training points that are nearest our new point. 

Suppose that we eventually find out the true class of our new point. Then we will know whether we got the classification right. Also, we will have a new point that we can add to our training set, because we know its class. This *updates* our training set. So, naturally, we will want to *update our classifier* based on the new training set.

This chapter looks at some simple scenarios where new data leads us to update our predictions. While the examples in the chapter are simple in terms of calculation, the method of updating can be generalized to work in complex settings and is one of the most powerful tools used for machine learning.

