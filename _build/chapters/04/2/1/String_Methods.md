---
redirect_from:
  - "/chapters/04/2/1/string-methods"
interact_link: content/chapters/04/2/1/String_Methods.ipynb
kernel_name: python3
has_widgets: false
title: 'String Methods'
prev_page:
  url: /chapters/04/2/Strings
  title: 'Strings'
next_page:
  url: /chapters/04/3/Comparison
  title: 'Comparisons'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# String Methods

From an existing string, related strings can be constructed using string methods, which are functions that operate on strings. These methods are called by placing a dot after the string, then calling the function.

For example, the following method generates an uppercased version of a string.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"loud".upper()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'LOUD'
```


</div>
</div>
</div>



Perhaps the most important method is `replace`, which replaces all instances of a substring within the string. The `replace` method takes two arguments, the text to be replaced and its replacement.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
'hitchhiker'.replace('hi', 'ma')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'matchmaker'
```


</div>
</div>
</div>



String methods can also be invoked using variable names, as long as those names are bound to strings. So, for instance, the following two-step process generates the word "degrade" starting from "train" by first creating "ingrain" and then applying a second replacement.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
s = "train"
t = s.replace('t', 'ing')
u = t.replace('in', 'de')
u

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'degrade'
```


</div>
</div>
</div>



Note that the line `t = s.replace('t', 'ing')` doesn't change the string `s`, which is still "train".  The method call `s.replace('t', 'ing')` just has a value, which is the string "ingrain".



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
s

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'train'
```


</div>
</div>
</div>



This is the first time we've seen methods, but methods are not unique to strings.  As we will see shortly, other types of objects can have them.

