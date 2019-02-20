## Infinite Precision

### Have you ever wondered whether it's possible to just add 1/10 and 2/10 so you'll get 3/10?

## Now you can!

```Python
# Classic float
>>> a = 1/10
>>> b = 2/10
>>> c = a + b
>>> print(c)
0.30000000000000004

# inf_prec
>>> import inf_prec
>>> a = inf_prec.Number(1, 10)
>>> b = inf_prec.Number(2, 10)
>>> c = a + b
>>> print(c)
3/10 False 0.3
```

## So what is it?

Basic definition of a fraction (numerator and denominator) and some arithmetic operations implemented. These are based on primary school level fractions, not smart floats, so on one hand you can do some operations that can not be done with 'normal' floating-point values (like addition above), but on the other hand it is much slower than these.

It is meant to be project for laughs, so don't run it on production or something.

### Some examples

Print object.
```Python
>>> a = inf_prec.Number(1, 3, True)
>>> print(a)
1/3             True            0.3333333333333333
fraction        is_negative     float representation
```

Define some fractions.
```Python
>>> a = inf_prec.Number(1, 3, True)     # - 1/3
>>> b = inf_prec.Number(4, 3, True)     # - 4/3
>>> c = inf_prec.Number(3)              #   3
>>> d = inf_prec.Number(3, 1, True)     # - 3
```

Multiply negative fraction with positive one.
```Python
>>> a = inf_prec.Number(1, 3, True)     # - 1/3
>>> b = inf_prec.Number(3, 2, False)    #   3/2
>>> print(a * b)
1/2 True 0.5
```
