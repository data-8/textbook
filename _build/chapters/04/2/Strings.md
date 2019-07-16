---
redirect_from:
  - "/chapters/04/2/strings"
interact_link: content/chapters/04/2/Strings.ipynb
kernel_name: python3
has_widgets: false
title: 'Strings'
prev_page:
  url: /chapters/04/1/Numbers
  title: 'Numbers'
next_page:
  url: /chapters/04/2/1/String_Methods
  title: 'String Methods'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Strings

Much of the world's data is text, and a piece of text represented in a computer is called a *string*. A string can represent a word, a sentence, or even the contents of every book in a library. Since text can include numbers (like this: 5) or truth values (True), a string can also describe those things.

The meaning of an expression depends both upon its structure and the types of values that are being combined. So, for instance, adding two strings together produces another string. This expression is still an addition expression, but it is combining a different type of value.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"data" + "science"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'datascience'
```


</div>
</div>
</div>



Addition is completely literal; it combines these two strings together without regard for their contents. It doesn't add a space because these are different words; that's up to the programmer (you) to specify.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"data" + " " + "science"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'data science'
```


</div>
</div>
</div>



Single and double quotes can both be used to create strings: `'hi'` and `"hi"` are identical expressions. Double quotes are often preferred because they allow you to include apostrophes inside of strings.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"This won't work with a single-quoted string!"

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
"This won't work with a single-quoted string!"
```


</div>
</div>
</div>



Why not? Try it out.



The `str` function returns a string representation of any value. Using this function, strings can be constructed that have embedded values.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"That's " + str(1 + 1) + ' ' + str(True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
"That's 2 True"
```


</div>
</div>
</div>

