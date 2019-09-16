## Write Number in Expanded Form

#### Problem

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form.

For example:
```
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```
NOTE: All numbers will be whole numbers greater than 0.

#### Solution

First, we have to turn our number into a string, we use str(number) for this operation. We also need an empty string, we use `b` for this Then we check every char in this string, if it is not '0' we concantanate that value to `b`, then we concantanate the exact amount of '0's, afer we do this for a digit, we add ' + ' part to match to the required format, when we are done, we are left with one unneeded ' + ', when we delete this, we are good to go.
