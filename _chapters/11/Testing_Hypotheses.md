---
interact_link: notebooks/11/Testing_Hypotheses.ipynb
title: '11. Testing Hypotheses'
previouschapter:
  url: chapters/10/3/Empirical_Distribution_of_a_Statistic
  title: '10.3 Empirical Distibution of a Statistic'
nextchapter:
  url: chapters/11/1/Assessing_Models
  title: '11.1 Assessing Models'
---

### Testing Hypotheses ###

Data scientists are often faced with yes-no questions about the world. You have seen some examples of such questions in this course:

- Is chocolate good for you?
- Did water from the Broad Street pump cause cholera?
- Have the demographics in California changed over the past decade?

Whether we answer questions like these depends on the data we have. Census data about California can settle questions about demographics with hardly any uncertainty about the answer. We know that Broad Street pump water was contaminated by waste from cholera victims, so we can make a pretty good guess about whether it caused cholera. 

Whether chocolate or any other treatment is good for you will almost certainly have to be decided by medical experts, but an initial step consists of using data science to analyze data from studies and randomized experiments. 

In this chapter, we will try to answer such yes-no questions, basing our conclusions on random samples and empirical distributions. 
