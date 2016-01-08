Chapter 1
=========

Introduction
============

Data are descriptions of the world around us, collected through observation and
stored on computers. Computers enable us to infer properties of the world from
these descriptions. Data science is the discipline of drawing conclusions from
data using computation. There are four core aspects of effective data analysis:
visualization, inference, prediction, and modeling. This text develops a
consistent approach to all four, introducing statistical ideas and fundamental
ideas in computer science concurrently. We focus on a minimal set of core
techniques, but demonstrate that they apply to a vast range of real-world
applications. A foundation in data science requires not only understanding
statistical and computational techniques, but also recognizing how they apply
to real scenarios.

For whatever aspect of the world we wish to study---whether it's the Earth's
weather, the world's markets, political polls, or the human mind---data we
collect typically offer an incomplete description of the subject at hand. The
central challenge of data science is to make reliable conclusions using this
partial information.

In this endeavor, we will combine two essential tools: computation and
randomization. For example, we may want to understand climate change trends
using temperature observations. Computers will allow us to use all available
information to draw conclusions. Rather than focusing only on the average
temperature of a region, we will consider the whole range of temperatures
together to construct a more nuanced analysis. Randomness will allow us to
consider the many different ways in which incomplete information might be
completed. Rather than assuming that temperatures vary in a particular way, we
will learn to use randomness as a way to imagine many possible scenarios that
are all consistent with the data we observe.

Applying this approach requires learning to program a computer, and so this
text interleaves a complete introduction to programming that assumes no prior
knowledge. Readers with programming experience will find that we cover several
topics in computation that do not appear in a typical introductory computer
science curriculum. Data science also requires careful reasoning about
quantities, but this text does not assume any background in mathematics or
statistics beyond basic algebra. You will find very few equations in this text.
Instead, techniques are described to readers in the same language in which they
are described to the computers that execute them---a programming language.

Computational Tools
-------------------

This text uses the Python 3 programming language, along with a standard set of
numerical and data visualization tools that are used widely in commercial
applications, scientific experiments, and open-source projects.
Python has recruited enthusiasts from many professions that use data to draw
conclusions. By learning the Python language, you will join a
million-person-strong community of software developers and data scientists.

