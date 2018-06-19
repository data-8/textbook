---
interact_link: notebooks/14/Why_the_Mean_Matters.ipynb
title: '14. Why the Mean Matters'
permalink: 'chapters/14/why-the-mean-matters'
previouschapter:
  url: chapters/13/4/using-confidence-intervals
  title: '13.4 Using Confidence Intervals'
nextchapter:
  url: chapters/14/1/properties-of-the-mean
  title: '14.1 Properties of the Mean'
---

### Why the Mean Matters ###
In this course we have studied several different statistics, including total variation distance, the maximum, the median, and also the mean. Under clear assumptions about randomness, we have drawn empirical distributions of all of these statistics. Some, like the maximum and the total variation distance, have distributions that are clearly skewed in one direction or the other. But the empirical distribution of the sample mean has almost always turned out close to bell-shaped, regardless of the population being studied.

If a property of random samples is true *regardless of the population,* it becomes a powerful tool for inference because we rarely know much about the data in the entire population. The distribution of the mean of a large random sample falls into this category of properties. That is why random sample means are extensively used in data science.

In this chapter, we will study means and what we can say about them with only minimal assumptions about the underlying populations. Question that we will address include:

- What exactly does the mean measure?
- How close to the mean are most of the data?
- How is the sample size related to the variability of the sample mean?
- Why do empirical distributions of random sample means come out bell shaped?
- How can we use sample means effectively for inference?
