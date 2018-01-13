"""
This script takes the SUMMARY.md file and adds section numbers to each part.

This script is idempotent, so running it multiple times on the same file
produces the same output as running it once.

To re-number sections, you should change the sequence of the sections in the
SUMMARY.md file and rerun the script without manually changing the sections
themselves.

For example, given this `SUMMARY.md` file:

```
# Table of Contents
* [Read Me](/README.md)
* [Introduction](/introduction/README.md)
  * [Motivation](/introduction/Motivation.md)
  * [Getting Started](/introduction/Getting_Started.md)
* [Tutorial](/tutorial/README.md)
  * [Simple Widgets](/tutorial/Simple_Widgets.md)
  * [Interact](/tutorial/Interact.md)
```

This script will generate:

```
# Table of Contents
* [1. Read Me](/README.md)
* [2. Introduction](/introduction/README.md)
  * [2.1 Motivation](/introduction/Motivation.md)
  * [2.2 Getting Started](/introduction/Getting_Started.md)
* [3. Tutorial](/tutorial/README.md)
  * [3.1 Simple Widgets](/tutorial/Simple_Widgets.md)
  * [3.2 Interact](/tutorial/Interact.md)
```

To re-number sections, we can just swap sections in the SUMMARY.md:

```
# Table of Contents
* [1. Read Me](/README.md)
* [3. Tutorial](/tutorial/README.md)
  * [3.1 Simple Widgets](/tutorial/Simple_Widgets.md)
  * [3.2 Interact](/tutorial/Interact.md)
* [2. Introduction](/introduction/README.md)
  * [2.1 Motivation](/introduction/Motivation.md)
  * [2.2 Getting Started](/introduction/Getting_Started.md)
```

And the script will produce:

```
# Table of Contents
* [1. Read Me](/README.md)
* [2. Tutorial](/tutorial/README.md)
  * [2.1 Simple Widgets](/tutorial/Simple_Widgets.md)
  * [2.2 Interact](/tutorial/Interact.md)
* [3. Introduction](/introduction/README.md)
  * [3.1 Motivation](/introduction/Motivation.md)
  * [3.2 Getting Started](/introduction/Getting_Started.md)
```
"""
import re
from codecs import open

# Name of the summary file
SUMMARY = 'SUMMARY.md'

# Indent amount in summary file
INDENT = '  '

# Regex to match any link
LINK_RE = re.compile(r'^\s*(\*|-|\+)')

# Regex to match previously labeled sections
LABEL_RE = re.compile(r'^[0-9\. ]+')


def main():
    lines = read_summary()
    lines_with_labels = add_section_labels(lines)
    write_summary(lines_with_labels)
    print('Successfully labeled SUMMARY.md')


def add_section_labels(lines, section=(0, 0, 0)):
    """
    Recursively adds the section label to each line. Removes previous labels
    before adding label to avoid duplication.
    """
    if len(lines) == 0:
        return lines

    line, *rest = lines
    part, subpart, subsubpart = section

    if not is_link(line):
        return [line, *add_section_labels(rest, section)]

    before, after = line.split('[')
    after = LABEL_RE.sub('', after)

    # We only increment the numbering for a section *after* the recursion since
    # we can't tell ahead of time whether the next link is nested.
    if is_subsubpart(line):
        labeled_line = ('{}[{}.{}.{} {}'
                        .format(before, part, subpart, subsubpart + 1, after))
        return [
            labeled_line,
            *add_section_labels(rest, (part, subpart, subsubpart + 1))
        ]
    elif is_subpart(line):
        labeled_line = ('{}[{}.{} {}'
                        .format(before, part, subpart + 1, after))
        return [
            labeled_line,
            *add_section_labels(rest, (part, subpart + 1, 0))
        ]
    else:
        labeled_line = ('{}[{}. {}'
                        .format(before, part + 1, after))
        return [
            labeled_line,
            *add_section_labels(rest, (part + 1, 0, 0))
        ]


def read_summary():
    with open(SUMMARY, encoding='utf8') as f:
        return f.readlines()


def write_summary(lines: [str]):
    with open(SUMMARY, mode='w', encoding='utf8') as f:
        f.writelines(lines)


def is_link(line: str):
    return LINK_RE.match(line)


def is_subpart(line: str):
    return line.startswith(INDENT)


def is_subsubpart(line: str):
    return line.startswith(INDENT * 2)


def test():
    test1 = [
        '# Table of Contents',
        '* [Read Me](/README.md)',
        '* [Introduction](/introduction/README.md)',
        '  * [Motivation](/introduction/Motivation.md)',
        '  * [Getting Started](/introduction/Getting_Started.md)',
        '* [Tutorial](/tutorial/README.md)',
        '  * [Simple Widgets](/tutorial/Simple_Widgets.md)',
        '  * [Interact](/tutorial/Interact.md)',
    ]

    res1 = [
        '# Table of Contents',
        '* [1. Read Me](/README.md)',
        '* [2. Introduction](/introduction/README.md)',
        '  * [2.1 Motivation](/introduction/Motivation.md)',
        '  * [2.2 Getting Started](/introduction/Getting_Started.md)',
        '* [3. Tutorial](/tutorial/README.md)',
        '  * [3.1 Simple Widgets](/tutorial/Simple_Widgets.md)',
        '  * [3.2 Interact](/tutorial/Interact.md)',
    ]

    test2 = [
        '# Table of Contents',
        '* [1. Read Me](/README.md)',
        '* [3. Tutorial](/tutorial/README.md)',
        '  * [3.1 Simple Widgets](/tutorial/Simple_Widgets.md)',
        '  * [3.2 Interact](/tutorial/Interact.md)',
        '* [2. Introduction](/introduction/README.md)',
        '  * [2.1 Motivation](/introduction/Motivation.md)',
        '  * [2.2 Getting Started](/introduction/Getting_Started.md)',
    ]

    res2 = [
        '# Table of Contents',
        '* [1. Read Me](/README.md)',
        '* [2. Tutorial](/tutorial/README.md)',
        '  * [2.1 Simple Widgets](/tutorial/Simple_Widgets.md)',
        '  * [2.2 Interact](/tutorial/Interact.md)',
        '* [3. Introduction](/introduction/README.md)',
        '  * [3.1 Motivation](/introduction/Motivation.md)',
        '  * [3.2 Getting Started](/introduction/Getting_Started.md)',
    ]

    assert add_section_labels(test1) == res1
    assert add_section_labels(test2) == res2

    print('Tests pass')


if __name__ == '__main__':
    main()
