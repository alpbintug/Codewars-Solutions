## Friend or Foe 

#### Problem


Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: `Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]`

i.e.
```
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
```
Note: keep the original order of the names in the output.

#### Solution

We have to iterate over the given list and check the length of current item, if the length equals to four, we add that to an empty list we create
