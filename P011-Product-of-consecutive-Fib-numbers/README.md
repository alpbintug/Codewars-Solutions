## Product of consecutive Fibonacci Numbers

#### Problem

The Fibonacci numbers are the numbers in the following integer sequence (Fn):
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
```
such as
```
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
```
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
```
F(n) * F(n+1) = prod.
```
Your function productFib takes an integer (prod) and returns an array:

`[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)`
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
```
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.
```
Examples
```
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```

#### Solution

We need two variables to store our data for Fibonacci Sequence, `first = 0` and `second = 1`, we have to loop until we reach the requested value (or exceed it) so we have to check if `first * second < prod`, if this is `True` we will continue to our loop and create new Fibonacci pairs using `first, second = second, first+second`, when this condition becomes `False` then there is two cases; 1: `first * second = prod`, 2: `first * second > prod`.

Case 1:

We need to return `True` because the conditions are met.

Case 2: 

We need to return `False` because the conditions are not met.

So basically what we need to return is;

`[first,second,first*second==prod]`