**Getting Started.** The easiest and recommended way to start writing programs
in Python is to log into the companion site for this text,
[program.dsten.org](http://program.dsten.org). If you are enrolled in a course
offering that uses this text, you should have full access to the programming
environment hosted on that site. The first time you log in, you will find a
brief tutorial describing how to proceed.

You are not at all restricted to using this web-based programming environment.
A Python program can be executed by any computer, regardless of its
manufacturer or operating system, provided that support for the language is
installed. If you wish to install the version of Python and its accompanying
libraries that will match this text, we recommend the [Anaconda][download]
distribution that packages together the Python 3 language interpreter, IPython
libraries, and the Jupyter notebook environment.

   [download]: http://continuum.io/downloads#py34

This text includes a complete introduction to all of these computational tools.
You will learn to write programs, generate images from data, and work with
real-world data sets that are published online.

Statistical Techniques
----------------------

The discipline of statistics has long addressed the same fundamental challenge
as data science: how to draw conclusions about the world using incomplete
information. One of the most important contributions of statistics is a
consistent and precise vocabulary for describing the relationship between
observations and conclusions. This text continues in the same tradition,
focusing on a set of core inferential problems from statistics: testing
hypotheses, estimating confidence, and predicting unknown quantities.

Data science extends the field of statistics by taking full advantage of
computing, data visualization, and access to information. The combination of
fast computers and the Internet gives anyone the ability to access and analyze
vast datasets: millions of news articles, full encyclopedias, databases for
any domain, and massive repositories of music, photos, and video.

Applications to real data sets motivate the statistical techniques that we
describe throughout the text. Real data often do not follow regular patterns or
match standard equations. The interesting variation in real data can be lost by
focusing too much attention on simplistic summaries such as average values.
Computers enable a family of methods based on resampling that apply to a wide
range of different inference problems, take into account all available
information, and require few assumptions or conditions. Although these
techniques have often been reserved for graduate courses in statistics, their
flexibility and simplicity are a natural fit for data science applications.

Why Data Science?
=================

Most important decisions are made with only partial information and uncertain
outcomes. However, the degree of uncertainty for many decisions can be reduced
sharply by public access to large data sets and the computational tools
required to analyze them effectively. Data-driven decision making has already
transformed a tremendous breadth of industries, including finance, advertising,
manufacturing, and real estate. At the same time, a wide range of academic
disciplines are evolving rapidly to incorporate large-scale data analysis into
their theory and practice.

Studying data science enables individuals to bring these techniques to bear on
their work, their scientific endeavors, and their personal decisions. Critical
thinking has long been a hallmark of a rigorous education, but critiques are
often most effective when supported by data. A critical analysis of any aspect
of the world, may it be business or social science, involves inductive
reasoning --- conclusions can rarely been proven outright, only supported by
the available evidence. Data science provides the means to make precise,
reliable, and quantitative arguments about any set of observations. With
unprecedented access to information and computing, critical thinking about
any aspect of the world that can be measured would be incomplete without
the inferential techniques that are core to data science.

The world has too many unanswered questions and difficult challenges to leave
this critical reasoning to only a few specialists. However, all educated adults
can build the capacity to reason about data. The tools, techniques, and data
sets are all readily available; this text aims to make them accessible to
everyone.

Example: Plotting the Classics
------------------------------

{% include "../notebooks-html/Books.html" %}

Causality and Experiments
======================

*"These problems are, and will probably ever remain, among the inscrutable
secrets of nature. They belong to a class of questions radically inaccessible to
the human intelligence."* —The Times of London, September 1849, on how cholera
is contracted and spread

Does the death penalty have a deterrent effect? Is chocolate good for you? What
causes breast cancer?

All of these questions attempt to assign a cause to an effect. A careful
examination of data can help shed light on questions like these. In this section
you will learn some of the fundamental concepts involved in establishing
causality.

Observation is a key to good science. An *observational study* is one in which
scientists make conclusions based on data that they have observed but had no
hand in generating. In data science, many such studies involve observations on a
group of individuals, a factor of interest called a *treatment*, and an
*outcome* measured on each individual.

It is easiest to think of the individuals as people. In a study of whether
chocolate is good for the health, the individuals would indeed be people, the
treatment would be eating chocolate, and the outcome might be a measure of blood
pressure. But individuals in observational studies need not be people. In a
study of whether the death penalty has a deterrent effect, the individuals could
be the 50 states of the union. A state law allowing the death penalty would be
the treatment, and an outcome could be the state’s murder rate.

The fundamental question is whether the treatment has an effect on the outcome.
Any relation between the treatment and the outcome is called an *association*.
If the treatment causes the outcome to occur, then the association is *causal*.
*Causality* is at the heart of all three questions posed at the start of this
section. For example, one of the questions was whether chocolate directly causes
improvements in health, not just whether there there is a relation between
chocolate and health.

The establishment of causality often takes place in two stages. First, an
association is observed. Next, a more careful analysis leads to a decision about
causality.

Observation and Visualization: John Snow and the Broad Street Pump
------------------------------------------------------------------

One of the earliest examples of astute observation eventually leading to the
establishment of causality dates back more than 150 years. To get your mind into
the right timeframe, try to imagine London in the 1850’s. It was the world’s
wealthiest city but many of its people were desperately poor. Charles Dickens,
then at the height of his fame, was writing about their plight. Disease was rife
in the poorer parts of the city, and cholera was among the most feared. It was
not yet known that germs cause disease; the leading theory was that “miasmas”
were the main culprit. Miasmas manifested themselves as bad smells, and were
thought to be invisible poisonous particles arising out of decaying matter.
Parts of London did smell very bad, especially in hot weather. To protect
themselves against infection, those who could afford to held sweet-smelling
things to their noses.

For several years, a doctor by the name of John Snow had been following the
devastating waves of cholera that hit England from time to time. The disease
arrived suddenly and was almost immediately deadly: people died within a day or
two of contracting it, hundreds could die in a week, and the total death toll in
a single wave could reach tens of thousands. Snow was skeptical of the miasma
theory. He had noticed that while entire households were wiped out by cholera,
the people in neighboring houses sometimes remained completely unaffected. As
they were breathing the same air—and miasmas—as their neighbors, there was no
compelling association between bad smells and the incidence of cholera.

Snow had also noticed that the onset of the disease almost always involved
vomiting and diarrhea. He therefore believed that that infection was carried by
something people ate or drank, not by the air that they breathed. His prime
suspect was water contaminated by sewage.

At the end of August 1854, cholera struck in the overcrowded Soho district of
London. As the deaths mounted, Snow recorded them diligently, using a method
that went on to become standard in the study of how diseases spread: *he drew a
map*. On a street map of the district, he recorded the location of each death.

Here is Snow’s original map. Each black bar represents one death. The black
discs mark the locations of water pumps. The map displays a striking
revelation–the deaths are roughly clustered around the Broad Street pump.
![Snow’s Cholera Map](../images/snow_map.jpg)

Snow studied his map carefully and investigated the apparent anomalies. All of
them implicated the Broad Street pump. For example:
- There were deaths in houses that were nearer the Rupert Street pump than the
  Broad Street pump. Though the Rupert Street pump was closer as the crow flies,
  it was less convenient to get to because of dead ends and the layout of the
  streets. The residents in those houses used the Broad Street pump instead.
- There were no deaths in two blocks just east of the pump. That was the
  location of the Lion Brewery, where the workers drank what they brewed. If
  they wanted water, the brewery had its own well.
- There were scattered deaths in houses several blocks away from the Broad
  Street pump. Those were children who drank from the Broad Street pump on their
  way to school. The pump’s water was known to be cool and refreshing.

The final piece of evidence in support of Snow’s theory was provided by two
isolated deaths in the leafy and genteel Hampstead area, quite far from Soho.
Snow was puzzled by these until he learned that the deceased were Mrs. Susannah
Eley, who had once lived in Broad Street, and her niece. Mrs. Eley had water
from the Broad Street pump delivered to her in Hampstead every day. She liked
its taste.

Later it was discovered that a cesspit that was just a few feet away from the
well of the Broad Street pump had been leaking into the well. Thus the pump’s
water was contaminated by sewage from the houses of cholera victims.

Snow used his map to convince local authorities to remove the handle of the
Broad Street pump. Though the cholera epidemic was already on the wane when he
did so, it is possible that the disabling of the pump prevented many deaths from
future waves of the disease.

The removal of the Broad Street pump handle has become the stuff of legend. At
the Centers for Disease Control (CDC) in Atlanta, when scientists look for
simple answers to questions about epidemics, they sometimes ask each other,
“Where is the handle to this pump?”

Snow’s map is one of the earliest and most powerful uses of data visualization.
Disease maps of various kinds are now a standard tool for tracking epidemics.

**Towards Causality**

Though the map gave Snow a strong indication that  the cleanliness of the water
supply was the key to controlling cholera, he was still a long way from a
convincing scientific argument that contaminated water was causing the spread of
the disease. To make a more compelling case, he had to use the method of
*comparison*.

Scientists use comparison to identify an association between a treatment and an
outcome. They compare the outcomes of a group of individuals who got the
treatment (the *treatment group*) to the outcomes of a group who did not (the
*control group*). For example, researchers today might compare the average
murder rate in states that have the death penalty with the average murder rate
in states that don’t.

If the results are different, that is evidence for an association. To determine
causation, however, even more care is needed.


Snow’s “Grand Experiment”
-------------------------

Encouraged by what he had learned in Soho, Snow completed a more thorough
analysis of cholera deaths. For some time, he had been gathering data on cholera
deaths in an area of London that was served by two water companies. The Lambeth
water company drew its water upriver from where sewage was discharged into the
River Thames. Its water was relatively clean. But the Southwark and Vauxhall
(S&V) company drew its water below the sewage discharge, and thus its supply was
contaminated.

Snow noticed that there was no systematic difference between the people who were
supplied by S&V and those supplied by Lambeth. “Each company supplies both rich
and poor, both large houses and small; there is no difference either in the
condition or occupation of the persons receiving the water of the different
Companies … there is no difference whatever in the houses or the people
receiving the supply of the two Water Companies, or in any of the physical
conditions with which they are surrounded …”

The only difference was in the water supply, “one group being supplied with
water containing the sewage of London, and amongst it, whatever might have come
from the cholera patients, the other group having water quite free from
impurity.”

Confident that he would be able to arrive at a clear conclusion, Snow summarized
his data in the table below.

| Supply Area    | Number of houses | cholera deaths | deaths per 10,000 houses |
|----------------|------------------|----------------|--------------------------|
| S&V            | 40,046           | 1,263          | 315                      |
| Lambeth        | 26,107           | 98             | 37                       |
| Rest of London | 256,423          | 1,422          | 59                       |


The numbers pointed accusingly at S&V. The death rate from cholera in the S&V
houses was almost ten times the rate in the houses supplied by Lambeth.


Establishing Causality
----------------------

In the language developed earlier in the section, you can think of the people in
the S&V houses as the treatment group, and those in the Lambeth houses at the
control group. A crucial element in Snow’s analysis was that the people in the
two groups were comparable to each other, apart from the treatment.

In order to establish whether it was the water supply that was causing cholera,
Snow had to compare two groups that were similar to each other in all but one
aspect–their water supply. Only then would he be able to ascribe the differences
in their outcomes to the water supply. If the two groups had been different in
some other way as well, it would have been difficult to point the finger at the
water supply as the source of the disease.  For example, if the treatment group
consisted of factory workers and the control group did not, then differences
between the outcomes in the two groups could have been due to the water supply,
or to factory work, or both, or to any other characteristic that made the groups
different from each other. The final picture would have been much more fuzzy.

Snow’s brilliance lay in identifying two groups that would make his comparison
clear. He had set out to establish a causal relation between contaminated water
and cholera infection, and to a great extent he succeeded, even though the
miasmatists ignored and even ridiculed him. Of course, Snow did not understand
the detailed mechanism by which humans contract cholera. That discovery was made
in 1883, when the German scientist Robert Koch isolated the *Vibrio cholerae*,
the bacterium that enters the human small intestine and causes cholera.

In fact the *Vibrio cholerae* had been identified in 1854 by Filippo Pacini in
Italy, just about when Snow was analyzing his data in London. Because of the
dominance of the miasmatists in Italy, Pacini’s discovery languished unknown.
But by the end of the 1800’s, the miasma brigade was in retreat. Subsequent
history has vindicated Pacini and John Snow. Snow’s methods led to the
development of the field of *epidemiology*, which is the study of the spread of
diseases.

**Confounding**

Let us now return to more modern times, armed with an important lesson that we
have learned along the way:

In an observational study, if the treatment and control groups differ in ways
other than the treatment, it is difficult to make conclusions about causality.

An underlying difference between the two groups (other than the treatment) is
called a *confounding factor*, because it might confound you (that is, mess you
up) when you try to reach a conclusion.

**Example: Coffee and lung cancer.** Studies in the 1960’s showed that coffee
drinkers had higher rates of lung cancer than those who did not drink coffee.
Because of this, some people identified coffee as a cause of lung cancer. But
coffee does not cause lung cancer. The analysis contained a confounding factor –
smoking. In those days, coffee drinkers were also likely to have been smokers,
and smoking does cause lung cancer. Coffee drinking was associated with lung
cancer, but it did not cause the disease.

Confounding factors are common in observational studies. Good studies take great
care to reduce confounding.


Randomization
--------------

An excellent way to avoid confounding is to assign individuals to the treatment
and control groups *at random*, and then administer the treatment to those who
were assigned to the treatment group. Randomization keeps the two groups similar
apart from the treatment.

If you are able to randomize individuals into the treatment and control groups,
you are running a *randomized controlled experiment*, also known as a
*randomized controlled trial* (RCT). Sometimes, people’s responses in an
experiment are influenced by their knowing which group they are in. So you might
want to run a *blind* experiment in which individuals do not know whether they
are in the treatment group or the control group. To make this work, you will
have to give the control group a *placebo*, which is something that looks
exactly like the treatment but in fact has no effect.

Randomized controlled experiments have long been a gold standard in the medical
field, for example in establishing whether a new drug works. They are also
becoming more commonly used in other fields such as economics.

**Example: Welfare subsidies in Mexico.** In Mexican villages in the 1990’s,
children in poor families were often not enrolled in school. One of the reasons
was that the older children could go to work and thus help support the family.
Santiago Levy , a minister in Mexican Ministry of Finance, set out to
investigate whether welfare programs could be used to increase school enrollment
and improve health conditions. He conducted an RCT on a set of villages,
selecting some of them at random to receive a new welfare program called
PROGRESA. The program gave money to poor families if their children went to
school regularly and the family used preventive health care. More money was
given if the children were in secondary school than in primary school, to
compensate for the children’s lost wages, and more money was given for girls
attending school than for boys. The remaining villages did not get this
treatment, and formed the control group. Because of the randomization, there
were no confounding factors and it was possible to establish that PROGRESA
increased school enrollment. For boys, the enrollment increased from 73% in the
control group to 77% in the PROGRESA group. For girls, the increase was even
greater, from 67% in the control group to almost 75% in the PROGRESA group. Due
to the success of this experiment, the Mexican government supported the program
under the new name OPORTUNIDADES, as an investment in a healthy and well
educated population.


In some situations it might not be possible to carry out a randomized controlled
experiment, even when the aim is to investigate causality. For example, suppose
you want to study the effects of alcohol consumption during pregnancy, and you
randomly assign some pregnant women to your “alcohol” group. You should not
expect cooperation from them if you present them with a drink. In such
situations you will almost invariably be conducting an observational study, not
an experiment. Be alert for confounding factors.


**Endnote**

In the terminology of that we have developed, John Snow conducted an
observational study, not a randomized experiment. But he called his study a
“grand experiment” because, as he wrote, “No fewer than three hundred thousand
people … were divided into two groups without their choice, and in most cases,
without their knowledge …”

Studies such as Snow’s are sometimes called “natural experiments.” However, true
randomization does not simply mean that the treatment and control groups are
selected “without their choice.”

The method of randomization can be as simple as tossing a coin. It may also be
quite a bit more complex. But every method of randomization consists of a
sequence of carefully defined steps that allow chances to be specified
mathematically. This has two important consequences.

1. It allows us to account–mathematically–for the possibility that randomization
   produces treatment and control groups that are quite different from each
   other.

2. It allows us to make precise mathematical statements about differences
   between the treatment and control groups. This in turn helps us make
   justifiable conclusions about whether the treatment has any effect.


In this course, you will learn how to conduct and analyze your own randomized
experiments. That will involve more detail than has been presented in this
section. For now, just focus on the main idea: to try to establish causality,
run a randomized controlled experiment if possible. If you are conducting an
observational study, you might be able to establish association but not
causation. Be extremely careful about confounding factors before making
conclusions about causality based on an observational study.


**Terminology**

* observational study
* treatment
* outcome
* association
* causal association
* causality
* comparison
* treatment group
* control group
* epidemiology
* confounding
* randomization
* randomized controlled experiment
* randomized controlled trial (RCT)
* blind
* placebo



**Fun facts**

1. John Snow is sometimes called the father of epidemiology, but he was an
   anesthesiologist by profession. One of his patients was Queen Victoria, who
   was an early recipient of anesthetics during childbirth.

2. Florence Nightingale, the originator of modern nursing practices and famous
   for her work in the Crimean War, was a die-hard miasmatist. She had no time
   for theories about contagion and germs, and was not one for mincing her
   words. “There is no end to the absurdities connected with this doctrine,” she
   said. “Suffice it to say that in the ordinary sense of the word, there is no
   proof such as would be admitted in any scientific enquiry that there is any
   such thing as contagion.”

3. A later RCT established that the conditions on which PROGRESA insisted –
   children going to school, preventive health care – were not necessary to
   achieve increased enrollment. Just the financial boost of the welfare
   payments was sufficient.


**Good reads**

[*The Strange Case of the Broad Street Pump: John Snow and the Mystery of
Cholera*](http://www.ucpress.edu/book.php?isbn=9780520250499) by Sandra Hempel,
published by our own University of California Press, reads like a whodunit. It
was one of the main sources for this section's account of John Snow and his
work. A word of warning: some of the contents of the book are stomach-churning.

[*Poor Economics*](http://www.pooreconomics.com), the best seller by Abhijit V.
Banerjee and Esther Duflo of MIT, is an accessible and lively account of ways to
fight global poverty. It includes numerous examples of RCTs, including the
PROGRESA example in this section.


Expressions
===========

{% include "../notebooks-html/Expressions.html" %}

Names
-----

{% include "../notebooks-html/Names.html" %}

Example: Growth Rates
---------------------

{% include "../notebooks-html/Growth.html" %}

Call Expressions
----------------

{% include "../notebooks-html/Calls.html" %}

Data Types
----------

{% include "../notebooks-html/Types.html" %}

Comparisons
-----------

{% include "../notebooks-html/Comparison.html" %}

Collections
-----------

{% include "../notebooks-html/Collections.html" %}

Arrays
------

{% include "../notebooks-html/Arrays.html" %}

Tables
======

{% include "../notebooks-html/Tables.html" %}

