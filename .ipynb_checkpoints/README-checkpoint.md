## Py_Pass_Gen

Welcome to Py_Pass_Gen, a Python password generator.
Author: William Ponton
January, 2019

## Description

This build will be a more cleverly written version of my previous Python Password Generator.  I will employ a more elegant solution to the Goals below:


## Goals

1. Automatically create the file to store the passwords.
2. Continue creating passwords until the user chooses to exit.
3. Provide a unique combination of upper chars, lower case chars, and special chars.
4. User entered password name and length.

```cool_code_bro```

```Syntax highlighted code block```

## Dependencies
If you want to run tests.py ```pip install -r dev-requirements.txt```

## Password Module: 

This module creates four lists:

### Logic
1. The lists are populated by a range of ASCII Integers of their category.
2. A second list of random items from each parent list is created.
    a. This technique provides an even probability of a pick from lists of differing lengths.
3. A third Master List is returned of random characters from each of the previous lists (passwordList).

### Lists of acceptable password characters.
- UPPER CASE (A - Z)
- LOWER CASE (a - z)
- INTEGER (0 - 9)
- SYMBOLS (#, $, %, &)

### Lists of ASCII Integers for each category:
- UPPER CASE (67 - 90)
- LOWER CASE (97 - 122)
- INTEGER (48 - 57)
- SYMBOLS (35, 36, 37, 38)


1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/gorbulus/Py_Pass_Gen/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Py_Pass_Gen? Get help at: [gorbulus](waponton@gmail.com) or [contact support](https://github.com/gorbulus) and we’ll help you sort it out.
