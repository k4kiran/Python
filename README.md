# Python
An interpreted, high-level, general-purpose programming language.

## Resources
* guidelines

 https://www.python.org/dev/peps/pep-0008/

*tutorials

 https://www.tutorialspoint.com/python/index.htm

 https://docs.python.org/3/tutorial/

 https://www.w3schools.com/python/default.asp
 
 * python with mysql

 https://www.w3schools.com/python/python_mysql_getstarted.asp


## Coding Standards

### Indentation

#### Aligned with opening delimiter.
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```
#### Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
#### Hanging indents should add a level.
```python
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

#### Max line length = 72

#### Opereators with expression

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```
#### Imports
Imports should usually be on separate lines:
```python
import os
import sys
```