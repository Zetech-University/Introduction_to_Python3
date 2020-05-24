# Challenges May 2020

## 1. List of Multiples

Write a function that taks two parameters say (`num, length`).  
The function should return a __list__ of multiples of `num`.  
The list should be of the size `length`.

### Examples

```python
    multiple(2, 8) --> [2, 4, 6, 8, 10, 12, 14, 16]
    multiple(3, 5) --> [3, 6, 9, 12, 15]
```

__Note__ that `num` is included in the list.

## 2. Stupid Addition  

Write a funtion that takes two parameters.  
The function should work in such a way that if both the parameters are __Strings__ it __adds__ them as if they were __integers__, but if both the parameters are __Integers__, it __Concatenates__ them.  
In the case that one is a string while the other is an integer, it returns, "None".  

### Example  

```python
    stupid(4, 2)     --> "42"
    stupid('4','2')  --> 6
    stupid('4', 2)   --> None
```

__Note__ that all the parameters must either be strings or integers.

## 3. Reverse Bool

Write a function that __Reverses__ a `boolean` value.  
The function should return `Bolean expected` if a `non-boolean` value is entered.  

### Examples

```python
    reverse(True)   --> False
    reverse(False)  --> True
    reverse(1)      --> 'Bolean expected'
    reverse("Man")  --> 'Bolean expected'
```

__Note__ that the function should consider `1` and `0` as `integers`, not `booleans`.