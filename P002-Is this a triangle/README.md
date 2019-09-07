## Is this a triange?

#### Problem

```
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
```
#### Solution

Let there be a trianble with edges A, B and C

For any edge pairs, if the sum of those edges are smaller or equal to the third edge, we can say that those three edges cannot form a triangle.

If we proof that sum of the length of all the possible pairs is greater than the length of the other edge, we can say that those three edges can form a triangle.

If A + B > C and B + C > A and C + A > B, A, B and C edges can form a triangle.
