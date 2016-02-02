Functions
=========

We are building up a useful inventory of techniques for identifying patterns
and themes in a data set. Sorting and filtering rows of a table can focus our
attention. Bar charts and histograms can summarize data visually to convey
broad numerical patterns. The next approach to analysis we will consider
involves grouping rows of a table by arbitrary criteria. To do so, we will
explore two core features of the Python programming language: function
definition and conditional statements.

We have used functions extensively already in this text, but never defined a
function of our own. The purpose of defining a function is to give a name to a
computational process that may be applied multiple times. Although there are
many situations in computing that require repeating a computational process
many times, the most natural one in our setting is to perform the same process
on each row of a table.

A function is defined in Python using a `def` statement, which is a multi-line
statement that begins with a *header* line giving the name of the function and
names for the arguments of the function. The rest of the `def` statement,
called the *body*, must be indented below the header.

A function expresses a relationship between its inputs (called *arguments*) and
its outputs (called *return values*). The number of arguments required to call
a function is the number of names that appear within parentheses in the `def`
statement header. The values that are returned depend on the body. Whenever a
function is called, its body is executed. Whenever a `return` statement within
the body is executed, the call to the function completes and the value of the
expression directly following `return` is returned.

{% include "../notebooks-html/Functions.html" %}
