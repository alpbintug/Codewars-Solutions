## IQ Test
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

#### Examples :
```
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
```
#### Solution : 

In order to check if there is only one even or odd value in given string, we have to split it into integers, when we do this we can check this array.

If `array[i-2] is odd, array[i-1] is odd, array[i] is even` we can say that there is only one even  value in that array, but what happens if `i<2`? Well, python helps us in this, in lists, list[-1] equals to last element in that list so we can use this in our favour.
